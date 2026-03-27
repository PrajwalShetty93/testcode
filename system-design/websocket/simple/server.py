import asyncio
import websockets

async def echo(websocket):
    # Receive a message from the client
    message = await websocket.recv()
    print(f"Received: {message}")
    
    # Send a response back
    await websocket.send(f"Server says: I got your message! ({message})")

async def main():
    # Start server on localhost port 8765
    async with websockets.serve(echo, "localhost", 8765):
        print("Server is running...")
        await asyncio.Future()  # Keeps the server running forever

if __name__ == "__main__":
    asyncio.run(main())