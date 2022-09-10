import pandas as pd
import nltk
from RawText.get_paper_content import get_paper_sentences_with_TE
from RegexRules.combine_rules import oligo_seq_regex, oligo_name_regex
from TP_FP_oligo.TfIdf_BOW_TpFp import check_true_positive_oligo_sentence

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
    skip_TP_FP - Variable with value "True" if CSV exists else "False"
    Returns:
    Panda dataframe consisting of IDs of research paper, oligos extracted (from each sentence), corresponding sentence
    and other related data
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
                                # if sentence in which oligos are present is a true positive oligo 
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
