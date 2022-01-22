def CleverWordCloud(text):
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
    
    """
    from wordcloud import WordCloud
    import nltk
    if not isinstance(text, str):
        raise TypeError("Input variable should be a string.")
    
    wordcloud = WordCloud(max_font_size=40, max_words=100).generate(text)
    image = wordcloud.to_image()
    image.show()