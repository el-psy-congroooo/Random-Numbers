import websockets
import asyncio
import random
import time


async def response(websocket, path):
    msg = await websocket.recv()
    print(f"", msg)
    while True:    
        await websocket.send(str(random.randint(0,100)))
        time.sleep(1)

start_server = websockets.serve(response, 'localhost', 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
