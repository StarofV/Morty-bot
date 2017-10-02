import hashlib
import os 
import time
import random
import discord
import asyncio
from discord.ext import commands


description = '''(OUTDATED)This bot is made by Rick Sanchez (DogeSec™)#5068
link for my bot: https://discordapp.com/oauth2/authorize?client_id=355185220456153089&scope=bot&permissions=100'''

bot = commands.Bot()

@bot.event
async def on_ready():
      print('Logged in')
      print('Name : {}'.format(bot.user.name))
      print('ID : {}'.format(bot.user.id))
      print(discord.__version__)
      await bot.change_presence(game=discord.Game(name='Trying to imrove myself'))

@bot.event
async def on_message(message):
  if message.content.lower().startswith("Morty "):
    await bot.say(f"But {ctx.message.author.mention}!!! I have so much to live for!")

@bot.event
async def on_message(message):
      if message.content.lower().startswith("How did you like that adventure morty?"):
            await bot.send_message(message.channel, 'Oh jeez rick, that was one hell of an adventure, not sure how am supposed to feel about it')
      await bot.process_commands(message)

@bot.event
async def on_message(message):
      if message.content.lower().startswith('im back'):
            await bot.send_message(message.channel, 'Welcome, but not with us.')
      await bot.process_commands(message)

@bot.event
async def on_message(message):
      if message.content.lower().startswith('suck my balls morty'):
            await bot.send_message(message.channel, 'Geez, I dunno Rick..')
            msg = await bot.wait_for_message(author=message.author, content='why not?')
            await bot.send_message(message.channel, 'Because you are my grandpa, Rick.. Are you insane?!')
      await bot.process_commands(message)

@bot.command(pass_context = True)
async def RPS(ctx, x):
      '''Rock paper scissor game, use like "Morty RPS Rock", etc..'''
      choices = ['rock','paper','scissor']
      computer_choice = random.choice(choices)
      choice = x.lower()
      if choice in choices:
        if choice == computer_choice:
          await bot.say("Tie")
        elif (choice == 'rock' and computer_choice == 'scissor') or \
             (choice == 'paper' and computer_choice == 'rock') or \
             (choice == 'scissor' and computer_choice  == 'paper'):
          await bot.say("You win")
        else:
          await bot.say("You lost!")
          await bot.say(f"I chose {computer_choice} and you chose {choice}... LOL")

@bot.command(pass_context=True)
async def check(ctx, _):
    return await bot.say(random.choice((
        "Maybe",
        "I say no",
        "Yes",
        "Most likely"
    )))

@bot.command(pass_context = True)
async def Binary(ctx, byte):
            while len(byte) == 8:
              decimal = 0
              for num in byte:
                  decimal = decimal*2 + int(num)
              await bot.say(decimal)
              break
            if len(byte) > 8 or len(byte) < 8: #Check length of the binary number
                    await bot.say("Not an 8 bit byte, please try again.")

@bot.command(pass_context = True)
async def Dm(ctx, member : discord.Member = None, *, message):
    if ctx.message.author.id == '289151838618648576':
        await bot.send_message(member, message)
    await bot.process_commands(message)
   

@bot.event
async def on_message(message):
      if message.content("Hey Morty"):
          await bot.add_reaction(message, '✅')
          await bot.send_message(message.channel, "I'm ALIVE!")
          return
      await bot.process_commands(message)

bot.run('Token here plz') #Will make an easy setup soon.
