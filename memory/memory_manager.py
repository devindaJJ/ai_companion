import json
import os
from datetime import datetime

MEMORY_FILE = "memory/memory.json"

class MemoryManager:
    def __init__(self):
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump({"chat_logs": [], "user_profile": {}}, f)

    def add_user_message(self, message):
        self._add_message("user", message)

    def add_bot_message(self, message):
        self._add_message("bot", message)

    def _add_message(self, sender, message):
        data = self.read_memory()
        data["chat_logs"].append({
            "sender": sender,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })
        self._write_memory(data)

    def read_memory(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def _write_memory(self, data):
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)
