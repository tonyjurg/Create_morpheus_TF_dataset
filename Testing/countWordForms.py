from collections import Counter

def countLettersAfterNL(filePath):
    with open(filePath, "r", encoding="utf-8") as f:
        content = f.read()

    counter = Counter()
    idx = 0
    while idx < len(content):
        idx = content.find("<NL>", idx)
        if idx == -1:
            break
        after_nl_idx = idx + len("<NL>")
        if after_nl_idx < len(content):
            letter = content[after_nl_idx]
            if letter.strip():  # skip any whitespace
                counter[letter] += 1
        idx = after_nl_idx

    return counter

if __name__ == "__main__":
    inputFile = "gnt_morphology_results2.txt"  # input text file
    letterCounts = countLettersAfterNL(inputFile)

    print("\nFrequency of first letters after <NL>:\n")
    for letter, count in letterCounts.most_common():
        print(f"{letter}: {count}")