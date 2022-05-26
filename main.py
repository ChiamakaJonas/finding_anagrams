# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



# def find_anagram(word, anagram):
    # [assignment] Add your code here

def find_anagram(word1, word2):



    word1 = input("first word:")
    word2 = input("second word:")

    #check if length are the same
    if(len(word1) == len(word2)):

        #sort the words
        sorted(word1) == sorted(word2)  

    if(sorted(word1) == sorted(word2)):
        print("true")
    else:
        print("false")

find_anagram("research", "searcher")

