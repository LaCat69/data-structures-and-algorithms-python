def locate_card(cards: list, target: int) -> int:
    left, right = 0, len(cards) - 1
    while left <= right:
        middle = (left + right) // 2
        if cards[middle] == target:
            return middle
        elif cards[middle] < target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def tests():
    assert locate_card([10, 8, 6, 4, 2, 0], 8) == 1
    assert locate_card([8, 4, 0], 8) == 0
    assert locate_card([12, 8, 4, 0], 0) == 3
    assert locate_card([13, 10, 7, 4, 1], 7) == 2
    assert locate_card([], 1) == -1
    assert locate_card([1], 4) == -1
    print("Good!")

tests()