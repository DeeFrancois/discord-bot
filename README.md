# Discord Bot
A Discord Bot that connects to the Microsoft Azure Speech Cloud Service to provide a server with a better text-to-speech option.
It also uses Selenium to webscrape Google, Bing, Reddit, and Instagram with the goal of providing the users with a "Left vs Right" game.

## Text to Speech
The [Microsoft Speech Cloud Service](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/text-to-speech) provides a very natural sounding tts and a large selection of languages. This bot automates the process of retrieving
an mp3 file from the service based on your desired text and playing it through your mic in a voice channel. 

![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/tts_demo.gif)


## Left versus Right
The "Left vs Right" game is a server activity that relies on the bot automatically searching for, downloading, and combining two images which are then voted on by the members. The bot can accomplish this by scraping from Bing, Reddit, or Instagram.
#### Scraping from Bing
```
"Which doctor is better?"
"Tenth for sure"
"No it's def Matt Smith, what are you smoking"
"START THE VOTE"
`lrbing Eleventh+Doctor Tenth+Doctor 
```

![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/bing_demo.gif)

#### Scraping from Instagram
![demo](https://github.com/DeeFrancois/discord-bot/blob/main/DocumentationImages/ig_demo.gif)

## External Dependencies:
- Selenium
- youtube-dl
- ffmpeg 
- Discord


## Main Python Libraries:
- Discord API
- requests
- Pillow

## Features:
- Custom TTS powered by Microsoft Azure
(demo video of discord and folder with subtitles, provide a side by side of azure's options for languages/voices with the retrieval command )
- Webscraping for Reddit/Bing/Google
(demo video of selenium)
- Autodetect TikTok and Reddit links and reupload upload a compressed version
(demo video of bot messages (can do a pretend version manually))
- Image Processing;  
(photo example with movie posters)
- Automated moderation commands (cleaning up chat)

