import discord
from discord.ext import commands
from dotenv import load_dotenv
import sentiment_analysis
import music_recommendation
import os


load_dotenv()

# Initialize bot
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()
async def sentiment(ctx, *, text: str):
    sentiment = sentiment_analysis.analyze(text)
    await ctx.send(f"Sentiment: {sentiment}")


@bot.command()
async def recommend(ctx, mood: str):
    recommendation = music_recommendation.get_recommendation(mood)
    await ctx.send(f"Recommended: {recommendation}")


# Run the bot
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
