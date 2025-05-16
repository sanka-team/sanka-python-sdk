import requests
from loguru import logger
from ..exceptions import SankaAPIError

class MetricsAPI:
    def __init__(self, client):
        self.client = client

    def get_engagement(self):
        logger.info("fetching engagement metrics")
        response = requests.get(
            f"{self.client.base_url}/metrics/engagement",
            headers=self.client._get_headers()
        )
        
        if response.status_code != 200:
            logger.error(f"metrics fetch failed: {response.text}")
            raise SankaAPIError(response.json().get("error", "Unknown error"))
            
        return response.json() 