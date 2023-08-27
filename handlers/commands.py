from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters

from config import updater, SETTINGS, logger
from keyboards.default import START_KEYBOARD
from keyboards.inline import PHOTO_INLINE_KEYBOARD, LINK_INLINE_KEYBOARD, VOICE_INLINE_KEYBOARD


@logger.catch()
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(SETTINGS['start'], parse_mode='HTML', reply_markup=START_KEYBOARD)


@logger.catch()
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(SETTINGS['help'], parse_mode='HTML', reply_markup=START_KEYBOARD)


@logger.catch()
def code_source(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(SETTINGS['code_source'], parse_mode='HTML', reply_markup=LINK_INLINE_KEYBOARD)


@logger.catch()
def photo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(SETTINGS['photo']['message'], parse_mode='HTML', reply_markup=PHOTO_INLINE_KEYBOARD)


@logger.catch()
def voice(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(SETTINGS['voice']['message'], parse_mode='HTML', reply_markup=VOICE_INLINE_KEYBOARD)


@logger.catch()
def hobby(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(SETTINGS['hobby'], parse_mode='MarkdownV2')


@logger.catch()
def last_handler(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(SETTINGS['any'])


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('code_source', code_source))

updater.dispatcher.add_handler(MessageHandler(Filters.text('ПОСМОТРЕТЬ ФОТО'), photo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('ПОСЛУШАТЬ ГОЛОС'), voice))
updater.dispatcher.add_handler(MessageHandler(Filters.text('ПОЧИТАТЬ ПРО УВЛЕЧЕНИЕ'), hobby))

updater.dispatcher.add_handler(MessageHandler(Filters.all, last_handler))
