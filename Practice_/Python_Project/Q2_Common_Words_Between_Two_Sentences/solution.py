import re
from collections import Counter

# Data Available in this DataFrame:
df = data.copy()

def clean_and_split(sentence):
    # Remove punctuation, keep case as-is
    sentence = re.sub(r"[.,!?]", "", sentence)
    return sentence.split()

def find_common_words(row):
    s1 = clean_and_split(row['sentence_1'])
    s2 = clean_and_split(row['sentence_2'])

    common_words = set(s1) & set(s2)
    counts = Counter(s2)

    # Build dictionary only for common words
    result = {word: counts[word] for word in sorted(common_words)}
    return result

# Apply row-wise
df['output'] = df.apply(find_common_words, axis=1)

# Return the DataFrame
df
