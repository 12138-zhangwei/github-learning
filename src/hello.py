"""A minimal interactive Python program."""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    clean_name = name.strip() or "GitHub"
    return f"Hello, {clean_name}! Welcome to programming."


if __name__ == "__main__":
    user_name = input("What is your name? ")
    print(greet(user_name))
