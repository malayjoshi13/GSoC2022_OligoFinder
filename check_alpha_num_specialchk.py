import re

def has_acgt(word):
    """
    Functionality:
    To check if "word" is an oligo or not, checks if "word" only has a,c,g,t

    Arg:
    word - each word of each sentence one at a time

    Returns:
    fn_output - None [if "word" has alphabets other than a,c,g,t], 
                "word" itself [if "word" has alphabets of a,c,g,t]
    """

    fn_output = None
    count = 0
    if word: # to avoid case where "word" is None    

        if re.findall("[a-z]", word, re.IGNORECASE):
            alpha = re.findall("[a-z]", word, re.IGNORECASE)
            if len(alpha)>1:
                for chr in alpha:
                    if re.search("[^atcgp]", chr, re.IGNORECASE) == None:
                        count += 1
                
                if count==len(alpha):
                        fn_output =word
        
    return fn_output

#------------------------------------------

def has_35(word):
    """
    Functionality:
    To check if "word" is an oligo or not, checks if "word" having numbers only has 3 and 5

    Arg:
    word - each word of each sentence one at a time

    Returns:
    fn_output - None [if "word" has number other than 3 and 5], 
                "word" itself [if "word" either dont has any number or has number of 3 and 5]
    """

    fn_output = None
    count = 0
    if word: # to avoid case where "word" is None

        # "word" (may or may not be oligo) having numbers
        if re.findall("[0-9]", word, re.IGNORECASE):
            num = re.findall("[0-9]", word, re.IGNORECASE)
            for chr in num:            
                if re.search("[3,5]", chr, re.IGNORECASE) != None:
                    count += 1

            if count==len(num):
                    fn_output =word                    

        # some oligos dont have numbers at all, so simply pass them withot any checking        
        elif not re.findall("[0-9]", word, re.IGNORECASE):
            fn_output = word

    return fn_output

#-------------------------------------------

# excpet " ' ", as it can come in oligo name like:- 3'-AGTTG-5'
def remove_special_characters(word):
    """
    Functionality:
    Removes spaces and special charaacters except inverted comma (')
    as it can come in oligo name like:- 3'-AGTTG-5'

    Arg:
    word - each word of each sentence one at a time

    Returns:
    fn_output - name of oligo after removing extra spaces and special characters except:- ' .
    """

    fn_output = None

    if word: # to avoid case where "word" is None  

        fn_output = re.sub('[^A-Za-z]', '', word)                  
    return(fn_output)
