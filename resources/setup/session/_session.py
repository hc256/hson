# š®š·š»šÆš¶šµ - Userbot
# šŗš¶š¼š¹šŖš¬ š®š·š»šÆš¶šµ - šŗšŗš»š¹š°šµš®_šŗš¬šŗšŗš°š¶šµ
# Owner ~ @GPTHON

from telethon.sessions import StringSession as ss
from telethon.sync import TelegramClient as tc

print("š© SOURCE š®š·š»šÆš¶šµ -  STRING SESSION šŖ")
print("")

APP_ID = int(input("āā® ENTER APP ID HERE - "))
API_HASH = input("āā® ENTER API HASH HERE - ")

with tc(ss(), APP_ID, API_HASH) as client:
    ics = client.send_message("me", client.session.save())
    ics.reply("āā® ŁŲ°Ų§ ŁŁ ŁŁŲÆ Ų§ŁŲŖŁŲ±ŁŁŲ³ Ų§ŁŲ®Ų§Ųµ ŲØŁ.\nāā® Ų§ŁŁŲ·ŁŲ± - @GPTHON. ")
    print("")
    print("")
    print(
        "āā® Below is the STRING_SESSION. You can also find it in your Telegram Saved Messages."
    )
    print("")
    print("")
    print(client.session.save())
