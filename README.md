## Medical-NER

## Description

Built a Named Entity Recognition model using spaCy.
The task is given an input text
Example: mild patient: fever, respiratory and other symptoms, the manifestation of pneumonia can be seen on
imaging.

Identify the Annotations (entities) in the input text for the domain of medical data.

E.g. of an Annotated Sentence : mild patient : fever [condition], respiratory [condition] and other symptoms [condition], the
manifestation of pneumonia [condition] can be seen on imaging [procedure].

This is just an approach that we can use for the purpose of extracting information from medical data.

training.json and training2.json are the inputs to the model. application.py and index.html contain the necessary code to build a User
Interface to display a basic Input-Output form.
