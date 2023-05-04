from typing import Set, List, Dict, Any

def collocations_simple(words:List[str]) -> List[str]:
    '''
    creates collocation list with collocation length 2\n
    Words parameter is an array of individual words\n
    returns list of collocations -> collocation_candidates
    '''
    collocation_candidates: List[str] = []

    #TODO

    return collocation_candidates

def merge_str(arr: List[str]) -> str:
    '''
    Merges all elements of str_dtype of an array into one element -> merge
    
    Returns merge
    '''
    merge: str

    #TODO

    return merge

def collocations(words: List[str], length:int) -> List[str]:
    '''
    Creates collocation list with variable length\n
    Words parameter is an array of individual words\n
    Length parameter defines the length of the created collocations out of the words array

    Note:\n
    Let n be len(words) and l be length\n
    then there are always n-l+1 collocations possible in a given array
    '''

    candidates: List[str] = []
    temp: List[str]

    #TODO      

    return candidates

def count_elements(elements: List[str]) -> Dict[str, int]: #TASK:
    '''
    ### counts elements of a document

    ---
    #### Parameters
    elements : list of elements of str dtype

    ---
    #### Returns
    A sorted dictionary with element as key and a count of element in elements as value, sorted by value DESC
    '''

    count: dict[str,int] = {} 
    
    #TODO

    return count 








