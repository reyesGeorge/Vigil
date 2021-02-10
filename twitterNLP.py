import pandas as pd
import json
from pandas.io.json import json_normalize

import re
import spacy
from collections import Counter
import pathlib


# get relative data folder
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../assets").resolve()

# tbird = DATA_PATH.joinpath("tburd.png")


def the_burd_is_the_word(new):
    nlp = spacy.load("en_core_web_sm")

    noun_chunks = []
    named_entity = []
    tokens = []

    for doc in nlp.pipe(new['text'].astype('unicode').values, batch_size=50,
                            n_process=5):
        if doc.is_parsed:
            noun_chunks.append([chunk.text for chunk in doc.noun_chunks])
            named_entity.append([ent.text for ent in doc.ents])
            tokens.append([token.text for token in doc if not token.is_stop and not token.is_punct])
        else:
            noun_chunks.append(None)
            named_entity.append(None)       
            tokens.append(None)
            
    new['results_noun_chunks'] = noun_chunks
    new['results_named_entities'] = named_entity
    new['results_tokens_clean'] = tokens

    flattened_list = [y for x in tokens for y in x]

    #remove special characters from tokens list before analyzing
    list_cleaned = [re.sub(r"[^a-zA-Z0-9]", "", file) for file in flattened_list]

    #remove the remainders of what was ampersands and paragraph breaks: \n and amp
    list_cleaned2 = [re.sub('\n', "", file) for file in list_cleaned]

    list_cleaned3 = [re.sub('amp', "", file) for file in list_cleaned2]

    str_list = list(filter(None, list_cleaned3))

    word_freq = Counter(str_list)
    common_words = word_freq.most_common(15)
    print(common_words)


    # Making a copy of the string list of word for further manipulation
    new_str_list = str_list.copy()

    word_frequency = Counter(new_str_list)

    # Sorting from high to low
    results_word_counts = pd.DataFrame.from_dict(word_frequency, orient='index',
                        columns=['keyword_count'])
    results_words = results_word_counts.sort_values(by=['keyword_count'],ascending=False)
    results_words.reset_index(inplace=True)
    results_words.rename(columns = {"index":"keyword","keyword_count":"count"}, inplace=True)
    return results_words
    #results_words.to_csv('keyword_counts.csv', index=False)






