# Study Steve - AI Study Buddy

Study Steve is a web-based AI study buddy that helps users simplify notes, ask study questions, and review concepts through a chat-style interface.

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- AI Model: Google Gemini

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd CPSC481FinalProject
```
### 2. Install Python Dependencies

```bash
pip install fastapi uvicorn python-dotenv google-genai
```

### 3. Create a .env File
Add your Gemini API key. You can check the .env example file for reference

### 4. Start the Back-end
Run 
```bash
python main.py
```
OR
```bash
python -m uvicorn main:app --reload
```
The backend should start at:
```bash
http://localhost:8000
```
OR
```bash
http://127.0.0.1:8000
```

### 5. Run Front-end
Option A:
Use Live Server in VS Code to open:
```bash
index.html
```
Option B:
Open index.html directly in your browser
