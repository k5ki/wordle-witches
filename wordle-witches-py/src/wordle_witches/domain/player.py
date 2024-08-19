class Guess:
    def __init__(self, witch_id: int, hint: list[str]):
        self.witch_id = witch_id
        self.hint = hint


class Player:
    def __init__(self, id: str, guesses: list[Guess]):
        self.id = id
        self.guesses = guesses

    def challenge_count(self) -> int:
        return len(self.guesses)
