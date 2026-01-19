import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "👋 Bienvenue sur Lucky Jet Expert ! Tape /predict pour une prédiction.")

@bot.message_handler(commands=['predict'])
def predict(msg):
    import random
    prediction = round(random.uniform(1.5, 50), 2)
    bot.send_message(msg.chat.id, f"🎯 Prédiction : x{prediction}")

@bot.message_handler(commands=['stop'])
def stop(msg):
    bot.send_message(msg.chat.id, "🛑 Surveillance arrêtée. Plus aucune alerte ne sera envoyée.", parse_mode="Markdown")

bot.polling()