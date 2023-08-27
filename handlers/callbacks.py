from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CallbackQueryHandler

from config import SETTINGS, logger, updater
from keyboards.inline import PHOTO_INLINE_KEYBOARD, LAST_PHOTO_INLINE_BUTTON, SCHOOL_PHOTO_INLINE_BUTTON


@logger.catch()
def school_photo(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.delete()
    update.callback_query.message.reply_photo(SETTINGS['photo']['school_photo'],
                                              caption=SETTINGS['photo']['school_photo_caption'],
                                              parse_mode='html',
                                              reply_markup=InlineKeyboardMarkup([[LAST_PHOTO_INLINE_BUTTON]]))


@logger.catch()
def last_photo(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.delete()
    update.callback_query.message.reply_photo(SETTINGS['photo']['last_photo'],
                                              caption=SETTINGS['photo']['last_photo_caption'],
                                              parse_mode='html',
                                              reply_markup=InlineKeyboardMarkup([[SCHOOL_PHOTO_INLINE_BUTTON]]))


@logger.catch()
def gpt_voice(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.reply_voice(SETTINGS['voice']['gpt_voice'],
                                              caption=SETTINGS['voice']['gpt_voice_caption'],
                                              parse_mode='html')


@logger.catch()
def sql_voice(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.reply_voice(SETTINGS['voice']['sql_voice'],
                                              caption=SETTINGS['voice']['sql_voice_caption'],
                                              parse_mode='html')


@logger.catch()
def love_voice(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.reply_voice(SETTINGS['voice']['love_voice'],
                                              caption=SETTINGS['voice']['love_voice_caption'],
                                              parse_mode='html')


updater.dispatcher.add_handler(CallbackQueryHandler(school_photo, pattern='school_photo'))
updater.dispatcher.add_handler(CallbackQueryHandler(last_photo, pattern='last_photo'))

updater.dispatcher.add_handler(CallbackQueryHandler(gpt_voice, pattern='gpt_voice'))
updater.dispatcher.add_handler(CallbackQueryHandler(sql_voice, pattern='sql_voice'))
updater.dispatcher.add_handler(CallbackQueryHandler(love_voice, pattern='love_voice'))
