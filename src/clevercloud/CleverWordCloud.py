def CleverWordCloud(text, stopwords=STOPWORDS, shape=CLOUD, max_words=100):
    """
    This function generates a visually appealing word cloud with customized shape and stopwords.   
    
    Parameters
    ----------
    text : numpy.array
        Input an array of text / strings 
    
    stopwords: set 
        Input an set of strings 
    
    shape: string 
        Input a string that represents the path to an image 
    
    max_words: int 
        Input an integer to indicate the maximum number of words included in the word cloud  
    
    Returns
    -------
    png image 
        The output word cloud  
    
    Examples
    --------
    >>> CleverWordCloud(sample_text, max_words=200) 
    
    """"