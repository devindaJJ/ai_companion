# 🤖 AI WhatsApp Companion
**Flask + Groq + Twilio**

An emotionally intelligent AI companion that lives on **WhatsApp**.  
Built with **Python**, **Flask**, **Twilio WhatsApp**, **Groq LLM**, and **persistent memory**.

---

## 🌟 Overview

This project enables a conversational AI that can:
- Hold natural, human-like conversations
- Remember past interactions
- Maintain a consistent personality
- Respond with emotionally intelligent and safe replies

The AI communicates entirely through **WhatsApp**, making interactions feel personal and engaging.

---

## ✨ Features

- 💬 Real-time WhatsApp conversations via Twilio  
- 🧠 Persistent memory (remembers previous chats)  
- 🎭 Personality-driven responses  
- ⚡ Groq-powered LLM replies  
- 🛡️ Safe emotional tuning  
- 🌐 Webhook-based architecture  
- ☁️ Cloud-deployable & production-ready  

---

## 🧠 Architecture

```
WhatsApp
   ↓
Twilio WhatsApp Webhook
   ↓
Flask App (Python)
   ↓
MessageController
   ↓
AIEngine (Groq)
   ↓
MemoryManager
   ↓
Response → WhatsApp
```

## ☁️ Deployment

This project can be deployed on:
- Railway
- Fly.io
- Render
- Heroku

After Deployment:
- Update the Twilio WhatsApp Webhook URL
- Use a permanent HTTPS endpoint
- Remove local tunneling (ngrok)

## 🔮 Future Improvements

- Memory summarization (short-term vs long-term)
- Scheduled messages (good morning, reminders)
- Multi-user support
- Emotion detection
- Voice message handling

## 🧩 Tech Stack

- Python
- Flask
- Twilio WhatsApp API
- Groq LLM
- JSON-based persistent memory
