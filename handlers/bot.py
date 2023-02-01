    if m.text == "بوت":
        if sudo2(m):
            await m.reply_text("◎ نعم حبيبى المطور 🥺❤️\n√", reply_to_message_id=m.message_id)
        else:
            if manager(m):
                await m.reply_text("◎ نعم حبيبي المالك 🥺❤️\n√", reply_to_message_id=m.message_id)
            else:
                if constractors(m):
                    await m.reply_text("◎ نعم حبيبى المنشئ 🥺❤️\n√", reply_to_message_id=m.message_id)
                else:
                    if admin(m):
                        await m.reply_text("◎ نعم حبيبى الادمن 🥺❤️\n√", reply_to_message_id=m.message_id)
                    else:
                        if special(m):
                            await m.reply_text("◎ نعم حبيبى المميز 🥺❤️\n√", reply_to_message_id=m.message_id)
                        else:
                            if get_db_botname() is None:
                                botname = "زيرو"
                            else:
                                botname = get_db_botname()
                            await m.reply_text("اسمى " + botname + " ياحب 🙄❤️", reply_to_message_id=m.message_id)

    if m.text == (get_db_botname() or "زيرو"):
        texting = ["اؤمر " + (get_db_botname() or "زيرو") + " شتريد؟❤️🥺",
                   "اى يقلب " + (get_db_botname() or "زيرو") + "❤️",
                   "موجود عايز اى بوشك ده😒",
                   "موجود عاوز اى 😒",
                   "مالك حبيبى🥺",
                   "شفلك كلبه❤️😂",
                   "مبكلمكش🥺",
                   "شبيك لبيك❤️😂",
                   "ثانيه واحده بتشقط وجى🙄",
                   "قلبى بينادى على " + (get_db_botname() or "زيرو") + "😘",
                   "نعسان محدش يصحينى🙄"
                   ]
        await m.reply_text(random.choice(texting), reply_to_message_id=m.message_id)
        return

كود بوت سورس دارك
-----------»»»
    if text == "بوت":
      t = IDrank(redis,userID,chatID,r)
      Bot("sendMessage",{"chat_id":chatID,"text":f"◎ نعم حبيبي » {t} 🥺❤️","reply_to_message_id":message.id,"parse_mode":"html"})
-----------»»»
كود بوت سورس صعيدي
