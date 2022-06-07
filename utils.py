import readability
def article_quality(jar_path,models_jar_path,text):
    # Path to CoreNLP jar unzipped
    #jar_path = '/content/stanford-corenlp-4.4.0/stanford-corenlp-4.4.0.jar'
    # Path to CoreNLP model jar
    #models_jar_path = '/content/stanford-corenlp-4.4.0-models-english.jar'
    scp = readability.init_scp(jar_path, models_jar_path)
    sdp = readability.init_sdp(jar_path, models_jar_path)
    readability_features=readability.all_features(text, scp, sdp)
    print(readability_features)
    readability_classes={0: 'A2',1:'B1',2:'B2',3:'C1',4:'C2'}
    readabilty_scores = {0: 0.2,1:0.4,2:0.6,3:0.8,4:1.0}
    X=[]
    temp=[]
    for k,v in readability_features.items():
        if k not in ['2.Sentiment scores are......2.1.Positive Sentiment','2.2.Neutral Sentiment','2.3.Negative Sentiment','3.Opinion Based Scores are....3.1.Polarity','3.2.Subjectivity']:
            temp.append(v)

    X.append(temp)
    filename="/content/quality_assessment/best_model.sav"
    yy=readability.classify(X,filename)
    print("readability: {}".format(readability_classes[yy[0]]))
    readabilty_score = readabilty_scores[yy[0]]
    return readability_classes[yy[0]]