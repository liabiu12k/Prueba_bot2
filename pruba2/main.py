from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Función para manejar el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde con un saludo cuando el usuario envía el comando /start."""
    await update.message.reply_text("Hola Mundo! 👋")

# Configuración del bot
if __name__ == "__main__":
    # Reemplaza 'tu_token_aqui' por tu token real de Telegram
    TOKEN = "7721418131:AAGRzdKFFHRfHjdtfAdZCc7l4N8HH1jKzjE"
    
    # Construir la aplicación con el token del bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Añadir el manejador para el comando /start
    application.add_handler(CommandHandler("start", start))

    # Ejecutar el bot con polling
    print("El bot está ejecutándose... Presiona Ctrl+C para detenerlo.")
    application.run_polling()

