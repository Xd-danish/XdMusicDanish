#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of  🅐Ⓓ🅐Ⓡ🅢Ⓗ✨🅣Ⓘ🅦Ⓐ🅡Ⓘ

# Kanged By © @Hitler_fed_owner
# Hitler © @Hitler_fed
# Owner  🅐Ⓓ🅐Ⓡ🅢Ⓗ✨🅣Ⓘ🅦Ⓐ🅡Ⓘ 
# Dr Victor
# All rights reserved. Yukki

from AasthaMusicBot.core.bot import AlexaBot
from AasthaMusicBot.core.dir import dirr
from AasthaMusicBot.core.git import git
from AasthaMusicBot.core.userbot import Userbot
from AasthaMusicBot.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = AlexaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
