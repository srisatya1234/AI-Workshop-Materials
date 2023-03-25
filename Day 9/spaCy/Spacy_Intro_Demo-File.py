
#pip install spacy
#python -m spacy download en

import spacy
# Load English language model
nlp = spacy.load('en_core_web_sm')

## Parsing text
text = open('file.txt').read()
doc = nlp(text)

## Extract Named Entities
for ent in doc.ents[:7]:
    print(ent.text, ent.label_)