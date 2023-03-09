def main():
    encryption = input()
    decryption(encryption)

def decryption(encryption_str):
    print("hello, {}!".format(encryption_str))

if __name__ == '__main__':
    main()