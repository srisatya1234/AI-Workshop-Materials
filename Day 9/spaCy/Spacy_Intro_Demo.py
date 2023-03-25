
#pip install spacy
#python -m spacy download en

import spacy
# Load English language model
nlp = spacy.load('en_core_web_sm')

## Parsing text
doc = nlp(u'London is a big city in the United Kingdom.')

## Extract Named Entities
print("\n--- Ex-1 : NER  ---\n")
print(doc.ents)
for ent in doc.ents:
    print(ent.label_, ent.text)

## Extract Parts-of-Speech
print("\n--- Ex-2 : PoS Tagging ---\n")
for token in doc:
    print(token, token.pos_)