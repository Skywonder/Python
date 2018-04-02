from collections import namedtuple
import sys
from Beautifulsoup import Beautifulsoup 
indexDict = dict()
Pair = namedtuple("Pair", ["id", "pages"])

##dont modify until later
def search_word(searchWord):
    global indexDict
    filename = "termID.txt"
    with open(filename, "r") as fp:
        for line in fp:
            tokens = line.rstrip().split(' ')
            if(tokens[1] == searchWord.lower()):
                indexDict[tokens[1]] = Pair(tokens[0], list())
                for pgs in sorted(open_invertedIndex(tokens[0])):
                    try:
                        ## change later
                        indexDict[tokens[1]].pages.append(pgs)
                    except:
                        continue
 
                
                return find_url(searchWord.lower())
    return list()
                    
##work on this one
def open_invertedIndex(searchId):
    with open("invertedIndex.txt","r") as fp:
        for line in fp:
            tokens = line.rstrip().split(' ')
            # word_id total_number list[doc_ids]
            if(tokens[0] == searchId):
                return tokens[2:]
    return list()


##dont modify
def find_url(searchWord):
    ret = list()
    with open('docID.txt','r') as doc_id:
        if indexDict:
            for line in doc_id:
                tokens = line.rstrip().split()
                #tokens[0] = doc_id
                if tokens[0] in indexDict[searchWord].pages:
                    ret.append(tokens[1])
    return ret

#take the list of document
def find_tf(pgs):
    
    
    #1. open the docid
    try:
    
        with open("./WEBPAGES_CLEAN" + pgs) as sites:
            soup = BeautifulSoup(sites, 'html.parser')
            print soup.find_all('body')
            
        
    except:
        raise Exception


                    
if __name__ == '__main__':
##    while(1):
##        inputVar = raw_input("Please input search word: ")
##        print 'Searching......'
##        l = search_word(inputVar.lower())
##        if(len(l)>0): print 'Found pages\n ----------------------------'
##        for p in sorted(l):
##            print p
##        print '----------------------------'
##        print 'Total Found pages:', len(l)
##        print '\n'
    find_tf("0/0")
    

    
