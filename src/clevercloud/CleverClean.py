def CleverClean(text):
    """
    A preprocessor to convert all letters to lower case, and to remove all punctuations and digits from the text.  
    
    Parameters
    ----------
    text : numpy.array
        Input an array of text / strings 
    
    Returns
    -------
    numpy.array
        The cleaned array of text 
    
    Examples
    --------
    >>> sample_text = numpy.array('Apple is MY favorite!')
    >>> CleverClean(sample_text)
    'apple is my favorite'   
    
    """
    #importing string package
    import string 

    #coverting text to lower case
    text_low = text.lower() 

    #removing all the digits from text
    text_low_noDigits = ''.join([i for i in text_low if not i.isdigit()])

    #removing all the punctuation from text using a for loop 
    prepro_text = "" #storing the complete preprocessed text in this variable 
    for i in text_low_noDigits:
        if i not in string.punctuation:
            text_low_noDigits+=i
    
    #returning the text 
    return prepro_text
