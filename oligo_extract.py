import pandas as pd
import nltk
import sys
from configure import setConfiguration
from get_paper_content import get_paper_sentences_with_TE
from regex_extraction import oligo_seq_regex, oligo_name_regex
from TfIdf_BOW_TpFp import check_true_positive_oligo_sentence  
from os.path import exists

nltk.download("stopwords")
nltk.download("punkt")

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
    Current_Sentence = list()
    Prev_Sentence = list()
    Next_Sentence = list()
    Number_of_Oligos = list()
    Oligo_name = list()
    TP_FP = list()

    for i in range(len(paperid_sentence_list)):
            
            oligo_seq_output = oligo_seq_regex(paperid_sentence_list[i][1]) # paperid_sentence_list[i][1] means (i)^th element of list "paperid_sentence_list", then choosing first part of this element which is a sentence
            oligo_name_output = oligo_name_regex(oligo_seq_output, paperid_sentence_list[i][1])
            true_positive_oligo_sentence = check_true_positive_oligo_sentence(paperid_sentence_list[i][1])
            
            if oligo_seq_output: # continue further if current sentence (i.e paperid_sentence_list[i][1])
                                 # has some oligo sequences
                    for output in oligo_seq_output:
                            WBPaperID.append(paperid_sentence_list[i][0]) # paperid_sentence_list[i][1] means (i)^th element of list "paperid_sentence_list", then choosing first part of this element which is a paper id
                        
                            Oligo.append(output)

                            #Oligo_name.append(oligo_name_output[output])
                            
                            Current_Sentence.append(paperid_sentence_list[i][1]) # paperid_sentence_list[i][0] means (i)^th element of list "paperid_sentence_list", then choosing first part of this element which is a sentence
                            
                            try:
                                Prev_Sentence.append(paperid_sentence_list[i-1][1])
                            except:
                                Prev_Sentence.append("Nill")

                            try:
                                Next_Sentence.append(paperid_sentence_list[i+1][1])
                            except:
                                Next_Sentence.append("Nill")

                            Number_of_Oligos.append(len(oligo_seq_output))

                            TpFp = ""
                            if true_positive_oligo_sentence=="oligo": 
                                # if sentence in which oligos are present is a true positive 
                                # oligo sentence
                                TpFp = "true positive"
                            elif true_positive_oligo_sentence=="non-oligo":
                                TpFp = "false positive"
                            TP_FP.append(TpFp)
                   

    #final = {'WBPaperID': WBPaperID, 'Oligo': Oligo, 'Oligo Name': Oligo_name, 'Prev Sentence': Prev_Sentence, 'Current Sentence': Current_Sentence, 'Next Sentence': Next_Sentence, 'Oligos per Sentence': Number_of_Oligos}
    final = {'WBPaperID': WBPaperID, 'Oligo': Oligo, 'Prev Sentence': Prev_Sentence, 'Current Sentence': Current_Sentence, 'Next Sentence': Next_Sentence, 'Oligos per Sentence': Number_of_Oligos, 'Is this an oligo (auto)': TP_FP}
    return pd.DataFrame(final)


if __name__ == "__main__":
    config = setConfiguration()
    paper_ids = ["WBPaper00003663", "WBPaper00003632", "WBPaper00003021", "WBPaper00005504", "WBPaper00030754", "WBPaper00005177", "WBPaper00004282", "WBPaper00003566", "WBPaper00001366", "WBPaper00004943", "WBPaper00002207", "WBPaper00001691", "WBPaper00003989", "WBPaper00003632", "WBPaper00044537", "WBPaper00050743", "WBPaper00001872", "WBPaper00005135", "WBPaper00000779", "WBPaper00025193", "WBPaper00005533", "WBPaper00001366", "WBPaper00002207", "WBPaper00001691",
"WBPaper00050123",
"WBPaper00002034",
"WBPaper00000779",
"WBPaper00006439",
"WBPaper00025193",
"WBPaper00005533",
"WBPaper00003989",
"WBPaper00002034",
"WBPaper00001677",
"WBPaper00005504",
"WBPaper00004503",
"WBPaper00001835",
"WBPaper00004282",
"WBPaper00003663",
"WBPaper00002207",
"WBPaper00001691",
"WBPaper00003632",
"WBPaper00051175",
"WBPaper00004275",
"WBPaper00002034",
"WBPaper00000779",
"WBPaper00030754",
"WBPaper00005504",
"WBPaper00001835"]

    df = find_Oligos(config, paper_ids)

    try:
        output_filename = sys.argv[1] # ex: oligos.csv
    except:
        output_filename = "oligos.csv"

    df.to_csv(output_filename, index=False)
