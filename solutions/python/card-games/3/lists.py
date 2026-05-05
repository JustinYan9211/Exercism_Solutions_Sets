"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

JACK = 11


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param number: Current round number.
    :return: Current round and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: First rounds played.
    :param rounds_2: Second set of rounds played.
    :return: All rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: Rounds played.
    :param number: Round number.
    :return: Whether the round was played.
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and return the average card value from the list.

    :param hand: Cards in hand.
    :return: Average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Check if an approximate average equals the actual average.

    :param hand: Cards in hand.
    :return: Whether one of the approximate averages equals the actual average.
    """
    actual_average = card_average(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]

    return actual_average in (first_last_average, middle_card)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Check if the average of even-indexed cards equals the average of odd-indexed cards.

    :param hand: Cards in hand.
    :return: Whether even and odd indexed averages are equal.
    """
    even_indexed_cards = hand[::2]
    odd_indexed_cards = hand[1::2]

    return card_average(even_indexed_cards) == card_average(odd_indexed_cards)


def maybe_double_last(hand: list[int]) -> list[int]:
    """Double the last card if it is a Jack.

    :param hand: Cards in hand.
    :return: Hand with the last Jack card doubled, if present.
    """
    if hand[-1] == JACK:
        hand[-1] *= 2

    return hand
