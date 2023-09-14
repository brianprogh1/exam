import sys
import string
import os.path

fname = input("Enter the filename: ")
# Sample file text.txt also provided

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")
filecontents = ""

for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            filecontents = filecontents + ch
        else:
            filecontents = filecontents + ' '

wordFreq = {}
wordList = filecontents.split()

# Calculate word Frequency
for word in wordList:
    if word not in wordFreq.keys():
        wordFreq[word] = 1
    else:
        wordFreq[word] += 1

# Sort Dictionary based on values in descending order
sortedWordFreq = sorted(wordFreq.items(), key=lambda x: x[1], reverse=True)

# Display 10 most frequently appearing words with their count
print("\n===================================================")
print("10 most frequently appearing words with their count")
print("===================================================")
for i in range(10):
    print(sortedWordFreq[i][0], "occurs", sortedWordFreq[i][1], "times")
