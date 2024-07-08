#!/usr/bin/python3
"""
Module to determine if all boxes can be opened using keys found in other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes, where each box contains
                                     keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    opened_boxes = set()
    keys_stack = [0]

    while keys_stack:
        current_key = keys_stack.pop()
        if current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys_stack.extend(boxes[current_key])

    return len(opened_boxes) == len(boxes)
