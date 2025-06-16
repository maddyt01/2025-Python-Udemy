# Project 3 from Nick Walter's "Python for Programmers Course" on udemy
# Word Counter
import os
import string

def get_count(wcpair):
    return wcpair[1]

def word_counter(filename):
    #open/read the file and split on whitespace
    with open(filename, "r") as f:
        read_file = f.read()
    
    word_list = read_file.split()
    
    #dictionary for storing words / counts
    word_counts = {}

    for word in word_list:
        word = word.strip(string.punctuation).lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    word_count_list = list(word_counts.items())
    word_count_list.sort(key=get_count, reverse = True)

    base, ext = os.path.splitext(filename)
    output_filename = base + "-count" + ext

    with open(output_filename, "w") as file:
        total_words = sum(word_counts.values())
        unique_words = len(word_counts)

        #write info about words overall to file
        file.write(f"Total words: {total_words}\n")
        file.write(f"Unique words: {unique_words}\n")

        #line by line write all words / counts to file 
        for w, c in word_count_list:
            file.write(f"{w} : {c}\n")
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 word_counter.py filename.txt")
    else:
        word_counter(sys.argv[1])