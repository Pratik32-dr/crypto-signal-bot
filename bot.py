import telebot
import requests
import time

# 🔥 CONFIGURATION (SETUP YOUR DETAILS HERE)
TOKEN = "7684846910:AAEBuBeZ0SGN2cw1bd6BhsxCKiU8xaOkxzY"
PAYEER_ID = "P1129183274"
TRUST_WALLET_ADDRESS = "bc1qxpze30u7vfukmh7xmdcf9d2ajwqhpjngmcs9ls"
bot = telebot.TeleBot(TOKEN)

# ✅ Binance API URLs
BINANCE_NEWS_API = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
BINANCE_PRICE_API = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSD"

# ✅ Print startup message
print("🚀 GainXpert Crypto Bot Running 24/7... Waiting for commands!", flush=T>

# 🏆 List of Premium Users
premium_users = set()

# 🔥 Welcome Message
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 Welcome to GainXpert Crypto Bot! 🔥\n\n"
        "🚀 Stay ahead with real-time **crypto signals** & **Binance news**.\n"
        "💰 Upgrade to **Premium** for **exclusive trading insights!**\n\n"
        "👉 Use /help to see available commands."
    )

# ℹ️ Help Command
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "**🤖 GainXpert Commands:**\n\n"
        "📌 /start - Welcome message\n"
        "📌 /help - Show command list\n"
        "📌 /news - Latest Binance news\n"
        "📌 /signals - Crypto trading signals\n"
        "📌 /premium - Premium benefits & payment\n"
        "📌 /verify - Verify premium access\n\n"
        "💰 *Upgrade to premium for VIP trading signals!*"
    )

# 📰 Crypto News from Binance API
@bot.message_handler(commands=['news'])
def news(message):
    try:
        response = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
        data = response.json()

        price = float(data["lastPrice"]) 
        change = float(data["priceChangePercent"])

        news_text = f"📢 **Latest Binance News:**\n\n"
        news_text += f"💰 **Bitcoin Price:** ${price:.2f}\n"
        news_text += f"📉 **24h Change:** {change:.2f}%\n\n"
        news_text += "**📈 Stay updated with real-time market trends!**"
        bot.send_message(message.chat.id, news_text)
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Error fetching news. Try again later.")

# 📊 Crypto Signals (Buy, Sell, Hold)
@bot.message_handler(commands=['signals'])
def signals(message):
    user_id = message.chat.id
    with open("premium_users.txt", "r") as f:
        premium_users = set(f.read().splitlines())

    if str(user_id) not in premium_users:
        bot.send_message(user_id, "❌ Only premium users can access trading si>
        return

    # Fetch crypto signal from Binance API
    import requests

    try:
        binance_api = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUS>
        response = requests.get(binance_api)
        data = response.json()
        price_change = float(data['priceChangePercent'])

        if price_change >= 1:
            signal = "📈 **BUY Signal:** BTC is up by 2% or more! 🚀"
        elif price_change <= -1.2:
            signal = "📉 **SELL Signal:** BTC is down by 2% or more! ❌"
        else:
            signal = "⚖ **HOLD Signal:** No significant change, stay steady. [>

        bot.send_message(user_id, f"📡 **Crypto Signal Update**:\n{signal}")
    except Exception as e:
        bot.send_message(user_id, f"❌ Error fetching signals: {str(e)}")

@bot.message_handler(commands=['premium'])
def premium(message):
    bot.send_message(
        message.chat.id,
        "🚀 **Premium Membership Details** 🚀\n\n"
        "💎 **Normal Users:**\n"
        "- ❌ No real-time signals\n"
        "- ❌ Limited API access\n"
        "- ❌ No priority support\n\n"
        "👑 **Premium Users:**\n"
        "- ✅ Real-time trading signals 📈\n"
        "- ✅ Advanced crypto analytics 🏆\n"
        "- ✅ Exclusive Binance insights 🔥\n\n"
        "💰 **Price:** $10 per month\n"
        "📩 **To Upgrade:** Send payment proof\n"
        "🔗 Pay via Payeer: `P1129183274`\n"
        "🔗 Trust Wallet (USDT-BEP20): `bc1qxpze30u7vfukmh7xmdcf9d2ajwqhpjngmc>
    )

@bot.message_handler(commands=['verify'])
def verify(message):
    user_id = str(message.chat.id)  # Convert user ID to string

    try:
        with open("premium_users.txt", "r") as f:
            premium_users = set(f.read().splitlines())  # Read and store premi>

        if user_id in premium_users:
            bot.send_message(
                user_id,
                "🎉 **Verification Successful!**\n\n"
                "✅ You are a **Premium Member** of *GainXpert* 🚀\n"
                "🔥 **Premium Benefits:**\n"
                "📊 Real-time signals with accuracy 📈\n"
                "💰 Exclusive buy/sell alerts 🛒\n"
                "📡 VIP market insights & early news ⏳\n"
                "🔔 Faster updates with no delay ⚡\n"
                "💎 24/7 priority support 🛠\n"
                "💳 Lifetime access to premium features!\n\n"
                "**🎯 Enjoy your premium perks and maximize your gains!** 💰"
            )
        else:
            bot.send_message(
                user_id,
                "⚠️ **Verification Failed!**\n\n"
                "🚨 You are currently using the **FREE version** of *GainXpert>
                "🔓 **Upgrade to Premium** to unlock exclusive benefits!\n\n"
                "💰 **Premium Features Include:**\n"
                "📊 Advanced signals with higher accuracy 📈\n"
                "💎 Private crypto insights & market alerts 🚀\n"
                "⏳ Early buy/sell signals before market moves 📡\n"
                "⚡ Instant news updates from Binance & other sources 📰\n"
                "🛠 24/7 VIP support & expert guidance 💬\n\n"
                "**🔑 Want to Upgrade?**\n"
                "💳 Pay via *Payeer or Trust Wallet* and send proof to the adm>
                "🔄 Use `/premium` to check plans & payment details.\n\n"
                "**📩 Contact Support:** @YourAdminUsername"
            )
    except FileNotFoundError:
        bot.send_message(
            user_id,
            "🚨 **Error: Premium Database Not Found!**\n"
            "🛠 The verification system is currently unavailable.\n"
            "⚙️ Please contact the admin for assistance."
        )

ADMIN_ID = 6777398940

@bot.message_handler(commands=['addpremium'])
def add_premium(message):
    if message.chat.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ You are not authorized to use th>
        return

    try:
        user_id = message.text.split()[1]  # Extract user ID from the message
        with open("premium_users.txt", "a") as f:
            f.write(user_id + "\n")
        bot.send_message(message.chat.id, f"✅ User {user_id} added as a premi>
        bot.send_message(user_id, "🎉 Congratulations! You are now a **Premium>
    except IndexError:
        bot.send_message(message.chat.id, "⚠️ Usage: /addpremium <user_id>")

# 🔄 Run the Bot
bot.polling(skip_pending=True)

