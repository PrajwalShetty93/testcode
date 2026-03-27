import asyncio
import json
import websockets
from collections import defaultdict

# Stores room_id -> set of client websockets
rooms = defaultdict(set)

async def handle_client(websocket):
    current_room = None
    try:
        async for message in websocket:
            data = json.loads(message)
            msg_type = data.get("type")

            # 1. Action: Join a specific room
            if msg_type == "join":
                current_room = data.get("room_id")
                rooms[current_room].add(websocket)
                print(f"Client joined room: {current_room}")
                await websocket.send(json.dumps({"status": "joined", "room": current_room}))

            # 2. Action: Message to a specific room
            elif msg_type == "message" and current_room:
                payload = json.dumps({
                    "from": data.get("user"),
                    "content": data.get("content")
                })
                # Broadcast only to people in THIS room
                if rooms[current_room]:
                    await asyncio.gather(
                        *[client.send(payload) for client in rooms[current_room]]
                    )

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cleanup: Remove from room on disconnect
        if current_room in rooms:
            rooms[current_room].remove(websocket)
            if not rooms[current_room]: # Delete empty room
                del rooms[current_room]
        print("Client disconnected.")

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("Uber-style Pub/Sub Server running on port 8765...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())