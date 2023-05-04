from typing import Set, List, Dict
import math

def compute_tf(words: List[str]) -> Dict[str, float]:  #TASK
    '''
    ###  calculates relative term-frequency of a term in a document

    ---
    #### Parameters
    words : list of all words of a document 

    ---
    #### Returns
    A dictionary with the word as key and the relative term-frequency as value
    '''

    number_of_terms: int = #TODO

    tf: Dict[str, float] = dict()
    single_word_weight: float = 1 / number_of_terms 

    #TODO

    return tf

def compute_idf(words_set: Set[str], corpus: List[str]) -> Dict[str, float]:
    '''
    ### calculates inverse-document-frequency

    ---
    #### Parameters
    words_set : Set of all unique words
    corpus : Collection of all documents used

    ---
    #### Returns
    A dictionary with every word of the words_set as key and
    the corresponding IDF-score as value
    '''

    number_of_docs: int = #TODO
    doc_contain_term_count: Dict[str, int] = dict() 
    idf: Dict[str, float] = dict() 

    #TODO

    return idf