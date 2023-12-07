# PR18_2.py

# Программа разработана Кошелевым Максимом 29 ноября 2023.

'''
Описание программы:
Программа просит пользователя ввести текст и выводит текст без гласных и без согласных букв.
'''

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)

def remove_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return ''.join(char for char in text if char not in consonants)

def main():
    continue_input = "да"

    while continue_input.lower() == "да":
        user_text = input("Введите текст: ")

        text_without_vowels = remove_vowels(user_text)
        text_without_consonants = remove_consonants(user_text)

        print(f"Текст без гласных букв: {text_without_vowels}")
        print(f"Текст без согласных букв: {text_without_consonants}")

        continue_input = input("Продолжить? (да/нет): ")

if __name__ == "__main__":
    main()
