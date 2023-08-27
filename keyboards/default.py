from telegram import KeyboardButton, ReplyKeyboardMarkup


START_KEYBOARD = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('ПОСМОТРЕТЬ ФОТО'),
            KeyboardButton('ПОСЛУШАТЬ ГОЛОС'),
            KeyboardButton('ПОЧИТАТЬ ПРО УВЛЕЧЕНИЕ'),
        ]
    ],
    resize_keyboard=True
)
