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
    if isinstance(num, str):            # if the input was given as a string, get rid of the leading 0s
        num = int(num.lstrip("0"))      #   otherwise the following bin() function doesn't like it
    
    _pure_bin: str = bin(num)[2:]       # convert the inputted number into b2,
                                        #   then get rid of the 0b from the start of the resulting string
    _b64_6bit_bin: list[str] = [
        f"0b{                           # iterate through the binary string in groups of 6 (log_2(64))
            _pure_bin[i:i+6]            #   then create a new binary digit out of all of them
        }"                              #   by prepending '0b' to every new digit
        for i in range(0, len(_pure_bin), 6)
    ]
    return "".join(
        map(lambda x:
            _encode_char_b64(
                int(x, base=2)          # convert the newly-created bin digits back to integers
            ),                          #   then use the lookup table to find their respective b64 chars
            _b64_6bit_bin)
    )
