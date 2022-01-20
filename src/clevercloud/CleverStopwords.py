# author: Adrianne Leung
# date: Jan 2022

def CleverStopwords(words):
    """
    A comprehensive list of English stopwords that allow adding more customized words.    
    
    Parameters
    ----------
    words : set of strings 
        Input a set of words that need to be included in the stopwords 
    
    Returns
    -------
    set of strings  
        The complete set of stopwords 
    
    Examples
    --------
    >>> sample_words = {'disney', 'paris'}
    >>> CleverStopwords(sample_words)
​
    """
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    if not isinstance(words, set):
        raise TypeError("Input variable should be a set.")

    # NLTK English stopwords
    stopwords = set(stopwords.words("english"))

    new_stopwords = words
    
    # Check for unique new stopwords
    for w in new_stopwords:
        if w is not stopwords:
            # Add customised new words to the existing NLTK stopwords
            stopwords_all = stopwords.union(stopwords, new_stopwords)

    return stopwords_all
