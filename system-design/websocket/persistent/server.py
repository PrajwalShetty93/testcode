import asyncio
import websockets
import datetime

async def push_updates(websocket):
    print("Client connected!")
    try:
        while True:
            # The server decides when to send data
            now = datetime.datetime.now().strftime("%H:%M:%S")
            await websocket.send(f"Server Push: The time is {now}")
            await asyncio.sleep(2) 
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")

async def main():
    async with websockets.serve(push_updates, "localhost", 8765):
        await asyncio.Future() # Run forever

if __name__ == "__main__":
    asyncio.run(main())