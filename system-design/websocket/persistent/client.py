import asyncio
import websockets

async def listen():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        print("Connected to server. Waiting for pushes...")
        
        # This loop keeps the client alive
        async for message in websocket:
            print(f"Received from server: {message}")

if __name__ == "__main__":
    try:
        asyncio.run(listen())
    except KeyboardInterrupt:
        print("Client closed.")


# Standard Web Server (HTTP): Every time the client wants data, it performs a full TCP 3-way handshake + TLS handshake (if HTTPS). This adds significant latency.
# WebSocket: It performs the handshake once. After that, the connection stays open. Data is sent in "frames" without the heavy HTTP headers (cookies, user-agents, etc.) every time.

# In a normal Spring Boot REST controller:
# The server cannot talk to the client unless the client asks first.
# If the server has new data (e.g., a price drop), it has to wait for the client to "poll" (refresh).

# In a WebSocket:
# The server can say, "Hey Client, I have new info!" and push it instantly.
# The client doesn't need to request anything; it just sits and listens.

# WebSockets vs. Webhooks: A Comparison
# While both technologies provide real-time data, they operate in opposite ways.
# 1. The Direct Comparison
# WebSockets are for continuous, two-way talk. Think of it like a phone call where the line stays open.
# Webhooks are for one-way, event-driven alerts. Think of it like a text message sent only when something happens
# 2. Use Cases
# Use WebSockets for live chats, gaming, or real-time dashboards where constant updates are needed.
# Use Webhooks for notifications like payment confirmations, form submissions, or any event where the server needs to inform another system.