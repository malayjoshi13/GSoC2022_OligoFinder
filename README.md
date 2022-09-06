# OligoFinder: RegEx and Machine Learning based system for finding and extracting Oligonucleotides mentions from biomedical research papers

> ## Made during Google Summer of Code 2022 for Genome Assembly and Annotation section of EMBL-EBI

![pic](https://user-images.githubusercontent.com/71775151/188505676-b48bbcb4-ef1f-42bf-be05-fcd3223370aa.jpg)
 
- **Mentors**: [Magdalena Zarowiecki](https://github.com/MagdalenaZZ), [Andrés Becerra Sandoval](https://github.com/abecerra), [Valerio Arnaboldi
](https://github.com/valearna) 
- **Project Category**: [Extract important information from scientific papers](https://summerofcode.withgoogle.com/programs/2022/projects/5b96vIqa)

## Table of Contents

- [Motivation](#1-motivation)
- [Objective](#2-objective)
- [Work overview](#3-work-overview) 
  * [Prerequisites](##prerequisites)
  * [Installation](#installation)
* [Dataset](#dataset)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Special Thanks](#special-thanks)


## 1) Motivation: What is an FDIR algorithm and why is it usefull?

Tell about the project, what are oligonucleotides, tell about recent work by EMBL-EBI, limitations of existing works that raise need for such product

One of the most challenging parts of space missions is knowing and controlling where your spacecraft is, what is its relative orientation with respect to earth and how it is moving. Being aware of these three things is crucial to know if your spacecraft is flying too high or too low, too close to other spacecrafts, or simply if its oriented in a way that will allow it expose its solar panels to the sun to produce power or to point its antenna down to earth for calling home.

To perform this crucial task of computing and controlling its position and orientation spacecraft are designed with a variety of sensors and actuators that, together with proper control algorithms, ensure that your satellite remains where you want it and pointing in the right direction. This is often referred to as Attitude and Orbit control subsystem or AOCS.

Since this subsystem is critical for the spacecraft, it is needless to say that a failure in one of these sensors or actuators could easily kill your spacecraft and put and end to your mission. A faulty reading of a gyroscope that says that your spacecraft is rotating when it is not, a dead gyroscope that gives no signal and can’t tell if it is, or just a faulty thruster that provided more thrust than it should could leave your spacecraft spinning uncontrolled.

For these reason, providing the spacecraft on board software with a way of detecting these kind of failures as well as guidelines on how to proceed if one of these failures is detected is crucial for any space mission. This is done by means of the so called Failure Detection, Isolation and Recovery algorithms (FDIR).

Traditionally, these types of algorithms where simple, as they where based mainly on hardware redundancy , i.e., having many sensors that measure the same thing so that if one fails, you could detect the failure by looking at the rest and seeing that the signal is not consistent, isolate the failure by ignoring the reading from that sensor, and recover from the failure simply by continue to listen to the rest non-faulty sensors. 

## 2) Objective
The problem of counting the linear extensions of a given partial order consists in counting all the possible ways that we can extend the partial order to a total order that preserve..........

## 3) Work overview
#### 3.1) Implementation of classes for representing Order Polytopes and Posets
  - Link to the PR - [#165 - describe in short](https://github.com/GeomScale/volume_approximation/pull/165)
  - Overview -
    - Created a class for representing a poset.
    - Created a class for representing an order polytope.
    - Implemented membership, boundary and reflection oracles. Also implemented their optimized versions for accelerated billiard walks which rely on preprocessing to speed up the oracles.
    - Added unit tests and examples for both the classes.
- add pictures and ss

More examples for overview

Input pipeline

Having an efficient input pipeline is a necessity for training on powerful hardware like TPUs. Thus, I spent a lot of time creating and optimizing the input pipeline. tf.data is a boon for such tasks and it took away most of the painpoints. However, the challenge was to augment the data as fast as possible. It all came down to the subtleties of the preprocessing functions. Which augmentation should be aaplied first? What parts can be added to the model itself? Is I/O the most time-consuming? The answers to all of these questions came with increased performance. It is noteworthy that tf.image and tfa made it a breeze to experiment with different setups.


Model implementation

RegNetY is originally implemented in PyTorch by Facebook AI Research in their repository pycls. It was crucial that the model was as close to the original implementation. This would greatly affect the accuracy of the models. Thus, we implemented the models with extreme care to ensure that the architecture was as close to the original one.


Training

Training and evaluation of the model was the most interesting part of the project. It included finding the perfect setup which suited the model and gave the best accuracy. During the training, we fixated on the hyperparameters which resulted in the best performance and started improving from there. Iteratively and progressively, we were able to get substantial gains. It was common to go back to the model implementation and input pipeline to check their correctness and improve them. We left no stone unturned. However, I was unable to obtain the accuracies mentioned by the authors, even after rigourous debugging. The following accuracies were obtained after substantial experimentation. I finally fixed upon using AdamW as the optimizer and keeping rest the same as the paper. This gave good performance boosts. I will continue to explore and try to improve the accuracy as far as possible.
Validation accuracies of models:


## 4) Usage
### 4.1) Install

- Create a virtual environment named "extractor" (only once):

  `python3 -m venv extractor`

- Activate the virtual environment each time:

  `source extractor/bin/activate`

- Install dependencies (only once):
  

  `pip install -r requirements.txt`
  
### 4.2) Configure credentials

Go to `utils` folder and there create `all_config.cfg` file as per the instructions mentioned in the README.md of `utils` folder.

### 4.3) Adding model

Go to `models` folder and follow instructions in README.md .

### 4.4) Execution

Extract oligos from research papers:

`python oligo_extract.py`

## 5) Results

In 100 papers tested (93 were in the manually curated ground truth file), gene-mutation matches were found in 53 papers.
Total 2433 matches were present in those 53 papers. And 977 matches were found using this developed pipeline.
TP: 472, FP: 505
Precision: 48.3%
After manually checking the false positives and updating the ground truth file -
TP: 807, FP: 170
Precision: 82.59%
Not all FP are FP. After manual verification of the final output, some were noticed to be true positive which were originally missed during the manual curation.

## 6) Future work

A lot has been achieved during this GSoC period, yet there is still plenty of work ahead in this ambitious project. Among the features that are still to be implemented and tasks to be performed there are:

- Continue to improve the neural networks to achieve better results at higher computational efficiencies.
Improve the simulator to generate better failure scenarios for thrusters.

## 7) Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## 8) License
Distributed under the MIT License. See ```LICENSE``` for more information.

## 9) Acknowledgements

I thank Google Summer of Code and the Genome Assembly and Annotation section of EMBL-EBI for granting me this opportunity. I am grateful to my mentors Magdalena Zarowiecki, Andrés Becerra Sandoval and Valerio Arnaboldi for their continuous guidance and encouragement. 

Without them this project would not have been possible. I thank them for their constant guidance, code reviews, timely feedback, and most importantly, for their encouragement throughout GSoC. It was great summer working on this project and I would definitely love to contribute more in the future to the EMBL-EBI.
