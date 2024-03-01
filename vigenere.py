import string

string.printable = string.printable.replace("\r", "à")

import string


def cesar_ciffer(message, key):
    if type(key) != int:
        print("La clé doit être un entier.")
        return None

    message = str(message)
    list_of_crypted_caracs = []

    for carac in message:
        if carac in string.printable:
            crypted_index = (string.printable.index(carac) + key) % len(
                string.printable
            )
            crypted_carac = string.printable[crypted_index]
            list_of_crypted_caracs.append(crypted_carac)
        else:
            # Si le caractère n'est pas imprimable, ajoutez-le tel quel sans le chiffrer
            list_of_crypted_caracs.append(carac)

    crypted_message = "".join(list_of_crypted_caracs)
    return crypted_message


def cesar_decrypt(crypted_message, key):
    return cesar_ciffer(crypted_message, -key)


def vigenere(message, password, ciffer):
    if ciffer:
        list_of_keys = [
            string.printable.index(password_carac) for password_carac in password
        ]
    else:
        list_of_keys = [
            -string.printable.index(password_carac) for password_carac in password
        ]

    list_of_crypted_caracs = []

    for index_carac, carac in enumerate(message):
        current_key = list_of_keys[index_carac % len(list_of_keys)]
        list_of_crypted_caracs.append(cesar_ciffer(carac, current_key))

    crypted_message = "".join(list_of_crypted_caracs)

    return crypted_message


if __name__ == "__main__":
    print("j'ai envie de manger gratin de pates avec des lardons")
    crypted_message = cesar_ciffer(
        "j'ai envie de manger gratin de pates avec des lardons", 3
    )
    print(crypted_message)
    print(cesar_decrypt("m*dlàhqylhàghàpdqjhuàjudwlqàghàsdwhvàdyhfàghvàodugrqv", 3))
