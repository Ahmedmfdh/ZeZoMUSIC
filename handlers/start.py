import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━───⊶⛧•[SOURCE SAKRAN⚡️](https://t.me/SOURCESAKRAN)•⛧⊷───━**\n

¦**انا بوت تشغيل وتنزيل الاغاني والفديو**\n
🎻

 👮🏼‍♂️¦**اضفني مشرف في مجموعتك لأعمل**\n

 🌐¦**اتبع مايلي لمعرفه كيفيه الاستخدام**\n

 ❓¦**اضغط علي ذر طريقه الاستخدام**\n

 ◍**مميزات الروبوت يعمل بجودة فائقه**\n

**━───⊶⛧•[SOURCE SKRAN🎧⚡️](https://t.me/SOURCESAKRAN)•⛧⊷───━**\n""",
    reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ],
            [
            InlineKeyboardButton( "🔎 كيف تستخدمني؟ قائمة الأوامر.",url=f"https://t.me/SOURCESAKRAN"),
            ],
            [
            InlineKeyboardButton("𓂄𓆩𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙵𝚁𝙰𝚆𝙽𓆪𓂁", url=f"https://t.me/SOURCESAKRAN"),
              ],
              [
                  InlineKeyboardButton(
                         " ☣️ ¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
            [
                InlineKeyboardButton("𓂄𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝚁𝙰𝚆𝙽𓆪𓂁", url=f"https://t.me/SOURCESAKRAN"),
            ]
         ]
     )
  )

@Client.on_message(
    command(["مبرمج السورس","سكران"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c8715291210af8f7a2878.jpg",
        caption=f"""المبرمج سكران مبرمج جميع السورس لو حاابب تتواصل معاه بالاسفل ⬇️ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓂄𓆩𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙵𝚁𝙰𝚆𝙽𓆪𓂁", url=f"https://t.me/D_A_D_S_A_K_R_A_N_N"),
                ],
                [
                    InlineKeyboardButton(
                    "𓂄𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝚁𝙰𝚆𝙽𓆪𓂁", url=f"https://t.me/SOURCESAKRAN"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["مطور السورس" ,"حشيشة","حشيشة","المبرمج حشيشة"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/22bc9024645f5bccb50fb.jpg",
        caption=f""" المطور حشيشة مطور جميع السورس لو حاابب تتواصل معاه بالاسفل ⬇️ """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓂄𓆩𝙳𝙴𝚂𝙷𝙰 𝙰𝙻𝙼𝙰𝙵𝚈𝙰𓆪𓂁", url=f"https://t.me/H_A_S_I_S_A"),
           ],
            [ 
                InlineKeyboardButton(
                    "𓂄𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝚁𝙰𝚆𝙽𓆪𓂁", url=f"https://t.me/SOURCESAKRAN"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["سورس","ياسورس","السورس","source","يا سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/5d3260e7ea265cc5896eb.mp4",
        caption=f"""[━═━═━ٰ˚₊·𝙵𝚁𝙰𝚆𝙽.↺═━═━•](https://t.me/SOURCESAKRAN)
 [✨╎𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝚁𝙰𝚆𝙽](https://t.me/
SOURCESAKRAN)

 [⚙╎𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝙴𝙶𝚈𝙿𝚃](https://t.me/SOURCESAKRAN)
 
 [⚡╎𝚁𝚄𝙽 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝚄𝚂 𝙽𝙾𝚆](https://t.me/SOURCESAKRAN)
[SOURCE SKRAN🎧⚡️](https://t.me/SOURCESAKRAN)
──┈┈┈┄┄╌╌╌╌┄┄┈┈┈
[SOURCE SKRAN🎧⚡️️](https://t.me/SOURCESAKRAN)
[SOURCE SKRAN🎧⚡️️](https://t.me/SOURCESAKRAN)""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓂄𓆩𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙵𝚁𝙰𝚆𝙽𓆪𓂁", url=f"https://t.me/D_A_D_S_A_K_R_A_N_N️"),
            ],
            [
            InlineKeyboardButton("𓂄𓆩𝙳𝙴𝚂𝙷𝙰 𝙰𝙻𝙼𝙰𝙵𝚈𝙰𓆪𓂁", url=f"https://t.me/H_A_S_I_S_A"),
            ],
            [
                InlineKeyboardButton(
                        "𓂄𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝚁𝙰𝚆𝙽𓆪𓂁", url=f"https://t.me/SOURCESAKRAN"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                " **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                " **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم او بيمبو تعاله` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⚙️ ¦ السورس ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            ],
                            [
                            InlineKeyboardButton("☣️ ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "أضف لبوت لمجموعتك ✅", url=f'https://t.me/{bu}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
