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

With wbtools access credentials

## Execution

Extract oligos from research papers:

`python oligos_extract.py`
