# OligoFinder: RegEx and Machine Learning based system for finding and extracting Oligonucleotides mentions from biomedical research papers

> ## Made during Google Summer of Code 2022 for Genome Assembly and Annotation section of EMBL-EBI

![pic](https://user-images.githubusercontent.com/71775151/188505676-b48bbcb4-ef1f-42bf-be05-fcd3223370aa.jpg)
 
- **Mentors**: [Magdalena Zarowiecki](https://github.com/MagdalenaZZ), [Andrés Becerra Sandoval](https://github.com/abecerra), [Valerio Arnaboldi
](https://github.com/valearna) 
- **Project Category**: [Extract important information from scientific papers](https://summerofcode.withgoogle.com/programs/2022/projects/5b96vIqa)

## Table of Contents

- [Background](#1-background)
- [Objective](#2-objective-of-oligoFinder)
- [Work overview](#3-work-overview) 
- [Folder Directory Structure](#4-folder-directory-structure)
- [Usage](#5-usage)
- [Data Flow Diagram](#6-data-flow-diagram)
- [Future work](#7-future-work)
- [Contributing](#8-contributing)
- [Acknowledgements](#9-acknowledgements)
- [License](#10-license)

## 1) Background

Our genetic information is stored in a repeating sequence of nucleotides, abbreviated by the letters A, C, G, T in DNA, and A, C, G, U in RNA. Oligonucleotides are short DNA or RNA oligomers between 20 and 60 units in length. However, they rarely exceed 200 nucleotides. They can be synthesized or found naturally as single-stranded (ss) or double-stranded (ds) fragments of DNA or RNA. Oligonucleotides (or oligos) have many uses, from research to disease diagnosis and, recently therapeutics.

The last few decades have witnessed an explosion of knowledge in molecular biology. It is increasingly evident that evolution has generated an astonishingly complex set of interconnected processes through which gene expression can be regulated. One such process that has evolved due to wide availability of inexpensive synthetic single-stranded DNA and RNA is routine DNA amplification by PCR primers. It has revolutionized the study of gene expression and disease processes via a range of processes, including RNAi, target degradation by RNase H-mediated cleavage, splicing modulation, non-coding RNA inhibition, gene activation and programmed gene editing. In addition to the use of Oligonucleotides as PCR primers, they are also used as probes, in microarray, in situ hybridization, antisense analyses, and even as drug carriers.

Such new findings about varied applications of Oligonucleotides typically first appear in the scientific literature and is then later manually curated into biomedical databases, such as [WormBase](https://wormbase.org//#012-34-5) where the information is presented in a standardized, queryable format. This process of manual curation by identifying and extracting Oligonucleotides is expensive, time-consuming, captures a small part of the relevant literature and therefore is a significant challenge in advancing precision medicine and gene expression.

Another curation method is automated information extraction, which uses text mining and biomedical natural language processing (aka BioNLP) techniques to assist in acquiring and managing this knowledge. However, it is found that previous efforts/developments in biomedical automated text mining have focused primarily upon named entity recognition of well-defined molecular objects such as genetic variations and mutations. Less work has been performed to identify entities like oligonucleotides, which in recent years have become crucial in biomedical research and practical applications. Another limitation of this method is its inability to efficiently scale to minimize manual efforts and still curate a constantly expanding corpus of literature with high accuracy.

## 2) Objective of OligoFinder

To solve the above-stated problem, we present an accurate, efficient, scalable and fully/semi-automated system called **OligoFinder** for identifying and extracting **oligonucleotide mentions** along with related data from Biomedical research paper(s). 

This extracted data will be stored in databases like WormBase from where Biomedical researchers will query and search for a specific oligonucleotide sequence to understand in which research paper is that oligonucleotide been used, the type of experiment in which that particular oligonucleotide sequence is used, the target used in that experiment along with that particular oligonucleotide and to study the structure of that particular oligonucleotide. 

![dd](https://user-images.githubusercontent.com/71775151/189496178-6023f3b4-e67a-4251-9187-c874df88b1bc.png)

The objectives for this system are:-

### Phase 1

- designing, training and getting inference from **regex based pipeline for extracting oligonucleotide mentions** (oligonucleotide sequences and corresponding names) from research papers and placing in a CSV format file.

- building, training and getting inference from **pipeline for filtering out false positive oligonucleotide mentions**. Its need arose as many extracted sequences follow structural patterns of an oligonucleotide but were actually gene expressions, mutations, variations, etc. Thus to further filter out false positives generated by Regex based oligonucleotide mentions and oligonucleotide names extraction pipeline, we need such tagging/curation system. 
  
    This objective is further sub-divided into:-
   - developing **CSV based pipeline to allow easy manual curation** of extracted sequences to be true or false positive oligonucleotide mentions by taking into account previous manually curated tags and relevant auto-tags (discussed below) of sequences being true positive or false positive.
   - developing **BOW based pipeline to auto-curate extracted sequences** to be True positive oligonucleotide mentions or False positive oligonucleotide mentions. This pipeline will also reduce efforts to manual curate sequences as TP or FP. 
     To keep improving this pipeline, a **pipeline for automatic advancement/improvisation of BOWs** needs to be developed. This pipeline will use manual curations done by curator on the CSV file to extend number of words in the existing BOWs.

- designing a **matrix for analysing the performance of regex based pipeline for extracting oligonucleotide mentions and Bag of Words based false positive filtering system** in each cycle/round of training these both systems over multiple training research papers.

### Expected Results
By end of Phase 1, training of **regex based pipeline for extracting oligonucleotide mentions** and **pipeline for filtering out false positive oligonucleotide mentions** will be completed. Then we will use these pipelines to prepare training data to train BioBERT model in Phase 2.

### Phase 2
- training BioBERT model on dataset of oligonucleotide mentions prepared by use of **regex based pipeline for extracting oligonucleotide mentions** and **pipeline for filtering out false positive oligonucleotide mentions**. OligoFinder system in addition to regex-based oligonucleotide mentions extraction pipeline, also needs BioBERT based extraction pipeline to cover wider range of sequences which don't follow a particular fixed patter to be captured by regex rules of OligoFinder.

### Expected Results
By end of Phase 2, training of **BioBERT based pipeline for extracting oligonucleotide mentions** will be completed. This pipeline alng with above two pipelines will be the three pillars of **OligoFinder system**.

### Phase 3
- preparing a **high-quality golden standard dataset of oligonucleotide mentions** using:-
   -  **regex based pipeline for extracting oligonucleotide mentions,**
   -  **pipeline for filtering out false positive oligonucleotide mentions,**
   -  **BioBERT based pipeline for extracting oligonucleotide mentions**
   
### Expected Results 
By end of Phase 3, standard dataset containing oligonucleotide mentions will be prepared and stored in databases like WormBase. Then it will be used by Biomedical researchers to take reference for use of specific oligonucleotide in experiments and to validate the performance of future developments of oligonucleotide extraction systems.

## 3) Work overview

During GSoC 2022, under the guidance of mentors, I successfully completed the major portion of Phase 1. Please note that many modifications made in the features of this system were directly committed to the main branch as they are well tested and hold more straightforward logic and code blocks. Developments and modifications made in the significant features of this system were committed in the form of Pull Requests (PRs), which you can view below.

#### 3.1) Implementation of pipeline to extract text from research papers
  - Directly commited to the main branch
  - Overview -
    - Created `get_paper_content.py` script, which via `textpresso.py` script extracts content from a research paper(s) in Wormbase corresponding to id(s) present in the `configure.py` file.

#### 3.2) Implementation of RegEx rules (present inside `RegexRules`) folder for extracting sequences following structure of Oligonucletides

  - Link to the PR - [#4](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/4), [#5](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/5), [#6](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/6/files)
  - Overview -
    - Created Regex rules `bw_brackets.py`, `check_alpha_num_specialchk.py`, `combine_oligo_parts.py`, `combine_rules.py` (earlier named as regex_extraction.py) 
    - Created `oligo_extract.py` script, which gets a text from a research paper(s), extracts sequences similar in structure to Oligonucleotide and returns data in a CSV format.

#### 3.3) Optimizing RegEx rules (present inside `RegexRules`) folder that extracts sequences following structure of Oligonucletides

  - Link to the PR - [#8](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/8/files), [#11](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/11/files)
  - Overview -
    - Optimized the logic used in `combine_oligo_parts.py` and `combine_rules.py` (earlier named regex_extraction.py) scripts to resolve the issue of incomplete extracted sequences.
    - Optimized the logic used in `combine_oligo_parts.py` `combine_rules.py` (earlier named regex_extraction.py) scripts to bring down False Positive sequences by not considering too short sequences, which often turn to be mutations, gene expression, etc. 

#### 3.4) Implementation of script to create BOWs

  - Link to the PR - [#10](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/10/files), [#13](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/13/files)
  - Overview -
    - Created `TfIdf_BOW_creator.py` script (formerly known as csv_reader.py) that uses manual curations made in the CSV (output by `oligo_extract.py` file) to generate two BOWs using the TF-IDF technique. One comprises words corresponding to oligo sequences, and another comprises words corresponding to non-oligo sequences. 

#### 3.5) Implementation of script to use BOWs for auto-labelling/curating sentences as True positive or False positive oligonucleotide sequences

  - Link to the PR - [#12](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/12/files), [#15](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/15/files)
  - Overview -
    - Created the `TfIdf_BOW_TpFp.py` script that works along with the `oligo_extract.py` script. `TfIdf_BOW_TpFp.py` script gets each sentence (of the extracted text) as an input from the `oligo_extract.py` script and uses BOWs (generated by the `TfIdf_BOW_creator.py` script) for auto-labelling/curating sentences as True positive or False positive oligonucleotide sequences.  
    
#### 3.6) Optimizing system's code to get input from user at a single place 

  - Link to the PR - [#16](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/16/files)
  - Overview -
     - Created `configure.py` script so that the user needs to input all arguments/variables at a single place and just for a single time unless needed to be changed. This reduces the extra hassle of passing inputs in the command line while running some file, which often gets skipped from the user's mind. 
     - Made corresponding changes in files like `oligo_extract.py` (it needs ids of papers in the Wormbase database from which the user wants to churn out oligo sequences and related data, and then it outputs this extracted data in the form of a CSV file in the location defined in `configure.py` file. It also needs credentials present in `all_config.cfg` to access these papers from Wormbase), `TfIdf_BOW_creator.py` (it needs the path of the CSV output by `oligo_extract.py` as an input to output two BOWs in locations defined in `configure.py` file) and `TfIdf_BOW_TpFp.py` (it needs paths of the two BOWs output by `TfIdf_BOW_creator.py` as an input to auto-curate the CSV).
    
#### 3.7) Implementation of script to automate BOW expansion 

  - Link to the PR - [#18](https://github.com/malayjoshi13/GSoC2022_OligoFinder/pull/18)
  - Overview -
    - Created `extraction_and_BOW.py` (formerly extract_BOW.py) script that will run BOW creator script, Oligo extraction script and True positive/False positive auto marking script one after another in a continuous manner till the time Oligo extraction script and BOW becomes so smart that the number of True positive oligo sequences is much higher than the number of False positive oligo sequences.
    - How does this cyclic pipeline work? Firstly, the curator manually labels the sentences using BOWs as True positive oligo sequences or False positive oligo sequences. This curation is turned into BOWs which then, in the second round of running the `extraction_and_BOW.py` script, auto-tags the sentences in a column separate from the one which the curator marked in the first round. Then in this second round, the curator again manually marks newer sequences as true positive or false positive and also takes reference from the auto-tags (done by BOWs) for curating these newer sequences. Once curation is done, the `extraction_and_BOW.py` script is run for the third time where again, BOWs (which got updated from curations of round 2) firstly auto-tags sequences and then curator manually tags and also take reference from sequences which BOWs have auto-tagged. 
    - This is how this cyclic pipeline controlled by running of `extraction_and_BOW.py` script after every manual curation, helps to improvise BOWs to be used in the next cycle, tells how smart BOW has become and tells how many True positives have increased in the final corpus.

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
├── oligo_extract.py 
│
│
├── TP_FP_oligo/
│   ├── TfIdf_BOW_TpFp.py
│   ├── TfIdf_BOW_creator.py
│   └── sentence_processor.py
│ 
│
├── extraction_and_BOW.py
│ 
│
├── LICENSE
│ 
│
└── README.md
```

#### 4.1) Part of system for setting up work/deployment/test environment

- `Setup` - stores the` config_readme.md` file containing credentials to access research papers from the Wormbase database via Textpresso and the `requirements.txt` file for setting up the development environment.

- `configure.py` - comprise of following parameters:-
  
  - `paper_ids` - from this parameter, user can add research paper ids (present in Wormbase) from which they want to extract oligonucleotide mentions,     
  - `output_CSVname` - from this parameter, the user can change the location of the CSV containing extracted oligonucleotide mention along with other related objects. This file is output by `oligo_extract.py` and is input for `TfIdf_BOW_creator.py`,
  
  - `oligo_BOW_filename` and `non_oligo_BOW_filename` - from this parameter user can change location of txt files containing BOW related to oligonucleotide and non-oligonucleotide mentions respectively. These files are output by `TfIdf_BOW_creator.py` and input for `TfIdf_BOW_TpFp.py` file

#### 4.2) Part of system for getting text from research paper(s)

- `RawText` - stores `textpresso.py` and `get_paper_content.py` files that extract content from research papers in the Wormbase database corresponding to their id mentioned in the `paper_ids` parameter of the `configure.py` file and returns a pair of paper id-sentence.

#### 4.3) Part of system having RegEx rules to extract sequences that follow structure of Oligonucleotides

- `bw_brackets.py` - contain RegEx rule `pick_from_brackets` that extracts Oligonucleotide sequence if present inside brackets. Input: insert(TGAGACGTCAACAATATGG)hg, Output: TGAGACGTCAACAATATGG.

- `check_alpha_num_specialchk.py` - contain three RegEx rules: 
  - `has_acgt` - this RegEx rule checks if the input word follows the structure of an Oligonucleotide or not. If the input word contains only alphabetic characters like A, a, C, c, G, g, T and T, then that word follows the structure of an Oligonucleotide; otherwise not. Input1: TGAGACGTCAACAATATGG, Output1: TGAGACGTCAACAATATGG and Input2: TXxvFDECAAOpJHTGG, Outpu2: None.
  -  `has_35` - this RegEx rule checks if the input word follows the structure of an Oligonucleotide or not. If the input word contains only numeric characters like 3 and 5 or does not have any numeric characters, then that word follows the structure of an Oligonucleotide; otherwise not. Input1: 3'-TGAGACGTCAACAATATGG-5', Output1: 3'-TGAGACGTCAACAATATGG-5' and Input2: TGAGACGTCAACAATATGG, Outpu2: TGAGACGTCAACAATATGG and Input3: 3'-TGAGA2CGT3CAACAATATG675G-5', Output3: None. 
  -  `remove_special_characters` - except alphabetic characters ranging from A to Z and a to z, remove every other character from the input word like numeric values (3, 5, etc.), special characters (,./?"':}{][, etc) and extra spacings.

- `combine_oligo_parts.py` - contain two RegEx rules:
  - `is_part` - this RegEx rule combines back Oligonucleotide sequences that are actually part of a single oligo sequence but are treated like individual oligo sequences due to spaces, newline, etc. Input: TT GCA ATG CGAAAATAC, Output: TTGCAATGCGAAAATAC.
  - `only_regex` - outputs a list of words that satisfies all structural rules of an Oligonucleotide and thus are called 'sequences' from now onwards.
  
- `combine_rules.py` - contain two RegEx rules:
  - `word_processor` - pass input word through four RegEx rules namely `pick_from_brackets`, `has_acgt`, `has_35`and `remove_special_characters` (all four mentioned above), and returns the ouput processed word.
  - `oligo_seq_regex` - output of `word_processor` rule becomes input for this which is passed to two RegEx rules namely `is_part` and `only_regex`. The output from this is a sequence that follows an Oligonucleotide's structural composition.

- `oligo_extract.py` - compiles extracted oligos (from research paper(s)), along with paper id, auto & manual true positive/false positive tags, previous, current (from which oligo sequence is extracted) & future sentences into a Pandas data frame which is saved as a CSV file.

#### 4.4) Part of system for creation and usage of BOWs 
- `TfIdf_BOW_creator.py` - uses 'TP or FP Oligo (manual)' column of CSV generated above (which has manual curations + auto curations which curator felt to be right) to generate two Bag of Words (BOW) having higher TF-IDF scores. 

  - First BOW has words related to sentences that have tag of containing "oligo" in the 'TP or FP Oligo (manual)' column. Second BOW has words related to sentences that have tag of containing "non-oligo", "other", "mutation", etc in the 'TP or FP Oligo (manual)' column of CSV genertaed.

- `TfIdf_BOW_TpFp.py` - uses BOWs generated above to auto-curate sentences in the upcoming output CSV to be a TP oligo or FP oligo.

- `sentence_processor.py` - process the words and adds only english dictionary words in the BOWs.  

#### 4.5) Part of system that builds a cyclic pipeline between Oligo extraction script and Bag of Words (BOWs)
- `extraction_and_BOW.py` - script that will run BOW creator script, Oligo extraction script and True positive/False positive auto marking script one after another in a continous manner till the time Oligo extraction script and BOW becomes so smart that number of True positive oligo sequences is high as a pre-defined number.

## 5) Usage 

In order to train and get inference from **regex based pipeline for extracting oligonucleotide mentions** and **pipeline for filtering out false positive oligonucleotide mentions**, follow below listed steps:-

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

Now within `Setup` folder, go to `configure.py` and there user can perform following actions:

a) `paper_ids` - can add research paper ids present in Wormbase from which you wanr to extract oligonuclotide mentions. By default Wormbase ids of a set of `100 research papers` are taken for extracting oligonucleotides from them.

b) `output_CSVname` - can change location of CSV containing extracted oligonucleotide mentions along with other related objects. This file is output by `oligo_extract.py` and is input for `TfIdf_BOW_creator.py`. By default CSV of name `oligo_test.csv` will be created and accessed from the base directory location.

c) `oligo_BOW_filename` and `non_oligo_BOW_filename` - can change location of txt files containing BOW related to oligonucleotide and non-oligonucleotide mentions respectively. These files are output by `TfIdf_BOW_creator.py` file and input for `TfIdf_BOW_TpFp.py` file. By default BOWs named `oligo_BOW.txt` and `non_oligo_BOW.txt` will be created and accessed from the base directory location.

### 5.3) Execution

Extract oligonucleotides from research papers and use as well as enhance BOWs:

`cd ..`

`python extraction_and_BOW.py`

## 6) Data Flow Diagram

**Step 1)** After cloning this GitHub repository, as the user for the first time runs the command `python extraction_and_BOW.py` (by following steps in section 5 of `Usage`), a CSV file gets created. This file comprises data like WormBase ID, the previous sentence, the present sentence from which oligonucleotide sequences are extracted, the next sentence, and extracted oligonucleotide sequences. Along with these columns having the extracted data, one empty column of 'TP or FP Oligo (manual)' will also be created (this column will be used in step 2).

This data is extracted from research paper(s) by using the `oligo_extract.py` script. This script firstly extracts the whole text of the research paper(s) corresponding to WormBase ID(s) (input by the user), using `textpresso.py`. This text is broken down into multiple pairs of formats `WormBase ID of paper + each sentence of extracted text from paper`.

Then in the second step, the `oligo_extract.py` script uses the `combine_rules.py` script. This script directs the pairs formed in the above step to get input into the `bw_brackets.py` script, followed by `check_alpha_num_specialchk.py` script and then `combine_oligo_parts.py` script to extract oligonucleotide sequences and other related data. 

**Step 2)** Once CSV is created, the manual curator curates each row by labelling it as a `true positive` or `false positive` oligonucleotide sequence. 

This step is needed because regex rules present in our OligoFinder system can extract sequences that look like an oligonucleotide. However, some sequences that look like but are not oligonucleotide also get extracted a few times. Thus to make OligoFinder immune to such sequences, we are using the supervision of curators to differentiate between actual and false oligonucleotide sequences.

**Step 3)** This manually curated CSV generates two BOWs, one corresponding to words related to oligo sequences and the other corresponding to non-oligo sequences in sentences, by using the `TfIdf_BOW_creator.py` script.

**Step 4)** Now, when the user re-runs the command `python extraction_and_BOW.py` for the second time on some new research papers, then in the CSV file (which was created above), a new column of `TP or FP Oligo (auto)` will also be created comprising of auto labels of `true positive` or `false positive` oligonucleotide sequence.  

The `TfIdf_BOW_TpFp.py` script generates these auto labels by using two BOWs created above. The idea behind using BOWs to auto-label rows of CSV is that the pattern/words present in sentences containing oligos or non-oligos sequences will automatically differentiate between the actual oligonucleotide and pseudo oligonucleotide sequences. Therefore manual curation work reduces to semi-manual curation work by using BOWs. It happens by first taking them out and then using them for auto-labelling newly extracted sequences, as the presence of these unique words from BOWs directly points to whether a sequence is an oligo or not.

**Step 5)** Again curator will manually label extracted sequences as true positive or not. However, this time curator can take help from auto-labels to label new extracted sequences. Also, note that the curator needs to only curate/label just new extracted sequences, not already labelled ones, as old labels will remain the same.

This supervision of manual curation will be helpful in following ways:-
- manual curation + curator-verified auto-tags, by adding more words to the existing two BOWs will widen the scope to include every possible word related to an oligo/non-oligo sequence, thus will improvise BOWs to be used in the next cycle,
- comparison between auto-tags and manual tags in each cycle tells how smart BOW has become because the larger number of auto-taggings BOW can do, shows its improved performance,
- analysis of each cycle's manual tags tells how many True positives have increased due to better BOWs and oligo extraction script. It also tells where the oligo extraction script can be further improvised.

**Therefore**, this cyclic pipeline comprising of processes of extraction of oligonucleotide mentions from training research papers, then manual curation by curator and creation/extension of BOWs, followed by auto-curation by BOWs, is run multiple times. As a result, in the end, oligo extraction script and BOWs will become smart enough to produce a large corpus of True positive oligos for training BioBERT in the near future.

This trained BioBERT along with RegEx (which we are currently using) based oligo extraction script, will be used to extract high true positive oligonucleotide mentions out of any given inference research paper.

## 7) Future work

Lots of development and implementation, planned before the start of the GSoC'22 coding period, have been achieved. Continuing ahead, I and mentors of this project have proposed a few more features and pipelines to be added to this ambitious project to improvise it further. These proposed plans are as follows:
- optimizing RegEx rules to resolve over-joint sequences issue.
- creating a matrix to analyze at what rate True positive oligonucleotide sequences are increasing compared to total and False positive extracted oligonucleotide sequences. Such analysis indicates how much smarter oligo extraction script and BOWs have become after multiple rounds of running the `extraction_and_BOW.py` script along with manual + auto curation.
- to train the BioBERT model on a corpus of True positive oligonucleotides by using the self-training method. Using trained BioeBERT along with Regex rules will extract more True positive oligo mentions from research papers.
- creating a pipeline to find and output oligonucleotide names in a separate new column of the same CSV, which is currently getting output from the `oligo_extract.py` script.

## 8) Contributing

Contributions make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
- Fork the Project
- Create a branch for your feature (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push changes to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request
- Wait for us to validate before accepting it in our code base
- That is it. Wohooo🥳🥳🥳, you made a valuable commit to this project!!


## 9) Acknowledgements

I thank Google Summer of Code and the Genome Assembly and Annotation section of EMBL-EBI for granting me this opportunity. I am grateful to my mentors, Magdalena Zarowiecki, Andrés Becerra Sandoval and Valerio Arnaboldi, for their continuous guidance and encouragement. Without them, this project would not have been possible. I thank them for their constant guidance, code reviews, timely feedback, and, most importantly, for their encouragement throughout GSoC.

I want to pay humble gratitude to my dearest mama (aka maternal uncle), Dr Nikhil Joshi, my parents and my sister for always believing in me and helping bring out the best of me right from the day of writing the proposal to this significant day of final submission. I am fortunate enough to get their support and encouragement throughout this summer. It was a great summer working on this project, and I would love to contribute more in the future to the EMBL-EBI.

## 10) License

Distributed under the MIT License. See ```LICENSE``` for more information.
