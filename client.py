import asyncio
import websockets
from datetime import datetime


async def client_connect():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                # Send "Hello Server" and ping every second
                await websocket.send("Hello Server")
                await websocket.send("ping")
                
                # Await and print the server's response
                server_message = await websocket.recv()
                print(f"Received from server: {server_message}")
                
                # Optionally, send a broadcast command every few seconds
                if datetime.now().second % 10 == 0:  # Every 10 seconds
                    await websocket.send("broadcast")
                
                await asyncio.sleep(1)
        
        except websockets.exceptions.ConnectionClosed:
            print("Connection to server closed")

# Uncomment the line below to run the client in a real environment
asyncio.run(client_connect())


