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

def patch(obj):
    def is_patchable(item):
        return getattr(item[1], 'patchable', False)

    def wrapper(container):
        for name,func in filter(is_patchable, container.__dict__.items()):
            old = getattr(obj, name, None)
            setattr(obj, 'old'+name, old)
            setattr(obj, name, func)
        return container
    return wrapper

def patchable(func):
    func.patchable = True
    return func