render_url:  https://ai-content-generator-jd9b.onrender.com


readme url: https://mohammad-724.github.io/ai-content-generator/



# AI Content Generation & Publishing Platform

A simple **Generative AI & AI Engineering** web application for creating, managing, scheduling, and publishing AI-generated content.

## Overview

This project demonstrates how AI models can be integrated into a practical software application using a **FastAPI backend** and a lightweight **HTML, CSS, and JavaScript frontend**.

## Features

- AI-powered text content generation
- AI image generation
- Save and manage generated content
- Content history with delete options
- Publishing simulation for social platforms
- Schedule posts for a future date and time
- Automatic scheduled-post processing while the application is open
- Responsive dashboard-style interface

## Tech Stack

**Generative AI / AI Engineering**
- OpenAI API
- AI text generation
- AI image generation integration

**Backend**
- Python
- FastAPI
- Uvicorn

**Frontend**
- HTML
- CSS
- JavaScript

**Tools**
- VS Code
- Git & GitHub
- Python Virtual Environment

## Project Structure

```text
ai-content-generator/
├── backend/
│   └── main.py
├── frontend/
│   └── index.html
├── .env.example
├── .gitignore
├── Procfile
├── render.yaml
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd ai-content-generator
```

### 2. Create and activate virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the application

```bash
uvicorn backend.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## AI Engineering Workflow

```text
User Input
   ↓
Frontend
   ↓
FastAPI Backend
   ↓
Generative AI API
   ↓
Generated Content
   ↓
Dashboard / Storage / Scheduling
```

## Deployment

The project includes configuration files for deployment on **Render**.

Required environment variable:

```text
OPENAI_API_KEY
```

## Note

Publishing and scheduling are currently implemented as **application simulations**. Real social-media publishing can be added later using platform APIs and a persistent backend scheduler/database.

## Future Enhancements

- User authentication
- MySQL database
- Real social-media API integration
- React-based frontend
- Advanced AI workflows, RAG, and AI agents

## Author

**Mohammad Azmath Ali**
