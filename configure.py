import pandas as pd
import nltk
import sys
from os.path import exists
from configure import setConfiguration
from RawText.get_paper_content import get_paper_sentences_with_TE
from RegexRules.combine_rules import oligo_seq_regex, oligo_name_regex
from TP_FP_oligo.TfIdf_BOW_TpFp import check_true_positive_oligo_sentence
from TP_FP_oligo.TfIdf_BOW_creator import main_fn  

nltk.download("stopwords")
nltk.download("punkt")


def find_Oligos(config, paper_ids, skip_TP_FP):
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
    TP_FP_auto = list()
    TP_FP_manual = list()

    for i in range(len(paperid_sentence_list)):
            
            oligo_seq_output = oligo_seq_regex(paperid_sentence_list[i][1]) # paperid_sentence_list[i][1] means (i)^th element of list "paperid_sentence_list", then choosing first part of this element which is a sentence
            oligo_name_output = oligo_name_regex(oligo_seq_output, paperid_sentence_list[i][1])

            # run auto TP_FP feature only when BOW is present
            # i.e if CSV files exists and no matter curator has done re-curation or not, just do auto TP_FP tagging using BOW
            if skip_TP_FP=="False":
                true_positive_oligo_sentence = check_true_positive_oligo_sentence(paperid_sentence_list[i][1])
            else:
                true_positive_oligo_sentence = None

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

                            TpFp_auto = ""
                            if true_positive_oligo_sentence=="oligo": 
                                # if sentence in which oligos are present is a true positive 
                                # oligo sentence
                                TpFp_auto = "true positive"
                            elif true_positive_oligo_sentence=="non-oligo":
                                TpFp_auto = "false positive"
                            else:
                                pass
                            TP_FP_auto.append(TpFp_auto)

                            TpFp_manual = ""
                            TP_FP_manual.append(TpFp_manual)

                            
    final = {'WBPaperID': WBPaperID, 'Oligo': Oligo, 'Prev Sentence': Prev_Sentence, 'Current Sentence': Current_Sentence, 'Next Sentence': Next_Sentence, 'Oligos per Sentence': Number_of_Oligos, 'TP or FP Oligo (auto)': TP_FP_auto, 'TP or FP Oligo (manual)':TP_FP_manual}
    return pd.DataFrame(final)


if __name__ == "__main__":

    config, paper_ids, output_CSVname, _, _ = setConfiguration()

#     paper_ids = ["WBPaper00003663", "WBPaper00003632", "WBPaper00003021", "WBPaper00005504", "WBPaper00030754", "WBPaper00005177", "WBPaper00004282", "WBPaper00003566", "WBPaper00001366", "WBPaper00004943", "WBPaper00002207", "WBPaper00001691", "WBPaper00003989", "WBPaper00003632", "WBPaper00044537", "WBPaper00050743", "WBPaper00001872", "WBPaper00005135", "WBPaper00000779", "WBPaper00025193", "WBPaper00005533", "WBPaper00001366", "WBPaper00002207", "WBPaper00001691",
# "WBPaper00050123",
# "WBPaper00002034",
# "WBPaper00000779",
# "WBPaper00006439",
# "WBPaper00025193",
# "WBPaper00005533",
# "WBPaper00003989",
# "WBPaper00002034",
# "WBPaper00001677",
# "WBPaper00005504",
# "WBPaper00004503",
# "WBPaper00001835",
# "WBPaper00004282",
# "WBPaper00003663",
# "WBPaper00002207",
# "WBPaper00001691",
# "WBPaper00003632",
# "WBPaper00051175",
# "WBPaper00004275",
# "WBPaper00002034",
# "WBPaper00000779",
# "WBPaper00030754",
# "WBPaper00005504",
# "WBPaper00001835"]

    # if CSV files exists, then create a new BOW using that CSV, and just do auto TP_FP tagging using BOW
    skip_TP_FP = "True" # by default dont create BOW
    file_exists = exists(output_CSVname)
    print(file_exists)
    if file_exists:
        # here BOW will be empty if 'TP or FP Oligo (manual)' column will be empty (i.e curator has not done manual tagging).
        # thus for the first cycle BOW will be only created if curator has done manual tagging (because BOW is formed by curator's manual tagging only)
        main_fn() 
        skip_TP_FP = "False"
    elif not file_exists:
        skip_TP_FP = "True"

    df = find_Oligos(config, paper_ids, skip_TP_FP)

    # try:
    #     output_filename = sys.argv[1] # ex: oligos.csv
    # except:
    #     output_filename = "oligos.csv"

    df.to_csv(output_CSVname, index=False)
