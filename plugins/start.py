
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.enums import ParseMode
import time
import random
import string as rohit

from config import SHORTLINK_API, SHORTLINK_URL, VERIFY_EXPIRE, TUT_VID, BAN_SUPPORT, START_MSG
from database import db
from utils import get_shortlink, get_exp_time, is_premium_user


@Client.on_message(filters.command('start') & filters.private)
async def start_command(client, message: Message):
    user_id = message.from_user.id
    text = message.text.strip()
    is_premium = await is_premium_user(user_id)
    verify_status = await db.get_verify_status(user_id)

    # CASE 1: Plain /start
    if text == "/start":
        return await message.reply_text(
            START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username='@' + message.from_user.username if message.from_user.username else None,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🤤 Jᴏɪɴ Aᴅᴜʟᴛ Hᴜʙ', url='https://t.me/+oOvo2Un_OC4xNWIx')],
                [
                    InlineKeyboardButton('🍿 Mᴏᴠɪᴇ ɢʀᴏᴜᴘ', url='https://t.me/MovieRequestGroupNj'),
                    InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/unfiltered_stuf')
                ],
                [
                    InlineKeyboardButton('💁‍♀️ ʜᴇʟᴘ', callback_data='help'),
                    InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                ]
            ]),
            parse_mode=ParseMode.HTML
        )

    # CASE 2: /start verify_TOKEN
    elif text.startswith("/start verify_"):
        try:
            token = text.split("verify_")[1]
            if verify_status['verify_token'] != token:
                return await message.reply("❌ Invalid or expired token. Please click /start again.")
            await db.update_verify_status(user_id, is_verified=True, verified_time=time.time())
            current = await db.get_verify_count(user_id)
            await db.set_verify_count(user_id, current + 1)
            return await message.reply("✅ You have been verified successfully.")
        except Exception:
            return await message.reply("⚠️ Invalid verification link. Please click /start again.")


@Client.on_callback_query()
async def callback_handler(client, callback_query: CallbackQuery):
    data = callback_query.data

    elif data == "about":
    await callback_query.message.edit(
        text="<b>👑 Aʙᴏᴜᴛ:\n\nI ᴀᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴀᴅs & ᴘʀᴇᴍɪᴜᴍ ᴜɴʟᴏᴄᴋ.</b>",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⟵ Bᴀᴄᴋ", callback_data="back")]
        ]),
        parse_mode=ParseMode.HTML
    )

I ᴀᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴀᴅs & ᴘʀᴇᴍɪᴜᴍ ᴜɴʟᴏᴄᴋ.</b>",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⟵ Bᴀᴄᴋ", callback_data="back")]
            ]),
            parse_mode=ParseMode.HTML
        )

    elif data == "help":
        await callback_query.message.edit(
            text="<b><blockquote>Tʜɪs ɪs Aɴ Pʀɪᴠᴀᴛᴇ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ Wᴏʀᴋɪɴɢ ɪɴ @ᴜɴғɪʟᴛᴇʀᴇᴅ_sᴛᴜғ

❏ Bᴏᴛ Cᴏᴍᴍᴀɴᴅs
├ /start : Sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
├ /about : Aʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
└ /help : Hᴇʟᴘ Mᴇɴᴜ

Sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ.</blockquote></b>

<b>Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ:</b> <a href='https://t.me/Mrxonfiree'>Mʀxᴏɴꜰɪʀᴇ</a>",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⟵ Bᴀᴄᴋ", callback_data="back")]
            ]),
            parse_mode=ParseMode.HTML
        )

    elif data == "premium":
        await callback_query.message.edit(
            text="<b>💎 Premium Plan:</b>

Uɴʟᴏᴄᴋ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇs ʙʏ ᴜᴘɢʀᴀᴅɪɴɢ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.
Cᴏɴᴛᴀᴄᴛ @Mrxonfiree ᴛᴏ ᴘᴜʀᴄʜᴀsᴇ.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⟵ Bᴀᴄᴋ", callback_data="back")]
            ]),
            parse_mode=ParseMode.HTML
        )

    elif data == "back":
        await callback_query.message.edit(
            text=START_MSG.format(
                first=callback_query.from_user.first_name,
                last=callback_query.from_user.last_name,
                username='@' + callback_query.from_user.username if callback_query.from_user.username else None,
                mention=callback_query.from_user.mention,
                id=callback_query.from_user.id
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🤤 Jᴏɪɴ Aᴅᴜʟᴛ Hᴜʙ', url='https://t.me/+oOvo2Un_OC4xNWIx')],
                [
                    InlineKeyboardButton('🍿 Mᴏᴠɪᴇ ɢʀᴏᴜᴘ', url='https://t.me/MovieRequestGroupNj'),
                    InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/unfiltered_stuf')
                ],
                [
                    InlineKeyboardButton('💁‍♀️ ʜᴇʟᴘ', callback_data='help'),
                    InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                ]
            ]),
            parse_mode=ParseMode.HTML
        )

    elif data == "close":
        await callback_query.message.delete()
