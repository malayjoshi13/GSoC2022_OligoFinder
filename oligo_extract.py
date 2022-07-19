import pandas as pd
from configure import setConfiguration
from get_paper_content import get_paper_sentences_with_TE
from regex_extraction import oligo_seq_regex, oligo_name_regex
import nltk
nltk.download("stopwords")
nltk.download("punkt")

# TGAATTGATTCCAACGCCTC;pkP400
# ACGATGTGACG;pkP406.2,CAGTACTTCCCACGTCGT- CATC  
    


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

    for i in range(len(paperid_sentence_list)):
            
            oligo_seq_output = oligo_seq_regex(paperid_sentence_list[i][1]) # paperid_sentence_list[i][1] means (i)^th element of list "paperid_sentence_list", then choosing first part of this element which is a sentence
            oligo_name_output = oligo_name_regex(oligo_seq_output, paperid_sentence_list[i][1])
            
            for output in oligo_seq_output:
                    WBPaperID.append(paperid_sentence_list[i][0]) # paperid_sentence_list[i][1] means (i)^th element of list "paperid_sentence_list", then choosing first part of this element which is a paper id
                   
                    Oligo.append(output)

                    Oligo_name.append(oligo_name_output[output])
                    
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

    final = {'WBPaperID': WBPaperID, 'Oligo': Oligo, 'Oligo Name': Oligo_name, 'Prev Sentence': Prev_Sentence, 'Current Sentence': Current_Sentence, 'Next Sentence': Next_Sentence, 'Oligos per Sentence': Number_of_Oligos}
    return pd.DataFrame(final)


if __name__ == "__main__":
    config = setConfiguration()
    paper_ids = ['WBPaper00002627', 'WBPaper00029073', 'WBPaper00031335', 'WBPaper00030973', 'WBPaper00028727',
'WBPaper00045317', 'WBPaper00036201', 'WBPaper00003815', 'WBPaper00049625', 'WBPaper00035548', 'WBPaper00001234',
'WBPaper00005783', 'WBPaper00045258', 'WBPaper00046820', 'WBPaper00002018', 'WBPaper00003969', 'WBPaper00046810',
'WBPaper00024569', 'WBPaper00027336', 'WBPaper00005045', 'WBPaper00002379', 'WBPaper00047026', 'WBPaper00045803',
'WBPaper00036086', 'WBPaper00041308', 'WBPaper00002121', 'WBPaper00031871', 'WBPaper00004181', 'WBPaper00024331',
'WBPaper00006107', 'WBPaper00026736', 'WBPaper00028462', 'WBPaper00005275', 'WBPaper00035150', 'WBPaper00005276',
'WBPaper00005955', 'WBPaper00006135', 'WBPaper00050677', 'WBPaper00005096', 'WBPaper00001768', 'WBPaper00038214',
'WBPaper00036384', 'WBPaper00041364', 'WBPaper00044057',
'WBPaper00032087',
'WBPaper00004985',
'WBPaper00031858',
'WBPaper00006052',
'WBPaper00026908',
'WBPaper00029143',
'WBPaper00002004',
'WBPaper00003021',
'WBPaper00048712',
'WBPaper00001677',
'WBPaper00005504',
'WBPaper00030754',
'WBPaper00004503',
'WBPaper00001835',
'WBPaper00030864',
'WBPaper00005177',
'WBPaper00004282',
'WBPaper00027748',
'WBPaper00003663',
'WBPaper00003566',
'WBPaper00001366',
'WBPaper00004943',
'WBPaper00027659',
'WBPaper00002207',
'WBPaper00001691',
'WBPaper00036485',
'WBPaper00049977',
'WBPaper00003989',
'WBPaper00032509',
'WBPaper00003632',
'WBPaper00003350',
'WBPaper00044537',
'WBPaper00048884',
'WBPaper00050743',
'WBPaper00050123',
'WBPaper00051175',
'WBPaper00051394',
'WBPaper00001872',
'WBPaper00003757',
'WBPaper00004275',
'WBPaper00004442',
'WBPaper00002034',
'WBPaper00005135',
'WBPaper00000779',
'WBPaper00005374',
'WBPaper00005208',
'WBPaper00005198',
'WBPaper00005233',
'WBPaper00045172',
'WBPaper00041467',
'WBPaper00006439',
'WBPaper00025193',
'WBPaper00001075',
'WBPaper00005533',
'WBPaper00040140',
'WBPaper00006391']

    df = find_Oligos(config, paper_ids)
    df.to_csv('oligoss.csv', index=False)
