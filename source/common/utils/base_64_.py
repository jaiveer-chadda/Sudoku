B64_LOOKUP_TABLE: tuple[str, ...] = (
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  # 10
    
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',  # 20
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',  # 30
    'u', 'v', 'w', 'x', 'y', 'z',
                                  'A', 'B', 'C', 'D',  # 40
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',  # 50
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',  # 60
    'Y', 'Z',
              '_', '-'                                 # +4 = 64 chars
)


def _encode_char_b64(char: int) -> str:
    return B64_LOOKUP_TABLE[char]


def encode_b64(num: str | int) -> str:
    if isinstance(num, str):
        num = int(num.lstrip("0"))
    
    _pure_bin: str = bin(num)[2:]
    _b64_chars: list[str] = [f"0b{_pure_bin[i:i+6]}" for i in range(0, len(_pure_bin), 6)]
    return "".join(map(lambda x: _encode_char_b64(int(x, base=2)), _b64_chars))
