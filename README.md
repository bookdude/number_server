<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unique Number Service Documentation</title>
</head>
<body>
    <h1>Unique Number Service: A Python Flask Application</h1>
    <p>Welcome to our Unique Number Service, a robust Python Flask application designed to deliver a unique, incrementing number to each visitor. This service is perfect for applications requiring unique identifiers, counters, or simple increment mechanisms. With enhanced security through Bearer token authentication and file-based persistence for reliability, our service stands out as a secure and persistent solution for managing unique counts.</p>

    <h2>Key Features</h2>
    <ul>
        <li><strong>Bearer Token Authentication</strong>: Maximize security with Bearer token verification, ensuring that only authenticated requests access the incrementing number service.</li>
        <li><strong>Persistent Counting</strong>: Leveraging a file-based storage system, our service reliably maintains the count state across application restarts, ensuring continuity and accuracy.</li>
        <li><strong>Thread Safety</strong>: With built-in locking mechanisms, the service is fully thread-safe, preventing race conditions and ensuring consistent access to the persistent storage file.</li>
    </ul>

    <h2>Getting Started</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.6 or higher</li>
        <li>Flask</li>
        <li>A Unix-like environment (necessary for the file locking mechanisms)</li>
    </ul>

    <h3>Installation</h3>
    <pre><code># Clone the repository
git clone https://github.com/yourgithubrepo/number_server.git

# Navigate into the repository
cd number_server

# Install dependencies
pip install flask
    </code></pre>

    <h3>Running the Service</h3>
    <pre><code># Start the Flask application
python app.py
    </code></pre>

    <h2>Example Usage</h2>
    <p>To access the unique number service, use the following curl command:</p>
    <pre><code>curl -H "Authorization: Bearer YOUR_BEARER_TOKEN" http://localhost:9001
    </code></pre>

    <h2>Contributing</h2>
    <p>We welcome contributions! Please read our contributing guidelines to learn how you can help improve the Unique Number Service.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the LICENSE.md file for details.</p>
</body>
</html>