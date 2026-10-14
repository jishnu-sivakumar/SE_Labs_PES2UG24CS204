import sys
from game import WordleGame


def select_word_length() -> int:
    """Gets word length from CLI argument if specified, or prompts the user interactively."""
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip()
        if arg in ("4", "5", "6"):
            return int(arg)
        print(f"Invalid length argument '{arg}'. Supported lengths are 4, 5, or 6.")
        sys.exit(1)

    while True:
        try:
            choice = input("Select word length (4, 5, 6) [default: 5]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(0)

        if choice == "":
            return 5
        if choice in ("4", "5", "6"):
            return int(choice)
        print("Invalid choice. Please enter 4, 5, or 6.")


if __name__ == "__main__":
    length = select_word_length()
    WordleGame(length=length).run()
