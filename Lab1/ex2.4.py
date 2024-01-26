import re
import time

def count_vowels(text):
    words = re.findall(r'\b\w+\b', text) # Used AI for this
    total_vowels = 0
    total_words = 0

    for word in words:
        vowels = sum(1 for letter in word if letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y'])
        total_vowels += vowels
        total_words += 1

    average_vowels = total_vowels / total_words if total_words > 0 else 0
    return average_vowels

with open('pg2701.txt', 'r') as file:
    text = file.read()

# Find the start of Chapter 1
start = text.find('CHAPTER 1')

# If Chapter 1 is found, start reading from there
if start != -1:
    text = text[start:]

start_time = time.time()
average_vowels = count_vowels(text)
end_time = time.time()

print(f"Average number of vowels per word: {average_vowels}")
print(f"Time taken: {end_time - start_time}")