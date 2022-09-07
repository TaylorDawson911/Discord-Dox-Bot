# bot.py
import asyncio
import os
import urllib

import requests
import time
import ipapi
import discord
from discord import Embed
from discord import message
from dotenv import load_dotenv
import what3words
import json
import sys

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
spam = 'true'


@bot.command()
async def stop(ctx):
    global spam
    spam = 'false'
    await ctx.send('All Commands Stopped!')
    time.sleep(5)
    spam = 'true'


@bot.command()
async def iplookup(ctx, ip=None):
    if not ip:
        await ctx.send("Please enter an ip address. for example: '!iplookup 192.168.0.1`")
    else:
        output = ipapi.location(ip)
        output = dict(output)
        templist = ""
        for key, value in output.items():
            templist = f"{templist}\n{key}  - {value}"
            print(templist)

        longitude = ipapi.location(ip, output="longitude")
        latitude = ipapi.location(ip, output="latitude")
        if latitude == "Undefined":
            embed = discord.Embed(title=f"iplookup for {ip}", description=f"{templist}", color=discord.Color.blue())
        else:
            geocoder = what3words.Geocoder("PHJM71BP")
            res = geocoder.convert_to_3wa(what3words.Coordinates(latitude, longitude))
            w3wname = res["words"]
            temp = f"https://www.maps.ie/draw-radius-circle-map/?lat={latitude}&lng={longitude}&radius=4000"
            embed = discord.Embed(title=f"iplookup for {ip}",
                                  description=f"{templist}\nWhat3Words - {w3wname}\nMap Lookup - {temp}",
                                  color=discord.Color.blue())
        embed.set_footer(text="Dox Tool Coded By Ryandigzz")
        embed.set_thumbnail(
            url="https://i.kym-cdn.com/photos/images/newsfeed/000/096/044/trollface.jpg?1296494117")
        await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Welcome To Diggy's Discord Dox Tool", url="https://digzzware.xyz",
                          description="This bot is an OSINT tool developed to gather "
                                      "information more easily about targets\nbelow is a the avaialable commands you "
                                      "can use",
                          color=discord.Color.blue())
    embed.add_field(name="!dox {username}", value="Performs a URL search on the inputted username", inline=True)
    embed.add_field(name="!iplookup {ip}", value="Looks up a certain IP", inline=True)
    embed.add_field(name="!stop", value="Stops all commands currently being entered", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def apply(ctx):
    await ctx.author.send("Hello! I heard you want to make a doxx? Thats Great!")  # Sends a message to the author
    await ctx.author.send("Please Answer these questions below.")  # Sends a message to the author

    questions = ["Name", "Reason of dox", "Location",""]  # Create your list of answers

    answers = []  # Empty list as the user will input the answers

    def check(m):
        return ctx.author == m.author and isinstance(m.channel,
                                                     discord.DMChannel)  # Check that the messages were sent in DM by the right author

    for i in questions:
        await ctx.author.send(i)  # Sends the questions one after another
        try:
            msg = await bot.wait_for('message', timeout=10000, check=check)
        except asyncio.TimeoutError:
            await ctx.author.send("Sorry, You have took to long to answer, Goodbye")
            return  # Will no longer proceed, user has to run the command again
        else:
            answers.append(msg)  # Appends the answers, proceed

    channel = bot.get_channel(971140353619025922)
    e = discord.Embed(color=ctx.author.color)
    e.title = "New application"
    e.description = f"First answer: {answers[0].content} [...]"
    await channel.send(embed=e)


@bot.command()
async def dox(ctx, username=None):
    if not username:
        await ctx.send("Please enter a username, for example: `!dox randomguy247`")
    else:
        ''' INPUT USERNMAE TO DOX '''
        total = "n/a"
        # INSTAGRAM
        instagram = f'https://www.instagram.com/{username}'

        # FACEBOOK
        facebook = f'https://www.facebook.com/{username}'

        # TWITTER
        twitter = f'https://www.twitter.com/{username}'

        # YOUTUBE
        youtube = f'https://www.youtube.com/{username}'

        # BLOGGER
        blogger = f'https://{username}.blogspot.com'

        # GOOGLE+
        google_plus = f'https://plus.google.com/s/{username}/top'

        # REDDIT
        reddit = f'https://www.reddit.com/user/{username}'

        # WORDPRESS
        wordpress = f'https://{username}.wordpress.com'

        # PINTEREST
        pinterest = f'https://www.pinterest.com/{username}'

        # GITHUB
        github = f'https://www.github.com/{username}'

        # TUMBLR
        tumblr = f'https://{username}.tumblr.com'

        # FLICKR
        flickr = f'https://www.flickr.com/people/{username}'

        # STEAM
        steam = f'https://steamcommunity.com/id/{username}'

        # VIMEO
        vimeo = f'https://vimeo.com/{username}'

        # SOUNDCLOUD
        soundcloud = f'https://soundcloud.com/{username}'

        # DISQUS
        disqus = f'https://disqus.com/by/{username}'

        # MEDIUM
        medium = f'https://medium.com/@{username}'

        # DEVIANTART
        deviantart = f'https://{username}.deviantart.com'

        # VK
        vk = f'https://vk.com/{username}'

        # ABOUT.ME
        aboutme = f'https://about.me/{username}'

        # IMGUR
        imgur = f'https://imgur.com/user/{username}'

        # FLIPBOARD
        flipboard = f'https://flipboard.com/@{username}'

        # SLIDESHARE
        slideshare = f'https://slideshare.net/{username}'

        # FOTOLOG
        fotolog = f'https://fotolog.com/{username}'

        # SPOTIFY
        spotify = f'https://open.spotify.com/user/{username}'

        # MIXCLOUD
        mixcloud = f'https://www.mixcloud.com/{username}'

        # SCRIBD
        scribd = f'https://www.scribd.com/{username}'

        # BADOO
        badoo = f'https://www.badoo.com/en/{username}'

        # PATREON
        patreon = f'https://www.patreon.com/{username}'

        # BITBUCKET
        bitbucket = f'https://bitbucket.org/{username}'

        # DAILYMOTION
        dailymotion = f'https://www.dailymotion.com/{username}'

        # ETSY
        etsy = f'https://www.etsy.com/shop/{username}'

        # CASHME
        cashme = f'https://cash.me/{username}'

        # BEHANCE
        behance = f'https://www.behance.net/{username}'

        # GOODREADS
        goodreads = f'https://www.goodreads.com/{username}'

        # INSTRUCTABLES
        instructables = f'https://www.instructables.com/member/{username}'

        # KEYBASE
        keybase = f'https://keybase.io/{username}'

        # KONGREGATE
        kongregate = f'https://kongregate.com/accounts/{username}'

        # LIVEJOURNAL
        livejournal = f'https://{username}.livejournal.com'

        # ANGELLIST
        angellist = f'https://angel.co/{username}'

        # LAST.FM
        last_fm = f'https://last.fm/user/{username}'

        # DRIBBBLE
        dribbble = f'https://dribbble.com/{username}'

        # CODECADEMY
        codecademy = f'https://www.codecademy.com/{username}'

        # GRAVATAR
        gravatar = f'https://en.gravatar.com/{username}'

        # PASTEBIN
        pastebin = f'https://pastebin.com/u/{username}'

        # FOURSQUARE
        foursquare = f'https://foursquare.com/{username}'

        # ROBLOX
        roblox = f'https://www.roblox.com/user.aspx?username={username}'

        # GUMROAD
        gumroad = f'https://www.gumroad.com/{username}'

        # NEWSGROUND
        newsground = f'https://{username}.newgrounds.com'

        # WATTPAD
        wattpad = f'https://www.wattpad.com/user/{username}'

        # CANVA
        canva = f'https://www.canva.com/{username}'

        # CREATIVEMARKET
        creative_market = f'https://creativemarket.com/{username}'

        # TRAKT
        trakt = f'https://www.trakt.tv/users/{username}'

        # 500PX
        five_hundred_px = f'https://500px.com/{username}'

        # BUZZFEED
        buzzfeed = f'https://buzzfeed.com/{username}'

        # TRIPADVISOR
        tripadvisor = f'https://tripadvisor.com/members/{username}'

        # HUBPAGES
        hubpages = f'https://{username}.hubpages.com'

        # CONTENTLY
        contently = f'https://{username}.contently.com'

        # HOUZZ
        houzz = f'https://houzz.com/user/{username}'

        # BLIP.FM
        blipfm = f'https://blip.fm/{username}'

        # WIKIPEDIA
        wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

        # HACKERNEWS
        hackernews = f'https://news.ycombinator.com/user?id={username}'

        # CODEMENTOR
        codementor = f'https://www.codementor.io/{username}'

        # REVERBNATION
        reverb_nation = f'https://www.reverbnation.com/{username}'

        # DESIGNSPIRATION
        designspiration = f'https://www.designspiration.net/{username}'

        # BANDCAMP
        bandcamp = f'https://www.bandcamp.com/{username}'

        # COLOURLOVERS
        colourlovers = f'https://www.colourlovers.com/love/{username}'

        # IFTTT
        ifttt = f'https://www.ifttt.com/p/{username}'

        # EBAY
        ebay = f'https://www.ebay.com/usr/{username}'

        # SLACK
        slack = f'https://{username}.slack.com'

        # OKCUPID
        okcupid = f'https://www.okcupid.com/profile/{username}'

        # TRIP
        trip = f'https://www.trip.skyscanner.com/user/{username}'

        # ELLO
        ello = f'https://ello.co/{username}'

        # TRACKY
        tracky = f'https://tracky.com/user/~{username}'

        # BASECAMP
        basecamp = f'https://{username}.basecamphq.com/login'

        ''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''
        WEBSITES = [
            instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
            wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus,
            medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
            mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
            goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
            dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
            wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
            contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
            bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
        ]

        ''' COLOUR PRINTING FUNCTION '''
        embed = Embed(title=f"{username} Username Search", description=f"Found Matches", color=discord.Color.blue())
        embed.set_footer(text="Dox Tool Coded By Ryandigzz")
        embed.set_thumbnail(
            url="https://i.kym-cdn.com/photos/images/newsfeed/000/096/044/trollface.jpg?1296494117")
        msg = await ctx.send(embed=embed)
        count = 0
        match = True
        username_found_list = str("")
        for url in WEBSITES:
            if spam == 'false':
                break
            try:
                r = requests.get(url, timeout=3)

                if r.status_code == 200:
                    if match == True:
                        temp_embed = Embed(title=f"{username} Username Search", description=f"Found Matches",
                                           color=discord.Color.blue())
                        temp_embed.set_footer(text="Dox Tool Coded By Ryandigzz")
                        temp_embed.set_thumbnail(
                            url="https://i.kym-cdn.com/photos/images/newsfeed/000/096/044/trollface.jpg?1296494117")

                        await msg.edit(embed=temp_embed)
                        match = False
                    if username in r.text:
                        username_found_list = f"{username_found_list}\n{url}  - USERNAME FOUND"
                        print(username_found_list)

                        temp_embed = Embed(title=f"{username} Username Search",
                                           description=f"Found Matches\n{username_found_list} <--- ",
                                           color=discord.Color.blue())
                        temp_embed.set_footer(text="Dox Tool Coded By Ryandigzz")
                        temp_embed.set_thumbnail(
                            url="https://i.kym-cdn.com/photos/images/newsfeed/000/096/044/trollface.jpg?1296494117")
                        await msg.edit(embed=temp_embed)
                        count += 1
                    else:
                        continue

                    total = len(WEBSITES)
                    temp_embed = Embed(title=f"{username} Username Search",
                                       description=f"Found Matches\n{username_found_list}\nA total of {count} MATCHES found out of {total} websites.",
                                       color=discord.Color.blue())
                    temp_embed.set_footer(text="Dox Tool Coded By Ryandigzz")
                    temp_embed.set_thumbnail(
                        url="https://i.kym-cdn.com/photos/images/newsfeed/000/096/044/trollface.jpg?1296494117")
                    await msg.edit(embed=temp_embed)
            except:
                print("error")
                pass


bot.run(TOKEN)
