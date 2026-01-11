*Over View*

┌─────────────────────────────────────────────────────┐
│                    EXTERNAL WORLD                    │
└───────────────────────┬─────────────────────────────┘
                        │
            WhatsApp Messages (via Twilio)
                        │
┌───────────────────────▼─────────────────────────────┐
│                 FLASK APPLICATION                    │
│  ┌─────────────────────────────────────────────┐    │
│  │  /whatsapp (POST)                           │    │
│  │  • Receives Twilio webhooks                 │    │
│  │  • Parses incoming messages                 │    │
│  │  • Returns Twilio XML responses             │    │
│  └─────────────────────────────────────────────┘    │
└───────────────────────┬─────────────────────────────┘
                        │
                Message Flow
                        │
┌───────────────────────▼─────────────────────────────┐
│              MESSAGE CONTROLLER LAYER               │
│  ┌─────────────────────────────────────────────┐    │
│  │  MessageController                          │    │
│  │  • Orchestrates conversation flow           │    │
│  │  • Manages memory storage/retrieval         │    │
│  │  • Coordinates AI response generation       │    │
│  └─────────────────────────────────────────────┘    │
└───────────────────────┬─────────────────────────────┘
                        │
          Memory Context + User Message
                        │
┌───────────────┬───────▼───────┬─────────────────────┐
│               │               │                     │
│   MEMORY      │      AI       │    PERSONALITY      │
│   MANAGER     │    CLIENT     │     TRAITS          │
│               │               │                     │
└───────────────┴───────┬───────┴─────────────────────┘
                        │
                AI-Generated Reply
                        │
┌───────────────────────▼─────────────────────────────┐
│               RESPONSE DELIVERY                     │
│  • Format for Twilio                                │
│  • Send back through webhook                        │
│  • Store in memory                                  │
└─────────────────────────────────────────────────────┘


*Project Structure*

ai_companion/
├── app.py                 # Main Flask application
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── ai/
│   ├── groq_client.py    # Groq AI integration
│   └── personality.py    # Rias Gremory personality traits
├── controllers/
│   └── message_controller.py  # Message handling logic
├── memory/
│   └── memory_manager.py      # Conversation memory system
├── messaging/
│   └── whatsapp_handler.py    # Twilio webhook handler
└── data/
    └── conversation_memory.json  # Conversation storage


*Usage Examples*

👤 You: Hello Rias!
🤖 Rias: Ara ara, hello there! How are you doing today, my dear?

👤 You: I need some advice
🤖 Rias: Of course, I'm here to help. As the president of the Occult Research Club, 
        I've guided many through difficult situations. Tell me what's troubling you.

👤 You: Can you tell me about yourself?
🤖 Rias: I'm Rias Gremory, a High-class Devil and Princess of the Gremory Clan. 
        I lead the Occult Research Club here at Kuoh Academy, and I take care of 
        my wonderful peerage members. *smiles warmly*

*System Architecture*

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