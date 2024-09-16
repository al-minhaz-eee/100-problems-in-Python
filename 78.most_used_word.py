from collections import Counter
import re

def process_lyrics(lyrics):
    lyrics = lyrics.lower()
    lyrics = re.sub(r'[^a-z\s]', '', lyrics)
    words = lyrics.split()
    return words
def find_most_frequent_word(lyrics):
    words = process_lyrics(lyrics)
    word_counts = Counter(words)
    most_common_word, count= word_counts.most_common(1)[0]
    return most_common_word, count

lyrics = lyrics = """
Chumma chumma de de chumma
Chumma chumma de de chumma
Chumma chumma de de chumma
Chumma chumma chumma chumma
Tor chumma lage sona sona
Chumma chumma chumma chumma
Tui amar jaan er jana
"""
disired_word, count = find_most_frequent_word(lyrics)
print(f"The most frequent word is '{disired_word}' which appears {count} times.")