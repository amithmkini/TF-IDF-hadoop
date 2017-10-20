import sys
for line in sys.stdin:
    word = line.strip().split("@")[0]
    document = line.strip().split("@")[1].split(",")[0]
    freq = line.strip().split(",")[1]
    sys.stdout.write("{0},{1}={2}\n".format(word, document, freq))