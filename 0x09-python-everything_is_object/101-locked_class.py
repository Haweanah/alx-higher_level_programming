#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents user from instantiating new LockedClass attributes
    for anything other than attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
