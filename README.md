# clevercloud

Creating meaningful and visually appealing word clouds! 

## Summary

This package is developed to serve as the one-step solution to create meaningful and visually appealing word clouds. To create meaningful word clouds, data scientists typically takes multiple steps to clean the data, such as removing punctuation and digits, making the letters lower cases, conducting lemmatization and stemming. This package will help data scientists clean the data easily following the common practices and also allow to create more visually appealing word clouds in relevant shapes.  

## Functions

There are 4 functions in this package:

-   `CleverClean` A preprocessor to convert all the letters to lower case and remove punctuations.

-   `CleverLemStem` A preprocessor to conduct lemmatization and stemming on the text.

-   `CleverStopwords` A comprehensive list of English stopwords that allow adding more customized words.

-   `CleverWordCloud` As function to generate a visually appealing word cloud with customized shape and stopwords.

## Fitting into the Python ecosystem

Packages that have similar functions:

- [WordCloud](https://github.com/amueller/word_cloud): a word count generator that emphasis more frequently used words from an array of strings and represents them in the form of an image. 

What we do different: 

- Our aim is to improve on the pre-processing of strings before creating a wordcloud in order to make it more user specific and efficient.

- Word cloud only eliminates limited amount of stopwords, but with our package we are giving users the opportunity to add more stopwords that cater to their analysis.

- We are focused on removing as many redundant and duplicate words by setting strings to lower case, removing punctuation, lemmatizing and stemming the text. 


## Installation

``` bash
$ pip install clevercloud
```

## Usage

-   TODO

## Contributing

Contributors of the project: Amelia Tang, Arushi Ahuja, Victor Francis, Adrianne Leung

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`clevercloud` was created by Group_20. It is licensed under the terms of the MIT license.

## Credits

`clevercloud` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
