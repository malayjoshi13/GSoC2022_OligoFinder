# OligoFinder: RegEx and Machine Learning based system for finding and extracting Oligonucleotides mentions from biomedical research papers

> ## Made during Google Summer of Code 2022 @The Genome Assembly and Annotation section of EMBL-EBI

![pic](https://user-images.githubusercontent.com/71775151/188505676-b48bbcb4-ef1f-42bf-be05-fcd3223370aa.jpg)
 
- **Mentor**: [Magdalena Zarowiecki](https://github.com/MagdalenaZZ)
- **Project Guides**: [Andrés Becerra Sandoval](https://github.com/abecerra), [Valerio Arnaboldi
](https://github.com/valearna) 
- **Project Category**: [Extract important information from scientific papers](https://summerofcode.withgoogle.com/programs/2022/projects/5b96vIqa)

## Objective
The problem of counting the linear extensions of a given partial order consists in counting all the possible ways that we can extend the partial order to a total order that preserve..........

## Work overview
#### Implementation of classes for representing Order Polytopes and Posets
  - Link to the PR: [#165](https://github.com/GeomScale/volume_approximation/pull/165)
  - Overview: 
    - Created a class for representing a poset.
    - Created a class for representing an order polytope.
    - Implemented membership, boundary and reflection oracles. Also implemented their optimized versions for accelerated billiard walks which rely on preprocessing to speed up the oracles.
    - Added unit tests and examples for both the classes.
  - add pictures and ss

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

## Next Steps
The TFLite model for BertNLClassifier API is not available yet (TFLite team is working on it), when it becomes available it will be integrated into the Text Classification Android Example, and we may also re

## Acknowledgements
My Google Summer of Code Experience was awesome ❤️ and a large part of this great experience was the good mentoring of Meghna Natraj, George Soloupis, Margaret Maynard-Reid, Lu Wang, Le Viet Gia Khanh, Tian Tian and TensorFlow Team.

I thank them for their constant guidance, code reviews, timely feedback, help and most importantly, for their dedicated advice and encouragement throughout GSoC. I would definitely love to contribute more in the future to the TensorFlow.
