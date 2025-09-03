import string

def is_pangram(sentence):
    norm_sentence = sentence.lower()
    return all(letter in norm_sentence for letter in string.ascii_lowercase)
