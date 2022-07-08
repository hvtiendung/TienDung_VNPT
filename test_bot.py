from turtle import update
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào anh {update.effective_user.first_name}')

def gioithieu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Em tên: Hồ Văn Tiến Dũng \nSinh ngày: 21/10/1999 \nHọc trường: ĐH Bách Khoa Đà Nẵng \nSở thích: Nghe nhạc, du lịch, đá bóng và đá ly bia \nTình trạng: Độc thân')

def end(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Phần giới thiệu đến đây là kết thúc')

updater = Updater('5509989608:AAEt2MJkuOYb3vJ24h1u7RPfdgePZKQq_Uw')


updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('gioithieu', gioithieu))
updater.dispatcher.add_handler(CommandHandler('end', end))


updater.start_polling()
updater.idle()
