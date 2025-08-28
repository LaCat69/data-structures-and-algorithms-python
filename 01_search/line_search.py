def locate_cards(cards, target):
    i = 0
    while i < len(cards):
        if cards[i] == target:
            return i
        i += 1
    return -1

def tests():
    assert locate_cards([20, 10, 5, 0], 10) == 1
    assert locate_cards([4, 3, 2, 1, 0], 4) == 0
    assert locate_cards([4, 3, 2, 1, 0], 0) == 4
    assert locate_cards([5, 4, 3, 2, 1, 0], 7) == -1
    assert locate_cards([], 1) == -1
    print("Good!")

tests()