# FastAPI-LLM — AI Chat & File Analysis API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A production-style **AI backend system** built with **FastAPI**, supporting:

* 🔐 JWT Authentication
* 💬 AI Chat API (LLM powered)
* 📄 PDF & Image Upload Analysis
* 🧠 Conversation Memory (Chat History)
* ⚡ Async database operations
* 🧩 Modular clean architecture

Designed as a **real-world backend architecture project** demonstrating modern Python backend engineering practices.

---

## 📌 Features

### ✅ Authentication

* User registration & login
* JWT token authentication
* Protected API routes
* Secure password hashing (bcrypt)

### ✅ AI Chat

* Conversational AI endpoint
* Context-aware chat history
* Persistent conversations per user

### ✅ File Analysis

Upload and analyze:

* 📄 PDF files
* 🖼 Images (OCR & content extraction)

Extracted content is automatically sent to the AI for analysis.

---

## 🏗 Architecture

```
app/
├── api/        
```
