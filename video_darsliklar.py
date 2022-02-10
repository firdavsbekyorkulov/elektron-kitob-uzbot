from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("◀️Bosh menyu▶️")
# --><-- Menu VideoLessons --><--
key = KeyboardButton("🇺🇸 Inliz tili")
key1 = KeyboardButton("💻 Informatika")
key2 = KeyboardButton("Rus tili")
key2 = KeyboardButton("Xitoy tili")
key3 = KeyboardButton("Matematika")
key4 = KeyboardButton("Ona tili")
key5 = KeyboardButton("Geografiya")
key9 = KeyboardButton("Yapon tili")
key8 = KeyboardButton("Biologiya")
key7 = KeyboardButton("Fizika")
key6 = KeyboardButton("Kimyo")
keyback =KeyboardButton("🔙 Back")

menuVideo = ReplyKeyboardMarkup(resize_keyboard= True).add(key).add(key1).add(key2).add(key3).add(key4).add(key5).add(key6).add(key7).add(key8).add(key9).add(btnMain)


# --><-- Menu Informatika --><--
f = KeyboardButton("Excel")
f1 = KeyboardButton("Word")
f2 = KeyboardButton("PhotoShop")
f3 = KeyboardButton("Power Point")
f4 = KeyboardButton("Access")
f5 = KeyboardButton("🐍Python🐍")
f6 = KeyboardButton("c++")
f7 = KeyboardButton("Java")
f8 = KeyboardButton("JavaScript")

menuInformatika = ReplyKeyboardMarkup(resize_keyboard = True).add(f).add(f1,f2).add(f3,f4).add(f5).add(f6).add(f7).add(f8).add(keyback,btnMain)