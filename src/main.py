import re
import os
from collections import Counter

# File paths
input_file = os.path.join("Data", "reddit_text_sample.txt")
output_folder = os.path.join("output")

word_output = os.path.join(output_folder, "wordcount.txt")
bigram_output = os.path.join(output_folder, "bigramcount.txt")

# Create output folder
os.makedirs(output_folder, exist_ok=True)

print(f"Word output: {word_output}")
print(f"Bigram output: {bigram_output}")

# Stopwords
stopwords = {
    "the", "a", "an", "and", "of", "to", "in", "is", "it", "that", "i", "you",
    "he", "she", "they", "we", "was", "were", "be", "been", "for", "on", "with",
    "as", "at", "by", "from", "or", "but", "not", "this", "my", "your", "our",
    "their", "me", "him", "her", "them", "are", "am", "will", "would", "can",
    "could", "should", "has", "have", "had"
}

# Extract clean words
def extract_words(line):
    words = re.findall(r"[a-zA-Z']+", str(line).lower())
    return [word for word in words if word not in stopwords and len(word) > 2]

# Create bigrams
def make_bigrams(words):
    return [' '.join(words[i:i+2]) for i in range(len(words)-1)]

# Read text
with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Process words
all_words = []
all_bigrams = []

for line in lines:
    words = extract_words(line)
    all_words.extend(words)
    all_bigrams.extend(make_bigrams(words))

# Count words
word_counts = Counter(all_words)
filtered_words = {word: count for word, count in word_counts.items() if count >= 5}

# Count bigrams
bigram_counts = Counter(all_bigrams)
filtered_bigrams = {bigram: count for bigram, count in bigram_counts.items() if count >= 5}

# Write word count in professor format
with open(word_output, 'w', encoding='utf-8') as f:
    for word, count in sorted(filtered_words.items(), key=lambda x: -x[1]):
        f.write(f"('{word}', {count})\n")

# Write bigram count in same format
with open(bigram_output, 'w', encoding='utf-8') as f:
    for bigram, count in sorted(filtered_bigrams.items(), key=lambda x: -x[1]):
        f.write(f"('{bigram}', {count})\n")

print("Word count and bigram count completed successfully.")