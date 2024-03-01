# from PIL import Image
# import os

# # Obtenez le chemin absolu du répertoire du script
# script_directory = os.path.dirname(os.path.abspath(__file__))

# # Construisez le chemin absolu vers l'image
# image_path = os.path.join(script_directory, "images", "image.png")

# # Fonction pour chiffrer/déchiffrer avec l'algorithme de Vigenère
# def vigenere(text, key, decrypt=False):
#     result = ""
#     key_length = len(key)
#     for i in range(len(text)):
#         char = text[i]
#         if char.isalpha():
#             key_char = key[i % key_length]
#             key_shift = ord(key_char.lower()) - ord("a")
#             if char.isupper():
#                 result += chr((ord(char) - key_shift - 65) % 26 + 65) if decrypt else chr((ord(char) + key_shift - 65) % 26 + 65)
#             elif char.islower():
#                 result += chr((ord(char) - key_shift - 97) % 26 + 97) if decrypt else chr((ord(char) + key_shift - 97) % 26 + 97)
#         else:
#             result += char
#     return result

# # Fonction pour cacher un message dans une image
# def hide_message_in_image(message, image_path, password):
#     crypted_message = vigenere(message, password)
#     image = Image.open(image_path)

#     # Convertir le message crypté en binaire
#     binary_message = "".join(format(ord(char), "08b") for char in crypted_message)

#     # Cacher le message dans les pixels de l'image
#     pixel_index = 0
#     for i in range(image.width):
#         for j in range(image.height):
#             pixel = list(image.getpixel((i, j)))
#             for k in range(3):  # R, G, B
#                 if pixel_index < len(binary_message):
#                     pixel[k] = pixel[k] & ~1 | int(binary_message[pixel_index])
#                     pixel_index += 1
#             image.putpixel((i, j), tuple(pixel))

#     # Sauvegarder l'image modifiée
#     output_path = os.path.join(script_directory, "hidden_image.png")
#     image.save(output_path)
#     print(f"Message caché avec succès dans l'image : {output_path}")

# # Fonction pour extraire un message d'une image
# def extract_message_from_image(image_path, password):
#     image = Image.open(image_path)
#     binary_message = ""

#     for i in range(image.width):
#         for j in range(image.height):
#             pixel = image.getpixel((i, j))
#             for value in pixel[:3]:  # R, G, B
#                 binary_message += str(value & 1)

#     # Convertir le message binaire en texte
#     binary_chunks = [
#         binary_message[i : i + 8] for i in range(0, len(binary_message), 8)
#     ]
#     extracted_message = "".join([chr(int(chunk, 2)) for chunk in binary_chunks])

#     # Déchiffrer le message extrait
#     decrypted_message = vigenere(extracted_message, password, decrypt=True)
#     return decrypted_message

# if __name__ == "__main__":
#     message_to_hide = "Ceci est un message secret"
#     password = "password"

#     # Cacher le message dans l'image
#     hide_message_in_image(message_to_hide, image_path, password)

#     # Extraire le message de l'image
#     extracted_message = extract_message_from_image(
#         os.path.join(script_directory, "hidden_image.png"), password
#     )
#     print(f"Message extrait : {extracted_message}")

from PIL import Image

def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - 65
            encrypted_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def hide_text_in_image(image_path, text):
    image = Image.open(image_path)
    width, height = image.size
    pixel_index = 0

    for char in text:
        if pixel_index < width * height:
            pixel_value = ord(char)
            image.putpixel((pixel_index % width, pixel_index // width), pixel_value)
            pixel_index += 1

    image.save("hidden_image.png")
    print("Image with hidden text saved as 'hidden_image.png'.")

def main():
    message = "Hello, this is a secret message!"
    key = "KEY"

    encrypted_message = encrypt_vigenere(message, key)
    print("Encrypted Message:", encrypted_message)

    image_path = "C:/Users/layed/Desktop/Stéganographie/steganosaure/hidden_image.png"
    hide_text_in_image(image_path, encrypted_message)

if __name__ == "__main__":
    main()
