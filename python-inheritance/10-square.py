#!/usr/bin/python3
"""command"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """command"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
