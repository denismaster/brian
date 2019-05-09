import asyncio
import websockets
import json

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps("Hello world!"))
        async for message in websocket:
            payload = json.loads(message)
            print(payload)
            await websocket.send(json.dumps(input()))

asyncio.get_event_loop().run_until_complete(hello('ws://localhost:8765'))