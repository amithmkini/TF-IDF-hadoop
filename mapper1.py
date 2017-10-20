import os, sys
os.chdir(r"/mnt/g/DCS/shakespeare_txt/")
stop_words = ["I", "a", "about", "an", "are", "as", "at", "be", "by", "com", "de", "en", "for", "from", "how",
             "in", "is", "it", "la", "of", "on", "or", "that", "the", "this", "to", "was", "what", "when", "where",
             "who", "will", "with", "and", "the", "www"]
for items in os.listdir():
    if items != 'intermediate.txt':
        with open(items, "r") as doc:
            for line in doc:
                line = line.replace("*", "")
                line = line.replace(".", "")
                line = line.replace("?", "")
                line = line.replace("'", "")
                line = line.replace(",", "")
                line = line.replace(":", "")
                line = line.replace(";", "")
                line = line.replace("(", "")
                line = line.replace("&", "")
                line = line.replace(")", "")
                line = line.replace("]", "")
                line = line.replace("[", "")
                line = line.replace("\t", " ")
                line = line.replace("-", " ")
                word_list = (str(line).strip().split(" "))
                for word in word_list:
                    word = word.strip().lower()
                    if word and word not in word_list:
                        sys.stdout.write(("{0}@{1},{2}\n".format(word, items, 1)))
