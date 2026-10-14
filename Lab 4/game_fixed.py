import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    SUPPORTED_LENGTHS = (4, 5, 6)
    MAX_GUESSES = 6

    def __init__(self, length=5, target=None):
        if length not in self.SUPPORTED_LENGTHS:
            raise ValueError(
                f"Invalid word length: {length}. Supported lengths are {self.SUPPORTED_LENGTHS}."
            )
        self.length = length

        available_words = [w for w in WORDS if len(w) == self.length]
        if not available_words:
            raise ValueError(f"No words available for length {self.length}.")

        if target is not None:
            target = target.strip().lower()
            if len(target) != self.length or not target.isalpha():
                raise ValueError(
                    f"Target '{target}' must be an alphabetic word of length {self.length}."
                )
            self.target = target
        else:
            self.target = random.choice(available_words)

        self.history = []  # List of tuples: (guess, feedback)

    def display_history(self):
        """Displays readable history after each accepted guess."""
        print(f"\n--- Guess History ({len(self.history)}/{self.MAX_GUESSES}) ---")
        for i, (g, fb) in enumerate(self.history, 1):
            print(f"  {i}. {g.upper()} -> {' '.join(fb)}")
        print("-" * 38)

    def display_summary(self, outcome: str):
        """Displays a clean final session summary."""
        print("\n" + "=" * 42)
        print("            SESSION SUMMARY")
        print("=" * 42)
        print(f"Status:         {outcome}")
        print(f"Secret Word:    {self.target.upper()}")
        print(f"Length Mode:    {self.length} letters")
        print(f"Guesses Used:   {len(self.history)} / {self.MAX_GUESSES}")
        if self.history:
            print("\nGuesses Made:")
            for i, (g, fb) in enumerate(self.history, 1):
                print(f"  [{i}] {g.upper()} : {' '.join(fb)}")
        else:
            print("\nNo accepted guesses were recorded.")
        print("=" * 42 + "\n")

    def run(self):
        print(f"Wordle — {self.length} letters, {self.MAX_GUESSES} guesses.")
        print("Type 'q' at any prompt to quit the game.\n")

        while len(self.history) < self.MAX_GUESSES:
            turn_number = len(self.history) + 1
            try:
                guess = input(f"Guess {turn_number}/{self.MAX_GUESSES} > ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nSession interrupted.")
                self.display_summary("Interrupted")
                return

            if guess == "q":
                print("Quitting game.")
                self.display_summary("Quit by player")
                return

            # Validation: invalid guesses do NOT consume a turn or duplicate history
            if len(guess) != self.length or not guess.isalpha():
                print(
                    f"Invalid guess! Please enter a {self.length}-letter alphabetic word."
                )
                print(
                    f"(Invalid guesses do not consume a turn. Remaining: {self.MAX_GUESSES - len(self.history)})\n"
                )
                continue

            # Valid guess evaluation
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(f"Feedback: {' '.join(feedback)}")
            self.display_history()

            if guess == self.target:
                print(f"Solved! You won in {len(self.history)}/{self.MAX_GUESSES} guess(es)!")
                self.display_summary(f"WIN (Solved in {len(self.history)}/{self.MAX_GUESSES} guesses)")
                return

        # Exhausted all guesses
        print(f"\nGame over! You ran out of guesses.")
        print(f"The word was: {self.target.upper()}")
        self.display_summary("LOSS (Max guesses reached)")
