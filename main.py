import re
from collections import Counter

# Common words that should not be treated as keywords
STOP_WORDS = {
    "the", "is", "a", "an", "and", "or", "of", "to", "in",
    "on", "for", "with", "this", "that", "are", "was", "were",
    "as", "at", "by", "it", "from", "be", "has", "have", "had",
    "he", "she", "they", "we", "you", "i", "his", "her",
    "their", "which", "who", "will", "can", "about", "into",
    "than", "also", "very", "its", "but", "not", "using",
    "used", "use", "more", "such", "these", "those"
}


def extract_keywords(text, number_of_keywords=10):

    # Convert text to lowercase
    text = text.lower()

    # Extract words
    words = re.findall(r'\b[a-zA-Z]+\b', text)

    # Remove stop words and very short words
    useful_words = [
        word for word in words
        if word not in STOP_WORDS and len(word) > 2
    ]

    # Count word frequency
    word_frequency = Counter(useful_words)

    # Get most common keywords
    keywords = word_frequency.most_common(number_of_keywords)

    return keywords


# --------------------------------
# MAIN PROGRAM
# --------------------------------

print("=" * 50)
print("             KEYWORD EXTRACTOR")
print("=" * 50)

print("\nEnter a paragraph.")
print("The program will find the most important words.\n")

text = input("Enter text: ")

if not text.strip():

    print("\nError: Please enter some text.")

else:

    keywords = extract_keywords(text, 10)

    print("\n" + "=" * 50)
    print("             EXTRACTED KEYWORDS")
    print("=" * 50)

    if keywords:

        for number, (word, frequency) in enumerate(keywords, 1):

            print(
                f"{number}. {word} "
                f"(frequency: {frequency})"
            )

    else:

        print("No keywords found.")

    print("=" * 50)