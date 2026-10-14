def evaluate(target: str, guess: str) -> list:
    """
    Evaluates a guess against a target word using standard Wordle scoring rules.

    Rules:
    - Target and guess must be of equal length.
    - Exact matches ('green') are resolved first.
    - Each occurrence of a letter in the target can satisfy at most one occurrence in the guess.
    - Remaining occurrences of letters in guess that appear in target are marked 'yellow'.
    - All other letters are marked 'gray'.
    """
    target = target.lower()
    guess = guess.lower()

    if len(target) != len(guess):
        raise ValueError("Target and guess must have the same length.")

    n = len(target)
    result = ["gray"] * n

    # Step 1: Resolve exact matches ('green') and count remaining target letters
    target_counts = {}
    for i in range(n):
        if guess[i] == target[i]:
            result[i] = "green"
        else:
            ch = target[i]
            target_counts[ch] = target_counts.get(ch, 0) + 1

    # Step 2: Resolve partial matches ('yellow') against remaining target counts
    for i in range(n):
        if result[i] != "green":
            ch = guess[i]
            if target_counts.get(ch, 0) > 0:
                result[i] = "yellow"
                target_counts[ch] -= 1

    return result
