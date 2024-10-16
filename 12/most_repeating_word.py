from collections import Counter

WORDS = ['this', 'is', 'an',
         'elementary', 'test', 'example']

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(words: str) -> str:
    """
    For each word, find the letter that appears the most times.
    Find the word whose most-repeated letter appears more than any other.
    """
    return max(words, key=most_repeating_letter_count)

print(most_repeating_word(WORDS))
    

