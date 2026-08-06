import os
import tempfile
import json
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from pydantic import BaseModel

from app.training.training_manager import TrainingManager
from app.storage.knowledge_index import KnowledgeIndex

router = APIRouter(prefix="/api/training", tags=["Training & Datasets"])
training_manager = TrainingManager()
knowledge_index = KnowledgeIndex()


class TextTrainingRequest(BaseModel):
    title: str
    content: str
    category: Optional[str] = "custom_dataset"


class ExportDatasetRequest(BaseModel):
    output_filename: Optional[str] = "first_son_finetune_dataset.jsonl"


@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    """
    Upload custom dataset file (.txt, .md, .pdf, .docx, .json, .csv) to train First-Son AI.
    """
    supported_extensions = {".txt", ".md", ".pdf", ".docx", ".json", ".csv"}
    filename = file.filename or "dataset.txt"
    file_ext = os.path.splitext(filename)[1].lower()

    if file_ext not in supported_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format '{file_ext}'. Supported: {', '.join(supported_extensions)}"
        )

    try:
        # Save to temp directory
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, filename)

        with open(temp_file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Train on file
        chunks_count = training_manager.train_file(temp_file_path)

        # Clean up temp file
        os.remove(temp_file_path)
        os.rmdir(temp_dir)

        return {
            "status": "success",
            "message": f"Successfully trained AI on '{filename}'",
            "filename": filename,
            "chunks_trained": chunks_count
        }

    except Exception as e:
        print(f"[Training Upload Error] {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to process dataset file: {str(e)}")


@router.post("/text")
def train_text(request: TextTrainingRequest):
    """
    Train First-Son AI directly on custom text/FAQ dataset entry.
    """
    if not request.content.strip():
        raise HTTPException(status_code=400, detail="Content cannot be empty")

    try:
        temp_dir = tempfile.mkdtemp()
        clean_title = "".join(c for c in request.title if c.isalnum() or c in (" ", "_", "-")).strip()
        filename = f"{clean_title or 'dataset_entry'}.txt"
        temp_file_path = os.path.join(temp_dir, filename)

        with open(temp_file_path, "w", encoding="utf-8") as f:
            f.write(f"# {request.title}\nCategory: {request.category}\n\n{request.content}")

        chunks_count = training_manager.train_file(temp_file_path)

        os.remove(temp_file_path)
        os.rmdir(temp_dir)

        return {
            "status": "success",
            "message": f"Successfully trained AI on text entry '{request.title}'",
            "chunks_trained": chunks_count
        }

    except Exception as e:
        print(f"[Training Text Error] {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to train text dataset: {str(e)}")


@router.get("/status")
def get_training_status():
    """
    Get current knowledge base training status and index statistics.
    """
    try:
        data = knowledge_index._load()
        return {
            "status": "active",
            "total_trained_files": len(data),
            "files": [
                {
                    "path": path,
                    "last_modified": meta.get("modified"),
                    "chunks": meta.get("chunks", 0)
                }
                for path, meta in data.items()
            ]
        }
    except Exception as e:
        return {"status": "active", "total_trained_files": 0, "files": []}


@router.post("/export")
def export_dataset(request: ExportDatasetRequest):
    """
    Export all stored knowledge base chunks into JSONL fine-tuning format.
    """
    try:
        from app.memory.vector_store import VectorStore
        store = VectorStore()
        
        # Retrieve all stored documents
        results = store.collection.get(include=["documents", "metadatas"])
        documents = results.get("documents", [])
        metadatas = results.get("metadatas", [])

        jsonl_entries = []
        for doc, meta in zip(documents, metadatas):
            if not doc:
                continue
            entry = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are First-Son AI, a helpful, intelligent assistant trained on domain-specific knowledge."
                    },
                    {
                        "role": "user",
                        "content": f"Information regarding {meta.get('filename', 'knowledge dataset')}:"
                    },
                    {
                        "role": "assistant",
                        "content": doc
                    }
                ]
            }
            jsonl_entries.append(entry)

        export_path = os.path.join(os.getcwd(), request.output_filename)
        with open(export_path, "w", encoding="utf-8") as f:
            for entry in jsonl_entries:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")

        return {
            "status": "success",
            "message": f"Exported {len(jsonl_entries)} fine-tuning dataset entries.",
            "export_file_path": export_path,
            "total_entries": len(jsonl_entries)
        }

    except Exception as e:
        print(f"[Export Dataset Error] {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to export fine-tuning dataset: {str(e)}")
