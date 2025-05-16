import requests
from loguru import logger
from ..exceptions import SankaAPIError

class ChatAPI:
    def __init__(self, client):
        self.client = client

    def create(self, message, conversation_id=None, max_tokens=None):
        logger.info("creating chat message")
        payload = {
            "message": message,
            "conversation_id": conversation_id,
            "max_tokens": max_tokens
        }
        
        response = requests.post(
            f"{self.client.base_url}/chat",
            headers=self.client._get_headers(),
            json={k: v for k, v in payload.items() if v is not None}
        )
        
        if response.status_code != 200:
            logger.error(f"chat creation failed: {response.text}")
            raise SankaAPIError(response.json().get("error", "Unknown error"))
            
        return response.json()

    def get_conversation(self, conversation_id):
        logger.info(f"fetching conversation {conversation_id}")
        response = requests.get(
            f"{self.client.base_url}/conversation/{conversation_id}",
            headers=self.client._get_headers()
        )
        
        if response.status_code != 200:
            logger.error(f"conversation fetch failed: {response.text}")
            raise SankaAPIError(response.json().get("error", "Unknown error"))
            
        return response.json()

    def delete_conversation(self, conversation_id):
        logger.info(f"deleting conversation {conversation_id}")
        response = requests.delete(
            f"{self.client.base_url}/conversation/{conversation_id}",
            headers=self.client._get_headers()
        )
        
        if response.status_code not in [200, 204]:
            logger.error(f"conversation deletion failed: {response.text}")
            raise SankaAPIError(response.json().get("error", "Unknown error")) 