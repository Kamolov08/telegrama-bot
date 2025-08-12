import telebot
import requests

# Telegram bot token
TELEGRAM_TOKEN = "7629649216:AAEOHlwKYL_7gWf9d67LsnrLbFpEWv4dJ3c"
# OpenRouter API key
OPENROUTER_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Tayyor savol-javoblar (100+)
READY_QA = {
    "salom": "Va alaykum assalom! Qalaysiz?",
    "isming nima": "Mening ismim EXPAN AI.",
    "qalesan": "Rahmat, yaxshi! O'zingizchi?",
    "sen kimsan": "Men sun'iy intellekt yordamchisiman.",
    "ozbekiston poytaxti": "O‘zbekistonning poytaxti Toshkent.",
    "bugun qanaqa kun": "Bugun juda ajoyib kun!",
    "eng katta daryo": "O‘zbekistondagi eng katta daryo Amudaryodir.",
    "telefon raqam": "Kechirasiz, telefon raqam bera olmayman.",
    "sen odam mısan": "Yo‘q, men sun’iy intellektman.",
    "qachon tug'ilding": "Men 2025-yilda ishga tushirilganman.",
    "rasm chiza olasanmi": "Afsuski, men rasm chiza olmayman, lekin tavsif bera olaman.",
    "hazil ayt": "Kompyuter nima uchun charchamaydi? Chunki u ‘sleep’ rejimiga ega!",
    "ob havo": "Kechirasiz, ob-havo ma'lumotini hozircha bera olmayman.",
    "sen nima qila olasan": "Men savollarga javob beraman, matn yozaman, tushuntiraman va maslahat beraman.",
    "toshkent haqida": "Toshkent O‘zbekistonning poytaxti va eng yirik shahri.",
    "o'zbekiston prezidenti": "O‘zbekiston prezidenti Shavkat Mirziyoyev.",
    "internet bormi": "Ha, internet mavjud.",
    "sen aqllisanmi": "Men juda ko‘p ma’lumotlarga ega sun’iy intellektman.",
    "sevgi nima": "Sevgi — bu odamlarning bir-biriga bo‘lgan chuqur mehr-muhabbati.",
    "kitob tavsiya qil": "Alisher Navoiy asarlarini o‘qishni tavsiya qilaman.",
    "ilm nima": "Ilm — bu insoniyatning bilimi va tajribasi to‘plami.",
    "sen qayerdansan": "Men bulutli serverlardanman, joyim o‘zgarib turadi.",
    "uzun sochli hayvon": "Sher, ot, yoki lama bo‘lishi mumkin.",
    "eng katta tog": "Dunyoning eng baland tog‘i — Everest.",
    "qaysi tillarni bilasan": "Men o‘zbek, rus, ingliz va boshqa ko‘plab tillarda gaplasha olaman.",
    "kompyuter nima": "Kompyuter — bu ma'lumotlarni qayta ishlaydigan elektron qurilma.",
    "dunyo nechta qit'adan iborat": "Dunyo 7 ta qit’adan iborat.",
    "baliq turlari": "O‘zbekistonda sazan, oq amur, laqqa kabi baliqlar mavjud.",
    "eng uzun daryo": "Dunyoning eng uzun daryosi Nil daryosidir.",
    "piyoz foydasi": "Piyoz immunitetni mustahkamlaydi.",
    "sen yolg'on gapirasanmi": "Yo‘q, men faqat mavjud ma’lumotlar asosida javob beraman.",
    "o'zbekiston bayrog'i": "Bayroq uch rangdan iborat: ko‘k, oq, yashil va qizil chiziqlar.",
    "qush turlari": "Bulbul, kaptar, lochin, burgut va boshqalar.",
    "sut foydasi": "Sut suyaklarni mustahkamlaydi.",
    "qaysi sport turlarini bilasan": "Futbol, basketbol, tennis, kurash, boks va hokazo.",
    "dunyo eng katta mamlakat": "Rossiya maydoni bo‘yicha eng katta davlat.",
    "kichik davlat": "Vatikan — eng kichik davlat.",
    "uchuvchi hayvon": "Yarasa va qushlar uchadi.",
    "suzuvchi hayvon": "Baliqlar va delfinlar suvda suzadi.",
    "kit turlari": "Ko‘k kit, kashalot va boshqalar.",
    "dunyo eng sovuq joy": "Antarktida eng sovuq joy.",
    "dunyo eng issiq joy": "Lut cho‘li (Eron) eng issiq joylardan biri.",
    "sayyora soni": "Quyosh tizimida 8 ta sayyora bor.",
    "eng katta sayyora": "Yupiter eng katta sayyora.",
    "oy haqida": "Oy — Yerning tabiiy yo‘ldoshi.",
    "quyosh haqida": "Quyosh — Quyosh tizimidagi asosiy yulduz.",
    "kompyuter qismlari": "Monitor, klaviatura, sichqoncha, protsessor va boshqalar.",
    "internet nima": "Internet — global axborot tarmog‘i.",
    "email nima": "Elektron pochta xabarlashish usuli.",
    "telegram nima": "Telegram — tezkor xabarlashish dasturi.",
    "google nima": "Google — qidiruv tizimi.",
    "youtube nima": "YouTube — video almashish platformasi.",
    "instagram nima": "Instagram — rasm va video almashish ijtimoiy tarmog‘i."
}

# OpenRouter AI javob olish (faqat o'zbek tilida)
def ask_ai(question):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "Siz faqat o'zbek tilida javob beradigan sun'iy intellekt yordamchisiz. Sizning ismingiz EXPAN AI."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return None
    except:
        return None

# Avvalgi kod shu yerda... (oldingi kod)

@bot.message_handler(func=lambda message: True)
def reply(message):
    question = message.text.lower().strip()

    # Maxsus javoblar
    if question in ["isming nima", "sening isming nima"]:
        bot.reply_to(message, "Mening ismim EXPAN AI.")
        # Stiker yuborish - ismga oid stiker (misol)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECW9Bj6oTlU4pBf3YFtUQ6-n9h0JnjywACXgADVp29CkWfM7PvP-OSLwQ")
        return

    # AI javob
    ai_answer = ask_ai(question)
    if ai_answer:
        bot.reply_to(message, ai_answer)

        # Stikerlarni mazmunga qarab yuborish
        if "salom" in question:
            # Salomlashish stikeri
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECXxBj6n1Udoy1sZ4QdbE3CW7ru5uejwACRAADVp29CvNxt1x6k7oOSLwQ")
        elif "hazil" in question or "kulgi" in question or "kul" in question:
            # Kulgi stikeri
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECXxFj6n7xw-4Qzn8kPRNTYYRx3HFAkwACRwADVp29CgQDea6AtVpASLwQ")
        elif "rahmat" in question or "tashakkur" in question:
            # Minnatdorlik stikeri
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECXxNj6n98d0bpD4Gqc1H6rwzAZZvzAACTQADVp29CkVdlJ6-cxhhSLwQ")
        else:
            # Umumiy javob stikeri
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECXxRj6n9n-dwtOy73bPG-iSHOqNyWfgACUQADVp29Cn-7n-oDd1YhSLwQ")

        return

    # Tayyor javoblar
    if question in READY_QA:
        bot.reply_to(message, READY_QA[question])
        # Tayyor javoblarga stiker qo'shish (misol)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECXxRj6n9n-dwtOy73bPG-iSHOqNyWfgACUQADVp29Cn-7n-oDd1YhSLwQ")
    else:
        bot.reply_to(message, "Kechirasiz, hozir javob bera olmayman.")
        # Javobsiz stiker
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECXxVj6n_7pQayb47nMY4XbXZo95W8sQACVgADVp29Ci8--XZs-5LZhSLwQ")

print("Bot ishga tushdi...")
bot.infinity_polling()
