import re
from sys import stdout


class Reprinter:
    def __init__(self) -> None:
        self.text: str = ''
    
    @staticmethod
    def move_up(lines: int) -> None:
        for _ in range(lines):
            stdout.write("\x1b[A")
    
    def reprint(self, text: str) -> None:
        # Clear previous text by overwriting non-spaces with spaces
        self.move_up(self.text.count("\n"))
        stdout.write(re.sub(r"\S", " ", self.text))
        
        # Print new text
        lines = min(self.text.count("\n"), text.count("\n"))
        self.move_up(lines)
        stdout.write(text)
        self.text = text


def main() -> None:
    reprinter: Reprinter = Reprinter()
    
    reprinter.reprint("Foobar\nBazbar")
    reprinter.reprint("Foo\nbar")


if __name__ == "__main__":
    main()
