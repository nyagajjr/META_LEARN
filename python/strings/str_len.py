def word_count(sentence):
    # Function to check the number of words. Returns the word count in string.
    print(len(sentence))
    words = sentence.split()
    print(words)
    return len(words)

print(word_count('hello you'))

# Function to check the first character using the string index. Returns the first character in string.
def first_char(sentence): 
    first = sentence[0]
    return first

print(first_char('Statement'))

# Function to check the last character using the string index. Returns the last character in string.
def last_char(sentence):
    last = sentence[-1]
    return last
print(last_char('Hohenzollerdamm'))