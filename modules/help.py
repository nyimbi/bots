import logging
from telegram.ext import CommandHandler
from telegram.ext import BaseFilter
from telegram.ext.dispatcher import run_async
from telegram import ParseMode


logger = logging.getLogger(__name__)

class FilterPrivateChat(BaseFilter):
    def filter(self, message):
        return message.chat_id > 0

private_chat = FilterPrivateChat()

help_message = """\
Welcome to NyimbiBot!
/start - start
/help - get this help text
/ocr - convert image to text
Take a picture of a printed page and send to this bot
"""

@run_async
def send_help(bot, update):
	logger.info("start or help command")
	bot.send_message(update.message.chat_id, help_message,
		parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

class module:
	name = "help"
	handlers = (
		CommandHandler(["start", "help"], send_help),
	)