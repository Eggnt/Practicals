"""
Word Occurrences
Estimate: 25 minutes
Actual:   19 minutes
"""

word_to_count = {}


def main():
    sentence = str(input("Text: "))
    for word in sentence.split(" "):
        word_to_count[word] = word_to_count.get(word, 0) + 1
        max_length = max(len(word) for word in list(word_to_count.keys()))
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{max_length}} : {count}")


main()
