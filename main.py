from keep_alive import keep_alive
import discord
import asyncio

# Replace 'your_token_here' with your actual token
token = 'your_token_here' with your actual token'

# Intents for the bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Initialize the Discord client with intents
client = discord.Client(intents=intents)

# Global variables
message = None

@client.event
async def on_ready():
    print('Bot is ready.')

    # Find the channel where you want to send the message
    channel = client.get_channel(1179699904084463656)  # Replace CHANNEL_ID with the actual channel ID

    # Send the initial message
    global message
    message = await channel.send("Timer: 0 seconds")

    # Pin the message
    await message.pin()

    # Start the timer
    await update_timer()

async def update_timer():
    seconds = 0
    while True:
        # Update the message with the timer
        await message.edit(content=f"Timer: {seconds} seconds")

        # Wait for 1 second
        await asyncio.sleep(1)
        seconds += 1

# Run the client with your token
client.run(token)
