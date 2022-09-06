# OligoFinder: RegEx and Machine Learning based system for finding and extracting Oligonucleotides mentions from biomedical research papers

> ## Made during Google Summer of Code 2022 for Genome Assembly and Annotation section of EMBL-EBI

![pic](https://user-images.githubusercontent.com/71775151/188505676-b48bbcb4-ef1f-42bf-be05-fcd3223370aa.jpg)
 
- **Mentors**: [Magdalena Zarowiecki](https://github.com/MagdalenaZZ), [Andrés Becerra Sandoval](https://github.com/abecerra), [Valerio Arnaboldi
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

Input pipeline

Having an efficient input pipeline is a necessity for training on powerful hardware like TPUs. Thus, I spent a lot of time creating and optimizing the input pipeline. tf.data is a boon for such tasks and it took away most of the painpoints. However, the challenge was to augment the data as fast as possible. It all came down to the subtleties of the preprocessing functions. Which augmentation should be aaplied first? What parts can be added to the model itself? Is I/O the most time-consuming? The answers to all of these questions came with increased performance. It is noteworthy that tf.image and tfa made it a breeze to experiment with different setups.


Model implementation

RegNetY is originally implemented in PyTorch by Facebook AI Research in their repository pycls. It was crucial that the model was as close to the original implementation. This would greatly affect the accuracy of the models. Thus, we implemented the models with extreme care to ensure that the architecture was as close to the original one.


Training

Training and evaluation of the model was the most interesting part of the project. It included finding the perfect setup which suited the model and gave the best accuracy. During the training, we fixated on the hyperparameters which resulted in the best performance and started improving from there. Iteratively and progressively, we were able to get substantial gains. It was common to go back to the model implementation and input pipeline to check their correctness and improve them. We left no stone unturned. However, I was unable to obtain the accuracies mentioned by the authors, even after rigourous debugging. The following accuracies were obtained after substantial experimentation. I finally fixed upon using AdamW as the optimizer and keeping rest the same as the paper. This gave good performance boosts. I will continue to explore and try to improve the accuracy as far as possible.
Validation accuracies of models:


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

I thank Google Summer of Code and the Genome Assembly and Annotation section of EMBL-EBI for granting me this opportunity. I am grateful to my mentors Magdalena Zarowiecki, Andrés Becerra Sandoval and Valerio Arnaboldi for their continuous guidance and encouragement. 

Without them this project would not have been possible. I thank them for their constant guidance, code reviews, timely feedback, and most importantly, for their encouragement throughout GSoC. It was great summer working on this project and I would definitely love to contribute more in the future to the EMBL-EBI.
