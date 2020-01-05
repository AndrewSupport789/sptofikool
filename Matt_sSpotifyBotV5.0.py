import discord
import json, aiohttp
import re, os , time , subprocess , colorama
from os import listdir
from os.path import isfile, join
from colorama import init, Fore, Back, Style
from discord.ext import commands
init()

reminder = 'Do not forget try all links for all accounts!'

owo = "**__We are sorry but bot will be offline for other servers for few days due low account stock!__**"

msgg = '```Check your DMs man!```'

client = commands.Bot(command_prefix='!')
#client = discord.Client()
Clientdiscord = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['web: www.rabbits-gen.cf', 'With BlackRabbit', 'discord.gg/cZ8GcPF', '!cmds for commands', '!cmds'])

client.remove_command('help')

@client.command()
async def clr(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx):
    check_role = get(ctx.message.guild.roles, name='BAN-SQUAD')
    if check_role in ctx.author.roles:
        await ctx.send("https://gifimage.net/wp-content/uploads/2017/07/ban-hammer-gif-14.gif")
    else:
        await ctx.send("You can't use this!")




@client.event
async def on_message(message):
 message.content = message.content.lower().replace(' ', '')
 await client.wait_until_ready()
 print(message.author.name)
 twitter = ' ;) '
 if message.content.startswith("!hello"):
        print(message.author.name)
        embed = discord.Embed(color=0xFF09D7)

        await message.author.send(embed=embed)
        
        
 async def redeem(ctx, country: str,email: str, code: str):
        """ You can use this command to upgrade your account to premium.
            country - Country you live in, and you have spotify account in.
            email - Your email address, where bot will send invitation link.
            code - code you bought in order to upgrade your account.
        """
        await ctx.channel.purge(limit=1)
        if str(ctx.channel) in Channel:
            if '@' in email:
                if code not in bot.codes:
                    embed = discord.Embed(
                    title=f"{ctx.author} That's a bad upgrade key, sorry :/, please try again. It's possible that code wasn't in system so far", color=0xff5959)
                    with open(Codes, "r") as file:
                        bot.codes = [code.strip("\n") for code in file.readlines()]
                        print(Fore.GREEN + 'Codes file refreshed, new codes can be used now')
                    message = await ctx.send(embed=embed)
                    print(Fore.RED + f'@{ctx.author} tried to upgrade with an invalid upgrade key ({code})')
                    print(Fore.RESET)
                    return
                try:  # Check if code file does exist
                    with open(Codes, "r") as file:
                        bot.codes = [code.strip("\n") for code in file.readlines()]
                        print(Fore.GREEN + 'Codes file refreshed, new codes can be used now')
                except FileNotFoundError:
                    print(Fore.RED +
                          "Codes file can't be found or does not exist, please create new one or move it to same folder where exe of your bot is")
                    print(Fore.RED + f'@{ctx.author} tried to upgrade with an invalid upgrade key ({code})')
                    print(Fore.RESET)
                    return
                else:
                    print(Fore.YELLOW + f"@{ctx.author} upgrading his account {email} from {country.upper()} in paid mode with code {code}")
                    print(Fore.RESET)
                    result = 'false'
                    tries = 0
                    embed = discord.Embed(
                        title="Searching for an account...", color=0xffa500)
                    message = await ctx.send(embed=embed)
                    while result != "true":
                        while tries <= 5:
                            try:
                                with open(f"Accounts/{country.upper()}.txt") as filehandle:
                                    lines = filehandle.readlines()
                                with open(f"Accounts/{country.upper()}.txt", 'w') as filehandle:
                                    lines = filter(lambda x: x.strip(), lines)
                                    filehandle.writelines(lines)
                            except FileNotFoundError:
                                embed = discord.Embed(
                                    title=f"Sorry, but we currently don't have any stocks for {country.upper()}", color=0xff5959)
                                await message.edit(embed=embed)
                                print (Fore.RED + f"User @{ctx.author} tried to upgrade his account, but {country.upper()} is already out of stock or never had any stocks")
                                print (Fore.RESET)
                                result = "true"
                                break
                            try:
                                with open('Accounts/'+f'{country.upper()}'+'.txt','r') as (f):
                                    for line in f:
                                        clean = line.split('\n')
                                        Accounts.append(clean[0])
                                        lines = f.readlines()
                            except FileNotFoundError:
                                embed = discord.Embed(
                                title=f"Sorry, but We currently don't offer upgrades in this country.", color=0xd3d3d3)
                                await ctx.send(embed=embed)
                                result = "true"
                                break
                            try:
                                account = Accounts.pop()
                                embed = discord.Embed(
                                    title="An account has been found.", color = 0x00FF00
                                    )
                                await message.edit(embed=embed)
                            except IndexError:
                                embed = discord.Embed(
                                    title=f"Sorry, but {country.upper()} is currently out of stock.", color = 0xff5959
                                    )
                                await message.edit(embed=embed)
                                print (Fore.RED + f"User @{ctx.author} tried to upgrade his account, but {country.upper()} is already out of stock or never had any stocks")
                                print (Fore.RESET)
                                result = "true"
                                break
                            combo = account.split(':')
                            user = combo[0]
                            password = combo[1]
                            embed = discord.Embed(
                                title=f"Trying to send an invite...", color=0xffa500)
                            await message.edit(embed=embed)
                            async with aiohttp.ClientSession() as session:
                                url = 'https://accounts.spotify.com/en/login?continue=https://www.spotify.com/int/account/overview/'
                                headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
                                response = await session.get(url, headers=headers)
                                CSRF = session.cookie_jar.filter_cookies(url)[
                                    'csrf_token'
                                ].value

                                headers = {
                                    'Accept': '*/*',
                                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
                                    'Referer': 'https://accounts.spotify.com/en/login/?continue=https://www.spotify.com/us/googlehome/register/&_locale=en-US'
                                }

                                url = 'https://accounts.spotify.com/api/login'

                                credentials = {
                                    'remember': 'true',
                                    'username': user,
                                    'password': password,
                                    'csrf_token': CSRF
                                }

                                cookies = dict(
                                    __bon='MHwwfC0xNDAxNTMwNDkzfC01ODg2NDI4MDcwNnwxfDF8MXwx')

                                postLogin = await session.post(url, headers=headers, data=credentials, cookies=cookies)

                                postLoginJson = await postLogin.json()
                                if Debug == "Debug":
                                    print(postLoginJson)
                                    print(postLoginJson.get('error'))
                                errorMessage = postLoginJson.get('error')
                                if errorMessage == "errorInvalidCredentials":
                                    with open(f"Accounts/{country.upper()}.txt", "w") as f:
                                            for line in lines:
                                                if line.strip("\n") != f"{user}:{password}":
                                                    f.write(line)
                                            result = 'false'
                                            tries += 1
                                            if Debug == "Debug":
                                                print(Fore.RED + f"Failed to upgrade {ctx.author} retrying...({tries})")
                                                print(Fore.RESET)
                                            if tries >= 5:
                                                embed = discord.Embed(
                                                    title=f"There were some issues, retrying.", color=0xd3d3d3)
                                                await message.edit(embed=embed)
                                elif 'displayName' in postLoginJson:
                                    if 1 == 1:
                                        url = "https://www.spotify.com/us/account/overview/"

                                        secondLogin = await session.get(url, headers=headers)
                                        csrf = secondLogin.headers['X-Csrf-Token']

                                        url = 'https://www.spotify.com/us/home-hub/api/v1/family/home/'

                                        headers = {
                                            'Accept': '*/*',
                                            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
                                            'x-csrf-token': csrf
                                        }
                                        async with await session.get(url,headers=headers) as resp:
                                            WebsiteResponse = await resp.json()
                                            if Debug == "Debug":
                                                print(Fore.RESET + f"{WebsiteResponse}")
                                            accessControl = WebsiteResponse["accessControl"]
                                            Slots = accessControl["planHasFreeSlots"]
                                            if Slots is True:
                                                Address = WebsiteResponse["address"]
                                                inviteToken = WebsiteResponse["inviteToken"]
                                                embed = discord.Embed(
                                                    title=f"Invitation code was sent, check private messages @{ctx.author}.", color=0x00FF00)
                                                await message.edit(embed=embed)
                                                print(Fore.GREEN + f'@{ctx.author} successfully upgraded his account {email} from {country.upper()} in free mode')
                                                await ctx.author.send(f"In order to upgrade your account please click on lin below, and enter prov"
                                                                           f"\nFill in these informations in form!"
                                                                           f"\n"
                                                                           f'\n**Address**: `{Address}`'
                                                                           f'\n**Invite Link**: https://www.spotify.com/{country.lower()}/family/join/invite/{inviteToken}'
                                                                           f'\n**You can add random {country.upper()} address if these fields are empty.**'
                                                                           )
                                                bot.codes.remove(code)  # Remove code from codes list after user got invite code.
                                                with open("codes.txt", "a") as file:
                                                    file.truncate(0)
                                                    for code in bot.codes:
                                                        file.write(f"{code}\n")
                                                result = "true"
                                                break
                                            elif Slots is False:
                                                tries += 1
                                                if Debug == "Debug":
                                                    print(Fore.RED + f"Failed to upgrade {ctx.author} retrying...({tries})")
                                                    print(Fore.RESET)
                                                embed = discord.Embed(
                                                title=f"There were some issues, retrying.", color=0xd3d3d3)
                                                await message.edit(embed=embed)
                                                with open(f"Accounts/{country.upper()}.txt", "w") as f:
                                                    for line in lines:
                                                        if line.strip("\n") != f"{user}:{password}":
                                                            f.write(line)
                                                result = 'false'
                                    else:
                                        tries += 1
                                        if Debug == "Debug":
                                            print(Fore.RED + f"Failed to upgrade {ctx.author} retrying...({tries})")
                                            print(Fore.RESET)
                                        embed = discord.Embed(
                                        title=f"There were some issues, retrying.", color=0xd3d3d3)
                                        await message.edit(embed=embed)
                                        with open(f"Accounts/{country.upper()}.txt", "w") as f:
                                            for line in lines:
                                                if line.strip("\n") != f"{user}:{password}":
                                                    f.write(line)
                                        result = 'false'
                        if result == "true":
                            break
                        if tries >= 6:
                            if Debug == "Debug":
                                            print(Fore.RED + f"Failed to upgrade user bacuse of too many fails")
                                            print(Fore.RESET)
                            embed = discord.Embed(
                                        title=f"Oops, we're not able to upgrade your account at the moment, please try again later.", color=0xff5959)
                            await message.edit(embed=embed)
                            print(Fore.RED + f"Seems like there are some issues with {country.upper()} please check your stock if there isn't something weird happening.")
                            print(Fore.RESET)
                            return
            else:
                if Debug == "Debug":
                    print(Fore.RED + f"User {ctx.author} tried to upgrade with invalid email address {email}")
                    print(Fore.RESET)
                embed = discord.Embed(
                    title=f"Please use valid email address in order to upgrade your account.", color=0xff5959)
                await ctx.send(embed=embed)
        else: 
            embed = discord.Embed(
                title=f"You can only use this command in #{Channel}", color=0xd3d3d3)
            message = await ctx.send(embed=embed)



#embed.add_field(name="link #2:", value="https://up-to-down.net/27527/pinterest", inline=False)
		
@client.event
async def on_ready():
    change_status.start()

    
client.run(os.getenv('BOT_TOKEN'))
