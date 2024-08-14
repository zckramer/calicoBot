import asyncio
import os
import random
from timedMessenger import MessageOnTimer
from twitchio.ext import commands
from supabase import create_client, Client
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# Replace these with your own values
twitchToken: str = os.getenv('TMI_TOKEN')
twitchClientID: str = os.getenv('CLIENT_ID')
twitchChannelName: str = os.getenv('CHANNEL')

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

HAIKUS = [
    "An old silent pond... | A frog jumps into the pond— | Splash! Silence again.",
    "Over the wintry | Forest, winds howl in rage | With no leaves to blow.",
    "In the cicada's cry | No sign can foretell | How soon it must die.",
    "The light of a candle | Is transferred to another candle— | Spring twilight",
    "The light of a candle | Is transferred to another candle— | Spring twilight",
    "A world of dew, | And within it, a world of willow | And a world of dew.",
    "The sea darkens— | The voices of the wild ducks | Are faintly white.",
]

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=twitchToken, client_id=twitchClientID, prefix='!', initial_channels=[twitchChannelName])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Call command handler
        await self.handle_commands(message)
        prefix = '>'
        
        if message.content.startswith(prefix + 'selfPromo'):
            row = supabase.table("timers").select("*").eq("timer_id", 1).execute()
            phrase = row.data[0]['messages'] 
            frequency = row.data[0]['frequency']  # frequency in seconds
            theMessage = MessageOnTimer(phrase, frequency, message)
            await theMessage.start()
            
            try:
                await asyncio.sleep(3600)
                # Run for 10 seconds for demonstration
                # await asyncio.sleep(10)
                # 3600 seconds in an hour
            finally:
                await message.channel.send('command: selfPromo finished running')
                await theMessage.stop()
            
        if message.content.startswith(prefix + 'haiku'):
            haiku = random.choice(HAIKUS)
            await message.channel.send(haiku)
            
    @commands.command(name='userinfo')
    async def user_info(self, ctx: commands.Context):
        # Fetch user information
        user = ctx.author
        if user.is_mod:
            response = 'User is mod'
        if user.is_broadcaster:
            response = 'User is broadcaster'
        else:
            response = 'User not authenticated.'
        await ctx.send(response)

#INIT AND MAIN BEHAVIOR
async def main():
    bot = Bot()
    await bot.start()
        
if __name__ == '__main__':
    asyncio.run(main())

# list social links
# timer to repeat ! commands
#   - specific commands
#   - all status being repeated
#   - set timer for repeat
#   - set individual timers
#   - show timer on a command
#   - create multiple timers
# web GUI for bot stats (outside of chat)
#   - Status of bot/timers
#   - PM / Notifications
