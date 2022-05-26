import stanza
def return_sentiment_score(text):
    nlp=stanza.Pipeline('en',processors='tokenize,sentiment')
    doc=nlp(text)
    #print(doc)
    sentiments=[sent.sentiment for sent in doc.sentences]
    Num_sentences=len(doc.sentences)
    scores=[sentiments.count(0)/Num_sentences,
            sentiments.count(1)/Num_sentences,
            sentiments.count(2)/Num_sentences]
    return scores