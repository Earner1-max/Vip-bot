"""
🤖 USDT Airdrop Bot - Premium Edition
🌟 Enhanced with VIP emoji experience
"""

import asyncio
import logging
import sqlite3
import threading
import time
from datetime import datetime
from typing import Optional, List, Tuple
import os
import requests

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import MessageNotModified, TelegramAPIError

# =============================================================================
# 🔐 CONFIGURATION (Updated with your token)
# =============================================================================
BOT_TOKEN = "7080210749:AAEkHPglZHRcwns3jEdF4n8kmz0i61OClvc"
ADMIN_USER_ID = 5574348933  # Your admin ID

# VIP Channels Configuration
CHANNELS = [
    {"name": "✨ Premium Crypto", "username": "@Restrictionlesschat", "url": "https://t.me/Restrictionlesschat"},
    {"name": "💰 USDT Deals", "username": "@botfypay", "url": "https://t.me/botfypay"},
    {"name": "🚀 Income Group", "username": "@groupofincom", "url": "https://t.me/groupofincom"},
    {"name": "🔍 Crypto Hunter", "username": "@Crpto_Hnter", "url": "https://t.me/Crpto_Hnter"}
]

# 💎 Premium Messages with VIP Emojis
MESSAGES = {
    "welcome": (
        "✨🌟 *WELCOME TO VIP USDT AIRDROP!* 🌟✨\n\n"
        "💰 *INSTANT BONUSES WAITING!*\n\n"
        "🎁 *YOUR REWARDS:*\n"
        "• 🎉 0.12 USDT Welcome Gift\n"
        "• 👥 0.10 USDT Per Friend\n"
        "• ⚡ Instant Withdrawals\n"
        "• 🚀 Premium Earnings\n\n"
        "👇 *Join our VIP channels to start!*"
    ),
    "verification_success": (
        "🎊 *VIP ACCESS GRANTED!* 🎊\n\n"
        "💰 *Your account is activated with:*\n"
        "• 💎 0.12 USDT Bonus\n"
        "• 🔑 Personal Referral Link\n"
        "• 💸 Withdrawal Privileges\n\n"
        "🚀 Start earning now!"
    ),
    # ... [rest of the original bot.py content remains exactly the same]
}

# ... [rest of the original bot.py code remains unchanged]

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"💥 Critical error: {e}")