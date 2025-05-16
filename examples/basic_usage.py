from sanka import SankaClient
from sanka.exceptions import SankaAPIError

def main():
    client = SankaClient(api_key="your_api_key")

    try:
        # Create a new chat message
        chat_response = client.chat.create(
            message="What's the weather like today?",
            max_tokens=100
        )
        print("Chat Response:", chat_response["message"])

        # Get conversation history
        conversation = client.chat.get_conversation(
            conversation_id=chat_response["conversation_id"]
        )
        print("\nConversation History:")
        for message in conversation["messages"]:
            print(f"{message['role']}: {message['content']}")

        # Submit feedback
        feedback_response = client.feedback.submit(
            conversation_id=chat_response["conversation_id"],
            rating=5,
            feedback="Very helpful response!"
        )
        print("\nFeedback submitted:", feedback_response["message"])

        # Get metrics
        metrics = client.metrics.get_engagement()
        print("\nEngagement Metrics:")
        print(f"Total Conversations: {metrics['total_conversations']}")
        print(f"Total Messages: {metrics['total_messages']}")
        print(f"Average Rating: {metrics['satisfaction_summary']['average_rating']}")

    except SankaAPIError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main() 