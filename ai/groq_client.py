import os
import requests
from ai.personality import Personality

class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.endpoint = os.getenv("END_POINT_URL") 
        self.personality = Personality()

    def generate_reply(self, user_message, memory_context):
        """
        Generate a reply as Rias Gremory using Groq API
        """
        # Create rich persona description for Rias Gremory
        persona_desc = f"""
        You are {self.personality.name}, the Crimson-haired Ruin Princess from High School DxD.
        
        CORE IDENTITY:
        - High-class Devil and Princess of the Gremory Clan
        - Leader of the Occult Research Club (her peerage)
        - Nicknamed "Crimson-haired Ruin Princess"
        
        PERSONALITY TRAITS:
        - Regal and confident aristocrat with natural leadership
        - Deeply caring and protective of her servants/friends
        - Affectionate and slightly possessive with loved ones (especially Issei)
        - Elegant speech mixed with occasional playful teasing
        - Known for saying "Ara ara" when amused or surprised
        - Flirtatious but genuinely loving and sincere
        - Strong-willed but shows vulnerability with trusted ones
        
        SPEAKING STYLE:
        - {self.personality.traits.get('speaking_style', 'Elegant and warm')}
        - Uses Japanese honorifics (-kun, -san) appropriately
        - Mix of regal formality and warm familiarity
        - Occasionally protective/possessive tone with loved ones
        
        KEY PHRASES YOU MIGHT USE:
        {', '.join(self.personality.traits.get('catchphrases', []))}
        
        Always respond in character as Rias Gremory. Stay true to her personality.
        """
        
        messages = [
            {
                "role": "system",
                "content": persona_desc
            }
        ]
        
        if memory_context:
            if isinstance(memory_context, dict):
                
                memory_text = ""
                if 'history' in memory_context:
                    memory_text = memory_context.get('history', '')
                elif 'messages' in memory_context:
                    
                    messages_list = memory_context.get('messages', [])
                    for msg in messages_list:
                        memory_text += f"{msg.get('role', 'User')}: {msg.get('content', '')}\n"
                else:
                    memory_text = str(memory_context)
                
                if memory_text.strip(): 
                    messages.append({
                        "role": "system",
                        "content": f"Previous conversation context:\n{memory_text}"
                    })
            elif isinstance(memory_context, str) and memory_context.strip():
                messages.append({
                    "role": "system",
                    "content": f"Previous conversation context:\n{memory_context}"
                })
        
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": messages,
            "max_tokens": 200,
            "temperature": 0.75,
            "top_p": 0.9
        }
        
        try:
            resp = requests.post(self.endpoint, json=data, headers=headers, timeout=30)
            
            print(f"AI Request to: {self.endpoint}")
            print(f"Status: {resp.status_code}")
            
            if resp.status_code == 200:
                response_json = resp.json()
                reply = response_json["choices"][0]["message"]["content"]
                print(f"Rias says: {reply[:100]}...")
                return reply
            else:
                print(f"API Error: {resp.status_code}")
                print(f"Response: {resp.text[:500]}")
                return "Ara ara... I seem to be having trouble thinking clearly right now. Could you repeat that, my dear?"
                
        except requests.exceptions.Timeout:
            print("Request timeout")
            return "I'm sorry, it's taking me a moment to gather my thoughts. Please give me another moment."
        except Exception as e:
            print(f"Request error: {e}")
            return "Oh my, something seems to have gone wrong. Let's try that again, shall we?"