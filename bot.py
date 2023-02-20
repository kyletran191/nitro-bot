__author__ = 'Kyle Tran'
__version__ = '1.2'
__github__ = 'github.com/kyletran191'
__license__ = 'GNU General Public License v3.0'
#Kyle Tran
#=====Import Module=====#
from discord.ext import commands    
from discord.ext.commands import Bot 
from os import system        
from os import name                  
from colorama import *                                                
import random, datetime, discord, string, numpy, requests                        
year_now= datetime.datetime.now().strftime("%Y")     
token   = '' # your bot token
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
intents.dm_messages = True       
bot     = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")    
#=====Random Color=====#
async def random_color():
    number_lol = random.randint(1, 999999)
    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))
    return number_lol
#=====Bot Command=====#
@bot.command()
async def help(ctx):
        embed = discord.Embed(title="Nitro Code Generator X Checker | ZerosDev", description=f"{ctx.author.mention}", color=await random_color())
        embed.add_field(name = "**Syntax**", value = "```md\n.ncg <amount>```")
        embed.add_field(name = "**NOTE**", value = "> __**Code by Kyle Tran**__ \n\n> Regards, \n> Kyle Tran")
        embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
        await ctx.send(embed=embed)

@bot.command()
async def ncg(ctx, amount : int = None):
    if amount is None:
        embed = discord.Embed(title=f"Error!", description=f"You need a amount! {ctx.author.mention}", color=await random_color())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"Nitro Code Is Generating And Checking...", description=f"{ctx.author.mention}", color=await random_color())
        await ctx.send(embed=embed)
        invalid = 0
        valid = []
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[amount, 16])
        for s in c:
            code = ''.join(x for x in s)
            nitro = f"https://discord.gift/{code}" 
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            response = requests.get(url)  
            if response.status_code == 200:
                embed = discord.Embed(title=f"VALID NITRO CODE | ZerosDev", description=f"{ctx.author.mention}", color=await random_color())
                embed.add_field(name = "**VALID CODE**", value = f"```yaml\n{nitro}```")
                embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                await ctx.send(embed=embed)
                valid.append(nitro)
            else:
                invalid=invalid+1
        embed = discord.Embed(title=f"COMPELETED CHECK | ZerosDev", description=f"{ctx.author.mention}", color=await random_color())
        embed.add_field(name = "**VALID CODE**", value = f"```yaml\n{len(valid)}```")
        embed.add_field(name = "**INVALID CODE**", value = f"```yaml\n{invalid}```")
        embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
        await ctx.send(embed=embed)
@bot.event
async def on_ready():
    banner = f"""
\033[1;96mdb   dD db    db db      d88888b   d8888b.  .d88b.  d888888b 
\033[1;97m88 ,8P' `8b  d8' 88      88'       88  `8D .8P  Y8. `~~88~~' 
\033[1;92m88,8P    `8bd8'  88      88ooooo   88oooY' 88    88    88    
\033[1;93m88`8b      88    88      88~~~~~   88~~~b. 88    88    88    
\033[1;96m88 `88.    88    88booo. 88.       88   8D `8b  d8'    88    
\033[1;97mYP   YD    YP    Y88888P Y88888P   Y8888P'  `Y88P'     YP 
\033[1;92m                                      @kyletran191
\033[1;97m=============================================================
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(banner)
    print(f'\033[1;97mLogged \033[1;96m{bot.user.name}')
    print(f'\033[1;97mBot ID: \033[1;97m{bot.user.id}')
    print('\033[1;97m=============================================================')
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))
if __name__ == '__main__':
    init(convert=True)
    bot.run(token)

