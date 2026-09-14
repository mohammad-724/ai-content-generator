# AI Content Generation & Publishing Platform

A beginner-friendly Generative AI web application that combines AI text generation, image prompting, local content history, simulated publishing, scheduled posts, and a dashboard UI.

## Features

- AI text generation with topic, content type, tone, and length controls
- Save generated content in browser localStorage
- Saved content history with individual delete and clear-all actions
- AI image generation endpoint using the configured Pollinations image URL
- Manual publishing simulation for LinkedIn, Instagram, X/Twitter, and Facebook
- Scheduled post simulation
- Automatic scheduled-post processing while the dashboard is open
- Responsive dashboard with statistics and backend status indicator
- FastAPI backend
- Single-service deployment: FastAPI serves both API endpoints and the frontend
- Render deployment configuration included

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
├── README.md
├── render.yaml
└── requirements.txt
```

## Local Setup

### 1. Open the project

```powershell
cd C:\Users\reeha\Desktop\ai-content-generator
```

### 2. Create/activate the virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Create `.env`

Copy `.env.example` to `.env` and add your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Start the application

```powershell
uvicorn backend.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Important Scheduler Note

The automatic scheduler is intentionally implemented in the browser for this learning project. A scheduled post moves from `Scheduled` to `Published` when its time arrives **while the dashboard page is open**. This is a simulation and does not publish to real social-media accounts.

For a production scheduler, move scheduling to the backend and store jobs in a database with a server-side worker/scheduler.

## GitHub

```powershell
git init
git add .
git commit -m "Finalize AI content generation and publishing platform"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

## Render Deployment

This repository includes `render.yaml`, so the deployment can use the project configuration directly.

### Environment variable

Set this secret in Render:

```text
OPENAI_API_KEY=your_openai_api_key
```

### Manual settings, if needed

Build Command:

```text
pip install -r requirements.txt
```

Start Command:

```text
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

After deployment, open the assigned Render URL.

## Project Limitations

- Social-media publishing is simulated.
- Browser localStorage is used for saved/scheduled/published data.
- Scheduled processing requires the browser page to remain open.
- Image generation depends on the configured image service endpoint.
- The OpenAI API requires an available API account/usage allowance.

## Future Production Upgrades

- User authentication
- MySQL/PostgreSQL persistence
- Real social-media APIs and OAuth
- Rich content editor
- Server-side scheduling worker
- Content templates and analytics
- File/image storage
- React frontend
- RAG/vector database features
- AI agents and workflow automation
