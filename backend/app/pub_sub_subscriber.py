import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
from app.db import save_topic_message  # Ensure this is the correct import

credentials_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
subscription_path = os.environ['SUBSCRIPTION_PATH']

def start_subscriber():
    from app import app  # Import here to avoid circular import

    subscriber = pubsub_v1.SubscriberClient()

    def callback(message):
        # Use the application context
        with app.app_context():
            try:
                print(f'data: {message.data}')
                save_topic_message(message)
                message.ack()
            except Exception as e:
                print(f'Error processing message: {e}')

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f'Listening for messages on {subscription_path}')

    with subscriber:
        try:
            streaming_pull_future.result()  # Block indefinitely
        except TimeoutError:
            streaming_pull_future.cancel()  # Shutdown
            streaming_pull_future.result()  # Block until shutdown complete