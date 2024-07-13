"""
Time management:
    predict time: 20min
    Actual time: 35min

"""
word_to_count = {}
text = input("Enter: ")
words = text.split(" ")
words = sorted(words)
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_word_length = max([len(word) for word in words])
for word in word_to_count:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
