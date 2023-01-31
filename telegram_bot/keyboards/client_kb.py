from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query


# Токен
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


# Клавиатура номер 1 (выбором языка)
mainMenu_en_rus = InlineKeyboardMarkup(row_width=2)
lang_rus = InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus")
lang_en = InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en")

# Добавляем кнопки для клавиатуры c выбором языка
mainMenu_en_rus.add(lang_en).add(lang_rus)


# Клавиатура номер 1.2 (выбором языка)
mainMenu_en_rus_two = InlineKeyboardMarkup(row_width=2)
lang_rus_two = InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus_two")
lang_en_two = InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en_two")

# Добавляем кнопки для клавиатуры c выбором языка
mainMenu_en_rus_two.add(lang_en_two)
mainMenu_en_rus_two.add(lang_rus_two)



# English
# Клавиатура номер 1 (English_main_menu)
en_mainMenu = InlineKeyboardMarkup(row_width=2)
en_in_our_games = InlineKeyboardButton(text="Our games 🎮", callback_data="en_in_our_games")
en_in_social_network = InlineKeyboardButton(text="Social Media 🌍", callback_data="en_in_social_network")
en_in_FAQ = InlineKeyboardButton(text="FAQ❓", callback_data="en_in_FAQ")
en_in_Profile = InlineKeyboardButton(text="Profile 🧒", callback_data="en_in_Profile")
en_in_donation = InlineKeyboardButton(text="Support 💰", callback_data="en_in_donation")
en_back_mainMenu = InlineKeyboardButton(text="Back", callback_data="en_back_mainMenu")

# Добавляем кнопки для клавиатуры номер 1 (English)
en_mainMenu.add(en_in_our_games, en_in_social_network).add(en_in_FAQ, en_in_Profile)
en_mainMenu.add(en_in_donation)
en_mainMenu.add(en_back_mainMenu)


# Клавиатура номер 2 (Наши игры)
en_in_our_games = InlineKeyboardMarkup(row_width=2)
en_in_ios = InlineKeyboardButton(text="IOS 🍏", callback_data="en_in_ios")
en_in_android = InlineKeyboardButton(text="ANDROID 🤖", callback_data="en_in_android")
en_in_pc = InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc")
en_in_web_games = InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="en_in_web_games")
en_back_games = InlineKeyboardButton(text="Back", callback_data="en_back_games")

# Добавляем кнопки для клавиатуры номер 2 (Наши игры)
en_in_our_games.add(en_in_ios, en_in_android)
en_in_our_games.add(en_in_pc, en_in_web_games)
en_in_our_games.add(en_back_games)


# Клавиатура номер 3 (ios)
en_in_ios = InlineKeyboardMarkup(row_width=2)
en_back_ios = InlineKeyboardButton(text="Back", callback_data="en_back_ios")

# Добавляем кнопки для клавиатуры 3 (ios)
en_in_ios.add(en_back_ios)


# Клавиатура номер 4 (android)
en_in_android = InlineKeyboardMarkup(row_width=2)
en_in_google_play = InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="en_in_google_play")
en_in_cars_two = InlineKeyboardButton(text="Cars 🚗", url="https://disk.yandex.ru/d/VEy132RmANfIMA", callback_data="en_in_cars_two")
en_back_android = InlineKeyboardButton(text="Back", callback_data="en_back_android")

# Добавляем кнопки для клавиатуры номер 4 (android)
en_in_android.add(en_in_google_play, en_in_cars_two)
en_in_android.add(en_back_android)


# Клавиатура номер 5 (pc)
en_in_pc = InlineKeyboardMarkup(row_width=2)
en_in_mod_bl = InlineKeyboardButton(text="ES MOD 🧚‍♂️", callback_data="en_in_mod_bl")
en_in_horror = InlineKeyboardButton(text="Horror 🧟‍♂️", url="https://disk.yandex.ru/d/nzt0GC6gXpJ83w", callback_data="en_in_horror")
en_back_pc = InlineKeyboardButton(text="Back", callback_data="en_back_pc")

# Добавляем кнопки для клавиатуры номер 5 (pc)
en_in_pc.add(en_in_mod_bl, en_in_horror)
en_in_pc.add(en_back_pc)


# Клавиатура номер 6 (web_games)
en_in_web_games = InlineKeyboardMarkup(row_width=2)
en_in_pc_web_games = InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc_web_games")
en_in_phone_web_games = InlineKeyboardButton(text="PHONE 📱", callback_data="en_in_phone_web_games")
en_back_in_web_games= InlineKeyboardButton(text="Back", callback_data="en_back_in_web_games")

# Добавляем кнопки для клавиатуры номер 6 (web_games)
en_in_web_games.add(en_in_pc_web_games, en_in_phone_web_games)
en_in_web_games.add(en_back_in_web_games)


# Клавиатура номер 7 (pc_web_games)
en_in_pc_web_games = InlineKeyboardMarkup(row_width=2)
en_in_pc_web_games_game_one = InlineKeyboardButton(text="Warrunner 🪖", url="https://okko.tv/serial/game-of-thrones", callback_data="en_in_pc_web_games_game_one")
en_back_in_pc_web_games = InlineKeyboardButton(text="Back", callback_data="en_back_in_pc_web_games")

# Добавляем кнопки для клавиатуры номер 7 (pc_web_games)
en_in_pc_web_games.add(en_in_pc_web_games_game_one)
en_in_pc_web_games.add(en_back_in_pc_web_games)


# Клавиатура номер 8 (phone_web_games)
en_in_phone_web_games = InlineKeyboardMarkup(row_width=2)
en_in_phone_web_games_game_one = InlineKeyboardButton(text="Race 🏎️", url="https://okko.tv/serial/game-of-thrones", callback_data="en_in_phone_web_games_game_one")
en_back_in_phone_web_games = InlineKeyboardButton(text="Back", callback_data="en_back_in_phone_web_games")

# Добавляем кнопки для клавиатуры номер 8 (phone_web_games)
en_in_phone_web_games.add(en_in_phone_web_games_game_one)
en_in_phone_web_games.add(en_back_in_phone_web_games)


# Клавиатура номер 9 (google_play)
en_in_google_play = InlineKeyboardMarkup(row_width=2)
en_in_google_play_game_one = InlineKeyboardButton(text="Cars 🚗", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="en_in_google_play_game_one")
en_back_in_google_play = InlineKeyboardButton(text="Back", callback_data="en_back_in_google_play")

# Добавляем кнопки для клавиатуры номер 9 (google_play)
en_in_google_play.add(en_in_google_play_game_one)
en_in_google_play.add(en_back_in_google_play)


# Клавиатура номер 10 (Мод БЛ)
en_in_mod_bl = InlineKeyboardMarkup(row_width=2)
en_in_mod_bl_downl = InlineKeyboardButton(text="Download our mod for the game ES 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="en_in_mod_bl_downl")
en_back_mod = InlineKeyboardButton(text="Back", callback_data="en_back_mod")

# Добавляем кнопки для клавиатуры номер 10 (Мод БЛ)
en_in_mod_bl.add(en_in_mod_bl_downl)
en_in_mod_bl.add(en_back_mod)


# Клавиатура номер 11 (социальные сети)
en_in_social_network = InlineKeyboardMarkup(row_width=2)
en_in_youtube_one = InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw", callback_data="en_in_youtube_one")
en_in_youtube_two = InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg", callback_data="en_in_youtube_two")
en_in_twitch = InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn", callback_data="en_in_twitch")
en_in_discord = InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm", callback_data="en_in_discord")
en_in_github = InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif", callback_data="en_in_github")
en_in_vk = InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg", callback_data="en_in_vk")
en_back_social = InlineKeyboardButton(text="Back", callback_data="en_back_social")

# Добавляем кнопки для клавиатуры номер 11 (социальные сети)
en_in_social_network.add(en_in_youtube_one, en_in_youtube_two).add(en_in_twitch, en_in_discord)
en_in_social_network.add(en_in_github, en_in_vk)
en_in_social_network.add(en_back_social)


# Клавиатура номер 12 (FAQ)
en_in_FAQ = InlineKeyboardMarkup(row_width=2)
en_in_FAQ_ds = InlineKeyboardButton(text="Here ⬆", url = "https://1drv.ms/w/s!AtF4vCOqewgBoCr1uMzSn-xf_3fV?e=rmxrjf", callback_data="en_in_FAQ_ds")
en_back_faq = InlineKeyboardButton(text="Back", callback_data="en_back_faq")

# Добавляем кнопки для клавиатуры номер 12 (FAQ)
en_in_FAQ.add(en_in_FAQ_ds)
en_in_FAQ.add(en_back_faq)


# Клавиатура номер 13 (Профиль)
en_in_Profile = InlineKeyboardMarkup(row_width=2)
en_back_prof = InlineKeyboardButton(text="Back", callback_data="en_back_prof")

# Добавляем кнопки для клавиатуры номер 13 (Профиль)
en_in_Profile.add(en_back_prof)


# Клавиатура номер 14 (Пожертвования)
en_in_donation = InlineKeyboardMarkup(row_width=2)
en_in_donation_in = InlineKeyboardButton(text="Donation 💰", url="https://www.donationalerts.com/r/fetchy74", callback_data="en_in_donation_in")
en_back_donat = InlineKeyboardButton(text="Back", callback_data="en_back_donat")

# Добавляем кнопки для клавиатуры 14 (Пожертвования)
en_in_donation.add(en_in_donation_in)
en_in_donation.add(en_back_donat)



# Russian
# Клавиатура номер 1 (Russian_main_menu)
rus_mainMenu = InlineKeyboardMarkup(row_width=2)
rus_in_our_games = InlineKeyboardButton(text="Наши игры 🎮", callback_data="rus_in_our_games")
rus_in_social_network = InlineKeyboardButton(text="Социалки 🌍", callback_data="rus_in_social_network")
rus_in_FAQ = InlineKeyboardButton(text="FAQ❓", callback_data="rus_in_FAQ")
rus_in_Profile = InlineKeyboardButton(text="Профиль 🧒", callback_data="rus_in_Profile")
rus_in_donation = InlineKeyboardButton(text="Поддержка 💰", callback_data="rus_in_donation")
rus_back_mainMenu = InlineKeyboardButton(text="Назад",  callback_data="rus_back_mainMenu")

# Добавляем кнопки для клавиатуры номер 1 (Russian_main_menu)
rus_mainMenu.add(rus_in_our_games, rus_in_social_network).add(rus_in_FAQ, rus_in_Profile)
rus_mainMenu.add(rus_in_donation)
rus_mainMenu.add(rus_back_mainMenu)


# Клавиатура номер 2 (Наши игры)
rus_in_our_games = InlineKeyboardMarkup(row_width=2)
rus_in_ios = InlineKeyboardButton(text="IOS 🍏", callback_data="rus_in_ios")
rus_in_android = InlineKeyboardButton(text="ANDROID 🤖", callback_data="rus_in_android")
rus_in_pc = InlineKeyboardButton(text="PC 🖥️", callback_data="rus_in_pc")
rus_in_web_games = InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="rus_in_web_games")
rus_back_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_games")


# Добавляем кнопки для клавиатуры номер 2 (Наши игры)
rus_in_our_games.add(rus_in_ios, rus_in_android)
rus_in_our_games.add(rus_in_pc, rus_in_web_games)
rus_in_our_games.add(rus_back_games)


# Клавиатура номер 3 (ios)
rus_in_ios = InlineKeyboardMarkup(row_width=2)
rus_back_ios = InlineKeyboardButton(text="Назад", callback_data="rus_back_ios")

# Добавляем кнопки для клавиатуры 3 (ios)
rus_in_ios.add(rus_back_ios)


# Клавиатура номер 4 (android)
rus_in_android = InlineKeyboardMarkup(row_width=2)
rus_in_google_play = InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="rus_in_google_play")
rus_in_cars_two = InlineKeyboardButton(text="Cars 🚗", url="https://disk.yandex.ru/d/VEy132RmANfIMA", callback_data="rus_in_cars_two")
rus_back_android = InlineKeyboardButton(text="Назад", callback_data="rus_back_android")

# Добавляем кнопки для клавиатуры номер 4 (android)
rus_in_android.add(rus_in_google_play, rus_in_cars_two)
rus_in_android.add(rus_back_android)


# Клавиатура номер 5 (pc)
rus_in_pc = InlineKeyboardMarkup(row_width=2)
rus_in_mod_bl = InlineKeyboardButton(text="МОД БЛ 🧚‍♂️", callback_data="rus_in_mod_bl")
rus_in_horror = InlineKeyboardButton(text="Horror 🧟‍♂️", url="https://disk.yandex.ru/d/nzt0GC6gXpJ83w", callback_data="rus_in_horror")
rus_back_pc = InlineKeyboardButton(text="Назад", callback_data="rus_back_pc")

# Добавляем кнопки для клавиатуры номер 5 (pc)
rus_in_pc.add(rus_in_mod_bl, rus_in_horror)
rus_in_pc.add(rus_back_pc)


# Клавиатура номер 6 (web_games)
rus_in_web_games = InlineKeyboardMarkup(row_width=2)
rus_in_pc_web_games = InlineKeyboardButton(text="ПК 🖥️", callback_data="rus_in_pc_web_games")
rus_in_phone_web_games = InlineKeyboardButton(text="ТЕЛЕФОН 📱", callback_data="rus_in_phone_web_games")
rus_back_in_web_games= InlineKeyboardButton(text="Назад", callback_data="rus_back_in_web_games")

# Добавляем кнопки для клавиатуры номер 6 (web_games)
rus_in_web_games.add(rus_in_pc_web_games, rus_in_phone_web_games)
rus_in_web_games.add(rus_back_in_web_games)


# Клавиатура номер 7 (pc_web_games)
rus_in_pc_web_games = InlineKeyboardMarkup(row_width=2)
rus_in_pc_web_games_game_one = InlineKeyboardButton(text="Warrunner 🪖", url="https://okko.tv/serial/game-of-thrones", callback_data="rus_in_pc_web_games_game_one")
rus_back_in_pc_web_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_pc_web_games")

# Добавляем кнопки для клавиатуры номер 7 (pc_web_games)
rus_in_pc_web_games.add(rus_in_pc_web_games_game_one)
rus_in_pc_web_games.add(rus_back_in_pc_web_games)


# Клавиатура номер 8 (phone_web_games)
rus_in_phone_web_games = InlineKeyboardMarkup(row_width=2)
rus_in_phone_web_games_game_one = InlineKeyboardButton(text="Race 🏎️", url="https://okko.tv/serial/game-of-thrones", callback_data="rus_in_phone_web_games_game_one")
rus_back_in_phone_web_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_phone_web_games")

# Добавляем кнопки для клавиатуры номер 8 (phone_web_games)
rus_in_phone_web_games.add(rus_in_phone_web_games_game_one)
rus_in_phone_web_games.add(rus_back_in_phone_web_games)


# Клавиатура номер 9 (google_play)
rus_in_google_play = InlineKeyboardMarkup(row_width=2)
rus_in_google_play_game_one = InlineKeyboardButton(text="Cars 🚗", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="rus_in_google_play_game")
rus_back_in_google_play = InlineKeyboardButton(text="Back", callback_data="rus_back_in_google_play")

# Добавляем кнопки для клавиатуры номер 9 (google_play)
rus_in_google_play.add(rus_in_google_play_game_one)
rus_in_google_play.add(rus_back_in_google_play)


# Клавиатура номер 10 (Мод БЛ)
rus_in_mod_bl = InlineKeyboardMarkup(row_width=2)
rus_in_mod_bl_downl = InlineKeyboardButton(text="Скачать наш мод для игры БЛ 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="rus_in_mod_bl_downl")
rus_back_mod = InlineKeyboardButton(text="Назад", callback_data="rus_back_mod")

# Добавляем кнопки для клавиатуры номер 10 (Мод БЛ)
rus_in_mod_bl.add(rus_in_mod_bl_downl)
rus_in_mod_bl.add(rus_back_mod)


# Клавиатура номер 11 (социальные сети)
rus_in_social_network = InlineKeyboardMarkup(row_width=2)
rus_in_youtube_one = InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw", callback_data="rus_in_youtube_one")
rus_in_youtube_two = InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg", callback_data="rus_in_youtube_two")
rus_in_twitch = InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn", callback_data="rus_in_twitch")
rus_in_discord = InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm", callback_data="rus_in_discord")
rus_in_github = InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif", callback_data="rus_in_github")
rus_in_vk = InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg", callback_data="rus_in_vk")
rus_back_social = InlineKeyboardButton(text="Назад", callback_data="rus_back_social")

# Добавляем кнопки для клавиатуры номер 11 (социальные сети)
rus_in_social_network.add(rus_in_youtube_one, rus_in_youtube_two).add(rus_in_twitch, rus_in_discord)
rus_in_social_network.add(rus_in_github, rus_in_vk)
rus_in_social_network.add(rus_back_social)


# Клавиатура номер 12 (FAQ)
rus_in_FAQ = InlineKeyboardMarkup(row_width=2)
rus_in_FAQ_ds = InlineKeyboardButton(text="Тут ⬆", url = "https://1drv.ms/w/s!AtF4vCOqewgBoB1t_x6DdrpMX1QH?e=wrR0sq", callback_data="rus_in_FAQ_ds")
rus_back_faq = InlineKeyboardButton(text="Назад", callback_data="rus_back_faq")

# Добавляем кнопки для клавиатуры номер 12 (FAQ)
rus_in_FAQ.add(rus_in_FAQ_ds)
rus_in_FAQ.add(rus_back_faq)


# Клавиатура номер 13 (Профиль)
rus_in_Profile = InlineKeyboardMarkup(row_width=2)
rus_back_prof = InlineKeyboardButton(text="Назад", callback_data="rus_back_prof")

# Добавляем кнопки для клавиатуры номер 13 (Профиль)
rus_in_Profile.add(rus_back_prof)


# Клавиатура номер 14 (Пожертвования)
rus_in_donation = InlineKeyboardMarkup(row_width=2)
rus_in_donation_in = InlineKeyboardButton(text="Пожертвование 💰", url="https://www.donationalerts.com/r/fetchy74", callback_data="rus_in_donation_in")
rus_back_donat = InlineKeyboardButton(text="Назад", callback_data="rus_back_donat")

# Добавляем кнопки для клавиатуры 14 (Пожертвования)
rus_in_donation.add(rus_in_donation_in)
rus_in_donation.add(rus_back_donat)