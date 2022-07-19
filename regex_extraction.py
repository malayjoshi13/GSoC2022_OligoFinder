from bw_brackets import pick_from_brackets
from combine_oligo_parts import is_part, only_regex
from check_alpha_num_specialchk import has_acgt, has_35, remove_special_characters
import re


def word_processor(word):
    processed_word = pick_from_brackets(word)
    processed_word = has_acgt(processed_word)
    processed_word = has_35(processed_word)
    processed_word = remove_special_characters(processed_word)
    return processed_word


def oligo_seq_regex(row):
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
        oligo_seq = pick_from_brackets(word)
        oligo_seq = has_acgt(oligo_seq)
        oligo_seq = has_35(oligo_seq)
        oligo_seq = remove_special_characters(oligo_seq)
        int_result.append(oligo_seq)  

    None_Oligo_List = is_part(int_result)
    Oligo_List = only_regex(None_Oligo_List)

    return Oligo_List



def oligo_name_regex(oligo_seq_list, row):

    oligo_name_list = dict()
    final_prev_word = None
    #print(oligo_seq_list)

    word_list = row.split()
    for i in range(len(word_list)):
        processed_word = word_processor(word_list[i])

        # Will check if word picked from sentence is oligo or not. 
        # If not oligo, so no name needs to be find.
        # Move ahead. 
        if processed_word:

            # Picking oligo sequence
            for oligo in oligo_seq_list:

                # Checking out of which oligo seq picked from "oligo_seq_list",
                # do currently picked word from sentence is present
                if re.findall(processed_word, oligo, re.IGNORECASE):

                    # If word picked from sentence is first, then no previous word.
                    # Thus there will be no name for this picked word,
                    # even if this first word is an oligo.
                    # Move ahead.
                    if i>0:

                        prev_word = word_list[i-1]
                        processed_prev_word = word_processor(prev_word)

                        # "processed_prev_word" being true means "prev_word"
                        # is oligo; thus prev word can't be oligo-name.
                        # Move ahead as pre-word must be oligo-name and 
                        # current word must be an oligo sequence
                        if processed_prev_word: 
                            oligo_name_list[oligo] = final_prev_word
                            break

                        # No "processed_prev_word" means that prev word is not 
                        # an oligo.
                        # Thus u can directly that non-oligo prev word 
                        # will be name and oligo will the sequence.
                        else:
                                final_prev_word = re.sub("," , '', word_list[i-1])
                                #print(final_prev_word, oligo)
                                oligo_name_list[oligo] = final_prev_word
                                break

                    else:
                        oligo_name_list[oligo] = final_prev_word
                        break

    return oligo_name_list
