"""
Word Occurrences
Estimate: 15 minutes
Actual (functioning):  18  minutes 27 seconds
"""


s = input("Text: ").strip().split()

unique_word_set = sorted(set(s))
d = {}


for i in unique_word_set:
    d[i] = len([word for word in s if word == i])

max_word_length = max(len(word) for word in unique_word_set)
print(d)
for word, occurence in d.items():
    print(f"{word:{max_word_length}}: {occurence}")