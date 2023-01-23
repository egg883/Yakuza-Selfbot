from asyncio.windows_events import NULL
import asyncio
from urllib import response
import aiohttp
import re
from win10toast import ToastNotifier
from requests.utils import CaseInsensitiveDict
from itertools import cycle
from colour import Color
import time
import datetime, io, random, datetime
import json
from discord.ext import tasks
from discord.ext import commands
from colorama import Fore
import psutil
import sys
import urllib
import discord
import ctypes
from gtts import gTTS
from pypresence import Presence
import requests, wmi
import os
# ---------------------------------------- Imports

config = json.load(open('config.json', 'rb'))

def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0000000000000000000000001)

########### >> Defining
os.system("color")

########### >> Variables

########### >> Classes
class Colours:
    White = "\x1b[38;2;250;250;250m"
    Magenta = "\x1b[38;2;255;94;255m"

def new_splash():
    typingprint(f"""
                            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||                                           
                                             __   __    _                   
                                             \ \ / /   | |                  
                                              \ V /__ _| | ___   _ ______ _ 
                                               \ // _` | |/ / | | |_  / _` |
                                               | | (_| |   <| |_| |/ / (_| |
                                               \_/\__,_|_|\_\\__,_/___\__,_|
                            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    
                                                Cmds: {len(bot.commands)}       Prefix: {config['prefix']}
                                                Logged in as: {Colours.Magenta}{str(bot.user)}
                              
""")
prefix = config['prefix']
version = "1.0"
ids = "584879487850643456", "701792352301350973"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')
def restart_bot(): 
  #os.execv(sys.executable, ['python'] + sys.argv)
  os.execv(sys.executable,sys.argv)

print(chr(27) + "[2J")

def Clear():
    os.system('cls')

def is_me(m):
    return m.author == bot.user

snipermode = 1
gsniper= 1

giveaway_ids =   ["294882584201003009","716967712844414996","796315281688494081","673918978178940951","396464677032427530"]


@bot.event
async def on_message(message):
    time = datetime.datetime.now().strftime("%H:%M")
    start = datetime.datetime.now()
    token = config.get('token')
    headers = {'Authorization': token}

    def GiveawayData():
        print(f"{Colours.Magenta}[blicky Sniper] Giveaway Bot Used: {message.author}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Sniper] Server: {message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Sniper] Channel: {message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Sniper] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}" + Colours.White)
    
    def GiveawayData2():
        print(f"{Colours.Magenta}[blicky Skipped] Giveaway Bot Used: {message.author}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Server: {message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Channel: {message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Reason: ITS SUS CUTIE I SAVED YOU" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}" + Colours.White)

    def NitroData(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code sent by: {Fore.WHITE}{message.author}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code: {Fore.WHITE}{code}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Server: {Fore.WHITE}{message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Channel: {Fore.WHITE}{message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Status: {Fore.LIGHTGREEN_EX}REAL" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Snipe Time: {Fore.WHITE}{delay}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}API Delay: {Fore.WHITE}{response}ms" + Colours.White)

    def NitroData2(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code sent by: {Fore.WHITE}{message.author}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code: {Fore.WHITE}{code}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Server: {Fore.WHITE}{message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Channel: {Fore.WHITE}{message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Status: {Fore.LIGHTRED_EX}FAKE" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Snipe Time: {Fore.WHITE}{delay}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}API Delay: {Fore.WHITE}{response}ms" + Colours.White)

    def NitroData3(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code sent by: {Fore.WHITE}{message.author}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code: {Fore.WHITE}{code}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Server: {Fore.WHITE}{message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Channel: {Fore.WHITE}{message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Status: {Fore.YELLOW}ALREADY REDEEMED" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Snipe Time: {Fore.WHITE}{delay}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}API Delay: {Fore.WHITE}{response}ms" + Colours.White)

    if 'discord.gift/' in message.content:
        if snipermode == 1:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
            r = requests.post(f'https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem',headers=headers).text
            delay = datetime.datetime.now() - start
            delay = f'{delay.seconds}.{delay.microseconds}'
            if 'This gift has been redeemed already.' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Colours.White)
                NitroData3(delay, code)

            elif 'subscription_plan' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Colours.White)
                NitroData(delay, code)

            elif 'Unknown Gift Code' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Colours.White)
                NitroData2(delay, code)
            else:
                return

    if 'GIVEAWAY' in message.content:
        if gsniper == 1:
            if str(message.author.id) in giveaway_ids:
                embed = message.embeds[0].to_dict()
                prize = embed["author"]["name"]
                if "ban" in prize.lower() or "kick" in prize.lower() or "mute" in prize.lower() or "punish" in prize.lower() or "lol" in prize.lower() or "test" in prize.lower() or "fake" in prize.lower():
                    print(f"\n[{time}] - Giveaway Skipped")
                    GiveawayData2()
                else:
                    await asyncio.sleep(5)
                    await message.add_reaction("🎉")          
                    print(f"\n[{time}] - Giveaway Sniped And Entered")
                    GiveawayData()

    if f'Congratulations <@{bot.user.id}>' in message.content:
        if gsniper == 1:
            if str(message.author.id) in giveaway_ids:   
                print(f"\n[{time}] - Giveaway Has Been Won")
                GiveawayData()
        else:
            return

    await bot.process_commands(message)

@bot.event
async def on_connect():
    title = ctypes.windll.kernel32.SetConsoleTitleW(f"Yakuza Selfbot | Version: [{version}]  | Commands: [{len(bot.commands)}]") 
    time.sleep(1)
    title
    new_splash()


@bot.command()
async def nitrosnipermode(ctx):
        await ctx.message.delete()
        global snipermode
        if snipermode == 0:
            snipermode += 1        
        elif snipermode == 1:
            snipermode  -= 1

@bot.command()
async def blacklist(ctx):
    await ctx.message.delete()
    if ctx.message.author.id in ids:
        await ctx.send("Unfortunately, you have been blacklisted from the bot. If you wish to know why or appeal, join this server:")


@bot.command()
async def gsnipermode(ctx):
        await ctx.message.delete()
        global gsniper
        if gsniper == 0:
            gsniper += 1        
        elif gsniper == 1:
            gsniper -= 1


def color_fade(fade_ticks, *colors: list, repeat=False):
        if colors == ():
            colors = [[255, 0, 0], [255, 255, 0], [0, 128, 0], [0, 0, 255]]
        else:
            colors = list(colors)
        if repeat:
            colors.append(colors[0])
        active_RGB = colors[0].copy()
        active_RGB_list = []
        for color_pos, color in enumerate(colors[:-1]):
            for i in range(fade_ticks):
                active_RGB_list.append(active_RGB.copy())
                for pos, RGB in enumerate(color):
                    if color_pos == len(colors) - 1:
                        color_pos = 0
                        RGB2 = colors[color_pos+1][pos]
                    else:
                        RGB2 = colors[color_pos+1][pos]
                    distance = RGB2 - RGB
                    active_RGB[pos] += int(distance / fade_ticks)
        return active_RGB_list

def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb

def RGB_to_hex(RGB):
        for pos in range(len(RGB)):
            RGB[pos] = str(RGB[pos])
        hex_list = []
        hex_list.extend("0123456789ABCDEF")
        all_combo = [f"{x}{y}" for x in hex_list for y in hex_list]
        for pos, color in enumerate(RGB.copy()):
            RGB[pos] = all_combo[int(color)]
        return f"0x{''.join(RGB)}"



#/////// HELP ///////

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Help Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]     
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]general »» Displays general commands                            ║
║══════════════════════════════════════════════════════════════════════║
                            YAKUZA ON TOP                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    typingprint(Colours.Magenta+"[Command] <>Help Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])


# bot.run(config["token"], bot=False)
def Init():
    with open('config.json', encoding="utf-8") as f:
        config = json.load(f)
    token = config.get('token')
    try:
        bot.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        input(f"{Fore.RED}[SYSTEM] TOKEN IS INVALID CHECK CONFIG"+Colours.White)
        sys.exit
        python = sys.executable
        os.execl(python, python, * sys.argv)
Init()
