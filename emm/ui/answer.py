import sys
import time
import random

from rich import print


def typewriter_effect(text, speed_range=(0.001, 0.02)):
    """
    Print text with a typewriter effect.

    :param text: The text to print.
    :param speed: Time interval between characters (in seconds).
    """
    min_speed, max_speed = speed_range
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_speed, max_speed))
    print()


def get_user_answer(ans):
    print("[bold blue]Response from GPT: ")
    typewriter_effect(ans)
    return
