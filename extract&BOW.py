from configure import setConfiguration
from TP_FP_oligo.TfIdf_BOW_creator import create_BOW

config, paper_ids, output_CSVname, _, _ = setConfiguration()

# if CSV files exists, then create a new BOW using that CSV, and just do auto TP_FP tagging using BOW
skip_TP_FP = "True" # by default dont create BOW
file_exists = exists(output_CSVname)

if file_exists:
    # here BOW will be empty if 'TP or FP Oligo (manual)' column will be empty (i.e curator has not done manual tagging).
    # thus for the first cycle BOW will be only created if curator has done manual tagging (because BOW is formed by curator's manual tagging only)
    create_BOW() 
    skip_TP_FP = "False"
elif not file_exists:
    skip_TP_FP = "True"

df = find_Oligos(config, paper_ids, skip_TP_FP)
df.to_csv(output_CSVname, index=False)