import os
import discord
import youtube_dl
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="temb"), status=discord.Status.idle)
    print("ready")

@bot.command()
async def help(ctx):
    await ctx.send("If you wanna commands then go to this website `http://temb.glitch.me`.")

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You arent in the voice channel")

    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
        await ctx.send(f"Joined to `{ctx.author.voice.channel.name}`")
    else:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
        await ctx.send(f"Joined to `{ctx.author.voice.channel.name}`")

@bot.command()
async def disconnect(ctx):
    if ctx.author.voice is None:
        await ctx.send("You arent in the voice channel")
    else:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected")

@bot.command()
async def play(ctx,url):
    if ctx.author.voice is None:
        await ctx.send("You arent in the voice channel")
    else:
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()
            await ctx.send(f"Joined to `{ctx.author.voice.channel.name}`")
        else:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
            await ctx.send(f"Joined to `{ctx.author.voice.channel.name}`")

        with youtube_dl.YoutubeDL({'format': "bestaudio"}) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url2,**{
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn'
            })
            ctx.voice_client.play(source)
            await ctx.send(f"Now Playing `{url}`")

@bot.command()
async def pause(ctx):
    if ctx.author.voice is None:
        await ctx.send("You arent in the voice channel")
    else:
        await ctx.voice_client.pause()
        await ctx.send("Paused")

@bot.command()
async def resume(ctx):
    if ctx.author.voice is None:
        await ctx.send("You arent in the voice channel")
    else:
        await ctx.voice_client.resume()
        await ctx.send("Resumed")

if __name__ == "__main__":
    bot.run(os.environ['token'])
