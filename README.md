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


## 1) Motivation

Tell about the project, what are oligonucleotides, tell about recent work by EMBL-EBI, limitations of existing works that raise need for such product

As the cost of DNA sequencing continues to fall, an increasing amount of information on human genetic variation is being produced that could help progress precision medicine. Increasingly, improved understanding of an individual’s genetic mutations is being used to identify individuals at high risk for a given disease, make better predictions about disease prognosis and tailor treatments so that they best suit the given patient. New findings about genetic mutations typically first appear in the scientific literature. This novel information is then later manually curated into genomic databases, such as COSMIC (Catalogue of Somatic Mutations in Cancer) where the information is presented in a standardized, queryable format. 

While such databases are invaluable resources and often researchers required comprehensive and accurate data on mutations that have been studied in specific genes or proteins, the process of manual curation by identification and extraction of oligos is expensive, time-consuming, captures a small part of the relevant literature and therefore is a significant challenge in the advancement of precision medicine. 

Automated information extraction procedures which involve text mining and biomedical natural language processing (NLP) techhniques can assist in the acquisition and management of this knowledge but it is found that previous efforts in biomedical automated text mining have focused primarily upon named entity recognition of well-defined molecular objects such as genes, but less work has been performed to identify entities like oligonucleotide sequences and other related objects. Also exisiting text-mining approches have inability to efficiently scale so as to minimize manual efforts and still perform with high accuracy as the corpus of literature is constantly expanding. Thus the current rates of biological database curation will not provide full coverage of even just the currently sequenced genomes for the foreseeable future. 

## 2) Objective

We present MutationFinder, an open-source, rule-based system for recognizing descriptions of point mutations in conjunction with the mutation data from text and extracting them into consistent and unambiguous representations. It will help to create large, high-quality gold standard data set for judging and comparing the performance of oligonucleotide extraction systems. Like the earlier mutation recognition systems,8–10 MutationFinder applies a set of regular expressions to identify mutation mentions in input texts. Our currently top-performing collection of regular expressions results in a precision of 98.4% and a recall of 81.9% when extracting mutation mentions from completely blind test data

Accurately identifying gene and protein names in text is an open area of research, and classifying extracted names as referring to genes or proteins is a task which human experts only do with around 80% agreement. We view mutation extraction, gene/protein named-entity recognition and gene/protein mutation disambiguation as separate language processing problems, which may collectively be solved by combining independent systems. MutationFinder provides reliable extraction of mutation data, and its modular nature and open-source availability in multiple languages facilitate its incorporation into more complex systems. Combining the output of MutationFinder with the output of an independent gene/protein name extraction system would provide a basis for assigning mutations to their gene/protein source, and the ability to distinguish gene and protein names would provide the requisite information to disambiguate mutation types.

MutationFinder splits text on sentences and applies its regular expressions to each sentence, whereas the baseline system splits both on words and sentences and applies different regular expressions to each.

Production of a simplified output file. a script for judging the performance of mutation mention extraction systems. The simplified file only reports one entry for each unique residue or mutation mention in the article, rather than including each mention as a separate entry, and is thus easy to read quickly and to use for scoring the performance of the program. The fact that a residue is mentioned in an article provides a good reason to read the article, so as a default we report full statistics for unique mentions only. However, we retain as an option the ability to report all instances of a particular mention in each document, as a user choice.

A potential source of false positives for mutation extraction systems is mentions of other entities, such as genes, proteins or cell lines, whose names look similar to mutation mentions. For example, MutationFinder would mistakenly extract the gene name L23A and the cell line T98G, as mutation mentions. This difficulty is commonly encountered by information extraction systems, and in many cases, can be avoided by beginning with a good information retrieval system (we have BOW or differentiating between TP and FP). ![WhatsApp Image 2022-09-05 at 1 09 06 PM](https://user-images.githubusercontent.com/71775151/188703543-bd992456-1982-4dde-b30b-24f7f26705f5.jpeg)

The primary objective of the project was achieved within the specified time of GSoC, namely to establish that deep learning is capable of inferring the homology relationship of gene pairs with high accuracy. This was done using a set of convolutional neural networks, as detailed below, which were implemented using TensorFlow2.

extract seq that use TP-FP differentiator, corpus generated using this pipeline, system to score 
Flow diagram

Explain this flow diagram which is basically an overview of this project's working
extracts sequences
![WhatsApp Image 2022-09-05 at 11 43 52 AM](https://user-images.githubusercontent.com/71775151/188707465-d11274a5-97e4-4d8c-85a5-a126bb5cd99a.jpeg)

tells if TP or FP
![WhatsApp Image 2022-09-05 at 11 44 24 AM](https://user-images.githubusercontent.com/71775151/188707581-ee70f829-d1b1-43b4-9ca9-e788a9d82302.jpeg)

"A pre-training and self-training approach for biomedical named entity recognition" --> Future work....first pretrain biobert and then self train on oligos dataset created right now. DL will be also used to find oligo nanes which cant be found using regex 
![WhatsApp Image 2022-09-05 at 11 45 26 AM](https://user-images.githubusercontent.com/71775151/188708306-c7e426af-fe4b-4ac4-af2a-c4e85fc7fe67.jpeg)

![WhatsApp Image 2022-09-05 at 11 45 53 AM](https://user-images.githubusercontent.com/71775151/188708135-ae4ce587-f049-417b-bbd2-fdc1a1c50d70.jpeg)

![WhatsApp Image 2022-09-06 at 11 47 16 PM](https://user-images.githubusercontent.com/71775151/188709369-0c6156aa-31ec-41aa-a62d-f3664ed55068.jpeg)

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


## 4) Folder Directory Structure

```
GSoC2022_OligoFinder/
│
├── Setup/
│   ├── config_readme.md
│   └── requirements.txt    
├── configure.py
│
│
├── RawText/
│   ├── textpresso.py
│   └── get_paper_content.py 
│
│
├── RegexRules/
│   ├── bw_brackets.py
│   ├── check_alpha_num_specialchk.py
│   ├── combine_oligo_parts.py
│   └── combine_rules.py
│ 
│ 
├── TP_FP_oligo/
│   ├── TfIdf_BOW_TpFp.py
│   ├── TfIdf_BOW_creator.py
│   ├── sentence_processor.py
│   └── ProjectSettings
│ 
│
├── oligo_extract.py
│ 
│
├── LICENSE
│ 
│
└── README.md
```
folder->file->rule (explain each regex rule)

### Part 1 - Initiating project setup

- `Setup` - stores `config_readme.md` file that contains credentials to access research papers from Wormbase database via Textpresso and `requirements.txt` file for setting up of development environment.

- `configure.py` - comprises of parameters 
  
  - `paper_ids` - from this parameter user can add research paper ids (present in Wormbase) from which they want to extract oligonuclotide mentions,     
  
  - `output_CSVname` - from this parameter user can change location of CSV containing extracted oligonucleotide mention along with other related objects. This file is output by `oligo_extract.py` and is input for `TfIdf_BOW_creator.py`
  
  - `oligo_BOW_filename` and `non_oligo_BOW_filename` - from this parameter user can change location of txt files containing BOW related to oligonucleotide and non-oligonucleotide mentions respectively. These files are output by `TfIdf_BOW_creator.py` and input for `TfIdf_BOW_TpFp.py` file

### Part 2 - Getting text from research paper(s)

- `RawText` - stores `textpresso.py` and `get_paper_content.py` files that extract content from research papers present in Wormbase database corresponding to their id mentioned in `paper_ids` parameter of `configure.py` file and returns a pair of paperid-sentence.

### Part 3 - RegEx rules to extract sequences that follow structure of Oligonucleotides

- `bw_brackets.py` - contain RegEx rule that extracts Oligonucleotide sequence if present inside brackets. Input: insert(TGAGACGTCAACAATATGG)hg, Output: TGAGACGTCAACAATATGG.

- `check_alpha_num_specialchk.py` - contain three RegEx rules: 
  - `has_acgt` - this RegEx rule checks if input word follows structure of an Oligonucleotide or not. If input word contains only alphabetic characters like A,a,C,c,G,g,T and T, then that word follows structure of an Oligonucleotide, otherwise not. Input1: TGAGACGTCAACAATATGG, Output1: TGAGACGTCAACAATATGG and Input2: TXxvFDECAAOpJHTGG, Outpu2: None.
  -  `has_35` - this RegEx rule checks if input word follows structure of an Oligonucleotide or not. If input word contains only numeric characters like 3 and 5, or don't has any numeric characters at all, then that word follows structure of an Oligonucleotide, otherwise not. Input1: 3'-TGAGACGTCAACAATATGG-5', Output1: 3'-TGAGACGTCAACAATATGG-5' and Input2: TGAGACGTCAACAATATGG, Outpu2: TGAGACGTCAACAATATGG and Input3: 3'-TGAGA2CGT3CAACAATATG675G-5', Output3: None. 
  -  `remove_special_characters` - except alphabetic characters ranging from A to Z and a to z, remove every other character from the input word like numeric values (3,5,etc), special characters (,./?"':}{][, etc) and extra spacings.

- `combine_oligo_parts.py` - contain two RegEx rule:
  - `is_part` - this RegEx rule combines back Oligonucleotide sequences which are actually part of a single oligo sequence but due to spaces, newline, etc are treated like individual oligo sequences. Input: TT GCA ATG CGAAAATAC, Output: TTGCAATGCGAAAATAC.
  - `only_regex` - outputs list of words which satisfies all structural rules of an Oligonucleotide and thus are called as 'sequences' from now onwards.
  
## 5) Usage

### 5.1) Install

- Create a virtual environment named "extractor" (only once):

  `python3 -m venv extractor`

- Activate the virtual environment each time:

  `source extractor/bin/activate`

- Install dependencies (only once):
  
  `cd Setup`
  `pip install -r requirements.txt`
  
### 5.2) Configure credentials and set parameters

Go to `Setup` folder (in your cloned GitHub repository) and there create `all_config.cfg` file as per the instructions mentioned in the README.md of `utils` folder. 

Now within `Setup` folder, go to `configure.py` and there change paramaters like:

a) `paper_ids`: add research paper ids present in Wormbase from which you wanr to extract oligonuclotide mentions

b) `output_CSVname`: change location of CSV containing extracted oligonucleotide mention along with other related objects. This file is output by `oligo_extract.py` and is input for `TfIdf_BOW_creator.py`

c) `oligo_BOW_filename` and `non_oligo_BOW_filename`: change location of txt files containing BOW related to oligonucleotide and non-oligonucleotide mentions respectively. These files are output by `TfIdf_BOW_creator.py` and input for `TfIdf_BOW_TpFp.py` file  

### 5.3) Execution

Extract oligos from research papers:

`cd ..`
`python oligo_extract.py`

## 6) Results

![WhatsApp Image 2022-09-05 at 11 46 47 AM](https://user-images.githubusercontent.com/71775151/188710228-77a5f4e2-5533-4904-b7a6-dc356b399065.jpeg)

In 100 papers tested (93 were in the manually curated ground truth file), gene-mutation matches were found in 53 papers.
Total 2433 matches were present in those 53 papers. And 977 matches were found using this developed pipeline.
TP: 472, FP: 505
Precision: 48.3%
After manually checking the false positives and updating the ground truth file -
TP: 807, FP: 170
Precision: 82.59%
Not all FP are FP. After manual verification of the final output, some were noticed to be true positive which were originally missed during the manual curation.

## 7) Future work

A lot has been achieved during this GSoC period, yet there is still plenty of work ahead in this ambitious project. Among the features that are still to be implemented and tasks to be performed there are:

- Continue to improve the neural networks to achieve better results at higher computational efficiencies.
Improve the simulator to generate better failure scenarios for thrusters.

## 8) Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## 9) License

Distributed under the MIT License. See ```LICENSE``` for more information.

## 10) Acknowledgements

I thank Google Summer of Code and the Genome Assembly and Annotation section of EMBL-EBI for granting me this opportunity. I am grateful to my mentors Magdalena Zarowiecki, Andrés Becerra Sandoval and Valerio Arnaboldi for their continuous guidance and encouragement. 

Without them this project would not have been possible. I thank them for their constant guidance, code reviews, timely feedback, and most importantly, for their encouragement throughout GSoC. It was great summer working on this project and I would definitely love to contribute more in the future to the EMBL-EBI.
