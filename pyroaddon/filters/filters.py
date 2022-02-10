"""
pyroaddon - A monkeypatcher add-on for Pyrogram
Copyright (C) 2022 - <https://github.com/pyroaddon>

This file is part of pyroaddon.

pyroaddon is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyroaddon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyroaddon.  If not, see <https://www.gnu.org/licenses/>.
"""

import pyrogram 

@pyrogram.filters.create
async def ttl_message(_, __, m: pyrogram.types.Message):
    return (m.photo and m.photo.ttl_seconds) or (m.video and m.video.ttl_seconds)
pyrogram.filters.ttl_message = ttl_message

@pyrogram.filters.create
async def video_sticker(_, __, m: pyrogram.types.Message):
    if m.sticker:
        return m.sticker.is_video
    return False
pyrogram.filters.video_sticker = video_sticker
