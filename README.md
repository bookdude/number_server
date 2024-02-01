# Unique Number Service: A Python Flask Application

Welcome to our Unique Number Service, a robust Python Flask application designed to deliver a unique, incrementing number to each visitor. This service is perfect for applications requiring unique identifiers, counters, or simple increment mechanisms. With enhanced security through Bearer token authentication and file-based persistence for reliability, our service stands out as a secure and persistent solution for managing unique counts.

## Key Features

-   **Bearer Token Authentication**: Maximize security with Bearer token verification, ensuring that only authenticated requests access the incrementing number service.
-   **Persistent Counting**: Leveraging a file-based storage system, our service reliably maintains the count state across application restarts, ensuring continuity and accuracy.
-   **Thread Safety**: With built-in locking mechanisms, the service is fully thread-safe, preventing race conditions and ensuring consistent access to the persistent storage file.

## Getting Started

### Prerequisites

-   Python 3.6 or higher
-   Flask
-   A Unix-like environment (necessary for the file locking mechanisms)

### Installation

bashCopy code

`# Clone the repository
git clone https://github.com/yourgithubrepo/number_server.git

# Navigate into the repository
cd number_server

# Install dependencies
pip install flask

### Running the Service

bashCopy code

`# Start the Flask application
python app.py` 

## Example Usage

To access the unique number service, use the following curl command:

bashCopy code

`curl -H "Authorization: Bearer YOUR_BEARER_TOKEN" http://localhost:9001` 

Replace `YOUR_BEARER_TOKEN` with your valid Bearer token to authenticate and receive a unique, incrementing number.

## Contributing

We welcome contributions! Please read our contributing guidelines to learn how you can help improve the Unique Number Service.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
