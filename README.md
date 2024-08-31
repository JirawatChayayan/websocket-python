# WebSocket Server and Client

This project implements a simple WebSocket server and client using Python. The server and client communicate by sending messages every second, with additional features like ping-pong responses, broadcasting, and client connection tracking.

## Features

- **WebSocket Server:**
  - Sends a "Hello Client + current time" message every second.
  - Handles multiple clients.
  - Responds to "ping" messages with "pong".
  - Broadcasts messages to all connected clients on receiving a "broadcast" command.
  - Tracks client connections and disconnections.

- **WebSocket Client:**
  - Connects to the server and sends a "Hello Server" message every second.
  - Sends a "ping" message and expects a "pong" response.
  - Sends a "broadcast" command every 10 seconds.

## Requirements

- Python 3.7+
- `websockets` library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/websocket-server-client.git
   cd websocket-server-client
   ```
   
2. Install the required Python packages

   ```bash
   pip install websockets
   ```
3.Usage
- **Running the Server**
  - Navigate to the project directory.
  - Run the server script:
     ```bash
     python server.py
     ```
  - The server will start listening on ws://localhost:8765.



- **Running the Client**
  - In a separate terminal, navigate to the project directory.
  - Run the client script:
     ```bash
     python client.py
     ```
  - The client will connect to the server and start sending messages.

4.Customization
  - You can customize the behavior of the server and client by modifying the respective Python scripts:

    - server.py: Customize how the server handles different client messages, broadcasts, or other events.
    - client.py: Customize the messages sent to the server, or add new commands.
