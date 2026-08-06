#!/usr/bin/env python3
"""
First-Son AI Dataset Exporter for Fine-Tuning

Converts vector store knowledge chunks and conversation history into 
standard JSONL format for fine-tuning models on Google AI Studio or OpenAI.
"""

import json
import os
import sys
from pathlib import Path

# Add app directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from app.memory.vector_store import VectorStore
from app.Database.database import SessionLocal
from app.models.message import Message
from app.models.conversation import Conversation


def export_fine_tune_dataset(output_path: str = "first_son_finetune.jsonl"):
    print("🚀 Starting Fine-Tuning Dataset Export...")
    jsonl_entries = []

    # 1. Export Knowledge Base Chunks from Vector Store
    try:
        store = VectorStore()
        results = store.collection.get(include=["documents", "metadatas"])
        documents = results.get("documents", [])
        metadatas = results.get("metadatas", [])

        print(f"📦 Found {len(documents)} document chunks in Vector Store.")

        for doc, meta in zip(documents, metadatas):
            if not doc or len(doc.strip()) < 10:
                continue

            filename = meta.get("filename", "knowledge base") if meta else "knowledge base"
            
            entry = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are First-Son AI, an intelligent corporate and domain assistant."
                    },
                    {
                        "role": "user",
                        "content": f"Provide relevant information regarding {filename}:"
                    },
                    {
                        "role": "assistant",
                        "content": doc.strip()
                    }
                ]
            }
            jsonl_entries.append(entry)

    except Exception as e:
        print(f"⚠️ Notice: Could not extract from vector store: {e}")

    # 2. Export Chat Conversations from Database
    try:
        db = SessionLocal()
        conversations = db.query(Conversation).all()
        print(f"💬 Found {len(conversations)} chat conversations in Database.")

        for conv in conversations:
            messages = db.query(Message).filter(Message.conversation_id == conv.id).order_by(Message.id).all()
            if not messages or len(messages) < 2:
                continue

            formatted_msgs = [
                {
                    "role": "system",
                    "content": "You are First-Son AI, an intelligent, helpful AI assistant."
                }
            ]

            for msg in messages:
                formatted_msgs.append({
                    "role": "user" if msg.role == "user" else "assistant",
                    "content": msg.content
                })

            jsonl_entries.append({"messages": formatted_msgs})

        db.close()

    except Exception as e:
        print(f"⚠️ Notice: Could not extract from database: {e}")

    # 3. Write to JSONL File
    output_file = Path(output_path).resolve()
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in jsonl_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"\n✅ SUCCESS! Exported {len(jsonl_entries)} dataset samples to:")
    print(f"👉 {output_file}")
    print("\n-----------------------------------------------------------")
    print("💡 HOW TO USE THIS DATASET FOR FINE-TUNING YOUR AI:")
    print("1. Google AI Studio (Free Fine-Tuning):")
    print("   - Open https://aistudio.google.com/")
    print("   - Click 'Create Tuned Model'")
    print("   - Upload this `.jsonl` file to fine-tune Gemini 1.5 / 2.0 Flash!")
    print("2. OpenAI Dashboard:")
    print("   - Go to https://platform.openai.com/finetune")
    print("   - Upload this `.jsonl` file to train a custom GPT-4o-mini model.")
    print("-----------------------------------------------------------\n")

    return str(output_file)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "first_son_finetune.jsonl"
    export_fine_tune_dataset(out)
