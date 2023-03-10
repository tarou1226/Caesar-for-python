def main():
    encryption = "F^jQbolol"
    decryption = decrypt(encryption)
    encryption = encrypt(decryption)
    print("".join(decryption))
    print("".join(encryption))

def encrypt(plain_text: str) -> list:
    # print("hello, {}!".format(plain_text))
    encryption = list()
    for character in plain_text:
        encryption.append(chr(ord(character) - 3))
    return encryption

def decrypt(encryption_str: str) -> list:
    # print("hello, {}!".format(encryption_str))
    decryption = list()
    for character in encryption_str:
        decryption.append(chr(ord(character) + 3))
    return decryption

if __name__ == '__main__':
    main()