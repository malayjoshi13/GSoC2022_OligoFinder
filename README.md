# OligoFinder: RegEx and Machine Learning based system for finding and extracting Oligonucleotides mentions from biomedical research papers

> ## Made during Google Summer of Code 2022 @The Genome Assembly and Annotation section of EMBL-EBI

![pic](https://user-images.githubusercontent.com/71775151/188505676-b48bbcb4-ef1f-42bf-be05-fcd3223370aa.jpg)

## Install

- Create a virtual environment named "extractor" (only once):

  `python3 -m venv extractor`

- Activate the virtual environment each time:

  `source extractor/bin/activate`

- Install dependencies (only once):
  

  `pip install -r requirements.txt`
  
## Configure credentials

Go to `utils` folder and there create `all_config.cfg` file as per the instructions mentioned in the README.md of `utils` folder.

## Adding model

Go to `models` folder and follow instructions in README.md .

## Execution

Extract oligos from research papers:

`python oligo_extract.py`
