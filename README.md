![1200px-GSoC_logo svg](https://user-images.githubusercontent.com/71775151/188504149-fa9ddcf1-6de0-4b7a-bd98-4eb3170de296.png)

![600x600logos_hackathon_sponsors_logos2](https://user-images.githubusercontent.com/71775151/188504166-8272a4ed-a502-4b0f-a8fb-a11964212187.jpg)

![fbu2s36u7uatdgev-360](https://user-images.githubusercontent.com/71775151/188504178-b052d003-5ac1-4f74-b1bb-e944660970b6.png)

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
