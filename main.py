import json
import random
import re


def load_phrases(file_paths):
    phrases = {}
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            phrases.update(json.load(file))
    return phrases


def get_random_phrase(phrases):
    return random.choice(list(phrases.keys()))


def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text).lower()


def main():
    # Load phrases from files
    file_paths = ['phrases(0-50).json']
    phrases = load_phrases(file_paths)

    correct_count = 0
    incorrect_count = 0

    while True:
        ukr_phrase = get_random_phrase(phrases)
        print(f'Translate the phrase: "{ukr_phrase}"')
        user_input = input('Your translation: ')
        cleaned_user_input = remove_punctuation(user_input)
        cleaned_correct_answer = remove_punctuation(phrases[ukr_phrase])

        if cleaned_user_input == cleaned_correct_answer:
            print('Correct!\n')
            correct_count += 1
        else:
            print(f'Incorrect. The correct translation is: "{phrases[ukr_phrase]}"\n')
            incorrect_count += 1

        print(f'ANSWERS: Correct: {correct_count}, Incorrect: {incorrect_count}')


if __name__ == "__main__":
    main()
