"""
Word Occurrences
Estimate: 15 minutes
Actual (functioning):  18  minutes 27 seconds
Actual (Refactored): 20 minutes
"""


words = input("Text: ").strip().split()
unique_word_set = sorted(set(words))

words_to_occurences = {}
for unique_word in unique_word_set:
    words_to_occurences[unique_word] = len([word for word in words if word == unique_word])

max_word_length = max(len(word) for word in unique_word_set)
print(words_to_occurences)
for word, occurence in words_to_occurences.items():
    print(f"{word:{max_word_length}} : {occurence}")