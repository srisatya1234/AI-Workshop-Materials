#pip install nltk

from nltk import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 2
ngramsres = ngrams(sentence.split(), n)
for grams in ngramsres:
  print(grams)

  