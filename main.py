def encrypt(text, amount):
    encrypted_text = ""
    for character in text:
        if character.isalpha():  # Only shift alphabetic characters
            base = ord('A') if character.isupper() else ord('a')
            shifted = (ord(character) - base + amount) % 26 + base
            encrypted_text += chr(shifted)
        else:
            encrypted_text += character  # Non-alphabetic characters remain unchanged
    return encrypted_text


def decrypt(text, amount):
    decrypted_text = ""
    for character in text:
        if character.isalpha():
            base = ord('A') if character.isupper() else ord('a')
            shifted = (ord(character) - base - amount) % 26 + base
            decrypted_text += chr(shifted)
        else:
            decrypted_text += character  # Non-alphabetic characters remain unchanged
    return decrypted_text


print(encrypt("This is an example text that should be printed as a text shifted by 2", 2))
print(decrypt("Vjku ku cp gzcorng vgzv vjcv ujqwnf dg rtkpvgf cu c vgzv ujkhvgf da 2", 2))
