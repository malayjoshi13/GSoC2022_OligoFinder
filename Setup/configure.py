import configparser

def setConfiguration():
    
    db_config = configparser.ConfigParser()
    db_config.read('all_config.cfg')
    
    paper_ids = ["WBPaper00003663",
                "WBPaper00003632", 
                "WBPaper00003021", 
                "WBPaper00005504", 
                "WBPaper00030754", 
                "WBPaper00005177", 
                "WBPaper00004282", 
                "WBPaper00003566", 
                "WBPaper00001366", 
                "WBPaper00004943", 
                "WBPaper00002207", 
                "WBPaper00001691", 
                "WBPaper00003989", 
                "WBPaper00003632", 
                "WBPaper00044537", 
                "WBPaper00050743", 
                "WBPaper00001872", 
                "WBPaper00005135", 
                "WBPaper00000779", 
                "WBPaper00025193", 
                "WBPaper00005533", 
                "WBPaper00001366", 
                "WBPaper00002207", 
                "WBPaper00001691",
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

    output_CSVname = "oligos.csv"

    oligo_BOW_filename = "oligo_BOW.txt"
    non_oligo_BOW_filename = "non_oligo_BOW.txt"

    return db_config, paper_ids, output_CSVname, oligo_BOW_filename, non_oligo_BOW_filename
