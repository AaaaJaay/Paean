# Wordcount (Advanced)

### The project

This project is just like the wordcount exercise, where we want to find the top 3 most
common words

There are some new requirements for this exercise:

* Read the file `alice.txt` to get the data from which to count words
* Remove any punctuation at the starting or ending character so that `end` and `end.` will
  count as the same word. Punctuation to look for are: full stop, comma, question mark,
exclamation mark, single and double quotes, semicolon, colon, underscore. Any punctuation that comes
in the middle of the word can be left as it is, so `its` and `it's` will be different
words
* Handle the upper and lower cases, so that `the` and `The` are both counted as the same word

### More advanced

* Sometimes there will be more than one punctuation at the end,
  example `"wow!"`in that case remove all the punctuation from the end.
* Finally, remove stop words from the counting. Stop words are common grammer words like
  `the`, `and`, `what`, `she` etc. Usually the whole text is filled with lots of these words,
which we are not interested in. We want to find the top 3 excluding all these stop words.
A file `stopwords.txt` is provided with a list of stop words

### Super advanced

To do even more analysis of text like this, you can use the `nltk` (Natural Language
Tool Kit) library. Install it with `pip install nltk` to use. This library has features
like stopwords, sentiment analysis, identifying proper nouns and categorising as people
name, place name and many more features. Using `nltk` is beyond the scope of the training
but it is a good place to look if you are interested in text analysis.
