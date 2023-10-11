
import asyncio
import websockets

# Define a function to handle incoming WebSocket connections
async def handle_client(websocket, path):
    try:
        print(websocket)
        async for message in websocket:
            # You can process the received message here
            print(f"Received message: {message}")
            message= input("Enter Your Message ")
            # Send a response back to the client (echo)
            await websocket.send(f"manishcad: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

# Start the WebSocket server
start_server = websockets.serve(handle_client, "localhost", 8765)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
