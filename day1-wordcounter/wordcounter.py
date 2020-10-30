from collections import defaultdict
import argparse, sys

def count_words(fileobject):
    words_count = {}
    for word in fileobject.read().split():
        if len(word)<3:
            continue
        if word not in words_count:
            words_count[word] = 0
        words_count[word] += 1
    return words_count



if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument(
        "path",
        help="The path to read the file")
    args = p.parse_args()
    if args.path is None:
        sys.exit(1)
    
    try:
        f = open(args.path, encoding="utf-8")
    except IOError:
        print("file cant be opened")
        exit(1)

    words = count_words(f)
    f.close()
    for word in sorted(words, key=words.get, reverse=True)[:10]:
        print (f"word: '{word}' occurrence: {words[word]}")
