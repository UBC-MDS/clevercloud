def CleverLemStem(text):
    """
    A preprocessor to conduct lemmatinzation and stemming on the text.   
    
    Parameters
    ----------
    text : str
        Input a strng 
    
    Returns
    -------
    str
        The lemmatized and stemmed string 
    
    Examples
    --------
    >>> sample_text = "maximum crying feet"
    >>> CleverLemStem(sample_text)
    "maxim cry foot"
    """
    # check the type of the imput 
    if not isinstance(text, str):
        raise TypeError("The input value should be a string.")
    
    # import packages 
    from nltk.stem import LancasterStemmer, WordNetLemmatizer
    from nltk.tokenize import RegexpTokenizer
    
    # lemmatization 
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_text = tokenizer.tokenize(text)
    lem = WordNetLemmatizer()
    lem_text = ' '.join([lem.lemmatize(i) for i in tokenized_text])
    
    # stemming 
    tokenized_lem_text = tokenizer.tokenize(lem_text)
    stemmer = LancasterStemmer()
    clean_text = ' '.join([stemmer.stem(i) for i in tokenized_lem_text]) 
    
    return clean_text
