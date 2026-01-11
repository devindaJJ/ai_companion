from ai.groq_client import GroqClient
from memory.memory_manager import MemoryManager

class MessageController:
    def __init__(self):
        self.ai = GroqClient()
        self.memory = MemoryManager()

    def handle_message(self, incoming_msg):
        # log user message
        self.memory.add_user_message(incoming_msg)

        # fetch memory context
        memory_context = self.memory.read_memory()

        # AI generates reply
        reply = self.ai.generate_reply(incoming_msg, memory_context)
        print("AI Reply:", reply)

        # log bot reply
        self.memory.add_bot_message(reply)

        return reply
