# — External Imports —————————————————————————————————————————————————————————————————————————
from hashlib import md5
# ————————————————————————————————————————————————————————————————————————————————————————————


def hash_to_8_chars(int_to_hash: int) -> str:
    byte_string = str(int_to_hash).encode()
    return md5(byte_string).hexdigest()[:8]


# ————————————————————————————————————————————————————————————————————————————————————————————
def main() -> None:
    print(hash_to_8_chars(12345678901234567890))


if __name__ == '__main__':
    main()
