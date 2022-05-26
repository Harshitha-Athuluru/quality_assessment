from textblob import TextBlob
import nltk
nltk.download('punkt')
def return_opinion_score(text):
    textB = TextBlob(text)
    pol,sub=0,0
    Num_sentences=len(textB.sentences)
    for t in textB.sentences:
        analysis = t.sentiment
        pol+=analysis.polarity
        sub+=analysis.subjectivity
    Scores=[pol/Num_sentences,sub/Num_sentences]
    return Scores