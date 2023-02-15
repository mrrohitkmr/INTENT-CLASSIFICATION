# INTENT CLASSIFICATION
STEP==>1 CONVERT TEXT FILE INTO JSONL
convert text file into jsonl with the help of createdata.py

STEP==>2 TRAIN NER MODEL
==> Train ner model using model.py
==> This file generate loc file in home directiory

STEP==>3 THIS COMMAND CREATES A PYTHON PACKAGE FOLDER STRUCTURE.
> python -m spacy package loc . --force

STEP==>4 CREATE TAR FILE
> cd en_proglang-2.2.5
> python setup.py sdist 
> cd .. 

STEP==>5 
> python -m pip install en_loc-2.2.5/dist/en_loc-2.2.5.tar.gz
