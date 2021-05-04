from better_profanity import profanity
#this file is to test the library we are using for filtering.
badwords = {'fuck':True,'school':False,'water':False,'computer':False,'ass':True,'damn':True}
for word in badwords:
    if profanity.contains_profanity(word)!=badwords[word]:
        #if the filter does not work properly, throw an error
        raise Exception("ERROR: Did not correctly filter words")