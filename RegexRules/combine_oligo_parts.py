def is_part(int_result):
    """
    Functionality:
    Combines back name of oligos which are actually part of single oligo name but due to 
    spaces, newline, - ; is treated like individual oligo names

    Then append the extracted and processed "oligo_name" into "int_result" list.
    This list is then passed to "is_part" function which clubs oligo names which are part of 
    each other and returns list of final names of oligos present in a "row"

    Arg:
    int_result - it's a list consisting of prediction for current sentence. It comprises of
                 oligo name, if word of sentence is an oligo, 
                 and None, if word of sentence is not an oligo
                 E.g. [None, TTGCA, None, None, GCAATGA, None, CAGGTAC,...]

    Returns:
    int_result - after editing inputted "int_result" list (by combining oligos parts together),
                 it outputs same list
    """

    fn_output = None

    for index, word in enumerate(int_result):

        # checks which index is in the range, then accordingly assigns values to 
        # "past", "present" and "future" variables corresponding to a picked "word" of
        # "int_result" list
        if index == 0:
            past = None
        else:
            past = int_result[index-1]

        present = int_result[index]

        if index == len(int_result)-1:
            future = None
        else:
            future = int_result[index+1]

        # checks if picked word (i.e "present") is itself not None 
        # e.g. None 'None' None or 'None' None None or None None 'None' or ATTCG 'None' None, etc
        if present: 
            # if picked word (i.e "present") is not None and has length more than 5 and less than 95, 
            if len(present)>0 and len(present)<95:

                # and its "past" also exists 
                # e.g. None CTGTGA 'GCTAGAT'
                if past: 
                    # then without thinking anything, that picked word (i.e "present") will be part of "past"
                    # so simply combine them
                    fn_output = str(past)+str(present)
                    # place them at place of "present"
                    int_result[index] = fn_output
                    # and write "None" at place of "past", as we have brought "past"
                    # to location of "present" and there combined both
                    int_result[index-1] = None

                # but if "past" of "present" term dont exist
                # e.g. None 'CTGTGACCGGA' None or None 'CTGTGACCGGA' GCTAGAT or None 'CTGTGACCGGA' GCT
                # or None 'CTGGA' None, then just move ahead (don't modify or delete) as:-
                elif not past:
                    # firstly for case like None 'CTGTGA' GCTAGAT or None 'CTGTGA' GCT 
                    # or None 'CTGGCGCGCATTGA' GCT; where "past" is None but still "future" is present, 
                    # there "present" will wait for GCTAGAT and GCT to come in their turn and 
                    # combine with it. 
                    # Here length of seq don't matter as shorter seq also becomes 
                    # large when joint with "future"
                    if future:
                        pass
                    # secondly for case like None 'CTGTGACCGGA' None or None 'CTGT' None; 
                    # only seq like "CTGTGACCGGA" will be treated as an oligo, exisiting between 
                    # two non-oligo sequences (marked as None) and not part of some longer sequence.
                    # Shorter seq like "CTGT" existing between non-oligo seq will be ignored as they 
                    # are not an oligo
                    elif not future and len(present)>10:
                        pass
                    elif not future and len(present)<10:
                        int_result[index] = None

            else:
                int_result[index] = None
    return (int_result)


def only_regex(int_result):
    """
    Functionality: "is_part" returns a list which is combination of None and extracted oligo names. 
    This function filter out and outputs a list just having oligos
    """
    oligo_list = list()
    for oligo in int_result:
        if oligo and len(oligo)>12:
            oligo_list.append(oligo)
    
    return oligo_list
