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
            # if picked word is not None and has length more than 5 and less than 95, 
            if len(present)>5 and len(present)<95:

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

                # but if "past" dont exist 
                # e.g. None 'CTGTGA' None or None 'CTGTGA' GCTAGAT or None 'CTGTGA' GCT
                # then just move ahead as 
                # for case:- None 'CTGTGA' None; "CTGTGA" is an independent oligo, not part of something
                # and for case:- None 'CTGTGA' GCTAGAT or None 'CTGTGA' GCT; "CTGTGA" will wait for
                #                 GCTAGAT and GCT to come in their turn and combine with it 
                elif not past:
                    pass




            # if picked word is not None and has length less than 5,
            # then 50-50 chances that it can be either realy an oligo or falsely predicted as 
            # oligo becoz of its appearance but actually not an oligo
            # so go carefully for this case
            elif len(present)<=5:

                # length less than 5 and its "past" also exists 
                # e.g. None CTGTGA 'GC'
                if past: 
                    # then without thinking anything, that picked word (i.e "present") will be part of "past"
                    # so simply combine them
                    fn_output = str(past)+str(present)
                    # place them at place of "present"
                    int_result[index] = fn_output
                    # and write "None" at place of "past", as we have brought "past"
                    # to location of "present" and there combined both
                    int_result[index-1] = None   

                # length less than 5 and its "future" exists but its "past" dont exists
                # e.g. None 'CA' GCTAGAT, then simply wait for GCTAGAT to come in its turn and 
                # combine with CA
                elif not past and future: 
                    # passes: None 'CA' GCTAGAT as oligo name
                    # but stops: None 'CA' None and place "None" 
                    pass

                # length less than 5 but its "future" and "past" dont exist
                # e.g. None 'CA' None, then it means CA is wrongly predicted oligo
                # in actual its not oligo. Thus place "None" in its place
                elif not past and not future:
                    int_result[index] = None

    return (int_result)


def only_regex(int_result):
    """
    Functionality: "is_part" returns a list which is combination of None and extracted oligo names. 
    This function filter out and outputs a list just having oligos
    """
    oligo_list = list()
    for oligo in int_result:
        if oligo:
            oligo_list.append(oligo)
    
    return oligo_list
