#index words in a list
#opfi=open("thedata.txt","r")

    #a standard lib to count/sort dictionary items i believe
import operator
    #a standard lib to pretty up printing
import pprint
    #define an empty dictionary
wdic={}
    #loop through a txt file word by word, count them and push them into wdic
with open('thedata.txt','r') as opfi:
    for line in opfi:
        for word in line.split():
           if word not in wdic:
               wdic[word]=1
           else:
               wdic[word]+=1
                #sort the dictionary by key, which is the count of items, which are unique words
    sdic = sorted(wdic.items(),key=operator.itemgetter(1))
        #lets see it
    pprint.pprint(sdic)
#opfi.close()

'''import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))'''