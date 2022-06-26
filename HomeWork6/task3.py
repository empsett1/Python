alphabet_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13_encoding(text: str) -> str:
    return cesar_encoding(text, 13)


def rot13_decoding(text: str) -> str:
    return cesar_encoding(text, -13)


def cesar_encoding(text: str, key: int) -> str:
    result = ''

    for ch in text.upper():
        if ch in alphabet_eng:
            result += alphabet_eng[(alphabet_eng.find(ch) + key) % len(alphabet_eng)]
        else:
            result += ch

    return result


print(cesar_encoding('In the room there is a king, a priest and a rich man, among them a mercenary, who will survive?..', 13))

print(rot13_encoding('In the room there is a king, a priest and a rich man, among them a mercenary, who will survive?..'))

print(rot13_decoding(rot13_encoding('In the room there is a king, a priest and a rich man, among them a mercenary, who will survive?..')))