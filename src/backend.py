import asyncio
import websockets
import signal
import json

async def wakeup():
    while True:
        await asyncio.sleep(1)

async def echo(websocket, path):
    async for message in websocket:
        payload = json.loads(message)
        await websocket.send(json.dumps(payload.split()))

loop = asyncio.get_event_loop()
# # add wakeup HACK
loop.create_task(wakeup())

try:
    loop.run_until_complete(websockets.serve(echo, 'localhost', 8765))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()