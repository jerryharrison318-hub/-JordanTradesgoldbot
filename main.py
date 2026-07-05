import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Set up logging tracking
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# System fetches your token automatically from Railway Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_URL = "https://t.me/xauusdcult"

def get_main_keyboard():
    """Generates the primary premium menu layout."""
    keyboard = [
        [InlineKeyboardButton("📢 Join XAUUSD CULT Channel", url=CHANNEL_URL)],
        [InlineKeyboardButton("🧰 Gold Position Calculator", callback_data="calc")],
        [InlineKeyboardButton("📈 XAUUSD Volatility Analytics", callback_data="volatility")],
        [InlineKeyboardButton("📚 Gold Trading Education", callback_data="edu")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🏆 **Welcome to JordanTrades Gold Analytics**\n\n"
        "Your utility control panel for XAUUSD execution structures, historical gold volatility baselines, "
        "and advanced risk calculation systems.\n\n"
        "✨ *Select an analytical utility below to optimize your gold market data tracking:* \n\n"
        "⚠️ *Disclaimer: This platform provides educational market analytics and formulas only. "
        "Content does not constitute financial or trade execution advice.*"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown", reply_markup=get_main_keyboard())

async def button_dispatcher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Back to Main Menu handler
    if query.data == "back_to_menu":
        welcome_text = (
            "🏆 **JordanTrades Gold Analytics Menu**\n\n"
            "Select an analytical utility below to optimize your gold market data tracking:"
        )
        await query.edit_message_text(text=welcome_text, reply_markup=get_main_keyboard(), parse_mode="Markdown")
        return

    # Back button to recycle menus
    back_btn = [[InlineKeyboardButton("⬅️ Back to Core Menu", callback_data="back_to_menu")]]
    back_markup = InlineKeyboardMarkup(back_btn)

    if query.data == "calc":
        calc_text = (
            "🧰 **Gold Risk & Position Size Metrics**\n"
            "--- \n"
            "Calculate standard contract size metrics on XAUUSD instantly:\n\n"
            "• **1.0 Standard Lot:** 100 Ounces of Gold ($10.00 per pip move)\n"
            "• **0.10 Mini Lot:** 10 Ounces of Gold ($1.00 per pip move)\n"
            "• **0.01 Micro Lot:** 1 Ounce of Gold ($0.10 per pip move)\n\n"
            "👉 *Standard Gold Lot Equation Formula:* \n"
            "$$Lot = \\frac{Account\\ Risk\\ Value}{(Stop\\ Loss\\ in\\ Pips \\times 0.10)}$$"
        )
        await query.edit_message_text(text=calc_text, reply_markup=back_markup, parse_mode="Markdown")

    elif query.data == "volatility":
        vol_text = (
            "📈 **XAUUSD Daily Volatility Baselines**\n"
            "--- \n"
            "Gold is a high-liquidity asset with significant historical daily ranges.\n\n"
            "📊 **Average True Range (ATR) Metrics:**\n"
            "• Quiet Session Conditions: 150 - 250 Pips\n"
            "• Standard New York Session Range: 300 - 500 Pips\n"
            "• Macro-Economic Impact Events (NFP/CPI): 700+ Pips\n\n"
            "💡 *Risk Protocol: Adjust stop-loss parameters wider during critical data releases to stay protected.*"
        )
        await query.edit_message_text(text=vol_text, reply_markup=back_markup, parse_mode="Markdown")

    elif query.data == "edu":
        edu_text = (
            "📚 **Gold Trading Structural Concepts**\n"
            "--- \n"
            "Master the specific variables that influence structural gold pricing changes:\n\n"
            "1️⃣ **US Dollar Inverse Scaling:** Gold price trends generally rise when the US Dollar index drops, and vice versa.\n"
            "2️⃣ **Risk-Off Liquidity Inflows:** Geopolitical escalations or global economic uncertainty historically drive investors into Gold as a safe haven.\n"
            "3️⃣ **Session Windows:** Maximum market momentum occurs during the London/New York session overlap."
        )
        await query.edit_message_text(text=edu_text, reply_markup=back_markup, parse_mode="Markdown")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(button_dispatcher))
    application.run_polling()

if __name__ == "__main__":
    main()
