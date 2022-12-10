from typing import Union
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ForceReply,
    Message,
)

from database import cur, save
from utils import create_mention, get_info_wallet, dobrosaldo, get_price
from config import BOT_LINK
from config import BOT_LINK_SUPORTE
from config import ADMIN_CHAT



@Client.on_message(filters.command(["frete", "fretes"]))
@Client.on_callback_query(filters.regex("^frete$"))
async def frete(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    #precos abaixo
    preco1 = "5"
    preco2 = "6"
    preco3 = "9"
    preco4 = "11"
    preco5 = "98"
    preco6 = "7"
    preco7 = "1"
    preco8 = "3"
    preco9 = "10"
    preco10 = "2"
    preco11 = "5"
    preco12 = "6"
    preco13 = "9"
    preco14 = "11"
    preco15 = "98"
    preco16 = "7"
    preco17 = "1"
    preco18 = "3"
    preco19 = "10"
    preco20 = "2"
    preco21 = "5"
    preco22 = "6"
    preco23 = "9"
    preco24 = "11"
    preco25 = "98"
    preco26 = "7"
    preco27 = "7"
    

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("AC", callback_data=f"frete_1 {preco1} Acre"),
                InlineKeyboardButton("AL", callback_data=f"frete_2 {preco2} Alagoas"),
            ],
            
            [
                InlineKeyboardButton("AP", callback_data=f"frete_3 {preco3} Amapa"),
                InlineKeyboardButton("AM", callback_data=f"frete_4 {preco4} Amazonas"),
                
            ],
            [
                InlineKeyboardButton("BA", callback_data=f"frete_5 {preco5} Bahia"),
                InlineKeyboardButton("CE", callback_data=f"frete_6 {preco6} Ceará"),
            ],
            
             [
                InlineKeyboardButton("DF", callback_data=f"frete_7 {preco7} DistritoFederal"),
                InlineKeyboardButton("ES", callback_data=f"frete_8 {preco8} EspiritoSanto"),
            ],
             [
                InlineKeyboardButton("GO", callback_data=f"frete_9 {preco9} Goias"),
                InlineKeyboardButton("MA", callback_data=f"frete_10 {preco10} Maranhao"),
            ],
            
            [
                InlineKeyboardButton("MT", callback_data=f"frete_11 {preco11} MatoGrosso"),
                InlineKeyboardButton("MS", callback_data=f"frete_12 {preco12} MatoGrossoDoSul"),
            ],
            
            [
                InlineKeyboardButton("MG", callback_data=f"frete_13 {preco13} MinasGerais"),
                InlineKeyboardButton("PA", callback_data=f"frete_14 {preco14} Para"),
                
            ],
            [
                InlineKeyboardButton("PB", callback_data=f"frete_15 {preco15} Paraiba"),
                InlineKeyboardButton("PR", callback_data=f"frete_16 {preco16} Parana"),
            ],
            
             [
                InlineKeyboardButton("PE", callback_data=f"frete_17 {preco17} Pernambuco"),
                InlineKeyboardButton("PI", callback_data=f"frete_18 {preco18} Piaui"),
            ],
             [
                InlineKeyboardButton("RJ", callback_data=f"frete_19 {preco19} RioDeJaneiro"),
                InlineKeyboardButton("RN", callback_data=f"frete_20 {preco20} RioGrandeDoNorte"),
            ],
            
            [
                InlineKeyboardButton("RS", callback_data=f"frete_21 {preco21} RioGrandeDoSul"),
                InlineKeyboardButton("RO", callback_data=f"frete_22 {preco22} Rondonia"),
            ],
            
            [
                InlineKeyboardButton("RR", callback_data=f"frete_23 {preco23} Roraima"),
                InlineKeyboardButton("SP", callback_data=f"frete_24 {preco24} SaoPaulo"),
                
            ],
            [
                InlineKeyboardButton("SC", callback_data=f"frete_25 {preco25} SantaCatarina"),
                InlineKeyboardButton("SE", callback_data=f"frete_26 {preco26} Sergipe"),
            ],
            
             [
                InlineKeyboardButton("TO", callback_data=f"frete_27 {preco27} Tocantins"),
            ],
            [
               InlineKeyboardButton("Voltar", callback_data=f"start"),
            ],
            
        ]
    )

    bot_logo, news_channel, support_user = cur.execute(
        "SELECT main_img, channel_user, support_user FROM bot_config WHERE ROWID = 0"
    ).fetchone()

    start_message = f"""Compre aqui o frete para que seu envio seja feito. ✈️
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
    
    
    

@Client.on_callback_query(filters.regex("^frete_1 (?P<value>\w+) (?P<id>.+)"))
async def frete_1(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_1 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_1} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_1}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)

    
@Client.on_callback_query(filters.regex("^frete_2 (?P<value>\w+) (?P<id>.+)"))
async def frete_2(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_2 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_2} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_2}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
 
@Client.on_callback_query(filters.regex("^frete_3 (?P<value>\w+) (?P<id>.+)"))
async def frete_3(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_3 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_3} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_3}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)    
    

    
@Client.on_callback_query(filters.regex("^frete_4 (?P<value>\w+) (?P<id>.+)"))
async def frete_4(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_4 = m.matches[0]["value"]
    id = m.matches[0]["id"]

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_4} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_4}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
                
                            
@Client.on_callback_query(filters.regex("^frete_5 (?P<value>\w+) (?P<id>.+)"))
async def frete_5(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_5 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_5} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_5}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
                                           
                                                                                  
@Client.on_callback_query(filters.regex("^frete_6 (?P<value>\w+) (?P<id>.+)"))
async def frete_6(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_6 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_6} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_6}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                                                                                                                         
                                                                                                                                                                  
  
@Client.on_callback_query(filters.regex("^frete_7 (?P<value>\w+) (?P<id>.+)"))
async def frete_7(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_7 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_7} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_7}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)  
  

  
@Client.on_callback_query(filters.regex("^frete_8 (?P<value>\w+) (?P<id>.+)"))
async def frete_8(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_8 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_8} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_8}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)    

        
                
@Client.on_callback_query(filters.regex("^frete_9 (?P<value>\w+) (?P<id>.+)"))
async def frete_9(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_9 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_9} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_9}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                        

                                        
@Client.on_callback_query(filters.regex("^frete_10 (?P<value>\w+) (?P<id>.+)"))
async def frete_10(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_10 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_10} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_10}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_11 (?P<value>\w+) (?P<id>.+)"))
async def frete_11(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_11 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_11} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_11}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_12 (?P<value>\w+) (?P<id>.+)"))
async def frete_12(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_12 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_12} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_12}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_13 (?P<value>\w+) (?P<id>.+)"))
async def frete_13(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_13 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_13} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_13}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_14 (?P<value>\w+) (?P<id>.+)"))
async def frete_14(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_14 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_14} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_14}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_15 (?P<value>\w+) (?P<id>.+)"))
async def frete_15(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_15 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_15} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_15}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    

@Client.on_callback_query(filters.regex("^frete_16 (?P<value>\w+) (?P<id>.+)"))
async def frete_16(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_16 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_16} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_16}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_17 (?P<value>\w+) (?P<id>.+)"))
async def frete_17(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_17 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_17} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_17}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)

@Client.on_callback_query(filters.regex("^frete_18 (?P<value>\w+) (?P<id>.+)"))
async def frete_18(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_18 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_18} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_18}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_19 (?P<value>\w+) (?P<id>.+)"))
async def frete_19(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_19 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_19} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_19}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_20 (?P<value>\w+) (?P<id>.+)"))
async def frete_20(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_20 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_20} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_20}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_21 (?P<value>\w+) (?P<id>.+)"))
async def frete_21(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_21 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_21} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_21}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_22 (?P<value>\w+) (?P<id>.+)"))
async def frete_22(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_22 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_22} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_22}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_23 (?P<value>\w+) (?P<id>.+)"))
async def frete_23(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_23 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_23} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_23}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_24 (?P<value>\w+) (?P<id>.+)"))
async def frete_24(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_24 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_24} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_24}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_25 (?P<value>\w+) (?P<id>.+)"))
async def frete_25(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_25 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_25} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_25}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_26 (?P<value>\w+) (?P<id>.+)"))
async def frete_26(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_26 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_26} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_26}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""
    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
    
@Client.on_callback_query(filters.regex("^frete_27 (?P<value>\w+) (?P<id>.+)"))
async def frete_27(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id
    frete_27 = m.matches[0]["value"]
    id = m.matches[0]["id"]


    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
           [
                InlineKeyboardButton("Comprar",callback_data=f"buyfrete {frete_27} {id}"),
            ],
[
                InlineKeyboardButton("Voltar para o Menu Frete✈️",callback_data="frete"),
            ],
            ]
    )
    

    link_foto = "https://i.ibb.co/7WfMhhM/avatar-1521775404.jpg"
    
    
    start_message = f"""<a href='{link_foto}'>&#8204</a>
<b>Preco:</b> {frete_27}


Após a compra do frete e do produto só aguardar o envio da mercadoria. 😜
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)                                                                                
                                                                                                                                                                
#@Client.on_callback_query(filters.regex(r"^buyfrete (?P<value>\w+) (?P<id>.+)"))
#async def buyfrete_food(c: Client, m: CallbackQuery):
#	await m.message.delete()
#	user_id = m.from_user.id
#	qry = m.matches[0]["value"]
#	id = m.matches[0]["id"]
#	start_message = f"SEU PEDIIDO FOI FEITO, ID: {id}"




#if None in (dados[0], dados[2]) and select_pay == "mercado pago":
#        name = await m.message.ask("Informe o cep", reply_markup=ForceReply())
#else:
	
#@Client.on_callback_query(
#    filters.regex(r"buyfrete (?P<value>.+) (?P<id>.+)")
#)
#async def buyfrete(c: Client, m: CallbackQuery):
#    await m.message.delete()
#    dados = cur.execute("SELECT cpf, name, email FROM users  WHERE id =?", [m.from_user.id]).fetchone()
#    qry = m.matches[0]["value"]
#    id = qry = m.matches[0]["value"]
#    buyfrete = "buyfrete"
#    
#if None in (dados[0], dados[2]) and buyfrete == "buyfrete":
#    name = await m.message.ask("Informe o nome do cep", reply_markup=ForceReply())
#   # isExist = os.path.exists(name.text)
#else:
#	await m.edit_message_text(f"""<b>Seu pedido foi efetuado com sucesso</b>
#Valor: {qry}
#Pedido: {id}

#Observações: podemos entrar em contato com você caso algo aconteça com seu pedido🍟

#Endereço de entrega: """,)
@Client.on_callback_query(
    filters.regex(r"buyfrete (?P<value>.+) (?P<id>.+)")
)
async def buyfrete_frete(c: Client, m: CallbackQuery):

    qry = m.matches[0]["value"]
    id = m.matches[0]["id"]
    dados = cur.execute(
        "SELECT cpf, name, email FROM users  WHERE id = ?", [m.from_user.id]
    ).fetchone()
    user_id = m.from_user.id
    balance: int = cur.execute("SELECT balance FROM users WHERE id = ?", [user_id]).fetchone()[0]
    price = int(qry)

    if balance < price:
        return await m.answer(
            "Você não possui saldo para realizar esta compra. Por favor, adicione saldo no menu principal.",
            show_alert=True,
        )
        
#    await m.message.delete()
#    name = await m.message.ask("""Informe o endereco completo de entrega\n
#NOME:
#CPF;
#ENDEREÇO:
#N⁰:
#COMPLEMENTO: 
#BAIRRO:
#CIDADE:
#ESTADO:
#CEP:""", reply_markup=ForceReply())
    


    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(f"ID: #{id}", callback_data=f"{id}")],
        ]
    )


    await m.message.reply_text(
        f"""<b>Seu pedido foi efetuado com sucesso</b>
Valor: {qry}
Pedido: {id}

Observações: seu pedido estará em breve em sua casa!🍟""", reply_markup=kb
    )	
    new_balance = balance - price
    diamonds = 0
    cur.execute(
        "UPDATE users SET balance = ?, balance_diamonds = round(balance_diamonds + ?, 2) WHERE id = ?",
        [new_balance, diamonds, user_id],
    )
    mention = create_mention(m.from_user)
    await m.message.reply_text(
        f"""<b>Foram descontados {qry} da sua carteira, seu pedido estará em breve em sua casa!

Observações: em caso de problemas entraremos em contato</b>
""", )
    adm_msg = f"""Usuário: {mention} comprou um: {id}
Valor: {qry}

Status: Pago com sucesso"""	  
    await c.send_message(ADMIN_CHAT, adm_msg)