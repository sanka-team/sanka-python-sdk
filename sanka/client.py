from loguru import logger
from .api.chat import ChatAPI
from .api.feedback import FeedbackAPI
from .api.metrics import MetricsAPI

class SankaClient:
    def __init__(self, api_key, base_url="https://api.sanka.gg"):
        self.api_key = api_key
        self.base_url = base_url
        logger.info("initializing sanka client")
        
        self.chat = ChatAPI(self)
        self.feedback = FeedbackAPI(self)
        self.metrics = MetricsAPI(self)
    
    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        } 