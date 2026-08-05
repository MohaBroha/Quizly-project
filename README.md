# Quizly Backend

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-REST%20Framework-green)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

An AI-powered Django REST Framework backend that generates quizzes from YouTube videos using **yt-dlp**, **Whisper**, and **Google Gemini**.

---

## Author

**Moha Broha**

---

## Table of Contents

- Overview
- Features
- Tech Stack
- Project Structure
- Requirements
- Local Installation
- Environment Variables
- Database Setup
- Running the Server
- Authentication
- API Endpoints
- AI Workflow
- Testing
- Troubleshooting
- License

---

# Overview

Quizly Backend allows authenticated users to generate quizzes from YouTube videos.  
The backend downloads the video's audio, transcribes it, generates quiz questions with Gemini AI, stores the quiz in the database, and exposes everything through a REST API.

---

# Features

- User Registration
- Login / Logout
- JWT Authentication using HTTP Cookies
- Refresh Token
- AI Quiz Generation
- YouTube Audio Processing
- Whisper Transcription
- Google Gemini Integration
- Quiz CRUD
- User-specific Quiz Ownership
- REST API

---

# Tech Stack

- Python 3.12
- Django
- Django REST Framework
- SQLite
- SimpleJWT
- Google Gemini API
- OpenAI Whisper
- yt-dlp
- FFmpeg

---

# Project Structure

```text
quizly-backend/
│
├── accounts/
├── ai/
│   └── services/
│       ├── gemini_service.py
│       ├── whisper_service.py
│       └── youtube_service.py
├── quizzes/
├── core/
├── manage.py
├── requirements.txt
└── .env
```

---

# Requirements

- Python 3.12+
- Git
- FFmpeg
- Gemini API Key

---

# Local Installation

## 1. Clone the repository

```bash
git clone https://github.com/<username>/quizly-backend.git
cd quizly-backend
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create a .env file

Create a file named `.env` in the project root.

Example:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

## 5. Install FFmpeg

### Ubuntu

```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows

Download FFmpeg from the official website and add the `bin` folder to your system PATH.

Verify the installation:

```bash
ffmpeg -version
```

## 6. Apply database migrations

```bash
python manage.py migrate
```

## 7. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

## 8. Start the development server

```bash
python manage.py runserver
```

The backend is now available at:

```
http://127.0.0.1:8000/
```

---

# Authentication

Authentication is handled using JWT stored in HTTP Cookies.

| Method | Endpoint |
|--------|----------|
| POST | `/api/register/` |
| POST | `/api/login/` |
| POST | `/api/logout/` |
| POST | `/api/token/refresh/` |

---

# Quiz API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/quizzes/` | Create a quiz |
| GET | `/api/quizzes/` | List user quizzes |
| GET | `/api/quizzes/{id}/` | Retrieve a quiz |
| PATCH | `/api/quizzes/{id}/` | Update quiz title/description |
| DELETE | `/api/quizzes/{id}/` | Delete a quiz |

Only authenticated users can access quizzes. Every user can only manage their own quizzes.

---

# AI Workflow

```text
YouTube URL
      │
      ▼
yt-dlp
      │
      ▼
FFmpeg
      │
      ▼
Whisper
      │
      ▼
Transcript
      │
      ▼
Google Gemini
      │
      ▼
Quiz JSON
      │
      ▼
SQLite Database
```

---

# Running Tests

Run all tests:

```bash
python manage.py test
```

Run quizzes tests only:

```bash
python manage.py test quizzes
```

---

# Troubleshooting

### FFmpeg not found

```bash
ffmpeg -version
```

If the command is not available, install FFmpeg and ensure it is available in your PATH.

### Gemini API

Make sure your `.env` file contains a valid API key.

### YouTube

Quiz generation depends on external YouTube services. Processing time depends on the video length and network speed.

---

# License

This project was developed for educational purposes as part of the Developer Academy Fullstack Development Program.

---

**Author:** **Moha Broha**
