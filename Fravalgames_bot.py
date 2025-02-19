from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Comando start
async def start(update: Update, context):
    await update.message.reply_text("Ben ritrovati carissimi FravalGamers. Ne è passato di tempo, mi siete mancati. Quel coglione del presentatore si prende una pausa per questa seconda edizione dei giochi, quindi tutto sarà operato tramite me, il bot ufficiale dei Fraval Easter Games. Tutto ciò che dovrete fare sarà rispondere correttamente ai quesiti che man mano vi porrò, e potrete andare avanti in questa specie di caccia al tesoro. La novità di questa edizione è che potrete avvalervi dell'uso di internet, MA NIENTE IA, NON ME FATE ROSICA. In bocca al lupo a tutti e buon divertimento, se avete dei dubbi su qualcosa scrivete al coglione, almeno lavora. Ciancio alle bande, diamo il via ai giochi! Per avviarmi, dovrai rispondermi scrivendomi la somma dei *numeri perduti*")

# Gestione delle risposte corrette
async def risposta(update: Update, context):
    risposta_corretta = "108"  # Cambia con la tua risposta corretta
    if update.message.text == risposta_corretta:
        await update.message.reply_text("Lost Numbers! Bravissim*. Che cazzo di serie")
    else:
        await update.message.reply_text("Dai frate, riprova. You got this.")

if __name__ == "__main__":
    # Sostituisci "TOKEN_DEL_TUO_BOT" con il token del tuo bot
    app = ApplicationBuilder().token("8109066916:AAH1mA694rCsTZ4PSxQM_5jgXgZfRPoB6kM").build()

    # Aggiungi i comandi e i gestori di messaggi
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, risposta))

    # Avvia il bot
    print("Bot in esecuzione...")
    app.run_polling()
