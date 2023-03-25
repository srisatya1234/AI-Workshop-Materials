# -*- coding: utf-8 -*-
"""NER_Spacy-Detailed.ipynb
"""

pip install spacy

pip show spacy

import pandas as pd
import numpy as np

import spacy
# Load English language model
nlp = spacy.load('en_core_web_sm')

# Define custom entity labels
LABEL_NAME = 'NAME'
LABEL_ROLE_NAME = 'ROLE_NAME'
LABEL_JOB_TITLE = 'JOB_TITLE'
LABEL_LOCATION = 'LOCATION'
LABEL_PROJECT_NAME = 'PROJECT_NAME'
LABEL_ACRONYM = 'ACRONYM'

## *** V2 *** (Fine Tuning)
# Define function to extract specified entities from text
def extract_entities(text):
  # Create doc object
  doc = nlp(text)
  # Initialize empty list to store extracted entities
  entities = []

  # Extract named entities using doc.ents
  for ent in doc.ents:
      # Extract entity label and text
      label = ent.label_
      entity = ent.text
      
      # Add entity to list if it is a name, role name, job title, or location
      if label == 'PERSON':
          label = LABEL_NAME
          entities.append((entity, label))
      elif label == 'ORG':
          label = LABEL_ROLE_NAME
          entities.append((entity, label))
      elif label == 'JOB':
          label = LABEL_JOB_TITLE
          entities.append((entity, label))
      elif label == 'GPE':
          label = LABEL_LOCATION
          entities.append((entity, label))

  # Extract noun chunks using doc.noun_chunks
  for chunk in doc.noun_chunks:
      # Check if chunk is a proper noun
      if chunk.root.pos_ == 'PROPN':
          # Extract entity label and text
          label = LABEL_ROLE_NAME
          entity = chunk.text
          entities.append((entity, label))

  # Extract verb conjugations using doc.token.pos_
  for token in doc:
      # Check if token is a verb conjugation
      if token.pos_ == 'VERB':
          # Extract entity label and text
          label = LABEL_ROLE_NAME
          entity = token.text
          entities.append((entity, label))

  # Return list of extracted entities
  return entities

text = "John is the project manager for the XYZ project at the San Francisco location. His job title is Senior Manager."
text = "Sarah is the HR manager at the New York location. Her role is to recruit new employees and manage employee benefits."
entities = extract_entities(text)
print(entities)

"""# **V2 - More complex**

"""

## sample text
text = [
"John is the project manager for the XYZ project at the San Francisco location. His job title is Senior Manager.",
"Sarah is the HR manager at the New York location. Her role is to recruit new employees and manage employee benefits.",
"The ABC project is a collaboration between the San Francisco and New York locations. The project acronym is AB-C.",
"The XYZ project is led by Jane, who is a Senior Director. The project is based in London.",
"The ABC project team includes Tom, who is a Data Scientist, and Emily, who is a Software Engineer."
]

## import pandas as pd
# Create data frame with sample text ** ## To be reaplaced with df = pd.read('file.xlsx')
df = pd.DataFrame({'Text': text},index=[0, 1, 2, 3, 4])
df.Text

# Initialize empty list to store extracted entities
entities = []
# Iterate through rows of data frame
for index, row in df.iterrows():
  # Extract text from 'Text' column
  text = row['Text']
  # Pass text to custom NER model function
  extracted_entities = extract_entities(text)
  # Append extracted entities to list and assign labels
  for entity, label in extracted_entities:
    entities.append({'Text': text, 'Entity': entity, 'Label': label})

# Create new data frame using extracted entities and labels
result_df = pd.DataFrame(entities, columns=['Text', 'Entity', 'Label'])
# print(result_df)

result_df



# Commented out IPython magic to ensure Python compatibility.
# ## Download this code as html
# %%shell
# jupyter nbconvert --to html /content/Learn-NLP_NER_Spacy_Detailed.ipynb



