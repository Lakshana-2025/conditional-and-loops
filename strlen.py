sentence =input("Enter a sentence:")
words=sentence.split()
for word in words:
    if len(word)>5:
        print(word)
