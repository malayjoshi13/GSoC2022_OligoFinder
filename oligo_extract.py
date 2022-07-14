import pandas as pd
from configure import setConfiguration
from get_paper_content import get_paper_sentences_with_TE
from bw_brackets import pick_from_brackets
from combine_oligo_parts import is_part
from check_alpha_num_specialchk import has_acgt, has_35, remove_special_characters
import nltk
nltk.download("stopwords")
nltk.download("punkt")

# TGAATTGATTCCAACGCCTC;pkP400
# ACGATGTGACG;pkP406.2,CAGTACTTCCCACGTCGT- CATC  
    
def oligo_regex(row):
    """
    Functionality:
    Pick each "word" of a sentence/"row", extracts oligo if present inside brackets,
    then check if "word" is an oligo by checking if it has only characters of
    a,c,g,t,p,A,C,G,T,P,3, 5 and ' .     
    If "word" is an oligo, then "oligo_name" stores that oligo in "oligo_name" variable, 
    else stores "None" in "oligo_name" variable

    Then append the extracted and processed "oligo_name" into "int_result" list.
    This list is then passed to "is_part" function which clubs oligo names which are part of 
    each other and returns list of final names of oligos present in a "row"

    Arg:
    row - sentence out of a big set of sentences extracted from research paper(s)

    Returns:
    processed_sentence - list of names of oligos (referred as "oligo_name")
                         extracted from each "row" 
    """

    int_result = list()
    for word in row.split():
        oligo_name = pick_from_brackets(word)
        oligo_name = has_acgt(oligo_name)
        oligo_name = has_35(oligo_name)
        oligo_name = remove_special_characters(oligo_name)
        int_result.append(oligo_name)  

    processed_sentence = is_part(int_result)
    return processed_sentence

#................................................................

def find_Oligos(config, paper_ids):
    """
    Functionality:
    Compile extracted oligos (from research paper(s)), alongwith paper id and sentence
    (from which oligo is extracted) into Panda dataframe

    Arg:
    paper_ids - List of wb papers ids e.g. ['WBPaper00002379']
    config - Dictionary with db_config properties and texpresso token

    Returns:
    Panda dataframe consisting of IDs of research paper, oligos extracted (from each sentence) and corresponding sentence
    """

    paperid_sentence_list = get_paper_sentences_with_TE(config, paper_ids)

    WBPaperID = list()
    Oligo = list()
    Sentence = list()
    for row in paperid_sentence_list:
            final_output = oligo_regex(row[1])
            for output in final_output:
                if output:
                    WBPaperID.append(row[0])
                    Oligo.append(output)
                    Sentence.append(row[1])

    final = {'WBPaperID': WBPaperID, 'Oligo': Oligo, 'Sentence': Sentence}
    return pd.DataFrame(final)


if __name__ == "__main__":
    config = setConfiguration()
    paper_ids = ["WBPaper00002627"]
    df = find_Oligos(config, paper_ids)
    df.to_csv('oligos.csv', index=False)