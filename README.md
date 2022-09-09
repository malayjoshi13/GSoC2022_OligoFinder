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


## 1) Background

Our genetic information is stored in a repeating sequence of nucleotides, abbreviated by the letters A, C, G, T in DNA, and A, C, G, U in RNA. Oligonucleotides are short DNA or RNA oligomers between 20 and 60 units in length. However, they rarely exceed 200 nucleotides. They can be synthesized or found naturally as single stranded (ss) or double stranded (ds) fragments of DNA or RNA. Oligonucleotides (or oligos) have many uses from research to disease diagnosis and recently therapeutics.

The last few decades have witnessed an explosion of knowledge in the field of molecular biology. It is increasingly evident that evolution has generated an astonishingly complex set of interconnected processes through which gene expression can be regulated. One such process which has evolved due to wide availability of inexpensive synthetic single-stranded DNA and RNA is for routine DNA amplification by PCR primers. It has revolutionized the study of gene expression and disease processes via a range of processes including RNAi, target degradation by RNase H-mediated cleavage, splicing modulation, non-coding RNA inhibition, gene activation and programmed gene editing. In addition to use of Oligonucleotides as PCR primers, they are also used as probes, in microarray, in situ hybridization, and antisense analyses, and even as drug carriers.

Such new findings about varied applications of Oligonucleotides typically first appear in the scientific literature and is then later manually curated into biomedical databases, such as [WormBase](https://wormbase.org//#012-34-5) where the information is presented in a standardized, queryable format. This process of manual curation by identification and extraction of Oligonucleotides is expensive, time-consuming, captures a small part of the relevant literature and therefore is a significant challenge in the advancement of precision medicine and gene expression.

Another way for curation is of automated information extraction which uses text mining and biomedical natural language processing (aka BioNLP) techniques that can assist in the acquisition and management of this knowledge but it is found that previous efforts/developments in the biomedical automated text mining have focused primarily upon named entity recognition of well-defined molecular objects such as genetic variations and mutations, but less work has been performed to identify entities like Oligonucleotides which in recent years have gained status of being very crucial entities in the biomedical research field and practical applications. Another limitation with this method is its inability to efficiently scale to minimize manual efforts and still curate a constantly expanding corpus of literature with high accuracy.

Thus having an accurate, efficient, scalable and fully/semi-automated curation system for identification and extraction of Oligonucleotide mentions along with related data is much needed by Biomedical researchers. Such a system will be used to develop a high-quality gold standard dataset of Oligonucleotide mentions across various Biomedical research papers.

## 2) Objective

Give script for oligo-extraction and other details and placing them on CSV, as many seq not TP thus a script to auto-tag using BOW, script to automatically update and advance BOW, system built upon a CSV file to allow easy manual curation by taking in account previous tags and relevant auto-tags (helps in easy data curation for training BioBERT, analyse performance of BOW and oligo extraction by giving matrix between TP vs FP, to provide corpus by use of RegEx + BioBERT to extract sequences and BOW to differentiate TP from FP

We present MutationFinder, an open-source, rule-based system for recognizing descriptions of point mutations in conjunction with the mutation data from text and extracting them into consistent and unambiguous representations. It will help to create large, high-quality gold standard data set for judging and comparing the performance of oligonucleotide extraction systems. Like the earlier mutation recognition systems,8–10 MutationFinder applies a set of regular expressions to identify mutation mentions in input texts. Our currently top-performing collection of regular expressions results in a precision of 98.4% and a recall of 81.9% when extracting mutation mentions from completely blind test data

Accurately identifying gene and protein names in text is an open area of research, and classifying extracted names as referring to genes or proteins is a task which human experts only do with around 80% agreement. We view mutation extraction, gene/protein named-entity recognition and gene/protein mutation disambiguation as separate language processing problems, which may collectively be solved by combining independent systems. MutationFinder provides reliable extraction of mutation data, and its modular nature and open-source availability in multiple languages facilitate its incorporation into more complex systems. Combining the output of MutationFinder with the output of an independent gene/protein name extraction system would provide a basis for assigning mutations to their gene/protein source, and the ability to distinguish gene and protein names would provide the requisite information to disambiguate mutation types.

MutationFinder splits text on sentences and applies its regular expressions to each sentence, whereas the baseline system splits both on words and sentences and applies different regular expressions to each.

Production of a simplified output file. a script for judging the performance of mutation mention extraction systems. The simplified file only reports one entry for each unique residue or mutation mention in the article, rather than including each mention as a separate entry, and is thus easy to read quickly and to use for scoring the performance of the program. The fact that a residue is mentioned in an article provides a good reason to read the article, so as a default we report full statistics for unique mentions only. However, we retain as an option the ability to report all instances of a particular mention in each document, as a user choice.

A potential source of false positives for mutation extraction systems is mentions of other entities, such as genes, proteins or cell lines, whose names look similar to mutation mentions. For example, MutationFinder would mistakenly extract the gene name L23A and the cell line T98G, as mutation mentions. This difficulty is commonly encountered by information extraction systems, and in many cases, can be avoided by beginning with a good information retrieval system (we have BOW or differentiating between TP and FP). ![WhatsApp Image 2022-09-05 at 1 09 06 PM](https://user-images.githubusercontent.com/71775151/188703543-bd992456-1982-4dde-b30b-24f7f26705f5.jpeg)

The primary objective of the project was achieved within the specified time of GSoC, namely to establish that deep learning is capable of inferring the homology relationship of gene pairs with high accuracy. This was done using a set of convolutional neural networks, as detailed below, which were implemented using TensorFlow2.

extract seq that use TP-FP differentiator, corpus generated using this pipeline, system to score 

Explain this flow diagram which is basically an overview of this project's working
extracts sequences
![WhatsApp Image 2022-09-05 at 11 43 52 AM](https://user-images.githubusercontent.com/71775151/188707465-d11274a5-97e4-4d8c-85a5-a126bb5cd99a.jpeg)

tells if TP or FP
![WhatsApp Image 2022-09-05 at 11 44 24 AM](https://user-images.githubusercontent.com/71775151/188707581-ee70f829-d1b1-43b4-9ca9-e788a9d82302.jpeg)

"A pre-training and self-training approach for biomedical named entity recognition" --> Future work....first pretrain biobert and then self train on oligos dataset created right now. DL will be also used to find oligo nanes which cant be found using regex 
![WhatsApp Image 2022-09-05 at 11 45 26 AM](https://user-images.githubusercontent.com/71775151/188708306-c7e426af-fe4b-4ac4-af2a-c4e85fc7fe67.jpeg)

![WhatsApp Image 2022-09-05 at 11 45 53 AM](https://user-images.githubusercontent.com/71775151/188708135-ae4ce587-f049-417b-bbd2-fdc1a1c50d70.jpeg)

![WhatsApp Image 2022-09-06 at 11 47 16 PM](https://user-images.githubusercontent.com/71775151/188709369-0c6156aa-31ec-41aa-a62d-f3664ed55068.jpeg)

## 3) Folder Directory Structure

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
├── oligo_extract.py 
│
│
├── TP_FP_oligo/
│   ├── TfIdf_BOW_TpFp.py
│   ├── TfIdf_BOW_creator.py
│   └── sentence_processor.py
│ 
│
├── extract_BOW.py
│ 
│
├── LICENSE
│ 
│
└── README.md
```

### 3.1) Part of system for setting up and initiating setup

- `Setup` - stores `config_readme.md` file that contains credentials to access research papers from Wormbase database via Textpresso and `requirements.txt` file for setting up of development environment.

- `configure.py` - comprise of following parameters:-
  
  - `paper_ids` - from this parameter user can add research paper ids (present in Wormbase) from which they want to extract oligonuclotide mentions,     
  
  - `output_CSVname` - from this parameter user can change location of CSV containing extracted oligonucleotide mention along with other related objects. This file is output by `oligo_extract.py` and is input for `TfIdf_BOW_creator.py`
  
  - `oligo_BOW_filename` and `non_oligo_BOW_filename` - from this parameter user can change location of txt files containing BOW related to oligonucleotide and non-oligonucleotide mentions respectively. These files are output by `TfIdf_BOW_creator.py` and input for `TfIdf_BOW_TpFp.py` file

### 3.2) Part of system for getting text from research paper(s)

- `RawText` - stores `textpresso.py` and `get_paper_content.py` files that extract content from research papers present in Wormbase database corresponding to their id mentioned in `paper_ids` parameter of `configure.py` file and returns a pair of paperid-sentence.

### 3.3) Part of system having RegEx rules to extract sequences that follow structure of Oligonucleotides

- `bw_brackets.py` - contain RegEx rule `pick_from_brackets` that extracts Oligonucleotide sequence if present inside brackets. Input: insert(TGAGACGTCAACAATATGG)hg, Output: TGAGACGTCAACAATATGG.

- `check_alpha_num_specialchk.py` - contain three RegEx rules: 
  - `has_acgt` - this RegEx rule checks if input word follows structure of an Oligonucleotide or not. If input word contains only alphabetic characters like A,a,C,c,G,g,T and T, then that word follows structure of an Oligonucleotide, otherwise not. Input1: TGAGACGTCAACAATATGG, Output1: TGAGACGTCAACAATATGG and Input2: TXxvFDECAAOpJHTGG, Outpu2: None.
  -  `has_35` - this RegEx rule checks if input word follows structure of an Oligonucleotide or not. If input word contains only numeric characters like 3 and 5, or don't has any numeric characters at all, then that word follows structure of an Oligonucleotide, otherwise not. Input1: 3'-TGAGACGTCAACAATATGG-5', Output1: 3'-TGAGACGTCAACAATATGG-5' and Input2: TGAGACGTCAACAATATGG, Outpu2: TGAGACGTCAACAATATGG and Input3: 3'-TGAGA2CGT3CAACAATATG675G-5', Output3: None. 
  -  `remove_special_characters` - except alphabetic characters ranging from A to Z and a to z, remove every other character from the input word like numeric values (3,5,etc), special characters (,./?"':}{][, etc) and extra spacings.

- `combine_oligo_parts.py` - contain two RegEx rules:
  - `is_part` - this RegEx rule combines back Oligonucleotide sequences which are actually part of a single oligo sequence but due to spaces, newline, etc are treated like individual oligo sequences. Input: TT GCA ATG CGAAAATAC, Output: TTGCAATGCGAAAATAC.
  - `only_regex` - outputs list of words which satisfies all structural rules of an Oligonucleotide and thus are called as 'sequences' from now onwards.
  
- `combine_rules.py` - contain two RegEx rules:
  - `word_processor` - pass input word through four RegEx rules namely `pick_from_brackets`, `has_acgt`, `has_35`and `remove_special_characters` (all four mentioned above), and returns the ouput processed word.
  - `oligo_seq_regex` - output of `word_processor` rule becomes input for this which is passed to two RegEx rules namely `is_part` and `only_regex`. The output from this is a sequence which follow structural composition of an Oligonucleotide.

- `oligo_extract.py` - compiles extracted oligos (from research paper(s)), alongwith paper id, auto & manual true positive/false positive tags, previous, current (from which oligo sequence is extracted) & future sentences into a Pandas dataframe which is saved as a CSV file.

### 3.4) Part of system for creation and usage of BOWs 
- `TfIdf_BOW_creator.py` - uses 'TP or FP Oligo (manual)' column of CSV generated above (which has manual curations + auto curations which curator felt to be right) to generate two Bag of Words (BOW) having higher TF-IDF scores. 

  - First BOW has words related to sentences that have tag of containing "oligo" in the 'TP or FP Oligo (manual)' column. Second BOW has words related to sentences that have tag of containing "non-oligo", "other", "mutation", etc in the 'TP or FP Oligo (manual)' column of CSV genertaed.

- `TfIdf_BOW_TpFp.py` - uses BOWs generated above to auto-curate sentences in the upcoming output CSV to be a TP oligo or FP oligo.

- `sentence_processor.py` - process the words and adds only english dictionary words in the BOWs.  

### 3.5) Part of system that builds a cyclic pipeline between Oligo extraction script and BOWs creation & usage script
- `extract_BOW.py` - script that will run BOW creator script, Oligo extraction script and True positive/False positive auto marking script one after another in a continous manner till the time Oligo extraction script and BOW becomes so smart that number of True positive oligo sequences is high as a pre-defined number.

## 4) Usage

### 4.1) Install

- Create a virtual environment named "extractor" (only once):

  `python3 -m venv extractor`

- Activate the virtual environment each time:

  `source extractor/bin/activate`

- Install dependencies (only once):
  
  `cd Setup`
  
  `pip install -r requirements.txt`
  
### 4.2) Configure credentials and set parameters

Go to `Setup` folder (in your cloned GitHub repository) and there create `all_config.cfg` file as per the instructions mentioned in the README.md of `utils` folder. 

Now within `Setup` folder, go to `configure.py` and there user can perform following actions:
1
a) `paper_ids` - can add research paper ids present in Wormbase from which you wanr to extract oligonuclotide mentions. By default Wormbase ids of a set of `100 research papers` are taken for extracting oligonucleotides from them.

b) `output_CSVname` - can change location of CSV containing extracted oligonucleotide mentions along with other related objects. This file is output by `oligo_extract.py` and is input for `TfIdf_BOW_creator.py`. By default CSV of name `oligo_test.csv` will be created and accessed from the base directory location.

c) `oligo_BOW_filename` and `non_oligo_BOW_filename` - can change location of txt files containing BOW related to oligonucleotide and non-oligonucleotide mentions respectively. These files are output by `TfIdf_BOW_creator.py` file and input for `TfIdf_BOW_TpFp.py` file. By default BOWs named `oligo_BOW.txt` and `non_oligo_BOW.txt` will be created and accessed from the base directory location.

### 4.3) Execution

Extract oligonucleotides from research papers and use as well as enhance BOWs:

`cd ..`

`python extract_BOW.py`

## 5) Data Flow Diagram
paste image

Currently, this system is divided into majorly two halves. The first half, find and extract sequences that have conventional Oligonucleotides' structure into a CSV file. Another half first uses manual curations by the curator (who tags the sequences present in the CSV file to be an Oligonucleotide [True positive] or not an Oligonucleotide but has the same structure that an Oligonucleotide has [False positive]) to generate a Bag of Words (aka BOW) corresponding to words related to oligo sequences and non-oligo sequences in sentences. These BOWs are then used in the next/upcoming cycle to auto-label oligo sequences to be true positive or false positive (the idea behind using BOWs to auto-curate is that the pattern/words which are present in sentences with oligos or non-oligos will be first taken out and then used in future for auto-labelling as the presence of unique words from BOWs directly points towards a sequence to be an oligo or not).  

When the oligo extraction script runs on more and more research papers, it finds more sequences which for the first time need to be fully manually curated and then auto-curation by use of BOW (which reduce this fully manually curation to semi-manual curation work). These curated sentences and oligo sentences furthure improvise the existing BOWs by adding more words, thus widening the scope to include every possible word related to an oligo/non-oligo sequence. Again this improvised BOW will reduce the need for manual curation and will be able to differentiate better between oligo and non-oligo sequences, thus increasing True Positive and reducing False Positive oligo sequences.

This cycling pipeline cmprising of processes of extraction of oligonucleotide mentions from papers, auto-curation by BOWs, manual curation by curator and creation/extension of BOWs is run multiple times so that in the end, oligo extraction script and BOWs will become so much smart to produce a large corpus of True positive oligos that, in future will be used along with RegEx (what we are currently using) and BioBERT (trained on large oligo corpus mentioned above) based oligo extraction script to generate high True positives out of any given research paper.  

### Scenario 1 (User for first time is using this project i.e. there is no CSV and BOWs with him/her as of now) 
- When the user runs the command `python extract_BOW.py`, then as initially no CSV (containing extracted oligo sequences and curations) is present, it means BOWs (corresponding to oligos and non-oligos sequences) cannot be created as of now (because BOWs are created using the manual curations by the curator in the CSV). 
- Absence of BOWs further indicates that auto labelling of sequences (True positive oligo or False positive oligo) also needs to be skipped. 
- Therefore, as a result, only the `find_Oligos` function of the `oligo_extract.py` file will be used to extract oligonucleotides and return them in a CSV format along with other pieces of information like paper id, empty auto & manual true positive/false positive tags' columns, previous, current (from which oligo sequences are extracted) & future sentences.

### Scenario 2 (User has already once used this project over few papers i.e. there is a CSV with him/her and BOWs if that CSV has been curated else no BOWs [because BOW is created using manual curation in the CSV, which is empty right now] and now again using it on new research papers)
- For the first sub-scenario where BOWs are empty (as CSV is still not curated), there will be no TP-FP auto curation available; thus, even after the first time, the curator has to curate every time manually). So, let us ignore this case as the curator, anyhow, at some point in time has to curate the CSV if he/she wants auto-curation.
- Focusing on the second sub-scenario where BOWs are not empty (as the curator did the initial manual curation on the CSV generated using the `find_Oligos` function of `oligo_extract.py` called when the user runs command `python extract_BOW.py` in the CMD), there in the second cycle, using the manual curations of CSV, BOWs are created via `create_BOW` function of `TfIdf_BOW_creator.py` when the user runs runs command `python extract_BOW.py`. Note that BOWs are created before oligos get extracted via the `oligo_extract.py` script. Furthermore, for each round, as we assume the system is running on new research papers along with currently listed papers, there will be new oligo sequences and already existing sequences in each cycle. 
  - Now, these BOWs in the second round will auto-curate the new oligo sequences in the output CSV (as in the second round, only non-empty BOW has come into existence) via the `TfIdf_BOW_TpFp.py` file called when user runs command `python extract_BOW.py`. Note that this auto-curation will happen after oligo extraction and BOWs creation happens. However, this auto-curation in starting stages will not be that efficient but will act as a good help for reducing even some manual curation work. These BOWs have a scope to be improvised in the near future.
  - Now curator uses the above-generated auto-curation (auto-curation which he/she feels to be correct) along with his/her manual curation to curate and label newly generated oligo sequences as true positive or false positive. In addition, he/she uses old tags for already present sequences (from previous papers).
  - These manual curations + old verified tag + new curator verified auto-tags (all present in the 'TP or FP Oligo (manual)' column of CSV) would improvise the existing BOWs. 
  - The process continues, and new oligo sequences will be extracted, auto-tagged by improvised BOWs (from the previous cycle), manually curated by the curator + use of auto-tags verified by the curator and again, these tags will improvise the existing BOWs. 

- Thus, in short 
  - manual curation + curator verified auto-tags improvise BOWs to be used in the next cycle, 
  - comparison between auto-tags and manual tags in each cycle tells how smart BOW has become because the larger number of auto-taggings BOW can do, shows its higher performance, 
  - analysis of each cycle's manual-tags tells how many True positives have increased due to better BOWs and oligo extraction script. It also tells where the oligo extraction script can be further improvised.

## 6) Work overview

Please note that many modifications made in the features of this system were directly committed to the main branch as they are well tested and hold more straightforward logic and code blocks. Developments and modifications made in the significant features of this system were committed in the form of Pull Requests (PRs), which you can view below.

### 6.1) Implementation of pipeline to extract text from research papers
  - Directly commited to the main branch
  - Overview -
    - Created `get_paper_content.py` script, which via `textpresso.py` script extracts content from a research paper(s) in Wormbase corresponding to id(s) present in the `configure.py` file.

#### 6.2) Implementation of RegEx rules (present inside `RegexRules`) folder for extracting sequences following structure of Oligonucletides

  - Link to the PR - [#4](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/4), [#5](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/5), [#6](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/6/files)
  - Overview -
    - Created Regex rules `bw_brackets.py`, `check_alpha_num_specialchk.py`, `combine_oligo_parts.py`, `combine_rules.py` (earlier named as regex_extraction.py) 
    - Created `oligo_extract.py` script, which gets a text from a research paper(s), extracts sequences similar in structure to Oligonucleotide and returns data in a CSV format.

#### 6.3) Optimizing RegEx rules (present inside `RegexRules`) folder that extracts sequences following structure of Oligonucletides

  - Link to the PR - [#8](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/8/files), [#11](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/11/files)
  - Overview -
    - Optimized the logic used in `combine_oligo_parts.py` and `combine_rules.py` (earlier named regex_extraction.py) scripts to resolve the issue of incomplete extracted sequences.
    - Optimized the logic used in `combine_oligo_parts.py` `combine_rules.py` (earlier named regex_extraction.py) scripts to bring down False Positive sequences by not considering too short sequences, which often turn to be mutations, gene expression, etc. 

#### 6.4) Implementation of script to create BOWs

  - Link to the PR - [#10](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/10/files), [#13](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/13/files)
  - Overview -
    - Created `TfIdf_BOW_creator.py` script (formerly known as csv_reader.py) that uses manual curations made in the CSV (output by `oligo_extract.py` file) to generate two BOWs using the TF-IDF technique. One comprises words corresponding to oligo sequences, and another comprises words corresponding to non-oligo sequences. 

#### 6.5) Implementation of script to use BOWs for auto-labelling/curating sentences as True positive or False positive oligonucleotide sequences

  - Link to the PR - [#12](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/12/files), [#15](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/15/files)
  - Overview -
    - Created the `TfIdf_BOW_TpFp.py` script that works along with the `oligo_extract.py` script. `TfIdf_BOW_TpFp.py` script gets each sentence (of the extracted text) as an input from the `oligo_extract.py` script and uses BOWs (generated by the `TfIdf_BOW_creator.py` script) for auto-labelling/curating sentences as True positive or False positive oligonucleotide sequences.  
    
#### 6.6) Optimizing system's code to get input from user at a single place 

  - Link to the PR - [#16](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/16/files)
  - Overview -
     - Created `configure.py` script so that the user needs to input all arguments/variables at a single place and just for a single time unless needed to be changed. This reduces the extra hassle of passing inputs in the command line while running some file, which often gets skipped from the user's mind. 
     - Made corresponding changes in files like `oligo_extract.py` (it needs ids of papers in the Wormbase database from which the user wants to churn out oligo sequences and related data, and then it outputs this extracted data in the form of a CSV file in the location defined in `configure.py` file. It also needs credentials present in `all_config.cfg` to access these papers from Wormbase), `TfIdf_BOW_creator.py` (it needs the path of the CSV output by `oligo_extract.py` as an input to output two BOWs in locations defined in `configure.py` file) and `TfIdf_BOW_TpFp.py` (it needs paths of the two BOWs output by `TfIdf_BOW_creator.py` as an input to auto-curate the CSV).
    
#### 6.7) Implementation of script to automate BOW expansion 

  - Link to the PR - [#18](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/18)
  - Overview -
    - Created `extract_BOW.py` script that will run BOW creator script, Oligo extraction script and True positive/False positive auto marking script one after another in a continuous manner till the time Oligo extraction script and BOW becomes so smart that the number of True positive oligo sequences is much higher than the number of False positive oligo sequences.
    - How does this cyclic pipeline work? Firstly, the curator manually labels the sentences using BOWs as True positive oligo sequences or False positive oligo sequences. This curation is turned into BOWs which then, in the second round of running the `extract_BOW.py` script, auto-tags the sentences in a column separate from the one which the curator marked in the first round. Then in this second round, the curator again manually marks newer sequences as true positive or false positive and also takes reference from the auto-tags (done by BOWs) for curating these newer sequences. Once curation is done, the `extract_BOW.py` script is run for the third time where again, BOWs (which got updated from curations of round 2) firstly auto-tags sequences and then curator manually tags and also take reference from sequences which BOWs have auto-tagged. 
    - This is how this cyclic pipeline controlled by running of `extract_BOW.py` script after every manual curation, helps to improvise BOWs to be used in the next cycle, tells how smart BOW has become and tells how many True positives have increased in the final corpus.

names in a separate new column of the same CSV, which is currently getting output from the `oligo_extract.py` script.

## 7) Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## 8) Acknowledgements

I thank Google Summer of Code and the Genome Assembly and Annotation section of EMBL-EBI for granting me this opportunity. I am grateful to my mentors, Magdalena Zarowiecki, Andrés Becerra Sandoval and Valerio Arnaboldi, for their continuous guidance and encouragement. Without them, this project would not have been possible. I thank them for their constant guidance, code reviews, timely feedback, and, most importantly, for their encouragement throughout GSoC.

I want to pay humble gratitude to my dearest mama (aka maternal uncle), Dr Nikhil Joshi, my parents and my sister for always believing in me and helping bring out the best of me right from the day of writing the proposal to this significant day of final submission. I am fortunate enough to get their support and encouragement throughout this summer. It was a great summer working on this project, and I would love to contribute more in the future to the EMBL-EBI.

## 9) License

Distributed under the MIT License. See ```LICENSE``` for more information.
