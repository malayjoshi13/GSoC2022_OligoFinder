import re
from TfIdf_BOW_creator import sentence_processor

def check_true_positive_oligo_sentence(sentence):
    threshold = 2
    count = 0
    countt = 0
    result = " "

    file1 = open("oligo_words.txt", "r")
    oligo_content = file1.read()
    oligo_content = re.sub(r'[\[\]\(\)\'\s]','',oligo_content)
    oligo_content = re.sub(r'dict_keys','',oligo_content)
    oligo_content = oligo_content.split(",")
    oligo_content = set(oligo_content)

    file2 = open("non_oligo_words.txt", "r")
    non_oligo_content = file2.read()
    non_oligo_content = re.sub(r'[\[\]\(\)\'\s]','',non_oligo_content)
    non_oligo_content = re.sub(r'dict_keys','',non_oligo_content)
    non_oligo_content = non_oligo_content.split(",")
    non_oligo_content = set(non_oligo_content)

    sentence = sentence_processor(sentence)
    sentence_words = sentence.split(" ")

    for word in sentence_words:
        if word in oligo_content: 
            #if word not in non_oligo_content:
                count+=1

        if word in non_oligo_content:
            # if word not in oligo_content: 
                countt+=1

    if count>threshold:
        result = "oligo"
    elif countt>threshold: 
        result = "non-oligo"

    return result


if __name__ == "__main__":
    sentence = "mutation followed genetic crosses PCR using primers rabx5-F (5 -ATTCCCCCAGATTGTGTATG-3) rabx5- R (5 -CCGGTGACGTGGAAGTTGGT-3 )."
    print(check_true_positive_oligo_sentence(sentence))