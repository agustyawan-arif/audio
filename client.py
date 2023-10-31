import argparse
import asyncio
import websockets
import pyttsx3

async def receive_and_process_text(language):
    engine = pyttsx3.init() if language == "zh" else pyttsx3.init()  # Initialize the engine if the language is "zh"
    voices = engine.getProperty('voices')
    if language == "zh":
        engine.setProperty('voice', 'zh')

    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            text = await websocket.recv()
            print("Received text:", text)
            # Implement text-to-speech (TTS) functionality here.
            if text != "":
                engine.say(text)
                engine.runAndWait()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-lang', default=None, help="Language argument (e.g., 'zh')")
    args = parser.parse_args()
    
    asyncio.get_event_loop().run_until_complete(receive_and_process_text(args.lang))
