import re
from TfIdf_BOW_creator import sentence_processor

def read_file(path_to_file):
    file = open(path_to_file, "r")
    content = file.read()
    content = re.sub(r'[\[\]\(\)\'\s]','',content)
    content = re.sub(r'dict_keys','',content)
    content = content.split(",")
    content = set(content)
    return content

def check_true_positive_oligo_sentence(sentence):
    threshold = 2
    count = 0
    countt = 0
    result = " "

    oligo_content = read_file("oligo_words.txt")
    non_oligo_content = read_file("non_oligo_words.txt")

    sentence = sentence_processor(sentence)
    sentence_words = sentence.split(" ")

    for word in sentence_words:
        if word in oligo_content: 
            if word not in non_oligo_content:
                count+=1

        if word in non_oligo_content:
            if word not in oligo_content: 
                countt+=1

    if count>threshold:
        result = "oligo"
    elif countt>threshold: 
        result = "non-oligo"

    return result

# if __name__ == "__main__":
#     sentence = "mutation followed genetic crosses PCR using primers rabx5-F (5 -ATTCCCCCAGATTGTGTATG-3) rabx5- R (5 -CCGGTGACGTGGAAGTTGGT-3 )."
#     print(check_true_positive_oligo_sentence(sentence))
