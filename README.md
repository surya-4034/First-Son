The first son is a personal AI assistant powered by a local language model.
To start it 
steps:
first start backend server

```bash
cd apps/backend
Create a new .venv
python -m venv .venv

install dependencies before starting
{
python -m pip install uvicorn
python -m pip install FastAPI
python -m pip install requests
}
Activate it:

Windows PowerShell

.\.venv\Scripts\Activate.ps1

for mac: source .venv/bin/activate
Step 5: Install all dependencies at once

Run:

pip install -r requirements.txt

Now all packages will be installed automatically.

Step 6: Make VS Code use the new .venv

VS Code:

Ctrl + Shift + P
↓
Python: Select Interpreter
↓
Choose:
apps/backend/.venv/Scripts/python.exe
Also add .venv to .gitignore

Never upload your virtual environment:

Create/edit .gitignore:

.venv/
__pycache__/
*.pyc
.env
Step1:apps/backend/:".\.venv\Scripts\Activate.ps1"
Enter
Enter:python3 -m uvicorn app.main:app --reload

After start frontend server

```bash

cd apps/frontend
step1:npm install
step2:
npm run dev
 and open http://localhost:3000

 to observe backend open http://localhost:8000
=======
 to observe backend open http://localhost:8000

