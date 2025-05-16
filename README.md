# Sanka SDK

A Python SDK for interacting with the Sanka API.

## Installation

```bash
pip install sanka-sdk
```

## Requirements

- Python 3.9 or higher (Python 3.12 recommended)
- requests library
- loguru library

## Usage

```python
from sanka import SankaClient

# Initialize the client
client = SankaClient(api_key="your_api_key")

# Create a new chat message
response = client.chat.create(message="Hello, how are you?")
print(response.message)

# Get conversation history
conversation = client.chat.get_conversation(conversation_id="conv_123")
print(conversation.messages)

# Submit feedback
client.feedback.submit(
    conversation_id="conv_123",
    rating=5,
    feedback="Great conversation!"
)

# Get metrics
metrics = client.metrics.get_engagement()
print(metrics.total_conversations)
```

## Features

- Chat conversation management
- Conversation history retrieval
- Feedback submission
- Metrics and analytics
- Comprehensive logging
- Error handling

## Error Handling

The SDK includes built-in error handling for all API responses. Errors are raised as exceptions with descriptive messages.

```python
try:
    response = client.chat.create(message="Hello")
except SankaAPIError as e:
    print(f"Error: {e}")
```
