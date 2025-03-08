import telebot
import requests
import json

TOKEN = 7684846910:AAEBuBeZ0SGN2cw1bd6BhsxCKiU8xaOkxzY
bot = telebot.TeleBot(TOKEN)

# 🏦 Crypto API URLs
COIN_API_URL = https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
NEWS_API_URL = https://www.binance.com/en/news

# 🎯 Start Command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 
        "🚀 *Welcome to the Crypto Signal Bot!*\n"
        "📈 Get real-time prices & AI-powered signals.\n"
        "📝 Use /help to see all commands.", parse_mode="Markdown")

# 🛠 Help Command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 
        "📌 *Available Commands:*\n"
        "/price BTC - Get Bitcoin Price\n"
        "/signals - Get Today's Crypto Signal\n"
        "/news - Get Latest Crypto News", parse_mode="Markdown")

# 📊 Crypto Price Command
@bot.message_handler(commands=['price'])
def get_price(message):
    try:
        coin = message.text.split()[1].lower()
        response = requests.get(COIN_API_URL.format(coin))
        data = response.json()
        price = data[coin]['usd']
        bot.send_message(message.chat.id, f"💰 *{coin.upper()} Price:* ${price}", parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, "❌ Invalid Coin Name. Try `/price BTC`", parse_mode="Markdown")

# 📉 AI-Generated Crypto Signals
@bot.message_handler(commands=['signals'])
def get_real_signal():
    response = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT")
    data = response.json()
    price_change = float(data['priceChangePercent'])
    return "BUY" if price_change > 2 else "SELL" if price_change < -2 else "HOLD"
    
    

# 📰 Latest Crypto News
@bot.message_handler(commands=['news'])
def get_news(message):
    response = requests.get(NEWS_API_URL)
    news = response.json()['data'][0]['title']
    bot.send_message(message.chat.id, f"📰 *Latest News:* {news}", parse_mode="Markdown")

# 🚀 Run the bot
bot.polling()
