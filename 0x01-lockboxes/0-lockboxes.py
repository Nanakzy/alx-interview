def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of list of int): A list of lists where
    each sublist represents keys contained in a box.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    # Number of boxes
    n = len(boxes)

    # Set to keep track of opened boxes
    opened = set()
    opened.add(0)

    # List to keep track of keys we have
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in opened and key < n:
                opened.add(key)
                keys.append(key)
                return len(opened) == n
