import re

def pick_from_brackets(word):
    """
    Functionality:
    Extracts name of oligo if present inside brackets in "word" variable.
    Like for example in words insert(TGAGACGTCAACAATATGG), insert(TGAGACGTCAACAATATGG, 
    insert(TGAGACGTCAACAATATGG)hg, (TGAGACGTCAACAATATGG)hg and TGAGACGTCAACAATATGG)hg, 
    oligo seq "TGAGACGTCAACAATATGG" is enclosed within ()
    If "word" don't has (), then "word" itself is possibly an oligo sequence

    Arg:
    word - each word of each sentence one at a time

    Returns:
    fn_output - oligo sequence extracted from in between brackets ()
    """

    fn_output = None
    left_curl = re.search("\(", word, re.IGNORECASE)
    right_curl = re.search("\)", word, re.IGNORECASE)

    # Words with (). Like:- rat(TGAGACGTCAACAATATGG)
    if right_curl or left_curl:
        if left_curl and right_curl:
            in_between_word = word[left_curl.span()[1]:right_curl.span()[0]]
        elif left_curl and not right_curl:
            in_between_word = word[left_curl.span()[1]:len(word)]  
        elif not left_curl and right_curl:   
            in_between_word = word[0:right_curl.span()[0]]
        fn_output = in_between_word

    # Words with no (). Like:- TGAGACGTCAACAATATGG
    else:
        fn_output = word

    return(fn_output)
