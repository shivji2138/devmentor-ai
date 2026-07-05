import os
import time

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

class AIRouter:
    def __init__(self):
        groq_key = os.getenv("GROQ_API_KEY", "")
        if GROQ_AVAILABLE and groq_key and groq_key != "your_groq_api_key":
            self.client = Groq(api_key=groq_key)
        else:
            self.client = None

    def process_query(self, query: str, context: str):
        system_prompt = f"You are DevMentor, a helpful AI assistant. Use this memory context about the user to personalize the response if relevant:\n{context}"
        
        start_time = time.time()
        model_name = "openai/gpt-oss-120b"
        
        if self.client:
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": query}
                    ],
                    model=model_name,
                )
                response_text = chat_completion.choices[0].message.content
            except Exception as e:
                response_text = f"Error calling Groq API: {str(e)}"
        else:
            time.sleep(1.0) # Simulate latency
            response_text = f"Mock Response from {model_name}: I've processed your request. Please add a valid GROQ_API_KEY in .env to use real AI models."
                
        latency_ms = round((time.time() - start_time) * 1000, 2)
        
        return {
            "answer": response_text,
            "model": model_name,
            "latency": latency_ms
        }
