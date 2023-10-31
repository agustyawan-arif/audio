import asyncio
import os
import websockets

async def monitor_directory(directory_path, websocket):
    current_files = set()
    while True:
        new_files = set(os.listdir(directory_path))

        # Check for new files
        for file in new_files - current_files:
            current_files.add(file)
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as fx:
                    text = fx.readline()
                    if text.strip():
                        await websocket.send(text)
                        print("Send text:", text)
                        os.remove(file_path)
                    else:
                        os.remove(file_path)

async def main(websocket, path):
    directory_path = 'result'
    await monitor_directory(directory_path, websocket)

if __name__ == "__main__":
    start_server = websockets.serve(main, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
