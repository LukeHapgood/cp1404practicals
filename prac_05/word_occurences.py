
input_text = input("Text: ")
words = input_text.split()
word_count = {}
longest_word = 0

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        if len(word) > longest_word:
            longest_word = len(word)


for word, count in sorted(word_count.items()):
    print("{:<{}} : {}".format(word, longest_word, count))
