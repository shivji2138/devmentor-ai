import os
import sqlite3
from devmentor.db import DB_PATH

class HindsightClientMock:
    """Mock implementation of Hindsight SDK that uses local SQLite"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def create_memory(self, user_id: str, content: str, metadata: dict):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO memories (user_id, content, memory_type) VALUES (?, ?, ?)',
            (user_id, content, metadata.get("type", "general"))
        )
        conn.commit()
        conn.close()
        return True

    def search_memories(self, user_id: str, query: str, limit: int = 3):
        # Simple keyword matching mockup since we don't have vector search
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        words = [w for w in query.split() if len(w) > 3]
        if words:
            conditions = " OR ".join(["content LIKE ?" for _ in words])
            params = [user_id] + [f"%{w}%" for w in words]
            sql = f'SELECT content FROM memories WHERE user_id = ? AND ({conditions}) ORDER BY id DESC LIMIT ?'
            params.append(limit)
            cursor.execute(sql, tuple(params))
        else:
            cursor.execute('SELECT content FROM memories WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id, limit))
            
        rows = cursor.fetchall()
        conn.close()
        
        # Also blindly return all memories if it's a small DB, to guarantee context injection for the demo
        if not rows:
             conn = sqlite3.connect(DB_PATH)
             cursor = conn.cursor()
             cursor.execute('SELECT content FROM memories WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id, limit))
             rows = cursor.fetchall()
             conn.close()
             
        return [{"content": row[0]} for row in rows]

class DevMemory:
    def __init__(self):
        api_key = os.getenv("HINDSIGHT_API_KEY", "mock-hindsight-key")
        self.client = HindsightClientMock(api_key=api_key)
        self.user_id = "local_dev_1"

    def store(self, content: str, memory_type: str = "general"):
        return self.client.create_memory(
            user_id=self.user_id,
            content=content,
            metadata={"type": memory_type}
        )

    def retrieve_context(self, query: str, limit: int = 3) -> str:
        results = self.client.search_memories(
            user_id=self.user_id,
            query=query,
            limit=limit
        )
        if not results:
            return ""
        return "\n".join([f"- {r['content']}" for r in results])
