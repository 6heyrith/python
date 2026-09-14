# # Final project: 


from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8611382716:AAHtyJE_gCEHAXb5SJEInDJ-hwmzKDWk8xM"

class Country:
    # Manually defined constructor replacing
    def __init__(self, capital: str, population: str, currency: str, region: str):
        self.capital = capital
        self.population = population
        self.currency = currency
        self.region = region

    def __str__(self):
        return f"🏛 Capital: {self.capital}\n👥 Population: {self.population}\n🪙 Currency: {self.currency}\n📍 Region: {self.region}"

DATA = {
    "cambodia": Country("Phnom Penh", "16.9 million", "Riel (KHR)", "Southeast Asia"),
    "japan": Country("Tokyo", "125.1 million", "Yen (JPY)", "East Asia"),
    "france": Country("Paris", "67.7 million", "Euro (EUR)", "Western Europe"),
    "vietnam": Country("Hanoi", "98.8 million", "Dong (VND)", "Southeast Asia"),
    "south_korea": Country("Seoul", "51.7 million", "Won (KRW)", "East Asia"),
    "brazil": Country("Brasília", "215.3 million", "Real (BRL)", "South America"),
    "germany": Country("Berlin", "84.4 million", "Euro (EUR)", "Western Europe"),
    "canada": Country("Ottawa", "38.9 million", "Canadian Dollar (CAD)", "North America"),
    "egypt": Country("Cairo", "112.7 million", "Egyptian Pound (EGP)", "North Africa"),
    "australia": Country("Canberra", "26.0 million", "Australian Dollar (AUD)", "Oceania"),
    "india": Country("New Delhi", "1.43 billion", "Indian Rupee (INR)", "South Asia"),
    "kenya": Country("Nairobi", "54.0 million", "Kenyan Shilling (KES)", "East Africa"),
    "united_states": Country("Washington, D.C.", "333.3 million", "US Dollar (USD)", "North America"),
    "united_kingdom": Country("London", "67.3 million", "Pound Sterling (GBP)", "Northern Europe"),
    "italy": Country("Rome", "58.9 million", "Euro (EUR)", "Southern Europe"),
    "spain": Country("Madrid", "47.4 million", "Euro (EUR)", "Southern Europe"),
    "mexico": Country("Mexico City", "127.5 million", "Mexican Peso (MXN)", "North America"),
    "argentina": Country("Buenos Aires", "45.8 million", "Argentine Peso (ARS)", "South America"),
    "singapore": Country("Singapore", "5.6 million", "Singapore Dollar (SGD)", "Southeast Asia"),
    "indonesia": Country("Jakarta", "275.5 million", "Rupiah (IDR)", "Southeast Asia"),
    "south_africa": Country("Pretoria", "59.9 million", "Rand (ZAR)", "Southern Africa"),
}

async def reply_capital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    country = update.message.text.strip().lower()
    info = DATA.get(country)

    if info:
        await update.message.reply_text(str(info))
    else:
        await update.message.reply_text(f"❌ '{update.message.text}' doesn't look like a valid country name. Try again!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_capital))
app.run_polling()

# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters


# BOT_TOKEN = "8611382716:AAHtyJE_gCEHAXb5SJEInDJ-hwmzKDWk8xM"

# class Country:
#     # Manually defined constructor replacing
#     def __init__(self, capital: str, population: str, currency: str, region: str):
#         self.capital = capital
#         self.population = population
#         self.currency = currency
#         self.region = region

#     def __str__(self):
#         return f"'🏛 Capital: {self.capital}\n👥 Population: {self.population}\n🪙 Currency: {self.currency}\n📍 Region: {self.region}'"

# DATA = {
#     "cambodia": Country("Phnom Penh", "16.9 million", "Riel (KHR)", "Southeast Asia"),
#     "japan": Country("Tokyo", "125.1 million", "Yen (JPY)", "East Asia"),
#     "france": Country("Paris", "67.7 million", "Euro (EUR)", "Western Europe"),
# }

# async def reply_capital(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     country = update.message.text.strip().lower()
#     info = DATA.get(country)

#     if info:
#         await update.message.reply_text(str(info))
#     else:
#         await update.message.reply_text(f"❌ '{update.message.text}' doesn't look like a valid country name. Try again!")

# app = ApplicationBuilder().token(BOT_TOKEN).build()
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_capital))
# app.run_polling()


