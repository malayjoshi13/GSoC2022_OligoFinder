![image](https://user-images.githubusercontent.com/71775151/188505048-90243899-f39d-4816-90ac-e9ab02ed4453.png)

# GSoC2022_genomic_info_extract
Extract genomic information from papers. Made during GSoC 2022 for @Genome Assembly And Annotation @WormBase

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
