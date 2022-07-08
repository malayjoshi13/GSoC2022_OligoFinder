# GSoC2022_genomic_info_extract
Extract genomic information from papers. Made during GSoC 2022 for @Genome Assembly And Annotation @WormBase

## Install

- Create a virtual environment named "extractor" (only once):

  `conda create -n extractor`

- Activate the virtual environment each time:

  `conda activate extractor`

- Install dependencies (only once):
  
  `conda install pip`

  `pip install -r requirements.txt`
  
## Configure credentials

Go to `utils` folder and there create `all_config.cfg` file as per the instructions mentioned in the README.md of `utils` folder.

## Execution

Extract oligos from research papers:

`python oligo_extract.py`
