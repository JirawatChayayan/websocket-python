import asyncio
import websockets
from datetime import datetime

connected_clients = set()

async def handle_client(websocket, path):
    # Register client connection
    connected_clients.add(websocket)
    print(f"Client connected: {path}")
    await websocket.send("Welcome to the server!")
    
    try:
        while True:
            # Send current time to the client every second
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"Hello Client! Current time: {current_time}"
            await websocket.send(message)
            
            # Listen for client messages
            client_message = await websocket.recv()
            print(f"Received from client: {client_message}")
            
            if client_message == "ping":
                # Respond to ping with a pong
                await websocket.send("pong")
            elif client_message == "broadcast":
                # Broadcast a message to all connected clients
                broadcast_message = f"Broadcast message from {path}"
                await asyncio.wait([client.send(broadcast_message) for client in connected_clients])
            else:
                print(f"Unknown command from client: {client_message}")
            
            await asyncio.sleep(1)
    
    except websockets.exceptions.ConnectionClosed:
        print(f"Client {path} disconnected")
    finally:
        # Unregister client on disconnect
        connected_clients.remove(websocket)

async def start_server():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("Server started on ws://localhost:8765")
    await server.wait_closed()

# Uncomment the line below to run the server in a real environment
asyncio.run(start_server())
