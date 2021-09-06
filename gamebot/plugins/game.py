from uuid import uuid4

from pyrogram import Client, filters
from pyrogram.raw.functions.messages import (
    SendMedia,
    SetInlineBotResults,
)
from pyrogram.raw.types import (
    InputBotInlineMessageGame,
    InputBotInlineResultGame,
    InputMediaGame,
    InputGameShortName,
)
from pyrogram.types import Message, InlineQuery, CallbackQuery

from gamebot.config import shared
from gamebot.utils import ADMINS


@Client.on_message(filters.command("game") & ADMINS)
async def send_game(bot: Client, msg: Message):
    r = await bot.send(
        SendMedia(
            peer=await bot.resolve_peer(msg.chat.id),
            media=InputMediaGame(
                id=InputGameShortName(
                    bot_id=await bot.resolve_peer("self"),
                    short_name=shared.settings.GAME,
                )
            ),
            message="",
            random_id=bot.rnd_id(),
        )
    )


@Client.on_inline_query()
async def inline_game(bot: Client, query: InlineQuery):
    return await bot.send(
        SetInlineBotResults(
            query_id=int(query.id),
            results=[
                InputBotInlineResultGame(
                    id=uuid4().hex,
                    short_name=shared.settings.GAME,
                    send_message=InputBotInlineMessageGame(
                        reply_markup=None,
                    ),
                )
            ],
            cache_time=0,
            private=True,
        )
    )


@Client.on_callback_query()
async def game_callback(bot: Client, query: CallbackQuery):
    return await query.answer(
        text=f"Test text | Game: {query.game_short_name!r}",
        show_alert=True,
        url=f"https://duckduckgo.com/?q={query.game_short_name}",
        cache_time=0,
    )


# @Client.on_raw_update(group=-10)
# async def _raw(bot: Client, update: Update, users: Dict[int, User], chats: Dict[int, Chat]):
#     # print(type(x) for x in (update, users, chats))
#     # print(update, users, chats)
#     print(update)
#     # if isinstance(update, int):
#     #     print(update)
#     # else:
#     #     raise ContinuePropagation()
