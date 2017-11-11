#!/usr/bin/env python
import sys
word_dict = {}
for line in sys.stdin:
    word = line.split(",")[0]
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
for key, value in word_dict.items():
	sys.stdout.write(("{0},{1}\n".format(key, value)))
