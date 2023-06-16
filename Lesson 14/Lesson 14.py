from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [KeyboardButton("Корпорати́вное пра́во"), KeyboardButton("Интеллектуа́льная со́бственность")],
        [KeyboardButton("Гражданское право")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите раздел:', reply_markup=reply_markup)

def section1(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Корпорати́вное пра́во подотрасль гражданского права, совокупность норм, регулирующих на основе частно-управленческих методов правового регулирования общественные отношения, связанные с образованием и деятельностью корпораций (корпоративных форм юридических лиц).')

def section2(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Интеллектуа́льная со́бственность — в широком понимании термин означает закреплённое законом временное исключительное право, а также личные неимущественные права авторов на результат интеллектуальной деятельности или средства индивидуализации.Законодательство, которое определяет права на интеллектуальную собственность, устанавливает монополию авторов на определённые формы использования результатов своей интеллектуальной, творческой деятельности, которые, таким образом, могут использоваться другими лицами лишь с разрешения первых.')

def section3(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Гражданское право — отрасль права, объединяющая правовые нормы, регулирующие имущественные, а также связанные и несвязанные с ними личные неимущественные отношения, возникающие между разными организациями и гражданами, а также между отдельными гражданами.')

def main() -> None:
    updater = Updater("6075002489:AAF5xYtlWglobXST_N9i7IGDvyX_uBMjhaM")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('^Корпорати́вное пра́во$'), section1))
    dp.add_handler(MessageHandler(Filters.regex('^Интеллектуа́льная со́бственность$'), section2))
    dp.add_handler(MessageHandler(Filters.regex('^Гражданское право$'), section3))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
