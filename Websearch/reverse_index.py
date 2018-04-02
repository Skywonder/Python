

# -*- coding: utf-8 -*-
# -*- coding: ascii -*-

import os
import sys
import collections
import json
import re
from sets import Set
import nltk.corpus import stopwords


#data path to create the index from 
d_p = './WEBPAGES_CLEAN/'

#counts, t_c: terms, d_c: documents
t_c = 0
d_c = 0

#dictionary for Terms ID
termID = {}
#dictionary for document ID
docID = {}
#dictionary for Inverted term id with documentlist. ex.
term_doc_invertedID = {}
BUFFER_SIZE = 65536
ignored = {"bookkeeping.json"}
# Tags:
#"<body>", "</body>",
#"<title>", "</title>",
#"<h1>", "</h1>",
#"<h2>", "</h2>",
#"<h3>", "</h3>",
# "<b>", "</b>",
#"<strong>", "</strong>"
#


def reverseIndex():
    global t_c;
    global d_c;
    global termID;
    global docID;
    global term_doc_invertedID
    global BUFFER_SIZE
    f_c = len(os.listdir(d_p))
    p_c = 0 #check the number of files parsed
    stop = set(stopwords.words('english'))
    
    #print(f_c)

    ##
    # Trying our best to access the files 
    ##

    #get the matching data id (directory folder) and file name
    for dir_folder in os.listdir(d_p):
        if (dir_folder.startswith('bookkeeping.json')):
            with open(d_p + str(dir_folder)) as json_file:
                json_file = json.load(json_file)
                    #print(json_file)
                for k, v in json_file.items():
                    print ("Data ID: " + k + "URL: " + v)
                    docid = k
                    docUrl = v
                    docID[docid] = docUrl

    #Continue to access each file and token all the words and process reverse indexing 
    for dir_folder in os.listdir(d_p): #get all the folder
        try:
            #lets look for the data within the text files inside folder directory
            if not dir_folder.startswith('.') | dir_folder.startswith('bookkeeping.tsv') | dir_folder.startswith('bookkeeping.json'):#if they are folder
                #print(len(os.listdir(d_p + dir_folder)))
                print(dir_folder)
                for index in os.listdir(d_p + dir_folder):
                    with open(d_p + str(dir_folder) + '/' + index,"rb") as raw_data_file: #this is opening individual files inside the folder
                        #print("Get raw_data_file")
                        #print("Path: " + d_p + str(dir_folder) + '/' + index)
                        #now that we can access the folder text we can work on it

                        #ID in the json file....use this to find the url 
                        di_id = dir_folder + '/' + index #this is equivalent of #/# 
                        
                        lines = raw_data_file.readlines()
                        #print(lines)
                        for line in lines:
                            line = re.sub('[^a-zA-Z0-9]', ' ', line)
                            #print(line)
                            for word in [k.lower() for k in line.split()]:
                                #word from the line starts here
                                #print(word)
                                if (word not in stop) and (not word.isdigit()):
                                    value = termID.get(word)                                
                                    if (not value):
                                        termID[word] = t_c
                                        term_doc_invertedID[t_c] = Set([di_id])
                                        #takes the doc id 
                                        t_c = t_c + 1
                                    else:
                                        term_doc_invertedID[value].add(di_id) #use set
                    #count as finished parsing a file                                
                    p_c = p_c + 1;
                #show overall progress .... for our debug
                progress = (p_c/float(f_c * 500)) * 100
                sys.stdout.write("Parsing files... %d%%  \r" % progress)
                if (progress != 100):
                    sys.stdout.flush()
                else:
                    sys.stdout.write('\n')
            
                        

        except ValueError:
            print('No Valid json ' + dir_folder)
    #output term id, doc id, and index
  
    with open('termID.txt','w') as t_id, open('docID.txt', 'w') as d_id, open('invertedIndex.txt', 'w') as i_id:
        termID = collections.OrderedDict(sorted(termID.items(), key = lambda x:x[1]))
        docID = collections.OrderedDict(sorted(docID.items(), key = lambda x:x[1]))
        m_t = len(termID)
        m_d = len(docID)
        term_count = 0
        doc_count = 0
        t_d_count = 0
        
        for k, v in termID.iteritems():
            t_id.write(str(v) + ' ' + k + '\n')
            term_count = term_count + 1
            progress = (term_count/float(m_t)) * 100
            sys.stdout.write("Writing to file... %d%%  \r" % (progress))
            if (progress != 100):
                sys.stdout.flush()
            else:
                sys.stdout.write('\n')

        for k, v in docID.iteritems():
            d_id.write(str(k) + ' ' + v + '\n')
            doc_count = doc_count + 1
            progress = (doc_count/float(m_d)) * 100
            if(progress%10==0):sys.stdout.write("Writing to file... %d%% \r" % (progress))
            if(progress != 100):
                sys.stdout.flush()
            else:
                sys.stdout.write('\n')

        for k,v in term_doc_invertedID.iteritems():
            list_doc = str(len(v))
            for document_id in set(v):#make it set
                list_doc += ' ' + str(document_id)
            i_id.write(str(k) + ' ' + list_doc + '\r\n')
            t_d_count = t_d_count + 1;
            progress = (t_d_count/float(m_t)) * 100
            sys.stdout.write("Writing inverted index.... %d%% \r" % (progress))
            if (progress != 100):
                sys.stdout.flush()
            else:
                sys.stdout.write('\n')
            
    print('Total terms: ' + str(m_t))
    print('Total docs: ' + str(m_d))
    print('...Completed Reverse Indexing') 

if __name__ == '__main__':
    print('Parsing...')
    reverseIndex()
    
