# ComicCrafter AI

Transform simple text prompts into complete AI-generated comic pages.

ComicCrafter AI combines Large Language Models and AI image generation to automatically create comic stories, generate panel illustrations, and assemble them into a finished comic page.

## Live Demo

Frontend: https://comic-crafter-ai.vercel.app

Backend API: https://comiccrafter-ai.onrender.com

---

## Features

* AI Story Generation using Groq LLM
* Automatic Comic Panel Creation
* AI Image Generation using Hugging Face
* Comic Page Assembly using Pillow
* Multiple Comic Styles

  * Comic
  * Manga
  * Webtoon
* FastAPI REST Backend
* Next.js Frontend
* Responsive Modern UI

---

## Tech Stack

### Backend

* FastAPI
* Python
* Groq API
* Hugging Face Inference API
* Pillow

### Frontend

* Next.js 16
* TypeScript
* Tailwind CSS

### Deployment

* Render (Backend)
* Vercel (Frontend)

---

## Project Architecture

User Prompt

↓

Groq Story Generation

↓

Panel Descriptions

↓

Hugging Face Image Generation

↓

Comic Builder

↓

Final Comic Page

---

## Project Structure

```text
ComicCrafter-AI
│
├── backend
│   ├── app
│   │   ├── models
│   │   ├── services
│   │   │   ├── image
│   │   │   └── llm
│   │   ├── utils
│   │   └── main.py
│   │
│   ├── tests
│   └── requirements.txt
│
├── frontend
│   ├── app
│   ├── lib
│   ├── public
│   └── package.json
│
├── README.md
└── .gitignore
```

---

## Local Setup

### Backend

```bash
cd backend/app

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

HF_TOKEN=your_huggingface_token

BASE_URL=http://127.0.0.1:8000
```

---

## Future Improvements

* Character consistency across panels
* Multiple comic layouts
* User authentication
* Comic history
* PDF export
* Story editing before generation

---

## Author

Ayak Manna
