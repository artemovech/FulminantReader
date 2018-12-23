from application.reader_logic import InitializeReadingApp
import asyncio

if __name__ == "__main__":
    app = InitializeReadingApp()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.start())
    loop.close()
