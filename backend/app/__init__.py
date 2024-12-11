from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
import threading

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Load environment variables from .env file
load_dotenv()
CORS(app)

from app.pub_sub_subscriber import start_subscriber  # Import your subscriber function

# # Start the Pub/Sub subscriber in a separate thread
subscriber_thread = threading.Thread(target=start_subscriber)
subscriber_thread.daemon = True  # Allows the thread to exit when the main program does
subscriber_thread.start()

from app import routes
