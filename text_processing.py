import string

# common words to ignore
STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "a", "for", "with",
    "we", "are", "be", "on", "that", "this", "as", "an"
}

def process_text(text):

    text = text.lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    words = text.split()

    # remove stopwords
    filtered_words = [word for word in words if word not in STOPWORDS]

    return filtered_words