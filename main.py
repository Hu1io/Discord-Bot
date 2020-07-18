import discord
from rss import RssAggregator


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            print("----Ping Detected----")
            print(message.author, ': ', message.content)
            print("Response: pong\n")
            await message.channel.send('pong')

    async def on_refresh(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == 'test':
            print('----New RSS Feed----')
            await message.channel.send(RssAggregator("https://www.theguardian.com/world/coronavirus-outbreak/rss").completeRssFeed)

client = MyClient()
client.run('TOKEN')

