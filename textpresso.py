import json
import logging
import requests
from typing import List

import nltk

logger = logging.getLogger(__name__)


def textpresso_paper_text(wbpid, token):
    ''' 
    Takes a wbpid (like:- WBPaper00056731) and returns its fulltext 
    '''
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    url = 'https://textpressocentral.org:18080/v1/textpresso/api/search_documents'
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    body = json.dumps({'token': token,
                       'query': {'accession': wbpid,
                                 'type': 'document',
                                 'corpora': ['C. elegans']},
                       'include_fulltext': True})
    response = requests.post(url, data=body, headers=headers, verify=False)
    if response.status_code == 200:
        if response.json() is None:
            return []
        else:
            paper = response.json()[0]
        abstract = tokenizer.tokenize(paper['abstract'])
        fulltext = tokenizer.tokenize(paper['fulltext'])
        return abstract + fulltext
    else:
        return []