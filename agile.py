#!/usr/bin/env python
# -*- coding: utf-8 -*-
content = 'The_Agile_process.csv'
#blog = open(content,'r')
#blog.readlines()

#Deal with whitespace with ''.strip().
#See that we need all the words that begin with s.
#But that's ambiguous because what about words that begin with s but start the sentence.. like 'String Filter Increment'.
#So we use ''.strip().lower() and see what that spits out.

with open(content) as o:
    blog_line = ' '.join([line.rstrip("\n").lower() for line in o])

#time to add every single word, white-space separated into each of its own place in a list, called 'all-words'.
all_words = list(blog_line.split(' '))
#this is very messy, need to add some correcting touches. First remove all empty containers.
all_words_clean = [all_words[i] for i in range(0,len(all_words)) if all_words[i] != '']

#So we've removed all empty array elements, all 21 of them. Lets see if wordcounter concurrs. Lets see we have 1054 words in total.
#Word counters give 1058. Weird.
#Both my program and online wordcounters are treating contractions like if it were a single word. Also they both treat buy-in like if it were a single word.
#However, with words such as 'UX-brining' the word counter treats that as two separate words..(they really are)
#whereas my program took that part to be a single word, replacing the spacing with its unicode equilavent being \u200a.

#find all elements with the '\u200a' code in it and
#for each one add it to a unicode array.
#for this array we are going to take each element and split it into two parts then
#we simply append them into our main big array.

unicode_array = [all_words_clean[i] for i in range(0,len(all_words_clean)) if all_words_clean[i].find("\u200a") != -1]
#split the unicode_array by the \u200a string.
list_1 = unicode_array[0].split("\u200a")
list_2 = unicode_array[1].split("\u200a")

#just removes the elements with the unicode part.
for i in range(0,len(all_words_clean) - 2):

    if all_words_clean[i].find("\u200a") != -1:
       all_words_clean.remove(all_words_clean[i])
#add the missed words to the end of the list.
all_words_clean.append(list_1[0])
all_words_clean.append(list_1[2])
all_words_clean.append(list_2[0])
all_words_clean.append(list_2[2])

#We have ended up with 1056 words. Still 2 short, so lets double check with the word-counter.
#The word counter counts the dash - in between hair spaces (that is the \u200a unicode equilv) as an additional word, thus overcounting by precicely two..
# and if the word counter says 1058, its really 1056 total number of words. Solved.

#print the words with the letter s now.
words_start_s = [all_words_clean[i] for i in range(0,len(all_words_clean)) if all_words_clean[i][0].find('s') != -1]
#its messy so we add some finishing touches
#Create a function that finds whether theres a character in the word.
#and if there is then we apply replace!

def fix(list):

    for i in range(0,len(list)):

        if list[i].find('(') != -1:
            list[i] = list[i].replace('(','')

        elif list[i].find(')') != -1:
            list[i] = list[i].replace(')','')

        elif list[i].find('.') !=-1:
            list[i] = list[i].replace('.','')

        elif list[i].find(';') !=-1:
            list[i] = list[i].replace(';','')

        elif list[i].find(',') !=-1:
            list[i] = list[i].replace(',','')

#call the function twice, one for the first non-alpha and two for the second non-alpha.
fix(words_start_s)
fix(words_start_s)

def print_results(word_s, tot_words):

    total_s = len(word_s) + 1 #len() starts counting from zero.
    total_all = len(tot_words) + 1
    percentage = (total_s / total_all)*100

    print("There are a total of: %r number of words that start with the letter s." % total_s)
    print("That corresponds to a percentage of: %r" % percentage)

    print("The words:\n")

    for i in range(0,len(word_s)):
# prints the words out line by line.
        print(word_s[i])



print_results(words_start_s,all_words_clean)
