# EasyControl, an easy-to-use template for creating a fully working userbot on Telegram
# Copyright (C) 2020  Mattia Chiabrando
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram.errors import BadRequest
from pyrogram import Client, Filters, MessageHandler, Message


class Module(object):
    def __init__(self, modules_class):
        modules_class.add_command(
            MessageHandler(self.check, Filters.command('check', modules_class.config['prefix']) & Filters.me),
            'Check if the userbot is online'
        )

    @staticmethod
    async def check(client: Client, message: Message):
        try:
            await client.edit_message_text(message.chat.id, message.message_id, '✌🏻 <b>Userbot online CHECK</b>')
        except BadRequest:
            await client.send_message(message.chat.id, '✌🏻 <b>Userbot online CHECK</b>')
