import nltk
from textpresso import textpresso_paper_text
import re

def get_paper_sentences_with_TE(config, paper_ids):
    """
    Functionality:
    Takes WB Paper IDs, returns a pair of paperid-sentence, after extracting from the papers

    Arg:
    paper_ids - List of wb papers ids e.g. ['WBPaper00002379']
    config - Variable having texpresso token

    Returns:
    paperid_sentence_list: List of paper ID and sentence e.g. [['WBPaper00002379', 'First sentence'],
        ['WBPaper00002379', 'Second sentence'], ....]
    """

    # Creates a list of commonly found stop words
    stop_words = set(nltk.corpus.stopwords.words("english"))
    stop_words = [w for w in stop_words if len(w) > 1]

    # Gets text from wb paper(s) using "textpresso_paper_text" and 
    # stores it in "txt" variable

    textpresso_token = config["textpresso"]["token"]
    paperid_sentence_list = []
    for id in paper_ids:
        txt = textpresso_paper_text(id, textpresso_token)
        #txt = textpresso_paper_text(id)
        count_total_rows = len(txt)

        for current_i, row in enumerate(txt):
            if any(
                    word in row.lower().split() for word in ("literature", "cited",
                    "supported", "references", "thank", "acknowledge", 
                    "acknowledgments", "thank", "contributions")  
            ):
                if current_i > count_total_rows / 3:
                    break

            # Remove sentence if number of characters (not words) are less 
            # than 40 or there is only 1 word in "row"
            if len(row) < 40 or len(row.split()) == 1:
                continue

            # Cleans stop words from current sentence
            clean_row = ""
            word_bank = row.split()
            for word in word_bank:
                if word.lower() not in stop_words:
                    clean_row+=word+" "

            # Remove sentence with links and email ids 
            # Here "|" means "or"
            if (re.search("\S+@\S+\.\S+|https:\/\/|www.", clean_row)):
                continue

            paperid_sentence_list.append((id, clean_row))

    return paperid_sentence_list
