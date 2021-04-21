TOKEN = "ODM0NTU3NjUxNjc2Mjk5MzM1.YICoYQ.0NkE0wPqHm-oQmE0i2rzKw454CQ"

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!Merhaba bot kardes"):
            await message.reply('Merhabana merhaba Kutay kardes!', mention_author=True)

client = MyClient()
client.run(TOKEN)