# Discord Bot
A Discord Bot that connects to the Microsoft Azure Speech Cloud Service to provide a server with a better text-to-speech option.
It also uses Selenium to webscrape Google, Bing, Reddit, and Instagram with the goal of providing the users with a "Left vs Right" game.

## Text to Speech
The Microsoft Speech Cloud Service provides a very natural sounding tts and a large selection of languages. This bot automates the process of retrieving
an mp3 file from the service based on your desired text and playing it through your mic in a voice channel.

demo image here


## Left versus Right
demo here
## Motivation
**This code is now outdated due to changes in the discord API, so this is purely for showcasing purposes.**
This bot was primarily meant for providing a server with a custom text-to-speech (utilizes Microsoft Azure's Speech Cloud Service) and automating certain tasks like searching for and scraping images from Google/Bing/Reddit/TikTok.

## Dependencies:
- Selenium
- youtube-dl

## Notable Libraries:
discord
requests
pillow

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

