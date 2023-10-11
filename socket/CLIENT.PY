import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"  # Change this to the server's address
    
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter a message to send (or 'exit' to quit): ")
            if message == 'exit':
                break
            await websocket.send(f"manishreal:- {message}")
            
            # Receive and print the server's response
            response = await websocket.recv()
            print(f"Server response: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
