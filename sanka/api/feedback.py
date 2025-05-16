import requests
from loguru import logger
from ..exceptions import SankaAPIError

class FeedbackAPI:
    def __init__(self, client):
        self.client = client

    def submit(self, conversation_id, rating, feedback=None):
        logger.info(f"submitting feedback for conversation {conversation_id}")
        payload = {
            "conversation_id": conversation_id,
            "rating": rating,
            "feedback": feedback
        }
        
        response = requests.post(
            f"{self.client.base_url}/feedback",
            headers=self.client._get_headers(),
            json={k: v for k, v in payload.items() if v is not None}
        )
        
        if response.status_code != 200:
            logger.error(f"feedback submission failed: {response.text}")
            raise SankaAPIError(response.json().get("error", "Unknown error"))
            
        return response.json() 