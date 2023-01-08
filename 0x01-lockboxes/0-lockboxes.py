#!/usr/bin/python3
"""defines the function `canUnlockAll`"""


def canUnlockAll(boxes):
    """determines of all `boxes` can be unlocked"""
    unlocked = [0]  # boxes whose keys are found
    searched = []  # boxes opened and searched for more keys
    new_key = []  # temporary container for new keys

    # since `box 0` can be opened without a key
    for key in boxes[0]:
        if key in range(len(boxes)) and key not in unlocked:
            unlocked.append(key)
    searched.append(0)

    # search for more keys until all boxes whose keys are found are all opened
    while len(unlocked) > len(searched):
        for key in unlocked:
            if key not in searched:
                for elm in boxes[key]:
                    if elm in range(len(boxes)) and elm not in unlocked:
                        new_key.append(elm)
                searched.append(key)
        unlocked.extend(new_key)
        new_key.clear()

    unlocked.sort()
    return unlocked == list(range(len(boxes)))
