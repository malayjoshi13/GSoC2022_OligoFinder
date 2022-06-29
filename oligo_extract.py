import numpy as np
import pandas as pd
from settings import setSettings
from textpresso import textpresso_paper_text
import re
import nltk
nltk.download("stopwords")
nltk.download("punkt")


def get_paper_sentences_with_TE(wbpids, settings):
    """
    Functionality:
    Takes WB Paper IDs, returns a list of sentences after extracting from the papers

    Arg:
    wbpids - List of wb papers ids e.g. ['WBPaper00002379']
    settings - Dictionary with db_config properties and texpresso token

    Returns:
    paperid_sentence_list: List of paper ID and sentence e.g. [['WBPaper00002379', 'First sentence'],
        ['WBPaper00002379', 'Second sentence'], ....]
    """
    # Creates a list of commonly found stop words
    stop_words = set(nltk.corpus.stopwords.words("english"))
    stop_words = [w for w in stop_words if len(w) > 1]

    # Gets text from wb paper(s) using "textpresso_paper_text" and 
    # stores it in "txt" variable
    textpresso_token = settings["db_config"]["textpresso"]["token"]
    paperid_sentence_list = []
    for id in wbpids:
        txt = textpresso_paper_text(id, textpresso_token)
        count_total_rows = len(txt)

        for current_i, row in enumerate(txt):
            # Limiting content inside "txt" variable to only "abstract"
            # and "main content" of paper not "reference" or 
            # "acknowledgments" sections, by checking if current row of
            # "txt" variable dont has any of the following things which 
            # is usually found in "reference" or "acknowledgments" sections
            # If it finds any of these words to be in the current "row",
            # it take it to reached the "reference" or "acknowledgments"
            # section and thus stops any further iteration through "rows"
            # of "txt" variable by using "break".
            # To avoid breaking/stopping process if these words comes in 
            # main content, it uses "current_i > count_total_rows / 3"
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

#................................................................

def fn1(word, final_output, part, output = None, last_output = None):
    """
    Functionality:
    Takes each word of each sentence.
    Firstly checks if that words has alphabets from a to z, like aaggctt, 3'aaggca5', icecream
    If it has alphabets, then it picks that portion having aplhabets (referred as "alpha"), like 
            alpha = aaggctt and alpha = aaggca and alpha = icecream
    Then it checks that "alpha" should be only made up of "a,c,g,t" alphabets (because "alpha" 
            corresponding to oligo only has these letters like alpha = aaggctt {corresponding to
            oligo "aaggctt"}, aaggca5 {corresponding to oligo "3'aaggca5'"})
    If "alpha" is only made up of "a,c,g,t" alphabets, then it checks "word" corresponding to the 
            "alpha" has numbers from 0 to 9. 
    If "word" corresponding to the "alpha" has numbers, then it checks that the numbers in "word"
            should be only 3 and 5 (because if oligos have numbers in addition to "a,c,g,t" alphabets
            , then those numbers are just 3 and 5 like "3'aaggca5'")
        If "word" corresponding to the "alpha" don't has numbers like "aaggctt", then we simply finalise 
        that "word" as "output". But considering "word" as "output" has further extension when "part" = True,
        where we add current "word" to previous "word" because we think that both are part of same oligo name
    If "word" has alphabets a,c,g,t and numbers 3,5 , then algo checks that the symbols in "word"
            should be only ' (because oligos those have numbers in addition to "a,c,g,t" alphabets
            only have either ' symbol or no symbol like "3'aaggca5'")    
        If "word" that has alphabets a,c,g,t and numbers 3,5, dont has any symbol like "aaggctt", then 
        we simply finalise that current "word" as "output" with extensions discussed above related to oligo part

    Arg:
    word - each word of each sentence one at a time
    final_output - list where all "output" are present
    part - discussed completly in "fn1()"

    Returns:
    output - gets value from "fn1". For "word" which is oligo like "word" = TTCGA, the "output" = TTCGA.
             For "word" which is not an oligo like "word" = Apple, the "output" = None.
    last_output - gets value from "fn1" by storing "output" corresponding to "word" which is previous to the current "word"
    """

    if re.search("[a-z]+", word, re.IGNORECASE):
        alpha = re.search("[a-z]+", word, re.IGNORECASE).group()
        # If word = C-terminal, then alpha = C
        # This alpha satisfies all conditions even though its not oligo
        # To avoid it, we use conditions len(wordd)>3 and len(wordd)<95
        if re.search("[^atcg]", alpha, re.IGNORECASE) == None and len(alpha)>3 and len(alpha)<95:

            if re.search("[0-9]+", word, re.IGNORECASE):
                num = re.search("[0-9]+", word, re.IGNORECASE).group()
                if re.search("[3,5]", num, re.IGNORECASE):
                    
                    if re.search("[^A-Za-z0-9]", word, re.IGNORECASE):
                        sign = re.search("[^A-Za-z0-9]", word, re.IGNORECASE).group()
                        if re.search("\'", sign, re.IGNORECASE):
                            if part:
                                output = str(final_output[-1])+str(word)
                                if output:
                                    last_output = output
                            else:
                                output = word
                                if output:
                                    last_output = output 

                    else:
                        if part:
                            output = str(final_output[-1])+str(word)
                            if output:
                                last_output = output
                        else:
                            output = word
                            if output:
                                last_output = output 

            else: 
                if part:
                    output = str(final_output[-1])+str(word)
                    if output:
                        last_output = output
                else:
                    output = word
                    if output:
                        last_output = output                    

    return(output, last_output)

#................................................................

def fn2(word, final_output, part, output = None, last_output = None):
    """
    Functionality:
    Takes each word of each sentence, then checks if that words has ().
    As for words like insert(TGAGACGTCAACAATATGG), insert(TGAGACGTCAACAATATGG, insert(TGAGACGTCAACAATATGG)hg, 
    (TGAGACGTCAACAATATGG)hg and TGAGACGTCAACAATATGG)hg, have the oligo name "TGAGACGTCAACAATATGG" enclosed
    within ().
    Thus it's important to identify words with (), and then extract out oligo name from in b/w () referred as 
    "in_between_word".

    Arg:
    word - each word of each sentence one at a time
    final_output - list where all "output" are present
    part - if True means "word" is actually part of previous "word"
           if False means "word" is not actually part of previous "word"
           ex1: if previous "word" = TTCGA and "word" = GCCAT
                and "part" = True, then TTCGA and GCCAT are single word, i.e TTCGAGCCAT
           ex2: if previous "word" = TTCGA and "word" = GCCAT
                and "part" = False, then TTCGA and GCCAT are two different word, i.e TTCGA and GCCAT 
    output and last_output - currently None, just to make them initialized, real use happens in "fn1"

    Returns:
    output - gets value from "fn1". For "word" which is oligo like "word" = TTCGA, the "output" = TTCGA.
             For "word" which is not an oligo like "word" = Apple, the "output" = None.
    last_output - gets value from "fn1" by storing "output" corresponding to "word" which is previous to the current "word"
    """

    left_curl = re.search("\(", word, re.IGNORECASE)
    right_curl = re.search("\)", word, re.IGNORECASE)

    # Words with (). Like insert(TGAGACGTCAACAATATGG)
    if right_curl or left_curl:
        if left_curl and right_curl:
            in_between_word = word[left_curl.span()[1]:right_curl.span()[0]]
        elif left_curl and not right_curl:
            in_between_word = word[left_curl.span()[1]:len(word)]  
        elif not left_curl and right_curl:   
            in_between_word = word[0:right_curl.span()[0]]

        output, last_output = fn1(in_between_word, final_output, part, output = None, last_output = None)

    # Words with no (). Like TGAGACGTCAACAATATGG
    else:
        output, last_output = fn1(word, final_output, part, output = None, last_output = None)

    return(output, last_output)

#................................................................
    
def regex_Oligos(row):
    """
    Functionality:
    Recombining left out part of oligo (like "CGGT") back with main oligo string (like "AT")
    Due to current limitations of text extraction and due to line breaks within paper (as writing
    long oligo names on a single line is not feasible), oligo name like "ATCGGT" is present as two
    seperate terms "AT" and "CGGT" in the text file.
    Thus it's important to identify such left out part of oligo (like "CGGT") and recombine it with main 
    oligo string (like "AT").
    To identify left out part we are using logic that if "CGGT" is actually left out part of "AT", then
    "last_output" (which is "AT" for this case) !=None (as if last/currrent "word" is obligo then 
    "last_output" is "word" itself, but if last/currrent "word" is not obligo then "last_output" is "None")

    Arg:
    row - group of sentence(s) out of a big set of sentences extracted from research paper(s)

    Returns:
    final_output - list of many "output" corresponding to each word of a "row". For word which is oligo,
    "output" is "word" itself (name of oligo itself) and or word which is not an oligo, "output" is "None"
    """

    final_output = list()
    last_output = None
    for word in row.split():
        output = None

        # It would be simple oligo "ATCGGT", with no other part at its back
        if last_output==None:
            output, last_output = fn2(word, final_output, part = False, output = None, last_output = None)

        # It would be "CGGT" which is part of "AT"
        elif last_output!=None:
            output, last_output = fn2(word, final_output, part = True, output = None, last_output = None)
            # Working ==>
            # Case 1) "TGAGACGTCAACAATATGG cloned"
                # As "cloned" is not an obligo thus fn1 and fn2 returns it as
                # None, thus we dont add "cloned" with "TGAGACGTCAACAATATGG"
            # Case 2) "TGAGACGTCAACAATATGG GCCT"
                # As "GCCT" is a obligo thus fn1 and fn2 adds it to "TGAGACGTCAACAATATGG"
                # and return us "output" which we place inplace of prev obilo, i.e
                # TGAGACGTCAACAATATGGGCCT in place of TGAGACGTCAACAATATGG 
                # at "final_output" list
            if output!=None:
                final_output[-1] = None

        final_output.append(output)
    return final_output

#................................................................

def find_Oligos(settings, paper_ids):
    """
    Functionality:
    Finds oligos in research paper(s)

    Arg:
    wbpids - List of wb papers ids e.g. ['WBPaper00002379']
    settings - Dictionary with db_config properties and texpresso token

    Returns:
    Panda dataframe with columns of IDs of research paper, Oligos extracted in each row/sentence(s) and Sentence
    """

    paperid_sentence_list = get_paper_sentences_with_TE(paper_ids, settings)

    final = [
        ['temporary', 'temporary', 'temporary'],\
        ['WBPaper ID', 'Oligo', 'Sentence']]

    for index, row in enumerate(paperid_sentence_list):
            final_output = regex_Oligos(row[1])
            for output in final_output:
                if output:
                    final.append([row[0], output, row[1]])

    temp = final[2:]
    return pd.DataFrame(
        temp[:],
        columns=['WBPaper ID', 'Oligo', 'Sentence'])


if __name__ == "__main__":
    settings = setSettings()
    paper_ids = ["WBPaper00050743"]
    df = find_Oligos(settings, paper_ids)
    df.to_csv('variants.csv', index=False)

