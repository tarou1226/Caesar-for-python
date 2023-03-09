def main():
    encryption = "F^jQbolol"
    decryption = decrypt(encryption)
    print("".join(decryption))

def decrypt(encryption_str: str) -> list:
    # print("hello, {}!".format(encryption_str))
    decryption = list()
    for character in encryption_str:
        decryption.append(chr(ord(character) + 3))
    return decryption

if __name__ == '__main__':
    main()