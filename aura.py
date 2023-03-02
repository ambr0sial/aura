from discord.ext import commands, tasks
import discord
import asyncio
import json
import os

with open('conf.json') as f:
	config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
mode = config.get('mode')

aura = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=None)

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

@aura.event
async def on_ready():
	clear()
	print(f'[AURA] Logged in as: {aura.user} (ID: {aura.user.id})')
	print('------\n')

@aura.event
async def on_command(ctx):
	print(f"[AURA] Executed command > {ctx.command.name}\n")

@aura.command()
async def stats(ctx):
	server = ctx.guild
	total_members = server.member_count
	online_members = len([m for m in server.members if m.status == discord.Status.online])
	text_channels = len(server.text_channels)
	voice_channels = len(server.voice_channels)
	bots = len([m for m in server.members if m.bot])
	categories = len(server.categories)
	roles = len(server.roles)
	emojis = len(server.emojis)
	region = server.region
	verification_level = server.verification_level
	default_notifications = server.default_notifications
	explicit_content_filter = server.explicit_content_filter
	server_name = server.name
	server_icon = server.icon_url
	server_banner = server.banner_url

	if mode == 'embed':
		embed = discord.Embed(title=f'Aura - Stats for {server_name}', color=discord.Color.blue())
		embed.set_thumbnail(url=server_icon)
		embed.set_image(url=server_banner)
		embed.add_field(name='Total Members', value=total_members, inline=True)
		embed.add_field(name='Online Members', value=online_members, inline=True)
		embed.add_field(name='Categories', value=categories, inline=True)
		embed.add_field(name='Text Channels', value=text_channels, inline=True)
		embed.add_field(name='Voice Channels', value=voice_channels, inline=True)
		embed.add_field(name='Bots', value=bots, inline=True)
		embed.add_field(name='Roles', value=roles, inline=True)
		embed.add_field(name='Emojis', value=emojis, inline=True)
		embed.add_field(name='Region', value=region, inline=True)
		embed.add_field(name='Verification Level', value=verification_level, inline=True)
		embed.add_field(name='Default Notifications', value=default_notifications, inline=True)
		embed.add_field(name='Explicit Content Filter', value=explicit_content_filter, inline=True)
		await ctx.send(embed=embed)
	elif mode == 'codeblock':
		if server_icon == None:
			server_icon = "Not any!"
		if server_banner == None:
			server_banner = "Not any!"
		stats = f"""```ansi
[ [2;34mAura[0m - Stats for [2;31m{server_name}[0m ]

• [2;34mServer Icon[0m: {server_icon}
• [2;34mServer Banner[0m: {server_banner}
• [2;34mTotal Members[0m: {total_members}
• [2;34mOnline Members[0m: {online_members}
• [2;34mCategories[0m: {categories}
• [2;34mText Channels[0m: {text_channels}
• [2;34mVoice Channels[0m: {voice_channels}
• [2;34mBots[0m: {bots}
• [2;34mRoles[0m: {roles}
• [2;34mEmojis[0m: {emojis}
• [2;34mRegion[0m: {region}
• [2;34mVerification Level[0m: {verification_level}
• [2;34m[2;34mDefault Notifications[0m[2;34m[0m: {default_notifications}
• [2;34mExplicit Content Filter[0m: {explicit_content_filter}```"""
		await ctx.send(stats)

@aura.command()
async def cls(ctx):
	clear()
	print(f'[AURA] Logged in as: {aura.user} (ID: {aura.user.id})')
	print('------\n')

@aura.command()
async def ping(ctx):
	latency = round(bot.latency * 1000)
	if mode == 'embed':
		embed = discord.Embed(title=f'Aura - Ping', color=discord.Color.blue())
		embed.set_thumbnail(url="https://user-images.githubusercontent.com/81994421/222477873-b62baf91-9968-45be-9537-3562b1a2ef4a.png")
		embed.add_field(name='Latency', value=latency, inline=True)
	elif mode == 'codeblock':
		await ctx.send(f"""```ansi
[ [2;34mAura[0m - Ping ]

• [2;34mLatency[0m: {latency}```""")

aura.run(token)