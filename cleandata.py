import nltk
from nltk.corpus import stopwords
from retrievecomments import RetrieveComments

def cleanData(comments: list):
    filteredWords = []
    splitWords = []

    #remove all non alphabetical characters 
    for comment in comments:
        #split each word in sentence
        splitWords = comment.split(' ')

        for word in splitWords:
            #filter non alphanumeric characters
            word = ''.join(filter(str.isalnum, word)).lower()

            if len(word) > 0:
                filteredWords.append(word)

        print(filteredWords)


