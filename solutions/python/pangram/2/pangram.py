abc = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(sentence):
    norm_sentence = sentence.lower()
    letter_count = 0
    
    for letter in abc:
        if norm_sentence.count(letter) > 0:
            letter_count += 1

    return letter_count >= 26
