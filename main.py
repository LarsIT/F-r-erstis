import json
import requests
from res.stopwords import stopwords
from typing import Set, List, Dict, Any
from res.test_article_tags import api_tag
from general import filter_elements, clean_text
from calculations import compute_idf, compute_tf
from collocation import count_elements, collocations


if __name__ == '__main__': #TASK

    api_key = 'e04d05a4-d17a-4ab6-989b-70b1ac386f4e'
    corpus: List[str] = []
    titles: List[str] = []
    word_count_complete: List[Dict[str,int]] = []
    collocation_count_complete: List[Dict[str,int]]= []

    #Text and Title aquisition
    for text in api_tag: #TASK

        #TODO


        doc = clean_text(body_text) #body_text ist der Text des Artikels, könnt ihr umbenennen wenn ihr mögt
        


    words_set: Set[str] = set()
    tf_all: List[Dict[str, int]] = []

    number_of_docs: int = #TODO

    #compute all metrics that have a scope of one document and store them for presentation
    for doc in corpus: #TASK
        #removing stopwords
        words: List[str] = #TODO
        #creating a set of all words
        words_set: Set[str] = #TODO
        
        # compute tf
        tf: Dict[str, int] = compute_tf(words) 
        #store all tf-values for tf-idf calculation (later)
        tf_all.append(tf) 

        #compute word count
        #store all word counts for presentation (later)
        word_count_complete.append(count_elements(words))  

        #compute collocation count
        collocation_candidates = collocations(words=words,length=2) 
        #store all colloccation counts for presentation (later)
        collocation_count_complete.append(count_elements(collocation_candidates))  

    #compute idf
    #has to be computed after the doc for-loop since if requires information from accross the whole corpus
    idf: Dict[str, float] = compute_idf(words_set, corpus) 

    # compute tf-idf
    tf_idf_complete: List[Dict[str, float]] =  []
    #TODO 


    #presentation
    j = 0
    for i in word_count_complete: 
        
        print('Document title:',titles[j])
        print('Keywords from Word Count:', filter_elements(i,3))
        print('Keywords from Collocations:', filter_elements(collocation_count_complete[j],2))
        print('Keywords generated from TF-IDF:', filter_elements(tf_idf_complete[j],0.009),'\n')

        j += 1

    
    