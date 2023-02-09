#!/usr/bin/python3
"""command"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """command"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self._Square__size = size

    def __str__(self):
        return (f"[Square] {self._Square__size}/{self._Square__size}")
