def get_word(sentence,n):
    #only proceed if n is positive
    if n>0:
    words=sentence.split()
    #Only proceed if n not more than the number of words
    if n<=len(words):
        return word[n-1]
    return("")
print(get_word("this is a lesson about lists",4)) #Should print:'lesson
print(get_word("this is a lesson about lists",-4))#nothing
print(get_word("now we are cookig!",1))#should print:now
print(get _word("now we are cooking",5))#nothing