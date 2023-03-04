import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━⚡️SOURCE ZELZAL⚡️━━━━━━
 مرحبا انا بوت يمكنني تشغيل الاغاني في المكالمات الصوتيه
اضغط على زر الاوامر لمعرفة طريقة التشغيل 
قناة ســـورس ميوزك [قناة السورس](t.me/SOURCESAKRAN)...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اضفني لي مجموعتك ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " ⚡️ ¦ السورس ", url=f"https://t.me/SOURCESAKRAN"
                    ),
                    InlineKeyboardButton(
                        " ☑️ ¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " 🖥 ¦ الأوامــر ", url=f"https://telegra.ph/%F0%9D%91%BA%F0%9D%91%BC%F0%9D%91%B6%F0%9D%91%B9%F0%9D%91%AA%F0%9D%91%AC-%F0%9D%91%A9%F0%9D%91%AC%F0%9D%91%B4%F0%9D%91%A9%F0%9D%91%B6-06-190%9D%91%B6-06-19"
                    ),
                    InlineKeyboardButton(
                        " 🧨 ¦ مطور السورس ", url="https://t.me/EE_03"
                    )]
            ]
       ),
    )

@Client.on_message(command(["مبرمج السورس" ,"سكران" ,"سورس" ,"السورس" ,"زلزال" ,"ميوزك زيزو" ,"زيزو"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/6dc0df2158e1de2aac29c.jpg",
        caption=f""" [SOURCE ZELZAL⚡️](t.me/EE_03)  """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("SAKRAN⚡️", url=f"https://t.me/D_A_D_S_A_K_R_A_N_N"),
           ],
            [ 
                InlineKeyboardButton("ZElZAL⚡️", url=f"https://t.me/EE_03"),
            ],
            [
                InlineKeyboardButton(
                    "SOURCE ZELZAL⚡️", url=f"https://t.me/SOURCESAKRAN"
                ),
            ],
            [
                InlineKeyboardButton("☑️اضفني الى مجموعتك☑️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور", "/godzela", "مطور" ,"مطور البوت"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b557e5cffeadff7704af9.jpg",
        caption=f""" الاول: هو مطور السورس☑️ \n الثاني: مطور البوت☑️ \n√""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("افـ ـSAKRAN⚡️", url=f"https://t.me/D_A_D_S_A_K_R_A_N_N"),
            ],
            [
                InlineKeyboardButton(
                        DEV_NAME, url=f"https://t.me/{OWNER_NAME}"
                ),
            ],
            [
                InlineKeyboardButton("☑️ضيـف البـوت لمجمـوعتـك☑️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
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
                "⚡️ **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                "⚡️ **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم او بيمبو تعاله` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⚙️ ¦ السورس ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("☣️ ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "☑️اضـفني لي مـجـمـوعـتـك☑️",
                        url=f'https://t.me/{H_a_g_a_r_M_U_S_I_C_C_bot?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
