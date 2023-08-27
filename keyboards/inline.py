from telegram import InlineKeyboardButton, InlineKeyboardMarkup


SCHOOL_PHOTO_INLINE_BUTTON = InlineKeyboardButton('МОЕ ФОТО ИЗ СТАРШЕЙ ШКОЛЫ', callback_data='school_photo')
LAST_PHOTO_INLINE_BUTTON = InlineKeyboardButton('МОЕ ПОСЛЕДНЕЕ СЕЛФИ', callback_data='last_photo')


PHOTO_INLINE_KEYBOARD = InlineKeyboardMarkup(
    [
        [SCHOOL_PHOTO_INLINE_BUTTON],
        [LAST_PHOTO_INLINE_BUTTON],
    ],
)

VOICE_INLINE_KEYBOARD = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('ЧТО ТАКОЕ GPT', callback_data='gpt_voice')],
        [InlineKeyboardButton('В ЧЕМ ОТЛИЧИЕ МЕЖДУ SQL И NOSQL', callback_data='sql_voice')],
        [InlineKeyboardButton('ИСТОРИЯ ПЕРВОЙ ЛЮБВИ', callback_data='love_voice')],
    ],
)

LINK_INLINE_KEYBOARD = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('ПЕРЕЙТИ НА GITHAB', callback_data='last_photo',
                              url='https://github.com/Andrey-Savitskiy/Test_help_bot')],
    ],
)
