import asyncio
import json
import websockets
import aioconsole # pip install aioconsole for async input

async def listen_for_messages(websocket):
    """Continuous loop to catch incoming server pushes."""
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"\n[NEW MESSAGE] {data.get('from', 'System')}: {data.get('content', data)}")
    except websockets.exceptions.ConnectionClosed:
        print("Server connection closed.")

async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Step 1: Join a room
        room_id = await aioconsole.ainput("Enter Trip ID to join: ")
        user_name = await aioconsole.ainput("Enter your name: ")
        
        join_payload = {"type": "join", "room_id": room_id}
        await websocket.send(json.dumps(join_payload))

        # Step 2: Run listener in the background
        listener_task = asyncio.create_task(listen_for_messages(websocket))

        # Step 3: Main loop for sending messages
        print("Type messages and press Enter. Type 'exit' to quit.")
        while True:
            content = await aioconsole.ainput("> ")
            if content.lower() == 'exit':
                break
            
            msg_payload = {
                "type": "message",
                "user": user_name,
                "content": content
            }
            await websocket.send(json.dumps(msg_payload))

        listener_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())