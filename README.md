# 🏆 JordanTrades Gold Analytics Bot

An automated, compliance-safe Telegram bot utility designed to provide interactive financial calculations, historical volatility metrics, and structural data tracking for the XAUUSD (Gold) market ecosystem. 

Built using `python-telegram-bot` and optimized for direct cloud deployment via Railway.

---

## 🛠️ Project Structure
*   `main.py` - Core execution script containing command routing and interactive menu callbacks.
*   `requirements.txt` - Python project dependencies.
*   `Procfile` - Production worker declaration for cloud app managers.

---

## 🚀 Deployment Instructions

1. Push this repository structure to your GitHub account.
2. Log into your Railway dashboard and select **Deploy from GitHub repository**.
3. Navigate to the **Variables** configuration page inside Railway and declare:
   * **`BOT_TOKEN`**: Paste your official API key token issued by `@BotFather`.
4. Run the deploy sequence. The background infrastructure worker will automatically build and bring the bot online.
