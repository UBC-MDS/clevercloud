# clevercloud

A package for creating clever word clouds

# Project Summary
This package is developed to expand the Stopwords library to capture more English words in various formats including different tense of verbs and plural nouns to achieve better result in machine learning models. For example, the word 'will' is in the current Stopword library and CleverCloud would include other formats such as 'would'. 

## Functions

There are 4 functions in this package:

-   `CleverClean` A preprocessor to convert all the letters to lower case and remove punctuations.

-   `CleverLemStem` A preprocessor to conduct lemmatinzation and stemming on the text.

-   `CleverStopwords` A comprehensive list of English stopwords that allow adding more customized words.

-   `CleverWordCloud` As function to generate a visually appealing word cloud with customized shape and stopwords.

## Installation

```bash
$ pip install clevercloud
```

## Usage

- TODO

## Contributing
Contributors of the project: Amelia Tang, Arushi Ahuja, Victor Francis, Adrianne Leung

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`clevercloud` was created by Group_20. It is licensed under the terms of the MIT license.

## Credits

`clevercloud` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
