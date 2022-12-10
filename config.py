# Cyberspace bot

##This source serves as a base for Cyberspace store bots.
##It aims to be as modular as possible, allowing adding new features with minor effort.

## Example config file

##```python
# Your Telegram bot token.
BOT_TOKEN = "5963320090:AAHIG9QqyEGRqXjCOvDxca-3JLaQSssQE7Q"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = "18375658"
API_HASH = "8239d19f0c650cd639e3b54f7e491fbc"

# Chat used for logging errors.
LOG_CHAT = -1001659363744

# Chat used for logging user actions (like buy, gift, etc).
ADMIN_CHAT = -1001659363744
GRUPO_PUB = -1001659363744



# How many updates can be handled in parallel.
# Don't use high values for low-end servers.
WORKERS = 20

# Admins can access panel and add new materials to the bot.
ADMINS = [5416629349]

# Sudoers have full access to the server and can execute commands.
SUDOERS = [5416629349]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []

# Bote o Username do bot sem o @
# Exemplo: default
BOT_LINK = "testefisicosbot"



# Bote o Username do suporte sem o @
# Exemplo: suporte
BOT_LINK_SUPORTE = "sltm7"
##```