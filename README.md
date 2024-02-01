# number_server
http based number distribution server


web_count_app.py listens on 

    This Python Flask application provides a simple HTTP service that returns a unique, incrementing number to each visitor. It features Bearer token authentication for security and uses a file-based persistence mechanism to maintain the count across restarts.

    Features
    Bearer Token Authentication: Ensures that only requests with a valid Bearer token can access the incrementing number service.
    Persistent Counting: The count is stored in a file, allowing the service to maintain state between restarts.
    Thread Safety: Implements locking to prevent race conditions when accessing the persistent storage file.
    Requirements
        Python 3.6 or higher
        Flask
        A Unix-like environment (for file locking mechanisms)
    Example useage:
    curl -H "Authorization: Bearer UVB76" http://localhost:9001



installer_number_server.sh

    installer_number_server Bash script automates the creation and management of a systemd service named number_server to run a Python web app, including enabling and starting the service. Check its status with:  systemctl status number_server

