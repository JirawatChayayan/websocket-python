import asyncio
import websockets
from datetime import datetime


async def client_connect():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                # Send "Hello Server" every second
                await websocket.send("Hello Server")
                
                # Await and print the server's response
                server_message = await websocket.recv()
                print(f"Received from server: {server_message}")
                
                # Wait for 1 second before sending the next message
                await asyncio.sleep(1)
        
        except websockets.exceptions.ConnectionClosed:
            print("Connection to server closed")

# Uncomment the line below to run the client in a real environment
asyncio.run(client_connect())

