from typing import List, Dict

def filter_elements(object:Dict, condition:float) -> List: #TASK
    '''
    #### filters and returns elements of dictionary dependent on condition value
    '''

    filtered: list[str]

    filtered = []

    for key in object:
        if object.get(key) >= condition:
            filtered.append(key)
        
    return filtered

def clean_text(text: str) -> List[str]: #TASK
    '''
    ### Prepares a text for further processing, returns 
    This removes sentence-marks, such as comma, questionmark etc.

    ---
    #### Parameters
    text : text of str_dtype

    ---
    #### Returns
    A list of all text_without_delimiters
    
    '''
    text_without_delimiters: str

    delimiters = [",", "?", "!", "\"", "\'", "(", ")", "-", "„", "“", "\n", ":", "'", "-", "–", ";",".","’"] #EXCLUDE

    #TODO

    return text_without_delimiters 