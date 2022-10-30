# bot.py
# This is very old very ugly code, it was one of my first "big" python projects and the focus was purely on getting what the client wanted functioning
# This will not run as sensitive but required info has been hidden. This is just for proof that I actually did it.
import os
import random
import logging
from discord.utils import get
import discord
from dotenv import load_dotenv
import numpy as np
from PIL import Image
import time
import subprocess
from bs4 import BeautifulSoup
import re
import urllib.request
from urllib.request import Request,urlopen
import requests

##TTS

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-text-to-speech-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)


# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "[REDACTED]", "eastus"




def speech_synthesis_to_mp3_file(text):
    """performs speech synthesis to an mp3 file"""
    # Creates an instance of a speech config with specified subscription key and service region.
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Sets the synthesis output format.
    # The full list of supported format can be found here:
    # https://docs.microsoft.com/azure/cognitive-services/speech-service/rest-text-to-speech#audio-outputs
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)
    # Creates a speech synthesizer using file as audio output.
    # Replace with your own audio file name.
    voice = "Microsoft Server Speech Text to Speech Voice (hi-IN, Hemant)"
    speech_config.speech_synthesis_voice_name = voice

    file_name = "ttsaudio.mp3"
    file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)
    
    # Receives a text from console input and synthesizes it to mp3 file.
    result = speech_synthesizer.speak_text_async(text).get()
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(text, file_name))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    
def downloadtiktok(link):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    firstRedirect = requests.get(link).url.split('.html?')[0]
    secondRedirect = requests.get(firstRedirect,headers=headers).url
    #thirdRedirect 
    id = link.split('.com/')[1].replace('/','')
    process = subprocess.Popen(fr'yt-dlp -o "tiktok.mp4" -v "{secondRedirect}"',shell=True)
    process.wait()
    print("Waiting for process")
    process.kill()





#####################
def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst
def combiner():
    list_im = ['combineOne.jpg', 'combineTwo.jpg',]
    imgs    = [ Image.open(i) for i in list_im ]

    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( 'outputComb.jpg' )    

def get_concat_h_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
    if im1.height == im2.height:
        _im1 = im1
        _im2 = im2
    elif (((im1.height > im2.height) and resize_big_image) or
          ((im1.height < im2.height) and not resize_big_image)):
        _im1 = im1.resize((int(im1.width * im2.height / im1.height), im2.height), resample=resample)
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize((int(im2.width * im1.height / im2.height), im1.height), resample=resample)
    dst = Image.new('RGB', (_im1.width + _im2.width, _im1.height))
    dst.paste(_im1, (0, 0))
    dst.paste(_im2, (_im1.width, 0))
    return dst

async def sayTheLine(name):
    channel = client.get_channel('[REDACTED]')
    voice = get(client.voice_clients, guild=channel.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    
    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print("Bot connected")
        
    #name = 'audioo.mp3'
    voice.play(discord.FFmpegPCMAudio(name), after=lambda e: print(f"{name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1
    time.sleep(10)
    await voice.disconnect()
#######################################################################################################

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

     
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(status=discord.Status.invisible)

@client.event 
async def on_voice_state_update(Member,before,after): # Do something whenever someone joins
    if not Member.bot and not before.channel:
        print("{0} just joined.".format(Member))
    
    elif not Member.bot:
        print("{0} has left the voice channel".format(Member.name))

    if not Member.bot and not before.channel and Member.id == '[REDACTED]':
        joined = "{0} just joined channel: {1}".format(Member,after.channel.name)
        #await sayTheLine("mp3/__.mp3")

@client.event
async def on_message(message): # Chat commands
        
    if message.channel.id != '[REDACTED]':
        print(message.channel.id)
        print(message.content)
        return

    if message.author == client.user:
        return

    if message.author.id == '[REDACTED]':
        message.channel.send("")
        return

    if message.content == '' and message.author != client.user and message.channel == '[REDACTED]': #Left V Right Channel
        await message.add_reaction('⬅')
        await message.add_reaction('➡')
        return

    if message.content == '`say':
        response = random.choice(quotes)
        await message.channel.send(response)
        return

    if message.content == '`help':
        await message.channel.send("Do `lr Left+Image Right+Image") 
        return

    if message.content == '`spam':
        await message.channel.send("spam")
        await message.channel.send("spam")
        await message.channel.send("spam")
        await message.channel.send("spam")
        await message.channel.send("spam")
        await message.channel.send("spam")
        return


    if message.content.startswith('`clean media'): # Delete Last X media messages 
        try:
            delete_count = message.content.split(' ')[2]
        except:
            delete_count = 10
        counter = 0
        async for message in message.channel.history(limit=int(delete_count)):
            if message.content == '':
                await message.delete()
                counter = counter + 1
        await message.channel.send("Cleaned {0} Images.".format(counter))
        return

    if message.content.startswith('`clean humans'): # Delete Last X non-bot messages
        try:
            delete_count = message.content.split(' ')[2]
        except:
            delete_count = 10
        counter = 0
        async for message in message.channel.history(limit=int(delete_count)):
            if message.content.startswith('`') or message.author != client.user and message.content != '':
                await message.delete()
                counter = counter + 1
        await message.channel.send("Cleaned {0} messages.".format(counter))
        return

    if message.content.startswith('`clean'): # Delete last X messages
        try:
            delete_count = message.content.split(' ')[1]
            print(delete_count)
        except:
            delete_count = 10
        counter = 0
        async for message in message.channel.history(limit=int(delete_count)):
            if message.content != '':
                await message.delete()
                counter = counter + 1
        await message.channel.send("Cleaned {0} messages.".format(counter))
        return

    if message.content == '`test':
        sent = await message.channel.send(file=discord.File('test.webm'))
        await sent.add_reaction('⬅')
        await sent.add_reaction('➡')
        return
    
    if message.content == '`check': 
        try:
            limit_num = message.content.split(' ')[1]
        except:
            limit_num = 40
        imgCount = 0
        async for message in message.channel.history(limit=limit_num):
            if message.content == '' and message.author == client.user:
                imgCount = imgCount + 1
                
        await message.channel.send("There are {0} images".format(imgCount))
        return

    if message.content == '`line':
        channel = message.author.voice.channel
        voice = get(client.voice_clients, guild=message.guild)
        
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await chan.connect()
        
        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await chan.connect()
            print("Bot connected")
            
        name = 'audioo.mp3'
        voice.play(discord.FFmpegPCMAudio("auido3.mp3"), after=lambda e: print(f"{name} has finished playing"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1
        time.sleep(5)
        await voice.disconnect()
        return
            
    #if message.content == '`line':    
    if message.content.startswith('`showme'):
        loading = await message.channel.send("Pulling random gif from folder...")
        fileSentNum = random.randint(1,20)
        sent = await message.channel.send(file=discord.File('toSend{0}'.format(fileSentNum)))
        return

    if message.content.startswith('`lrig'):
        argss = message.content.split()
        loading=await message.channel.send("Grabbing images from: Instagram...")
        os.system(("InstagramScraper.py {0} {1}").format(argss[1].replace(' ',"+"),argss[2].replace(' ',"+")))
        sent = await message.channel.send(file=discord.File('igOutput.jpg'))
        await sent.add_reaction('⬅')
        await sent.add_reaction('➡')
        #await message.delete()
        await loading.delete()
        return
    
    elif message.content.startswith('`lrbing'):
        argss = message.content.split()
        loading=await message.channel.send("Grabbing images from: Bing..")
        os.system(("BingScraper.py {0} {1}").format(argss[1].replace(' ',"+"),argss[2].replace(' ',"+")))
        sent = await message.channel.send(file=discord.File('bingOutput.jpg'))
        await sent.add_reaction('⬅')
        await sent.add_reaction('➡')
        #await message.delete()
        await loading.delete()
        return

    elif message.content.startswith('`lr'):
        argss = message.content.split()
        loading=await message.channel.send("Grabbing images from: Reddit....")
        os.system(("RedditScraperSFW.py {0} {1}").format(argss[1].replace(' ',"+"),argss[2].replace(' ',"+")))
        sent = await message.channel.send(file=discord.File('output.jpg'))
        await sent.add_reaction('⬅')
        await sent.add_reaction('➡')
        #await message.delete()
        await loading.delete()
    elif message.content.startswith('`lrmanual'):
        argss = message.content.split()
        os.system(("picDownloader.py {0} {1}").format(argss[1],argss[2]))
        combiner()
        sent = await message.channel.send(file=discord.File('outputComb.jpg'))
        await sent.add_reaction('⬅')
        await sent.add_reaction('➡')
        await message.delete()

    elif message.content == '`purge':
        counter = 0
        async for message in message.channel.history(limit=1000):
                await message.delete()
                counter = counter + 1
        await message.channel.send("Cleaned {0} Messages.".format(counter))

    elif message.content.startswith('`tts'):
        await message.delete()
        sent = await message.channel.send("Retrieving your tts..")
        argss = message.content.split("tts",1)[1]
        print("Requesting: EN (US) - 'Hello, this is my custom tts powered by Microsoft Azure Speech. blah. ha, haha' ")
        speech_synthesis_to_mp3_file(argss)
        print("ttsaudio.mp3 recieved, joining server for playback")
        await sent.delete()
        sent = await message.channel.send("tts retrieval successful, joining voice channel")
        chan = message.author.voice.channel
        voice = get(client.voice_clients, guild=message.guild)
        
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await chan.connect()
        
        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await chan.connect()
            print("Bot connected")
        
        name = 'ttsaudio.mp3'
        
        voice.play(discord.FFmpegPCMAudio("ttsaudio.mp3"), after=lambda e: print(f"{name} has finished playing. Leaving voice channel"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1
        time.sleep(10)
        await sent.delete()
        await voice.disconnect()
    
    elif message.content.startswith('https://www.tiktok.com/') or message.content.startswith('vm.tiktok.com') or message.content.startswith('www.tiktok.com') or message.content.startswith('https://vm.tiktok.com'):
        sent_initial = await message.channel.send("Tiktok detected; fetching video")
        link = message.content
        progress = await message.channel.send("Downloading..")
        downloadtiktok(link)
        
        print("Waiting for process")
        size = os.stat('tiktok.mp4').st_size
        if(size > 5194303):

            toolarge = await message.channel.send("The video is too long. Here's a 10 second preview")
            process = subprocess.Popen(fr'ffmpeg -i tiktok.mp4 -t 10 preview.mp4')
            process.wait()
            if os.stat('preview.mp4').st_size > 5194303:
                
                compression = await message.channel.send("still too large, compressing")
                process = subprocess.Popen(fr'ffmpeg -i preview.mp4 -vcodec libx265 -crf 28 -preset veryfast compressed.mp4')
                process.wait()
                fin = await message.channel.send("Finished. Here's the video")
                sent = await message.channel.send(file=discord.File('compressed.mp4'))
                os.remove('compressed.mp4')
                os.remove('tiktok.mp4')
                os.remove('preview.mp4')

                await progress.delete()
                await toolarge.delete()
                await fin.delete()
                await compression.delete()
                await sent_initial.delete()


            else:

                fin = await message.channel.send("Finished. Here's the video")
                sent = await message.channel.send(file=discord.File('preview.mp4'))
                os.remove('preview.mp4')
                os.remove('tiktok.mp4')
                await progress.delete()
                await toolarge.delete()
                await sent_initial.delete()
                #await sent.delete()

        else:

            await sent_initial.delete()
            await progress.delete()
            await message.channel.send("Here is your tiktok @{0}".format(message.author))
            sent = await message.channel.send(file=discord.File('tiktok.mp4'))
            os.remove('tiktok.mp4')

    elif 'reddit.com' in message.content:

        sent = await message.channel.send("Ooo a reddit link.. lemme get that for ya")
        link = message.content
        process = subprocess.Popen(fr'youtube-dl.exe -o C:\Users\dee\Desktop\Github_Projects\discordbot\reddit.mp4 -v --no-playlist "{link}"',shell=True)
        process.wait()
        print("Waiting for process")
        process.kill()
        size = os.stat('reddit.mp4').st_size
        if(size > 4194303):
            await message.channel.send("File is larger than the upload limit, attempting to compress...This may take a while")
            process = subprocess.Popen(fr'ffmpeg -i reddit.mp4 compressed.webm')
            process.wait()
            if os.stat('compressed.webm').st_size > 4194304:
                await message.channel.send("File is still too large.. FUCK")
            else:
                await message.channel.send("Finished. Here is the video")
                sent = await message.channel.send(file=discord.File('compressed.webm'))
                os.remove('compressed.webm')
                os.remove('reddit.mp4')
        else:
            await message.channel.send("Here is the video {0}".format(message.author))
            await message.channel.send(file=discord.File('reddit.mp4'))
            os.remove('reddit.mp4')
        process.kill()
        await message.channel.send("Here is the video {0}".format(message.author))


client.run(token)