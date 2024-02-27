import os
from collections import Counter
import re

def analyze_texts_in_directory(directory_path, top_n=10):
    all_text = ""
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                all_text += file.read().lower() + " "
    words = re.findall(r'\w+', all_text)
    total_words = len(words)
    unique_words = len(set(words))
    most_common_words = Counter(words).most_common(top_n)
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "top_words": most_common_words
    }