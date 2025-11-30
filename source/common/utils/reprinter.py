import re
import sys


class Reprinter:
    def __init__(self) -> None:
        self.text = ''
    
    @staticmethod
    def move_up(lines) -> None:
        for _ in range(lines):
            sys.stdout.write("\x1b[A")
    
    def reprint(self, text) -> None:
        # Clear previous text by overwriting non-spaces with spaces
        self.move_up(self.text.count("\n"))
        sys.stdout.write(re.sub(r"\S", " ", self.text))
        
        # Print new text
        lines = min(self.text.count("\n"), text.count("\n"))
        self.move_up(lines)
        sys.stdout.write(text)
        self.text = text


def main() -> None:
    reprinter = Reprinter()
    
    reprinter.reprint("Foobar\nBazbar")
    reprinter.reprint("Foo\nbar")


if __name__ == "__main__":
    main()
