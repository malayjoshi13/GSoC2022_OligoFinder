from configure import setConfiguration
from TP_FP_oligo.TfIdf_BOW_creator import create_BOW
from oligo_extract import find_Oligos
from os.path import exists

if __name__ == "__main__":
    config, paper_ids, output_CSVname, _, _ = setConfiguration()

    skip_TP_FP = "True" # by default don't do auto TP/FP tagging
    file_exists = exists(output_CSVname)

    if file_exists:
        # if CSV exists but 'TP or FP Oligo (manual)' column of that CSV would not be empty (i.e curator has done manual tagging),
        # then non-empty BOW will be created.
        # but if CSV exists but 'TP or FP Oligo (manual)' column of that CSV would be empty (i.e curator has not done manual tagging),
        # then empty BOW will be created.
        create_BOW() 
        # once BOW will be created it will be used for auto-tagging.
        skip_TP_FP = "False"
    elif not file_exists:
        # if CSV don't exists, then BOW wil not be created, and thus no auto TP_FP tagging will happen
        skip_TP_FP = "True"

    df = find_Oligos(config, paper_ids, skip_TP_FP)
    df.to_csv(output_CSVname, index=False)
