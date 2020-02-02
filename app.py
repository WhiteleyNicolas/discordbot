import discord
import re
from random import randint


donate_string = "https://streamlabs.com/raiders5495/tip"


comebacks = [
    "Too bad you can’t Photoshop your ugly personality.",
    "You should really come with a warning label.",
    "I finally got the last knife of the set you’ve been stabbing in my back all these years. Heads up: I re gift.",
    "Thanks for teaching me how sick and cruel a person can be."
]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as ', self.user)


    async def on_message(self, message):
        if str(message.author).lower() == str("julio#2431"):
            await message.channel.send(comebacks[randint(0, len(comebacks) - 1)])

        print(message.author)

        if message.content == '!nico':
            await message.channel.send('Okay! Boomer')

        elif message.content == '!help!':
            await message.channel.send(self.custom_help_message())

    def custom_help_message(self):
        return "List of all the commands !nico !help \n" + donate_string




client = MyClient()
client.run('secret key')
