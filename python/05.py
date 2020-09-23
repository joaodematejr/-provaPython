letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def translate(phrase):
    new_phrase = []
    phrase_list = phrase.split(',')
    for letter in phrase_list:
        new_phrase.append(letters[int(letter)])
    return ''.join(new_phrase)


while True:
    phrase = input("Digite a mensagem codificada:\n")
    print(translate(phrase))
