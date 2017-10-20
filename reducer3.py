import sys
import math
dict_word = {}
D = 12
for line in sys.stdin:
    word = line.strip().split(",")[0]
    if word in dict_word:
        dict_word[word] += 1
    else:
        dict_word[word] = 1

    word = line.strip().split(",")[0]
    document = line.strip().split(",")[1].split("=")[0]
    freq = line.strip().split("=")[1]
    d = dict_word[word]
    tf = math.log(D/d)
    tfidf = tf*float(freq)
    sys.stdout.write("{0}@{1},{2},{3},{4}\n".format(word, document, tf, freq, tfidf))