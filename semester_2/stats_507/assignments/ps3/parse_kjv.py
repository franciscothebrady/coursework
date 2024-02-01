import re
import string
from collections import defaultdict

filename = 'kjv.txt'
with open(filename, 'r') as file:
    lines = file.readlines()

# Create a list of unique books for indexing 
unique_books = []
for line in lines:
    if line.startswith("##"):  # this is a book title
        book_name = line[2:].strip()
        if book_name not in unique_books:
            unique_books.append(book_name)

# Initialize the nested dictionary
bible = { book_index: {} for book_index in range(len(unique_books)) }

# Go through each line of the file
for line in lines:
    line = line.strip()  # remove leading/trailing whitespaces
    if not line: continue  # skip empty lines

    if line.startswith("##"):  # this is a book title
        current_book = unique_books.index(line[2:].strip())

    elif line.startswith("["):  # this is a chapter:verse and text
        parts = line.split("\t")
        chapter_verse, current_text = parts[0][1:-1], parts[1] if len(parts) > 1 else ""
        chapter, verse = map(int, chapter_verse.split(":"))
        chapter -= 1
        verse -= 1

        # populate the nested dictionary
        if chapter not in bible[current_book]:
            bible[current_book][chapter] = {}

        bible[current_book][chapter][verse] = current_text.strip()

bible[0][0][0]  # 'In the beginning God created the heaven and the earth.'
bible[42][2][15]  