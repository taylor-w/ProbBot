#Import random library
#Import discord library
import random
import discord

#Define main fxn
def main():
    rng()
    dis()

#Define rng fxn
def rng():
    task = str(input('What is the task at hand? '))
    prob = (random.random() * 100)
    print('The likelihood of ' + task + ' is ' + format(prob, '.2f') + '%.')

#Define dis fxn
def dis():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_msg(msg):
        if msg.author == client.user:
            return
        
        if msg.content.startswith('$hello'):
            await message.channel.send('Howdy!')

    client.run('PIZZA')

main()