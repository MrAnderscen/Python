text = input("Введите текст: ")
words = text.split() 
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
most_freq_word = max(freq, key=freq.get)
longest_word = max(words, key=len)

print("Наиболее часто встречающееся слово:", most_freq_word)
print("Самое длинное слово:", longest_word)