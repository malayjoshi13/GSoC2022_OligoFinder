import csv
import numpy as np

#Create vocab
def create_vocab(filename):
    # open the file in read mode
    read_file = open(filename, 'r')
    
    # creating dictreader object
    file = csv.DictReader(read_file)
    
    # creating empty lists
    current_sentence = list()
    is_oligo = list()
    
    # iterating over each row and append
    # values to empty list
    for col in file:
        current_sentence.append(col['Current Sentence'])
        is_oligo.append(col['Is this an oligo?'])

    non_oligo_sentences = list()
    oligo_sentences = list()
    non_oligo_sentences_words = list()
    oligo_sentences_words = list()

    for i in range(len(current_sentence)):
        if is_oligo[i]=="Oligo" and current_sentence[i] not in oligo_sentences: #appends unique sentences only
            oligo_sentences.append(current_sentence[i])
            for word in current_sentence[i].split():

                if word not in oligo_sentences_words:

                    oligo_sentences_words.append(word)           

        elif is_oligo[i]!="Oligo" and current_sentence[i] not in non_oligo_sentences:
            non_oligo_sentences.append(current_sentence[i])
            for word in current_sentence[i].split():
                if word not in non_oligo_sentences_words:
                    non_oligo_sentences_words.append(word) 

    return non_oligo_sentences, oligo_sentences, non_oligo_sentences_words, oligo_sentences_words


#Creating an index for each word in our vocab.
def vocab_elements(vocab):
    index_dict = {} #Dictionary to store index for each word
    i = 0
    for word in vocab:
        index_dict[word] = i
        i += 1
    return index_dict


#Create a count dictionary to keep the count of the number of documents containing the given word
def count_dict(sentences, vocab):
    word_count = {}
    for word in vocab:
        word_count[word] = 0
        for sent in sentences:
            if word in sent:
                word_count[word] += 1
    return word_count


#Term Frequency
def termfreq(sentence, word):
    N = len(sentence.split())

    occurance = 0
    for token in sentence.split():
        if token == word:
            occurance+=1
    return occurance/N #ocurrennce of a word in a sentence/total length of that sentence
    #multiple sentences==multiple documents


#Inverse Document Frequency
def inverse_doc_freq(word, document_len, word_count):
    try:
        word_occurance = word_count[word] + 1
    except:
        word_occurance = 1 
    return np.log(document_len/word_occurance) #np.log(total number of sentences in oligo passage/occurence of a word in oligo passage)


#Combining the TF-IDF functions
def tf_idf(sentences, sentences_words, sentence):
    word_count = count_dict(sentences, sentences_words)
    document_len = len(sentences)

    tf_idf_vec = {}
    for word in sentence.split():
        tf = termfreq(sentence, word)
        idf = inverse_doc_freq(word, document_len, word_count)
        value = tf*idf

        if value>0.2:
            if word not in tf_idf_vec:
                tf_idf_vec[word] = [value]
            else:
                tf_idf_vec[word].append(value)

    return tf_idf_vec

def threshold_tfidf_words(sentences, sentences_words):
    tf_idf_vec_final = {}
    for sentence in sentences:
        tf_idf_vec = tf_idf(sentences, sentences_words, sentence)
        tf_idf_vec_final.update(tf_idf_vec)


    for i in tf_idf_vec_final:
        sum = 0
        # print(str(i)+": "+str(tf_idf_vec_final[i])) #before

        for j in tf_idf_vec_final[i]:
            sum += j
        tf_idf_vec_final[i] = sum/len(tf_idf_vec_final[i]) #if three tfidf are added then divide by 3
        
        # print(str(i)+": "+str(tf_idf_vec_final[i])) #after

    return tf_idf_vec_final

# main code
filename = "oligos.csv"
non_oligo_sentences, oligo_sentences, non_oligo_sentences_words, oligo_sentences_words = create_vocab(filename)


tf_idf_vec_oligo_final = threshold_tfidf_words(oligo_sentences, oligo_sentences_words)
oligo_words = tf_idf_vec_oligo_final.keys()
# print(oligo_words)

tf_idf_vec_non_oligo_final = threshold_tfidf_words(non_oligo_sentences, non_oligo_sentences_words)
non_oligo_words = tf_idf_vec_non_oligo_final.keys()
print(non_oligo_words)
