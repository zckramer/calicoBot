import asyncio

class MessageOnTimer:
    def __init__(self, message, frequency, twitch):
        self.message = message
        self.frequency = frequency
        self.twitch = twitch
        self._running = False

    async def _print_message(self):
        while self._running:
            print(self.message)
            await self.twitch.channel.send(self.message)
            await asyncio.sleep(self.frequency)
    
    async def start(self):
        if not self._running:
            self._running = True
            self._task = asyncio.create_task(self._print_message())
    
    async def stop(self):
        if self._running:
            self._running = False
            await self._task
