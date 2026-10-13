#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
### A Python Class to contain state across multiple functions and modules.
###
### Copyright (C) 2026 Christopher D. Shramko
###
### This library is free software; you can redistribute it and/or
### modify it under the terms of the GNU Library General Public License
### as published by the Free Software Foundation; either version 2 of
### the License, or (at your option) any later version.
###
### This library is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty
### of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
### See the GNU Library General Public License for more details.
###
### You should have received a copy of the GNU Library General Public
### License along with this library; if not, write to:
###   Free Software Foundation, Inc.
###   51 Franklin St, Fifth Floor
###   Boston, MA 02110-1301, USA
###

from ast import Return
from typing import Any

class State:
    """
    A Python Class to contain state across
    multiple functions and modules.

    Initializes a Class Instance of dictionary object
    to contain the state of the importing Python script
    and its called functions and modules.

    In an assignment, sets the value of
    the attribute named <name> to <value>.
    Non-existant attribute will be created.

    In a reference, returns the value of
    the attribute named <name>. Raises 'AttributeError'
    if the attribute does not exist.
    
    state.toggle(<name>)
        Toggles the value of bool attribute named <name>
        (False becomes True, True becomes False).
        Returns 'AttributeError' if the attribute is not a bool.
    """

    def __init__(self) -> None:
        """
        Initializes a Class Instance of dictionary object
        to contain the state of the importing Python script
        and its called functions and modules.
        """
        self._data: dict[str, object] = {
            # "debug"     : False,
            # "show"      : False,
            # "verbose"   : 2,
            # "quiet"     : 0,
        }
    # end def __init__()

    def getattr(self, name: str) -> Any:
        """
        In a reference, returns the value of
        the attribute named <name>. Raises'AttributeError'
        if the attribute does not exist.
        """
        if name in self._data:
            return self._data[name]
        else:
            raise AttributeError(f"{name} is not a valid state attribute")
    # end def getattr()


    def setattr(self, name: str, value: Any) -> None:
        """
        In an assignment, sets the value of
        the attribute named <name> to <value>.
        Non-existant attribute will be created.
        """
        self._data[name] = value
    # end def setattr()

    def toggle(self, name: str) -> None:
        """
        Toggles the value of bool attribute named <name>
        (False becomes True, True becomes False).
        Returns 'AttributeError' if the attribute is not a bool.
        """
        if name in self._data and isinstance(self._data[name], bool):
            self._data[name] = not self._data[name]
        else:
            raise AttributeError(f"{name} is not a boolean state attribute")
    # end def toggle()

# end class State

# Instantiate the variable object which functions and modules can reference.
state = State()
