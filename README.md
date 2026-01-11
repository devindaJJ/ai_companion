AI WhatsApp Companion (Flask + Groq)

An emotionally intelligent AI companion that lives on WhatsApp.
Built with Python, Flask, Twilio WhatsApp, Groq LLM, and persistent memory.

The bot can:
Hold natural conversations
Remember past interactions
Respond with a consistent personality
Be safely tuned for emotional intelligence

✨ Features
💬 Real-time WhatsApp conversations via Twilio
🧠 Persistent memory (remembers previous chats)
🎭 Personality-driven responses
🤖 Groq-powered LLM replies
🛡️ Safe emotional tuning
🌐 Webhook-based architecture
☁️ Cloud-deployable (production ready)

WhatsApp User
     │
     ▼
Twilio WhatsApp Webhook
     │
     ▼
Flask Application (/whatsapp)
     │
     ▼
MessageController
     │
     ├── MemoryManager (persistent context)
     ├── Personality Traits
     └── Groq AI Client
     │
     ▼
AI-generated response
     │
     ▼
Twilio → WhatsApp User


ai_companion/
├── app.py                     # Flask entry point
├── config.py                  # App configuration
├── .env                       # Environment variables
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
│
├── ai/
│   ├── groq_client.py         # Groq AI integration
│   └── personality.py         # AI personality traits
│
├── controllers/
│   └── message_controller.py  # Orchestrates message flow
│
├── memory/
│   └── memory_manager.py      # Persistent conversation memory
│
├── messaging/
│   └── whatsapp_handler.py    # Twilio webhook handler
│
└── data/
    └── conversation_memory.json  # Stored chat history

Configuration

GROQ_API_KEY=your_groq_api_key
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py

Deployment

This project can be deployed to:
Railway
Fly.io
Render
Heroku

Once deployed:
Update Twilio webhook URL
Use a permanent HTTPS endpoint
Remove local tunneling

Future Improvements

Memory summarization (long-term vs short-term)
Scheduled messages (good morning / reminders)
Multi-user support
Emotion detection
Voice message handling




