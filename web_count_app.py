# Path/filename: /mnt/data/web_app.py
# The purpose of this script is to enhance the Flask application with thread safety for file operations.

from flask import Flask, request, abort
import os
import threading

app = Flask(__name__)

# File to store the counter
COUNTER_FILE = 'counter.txt'
# Starting value for the counter
STARTING_VALUE = 10000
# Bearer token for authentication
BEARER_TOKEN = "UGB31"
# Lock for thread-safe file operations
file_lock = threading.Lock()

def read_counter():
    """Reads the counter value from the file. If file does not exist, returns the starting value."""
    with file_lock:
        try:
            with open(COUNTER_FILE, 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return STARTING_VALUE
        except ValueError:
            # In case the file is empty or has invalid content
            return STARTING_VALUE

def save_counter(value):
    """Saves the counter value to the file."""
    with file_lock:
        with open(COUNTER_FILE, 'w') as file:
            file.write(str(value))

def increment_counter():
    """Increments the counter safely and returns the new value."""
    new_value = read_counter() + 1
    save_counter(new_value)
    return new_value

def is_authorized():
    """Checks if the request contains the correct Bearer token."""
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        return token == BEARER_TOKEN
    return False

@app.route('/')
def index():
    """Handles GET request, incrementing and returning the counter if authorized."""
    if not is_authorized():
        abort(403)  # Forbidden

    new_value = increment_counter()
    return str(new_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)



# The Flask application now includes thread safety for the counter file read/write operations.
# example test string curl -H "Authorization: Bearer UVB76" http://number.exampleserver.com:9001