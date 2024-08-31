import asyncio
import websockets
from datetime import datetime

async def handle_client(websocket, path):
    print(f"New client connected: {path}")
    
    try:
        while True:
            # Sending a message to the client every second
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"Hello Client! Current time: {current_time}"
            await websocket.send(message)
            
            # Await and print any messages received from the client
            client_message = await websocket.recv()
            print(f"Received from client: {client_message}")
            
            # Wait for 1 second before sending the next message
            await asyncio.sleep(1)
    
    except websockets.exceptions.ConnectionClosed:
        print(f"Client {path} disconnected")

async def start_server():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("Server started on ws://localhost:8765")
    await server.wait_closed()

# Uncomment the line below to run the server in a real environment
asyncio.run(start_server())

