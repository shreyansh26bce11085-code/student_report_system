"""Helper module for validated console user input."""


def read_int(prompt: str) -> int:
    """Prompts user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_float(prompt: str) -> float:
    """Prompts user until a valid float is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")
