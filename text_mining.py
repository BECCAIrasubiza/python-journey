import string

try:
    with open("article.txt", "r", encoding="utf-8") as file:
        article = file.read().lower()

    with open("stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = {line.strip().lower() for line in file if line.strip()}

    # Replace punctuation with spaces so "data,analysis" does not become one word.
    cleaned_characters = []
    for character in article:
        if character in string.punctuation:
            cleaned_characters.append(" ")
        else:
            cleaned_characters.append(character)

    words = "".join(cleaned_characters).split()
    counts = {}
    for word in words:
        if word not in stopwords:
            counts[word] = counts.get(word, 0) + 1

    top_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:10]

    with open("top_words.txt", "w", encoding="utf-8") as report:
        report.write("TOP WORDS (excluding stopwords)\n")
        for word, count in top_words:
            report.write(f"{word}: {count}\n")

    # Append means the log grows by one line every time this script runs.
    with open("run_log.txt", "a", encoding="utf-8") as log:
        log.write(f"article.txt | words processed: {len(words)}\n")

    print(f"Processed {len(words)} words.")
    print("Top words saved to top_words.txt; run recorded in run_log.txt.")

except FileNotFoundError as error:
    print(f"Missing file: {error.filename}. Make sure article.txt and stopwords.txt exist.")
