import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello World!")
        response = await websocket.recv()
        print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(hello())


# Standard Web Server (HTTP): Every time the client wants data, it performs a full TCP 3-way handshake + TLS handshake (if HTTPS). This adds significant latency.
# WebSocket: It performs the handshake once. After that, the connection stays open. Data is sent in "frames" without the heavy HTTP headers (cookies, user-agents, etc.) every time.

# In a normal Spring Boot REST controller:
# The server cannot talk to the client unless the client asks first.
# If the server has new data (e.g., a price drop), it has to wait for the client to "poll" (refresh).

# In a WebSocket:
# The server can say, "Hey Client, I have new info!" and push it instantly.
# The client doesn't need to request anything; it just sits and listens.