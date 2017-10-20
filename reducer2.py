import sys
word_dict = {}
for line in sys.stdin:
    document = line.strip().split(",")[0]
    num = line.split("=")[1]
    if document not in word_dict:
        word_dict[document] = int(num)
    else:
        word_dict[document] += int(num)

    document = line.strip().split(",")[0]
    num = line.strip().split("=")[1]
    word = line.strip().split(",")[1].split("=")[0]
    total_word = word_dict[document]
    frequency = int(num)/total_word
    sys.stdout.write("{0}@{1},{2}\n".format(word, document, frequency))