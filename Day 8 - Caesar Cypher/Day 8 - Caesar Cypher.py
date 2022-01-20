alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encoder(text, shift):
    encodedText = ""
    shiftLimited = shift % 26

    for i in range(len(text)):
        if text[i] in alphabet:
            index = alphabet.index(text[i])

            encodedText += alphabet[index + shiftLimited]
        else:
            encodedText += text[i]

    print(f"Here's the encoded result: {encodedText}")


def decoder(text, shift):
    encodedText = ""
    shiftLimited = shift % 26

    for i in range(len(text)):
        if text[i] in alphabet:
            index = alphabet.index(text[i])

            encodedText += alphabet[index - shiftLimited]
        else:
            encodedText += text[i]

    print(f"Here's the decoded result: {encodedText}")


run = True
again = False

while run:
    if again == True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encoder(text, shift)
    elif direction == "decode":
        decoder(text, shift)

    repeat = input("Type 'yes' if you want to go again. otherwise type'no'.\n")

    if repeat == "yes":
        again = True
    elif repeat == "no":
        run = False
