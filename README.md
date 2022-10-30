# Discord Bot
A Discord Bot that connects to the Microsoft Azure Speech Cloud Service to provide a server with a better text-to-speech option.
It also uses Selenium to webscrape Google, Bing, Reddit, and Instagram with the goal of providing the users with a "Left vs Right" game.

## Text to Speech
The [Microsoft Speech Cloud Service](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/text-to-speech) provides a very natural sounding tts and a large selection of languages. This bot automates the process of retrieving
an mp3 file from the service based on your desired text and playing it through your mic in a voice channel. 

![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/tts_demo.gif)


## Left versus Right
The "Left vs Right" game is a server activity that relies on the bot automatically searching for, downloading, and combining two images which are then voted on by the members. The bot can accomplish this by scraping from Bing, Reddit, or Instagram.

```
"Which doctor is better?"
"Tenth for sure"
"No it's def Matt Smith, what are you smoking"
"START THE VOTE"
`lrbing Eleventh+Doctor Tenth+Doctor 
```
#### Scraping from Bing and Instagram
![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/bing_demosmall.gif)
![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/ig_demosmall.gif)

## External Dependencies:
- Selenium https://selenium-python.readthedocs.io/
- youtube-dlp https://github.com/yt-dlp/yt-dlp
- ffmpeg https://ffmpeg.org/download.html

## Main Python Libraries:
- Discord API 
- requests
- Pillow

requirements.txt file included so you can use pip to install the rest

    pip3 install -r requirements.txt
    
## TikTok / Reddit video detection, downloading, and compression
The bot also is capable of uploading linked TikTok/Reddit videos so that they can be watched within Discord itself. If the file size is too big, it will compress or trim the file using ffmpeg

##### Best Case
![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/tiktok_demo1.gif)
##### Compression
![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/tiktok_demo2.gif)

## Features:
- Custom TTS powered by Microsoft Azure
- Webscraping for Reddit/Bing/Google/Instagram
- Autodetect TikTok and Reddit links and reupload upload a compressed version
- Image Processing (To combine images for Left v Right game)
- Automated moderation commands (cleaning up chat)

Licensed under the [MIT License](LICENSE).
