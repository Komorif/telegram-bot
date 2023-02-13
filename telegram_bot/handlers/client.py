from aiogram import types, Dispatcher
from create_bot import dp, bot

# Inline клавиатуры
# Выбор языков 2 менюшки
from keyboards import mainMenu_en_rus
from keyboards import mainMenu_en_rus_two

# English
from keyboards import en_mainMenu
from keyboards import en_in_our_games
from keyboards import en_in_ios
from keyboards import en_in_android
from keyboards import en_in_pc

# Web games
from keyboards import en_in_web_games
from keyboards import en_in_pc_web_games
from keyboards import en_in_phone_web_games

# Google play и MOD BL
from keyboards import en_in_google_play
from keyboards import en_in_mod_bl

from keyboards import en_in_social_network
from keyboards import en_in_FAQ
from keyboards import en_in_Profile
from keyboards import en_in_donation

# Russian
from keyboards import rus_mainMenu
from keyboards import rus_in_mod_bl
from keyboards import rus_in_our_games
from keyboards import rus_in_ios
from keyboards import rus_in_android
from keyboards import rus_in_pc

# Web games
from keyboards import rus_in_web_games
from keyboards import rus_in_pc_web_games
from keyboards import rus_in_phone_web_games

# Google play и MOD BL
from keyboards import rus_in_google_play
from keyboards import rus_in_mod_bl

from keyboards import rus_in_social_network
from keyboards import rus_in_FAQ
from keyboards import rus_in_Profile
from keyboards import rus_in_donation


# Картинки для менюшек
menu_one="https://downloader.disk.yandex.ru/preview/711bb1adff875b15eb27bc2e953f8d0b36a69eecb3a2ca4648143ee0aa223585/63c1af3e/_6tncDV3aVZTsQg0TZbCornwjRjeQl6Sbl7ryrTKPw9pPdoQLXcQ1r0Yu5Untrt8SGGTmFGHYgs8E_rm6dSkYA%3D%3D?uid=0&filename=menu_one.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
ios="https://downloader.disk.yandex.ru/preview/5b42c746b53921a74847b49334ef13e01f2864a5e758af36484f783248b9f5f8/63c1af84/1iEydv63EpJWU_e7x7LDfqX3ATg9TGRKmTLY0YJUpIRbS974E5ceNrIrAqGV3o-TvDf9AYWnpGhBpJ15kq8vPw%3D%3D?uid=0&filename=ios.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
andoid="https://downloader.disk.yandex.ru/preview/5f590d1bcdda15d56e668bba0c430c5714439e97a3e188401357306c4b101eb2/63c1afb3/lsX9zrLWoYPzhyZU41o5w6X3ATg9TGRKmTLY0YJUpITesx_k25DxwZNvFQTOTgbNV1IjEwIpXQ4ssHZ9Bk8ywg%3D%3D?uid=0&filename=android.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
pc="https://downloader.disk.yandex.ru/preview/c2f1fbb4c7d3c2a355d7d61785ab22188ea5f22530e92a1f322a740a6501e478/63c1afe4/MNQlWgSL62OIKo3AGtl_v6X3ATg9TGRKmTLY0YJUpIQD6nmvIEl_RH7MzyL3Flp8Iowu8MDThx2y9aZ5ZE9loQ%3D%3D?uid=0&filename=pc.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
google_play="https://downloader.disk.yandex.ru/preview/96cff67912e20350583aa5e39a9bc6a0994ec30ef871a46c4a8444dde4134963/63d53985/lw9UVvCoowbEvBhKKB6sLYaa__hDX-jp_fjofm25VinHzXea_bSmCdK1PkFvjK4JS2ihJDr4UrHs0TjYNz4i8w%3D%3D?uid=0&filename=google_play.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
faq="https://downloader.disk.yandex.ru/preview/87f33def26b09db3e18c3dd2f3137cd3a43a08c83c2f6a02301fbd6035c6615a/63c1b002/cVQro105INirqiPWEro9H6X3ATg9TGRKmTLY0YJUpISHHAmrL6lUr33tyAmW2_qwI3ZwRG3eV-ovVOZmbOYMhg%3D%3D?uid=0&filename=FAQ.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"

# Картинки для менюшек English
en_menu="https://downloader.disk.yandex.ru/preview/a41d6e5b6e080dca6a0b27e0a2e10a3b93ebc5249c3a3e1a8b96f65ddee0c5f2/63d43877/8tUqByIlKdFjR7xnNbgYj0aXDJB59eX7utlYUyhGcf13gQHfmnklgyCQDu03CMNZ4VgzQDxwqs7YESJ7RPvBRA%3D%3D?uid=0&filename=mainmenu.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_social_network="https://downloader.disk.yandex.ru/preview/9e70fb7803245d98c211e0da3466d026bc57bd9a65ecd1a168ff36f3b8d0310c/63c1b070/nA_Tzw5hTAom4eLxCwtmX6X3ATg9TGRKmTLY0YJUpISRDKBSZerOmTeBwgs_AoTsQ8IeF_4aLiIgLFstdOiqBA%3D%3D?uid=0&filename=en_social_network.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_donation="https://downloader.disk.yandex.ru/preview/47d815b9afdaeb8a78227244ae18100ec9ab26db7f47a2ea7ef7227f537f960a/63c1b091/iHeFI6ozuVm4jxnyqkivl6X3ATg9TGRKmTLY0YJUpIRp9GktWZbSD8CYW5bOoozojw2HsB_q8F2vChjF_ASPvA%3D%3D?uid=0&filename=en_donation.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_mod_bl="https://downloader.disk.yandex.ru/preview/d77ef2bdff300f67bc3dfa76d428e50a2831c23fb027f785f3cc82c217bb504b/63c1b081/6CJXf9gXYkwgKeJuReORQbnwjRjeQl6Sbl7ryrTKPw94tzTUKvV07Tzv4_HOBQpduUo-Uz7qHopuycX_qB2HAA%3D%3D?uid=0&filename=en_mod_bl.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_platform="https://downloader.disk.yandex.ru/preview/0856ad63f6b1604d107cf01f435a3acb2870138debf1a821202ec6296d1102d2/63c1b0b0/KniNQVNcyYLVfZFvpQk_VrnwjRjeQl6Sbl7ryrTKPw9aIHZN5gDMTD2IB6NuXpiPBDcKAuknVXsIhEAr2IoqVg%3D%3D?uid=0&filename=en_platform.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_phone="https://downloader.disk.yandex.ru/preview/ab4d78a35c261ef702b4f7cc4b5831d77d86907a1d53d878232de22c9bcdf556/63d42a9a/sMY82TkfDdbpLU_KYp5ABHq9fksKA_u6Qdlxi1mzlvkYnKyNv5mu8n5nFdECD8WnvEzBXTA5xk_aVhWX8A57Vw%3D%3D?uid=0&filename=phone.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_profile="https://downloader.disk.yandex.ru/preview/dce9ab49782fe5182a7772c6a3cc164b74c6b38cdfce13ae96691cb6c7fdc634/63c1b0a1/s0oqgq8sySb2pAGHKhdAv6X3ATg9TGRKmTLY0YJUpISzy3nZJGCDYSf3glLT8pfLn_NK5CQ3-BGJ0RYRMMG39Q%3D%3D?uid=0&filename=en_profile.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"

# Картинки для менюшек Russian
rus_menu="https://downloader.disk.yandex.ru/preview/170dd84ecdd0e02a097dcb64a021a97c445181048d4d1b22cccd10867a8e5041/63c1b46a/BEY3ThlvSC5pLmNSlclnc9-rcZs5RLWR3E1vERxC9CgFY7Czim8bvmNQ7ppNK1A8NTJ1cnQ4t8Wfgd1UHtE3Pw%3D%3D?uid=0&filename=rus_menu.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_social_network="https://downloader.disk.yandex.ru/preview/5e6eaa54cbd5d273ed746392430ee67368b115b52be709a92067dc7a6881bd80/63c1b04c/0MK89FED-4X2FcfnPeA9y6X3ATg9TGRKmTLY0YJUpITIE_sADpIQGmAA6lNp-D4kDRRADv9EHBTb8y2v7B6Tzw%3D%3D?uid=0&filename=rus_social_network.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_donation="https://downloader.disk.yandex.ru/preview/d27eae5cda0522b720a1374cb15fe70b00866d5002ee80c256100c31b6428754/63c1b024/lCvTYZkOtl_KiCVwROLU4aX3ATg9TGRKmTLY0YJUpIRAZFVTQVGzo0u5ul1B10bh_B9lSwVv1bqwwGwSeWABmw%3D%3D?uid=0&filename=rus_donation.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_mod_bl="https://downloader.disk.yandex.ru/preview/713634f417141a913e250c473364de52fefaf4c71ba50673bb99ea591e76b39b/63c1b013/ekNSf85xrnEWXBFg-lT1z7nwjRjeQl6Sbl7ryrTKPw_oUKVUk4sd2kC9uuhEYadBpyH1tpWLS4Q0Sv775Jf7Aw%3D%3D?uid=0&filename=rus_mod_bl.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_platform="https://downloader.disk.yandex.ru/preview/06105be0af89d22c9670a08316b4b46e0f481bfe92d4a832d74fc8b9ad89c1a8/63c1b03b/jkk3Y7EBMq8COZs_yYwMI7nwjRjeQl6Sbl7ryrTKPw8rEB7s5cCmyZFg6ntzpGbUWhwhDkefJe83IztboXiOVA%3D%3D?uid=0&filename=rus_platform.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_phone="https://downloader.disk.yandex.ru/preview/51d2f367a1a41aa520cfc049eaec03d0d4c4212156a41f1daf28efa75fec1507/63d42ae4/IasrU8Hu2XzBVjdC6D6qZFBavCHoxKachbVWEqGMJmwxvAxbP3osMcrGPezZc3VuXhMOHAM2IACzYjAhChesVw%3D%3D?uid=0&filename=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_profile="https://downloader.disk.yandex.ru/preview/6811da4964699788c99ae5bb69b41048387bc2d9c1f9e7cb8c5349d9404ec053/63c1b05b/YgAWFr1vJHk_O_uT15w--aX3ATg9TGRKmTLY0YJUpIRVDHxEdaip2EyFseskn7OsIQ737D4UmDZHbGTolY1g3A%3D%3D?uid=0&filename=rus_profile.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"


# 1 меню выбор языка
@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)


# 1.2 меню выбор языка 
@dp.callback_query_handler(text_contains="start")
async def mainMenu_en_rus_two(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "mainMenu_en_rus_two":
        await bot.send_message(call.from_user.id, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)


# Итерация с кнопок English и Russian на их менюшки 
@dp.callback_query_handler(text_contains="lang_")
async def lang_all(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "lang_en":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    
    elif call.data == "lang_rus":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)


# Отдельный back с mainmenu на выбор языков en
@dp.callback_query_handler(text_contains="en_back_mainMenu")
async def lang_en_back(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "en_back_mainMenu":
        await bot.send_photo(call.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)


# Отдельный back с mainmenu на выбор языков rus
@dp.callback_query_handler(text_contains="rus_back_mainMenu")
async def lang_rus_back(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "rus_back_mainMenu":
        await bot.send_photo(call.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)


# Обычное эхо в боте которое на слово отвечает этим же словом
@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)



# English
@dp.callback_query_handler(text_contains="en_back_")
async def back_buttons_en(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех назад кнопок English
    if call.data == "en_back_games":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_ios":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_android":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_pc":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_in_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_web_games)
    elif call.data == "en_back_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_web_games)
    elif call.data == "en_back_in_google_play":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_android)
    elif call.data == "en_back_mod":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_pc)
    elif call.data == "en_back_social":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_faq":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_prof":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_donat":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)


# Все inline клавиатуры inline en_in_ перед каждой English
@dp.callback_query_handler(text_contains="en_in_")
async def it_buttons_en(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех inline клавиатур English
    if call.data == "en_in_our_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_in_ios":
        await bot.send_photo(call.from_user.id, photo=ios, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_ios)
    elif call.data == "en_in_android":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_android)
    elif call.data == "en_in_pc":
        await bot.send_photo(call.from_user.id, photo=pc, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_pc)
    elif call.data == "en_in_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_web_games)
    elif call.data == "en_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=pc, caption=r"Pick any game you want 🇺🇸", reply_markup=en_in_pc_web_games)
    elif call.data == "en_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=en_phone, caption=r"Pick any game you want 🇺🇸", reply_markup=en_in_phone_web_games)
    elif call.data == "en_in_mod_bl":
        await bot.send_photo(call.from_user.id, photo=en_mod_bl, caption="MOD FOR ENDLESS SUMMER 🇺🇸", reply_markup=en_in_mod_bl)
    elif call.data == "en_in_google_play":
        await bot.send_photo(call.from_user.id, photo=google_play, caption="GOOGLE PLAY 🇺🇸", reply_markup=en_in_google_play)
    elif call.data == "en_in_social_network":
        await bot.send_photo(call.from_user.id, photo=en_social_network, caption="SOCIAL MEDIA 🇺🇸", reply_markup=en_in_social_network)
    elif call.data == "en_in_FAQ":
        await bot.send_photo(call.from_user.id, photo=faq, caption="We have answered frequently asked questions for your convenience 🇺🇸", reply_markup=en_in_FAQ)
    elif call.data == "en_in_Profile":
        await bot.send_photo(call.from_user.id, photo=en_profile, caption=f"Your profile ID: {call.from_user.id} \nYou are a human being. \nGood luck using the bot 🇺🇸", reply_markup=en_in_Profile)
    elif call.data == "en_in_donation":
        await bot.send_photo(call.from_user.id, photo=en_donation, caption="You can help us be better 🇺🇸", reply_markup=en_in_donation)



# Russian
@dp.callback_query_handler(text_contains="rus_back_")
async def back_buttons_rus(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех назад кнопок English
    if call.data == "rus_back_games":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_ios":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_android":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_pc":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_in_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_web_games)
    elif call.data == "rus_back_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_web_games)
    elif call.data == "rus_back_in_google_play":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_android)
    elif call.data == "rus_back_mod":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_pc)
    elif call.data == "rus_back_social":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_faq":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_prof":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_donat":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)


# Все inline клавиатуры inline en_in_ перед каждой English
@dp.callback_query_handler(text_contains="rus_in_")
async def it_buttons_rus(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех inline клавиатур English
    if call.data == "rus_in_our_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫБЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_in_ios":
        await bot.send_photo(call.from_user.id, photo=ios, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_ios)
    elif call.data == "rus_in_android":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_android)
    elif call.data == "rus_in_pc":
        await bot.send_photo(call.from_user.id, photo=pc, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_pc)
    elif call.data == "rus_in_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫБЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_web_games)
    elif call.data == "rus_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=pc, caption="Выбирай любую игру какую хочешь 🇷🇺", reply_markup=rus_in_pc_web_games)
    elif call.data == "rus_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_phone, caption="Выбирай любую игру какую хочешь 🇷🇺", reply_markup=rus_in_phone_web_games)
    elif call.data == "rus_in_mod_bl":
        await bot.send_photo(call.from_user.id, photo=rus_mod_bl, caption="МОД НА БЕСКНОНЕЧНОГО ЛЕТО 🇷🇺", reply_markup=rus_in_mod_bl)
    elif call.data == "rus_in_google_play":
        await bot.send_photo(call.from_user.id, photo=google_play, caption="GOOGLE PLAY 🇷🇺", reply_markup=rus_in_google_play)
    elif call.data == "rus_in_social_network":
        await bot.send_photo(call.from_user.id, photo=rus_social_network, caption="SOCIAL MEDIA 🇷🇺", reply_markup=rus_in_social_network)
    elif call.data == "rus_in_FAQ":
        await bot.send_photo(call.from_user.id, photo=faq, caption="Мы ответили на часто задаваемые вопросы для вашего удобства 🇷🇺", reply_markup=rus_in_FAQ)
    elif call.data == "rus_in_Profile":
        await bot.send_photo(call.from_user.id, photo=rus_profile, caption=f"ID вашего профиля: {call.from_user.id} \nВы человек \nЖелаем удачи в пользовании ботом 🇷🇺", reply_markup=rus_in_Profile)
    elif call.data == "rus_in_donation":
        await bot.send_photo(call.from_user.id, photo=rus_donation, caption="Вы можете помочь нам стать лучше 🇷🇺", reply_markup=rus_in_donation)



# Register dispather
def register_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=["start"])