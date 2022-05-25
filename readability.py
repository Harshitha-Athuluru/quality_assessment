# -*- coding: utf-8 -*-
"""Readability.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VwfdGLKLHaI8gsaCoFuMw1BUkTVK2HDN
"""

# ! pip install pattern

# !pip install stanza

from __future__ import division
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('cmudict')
nltk.download('punkt')
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk import pos_tag
import math
import string
import numpy as np
from nltk.corpus import stopwords
cmuDictionary = None
from textblob import TextBlob

from pattern.en import parsetree, Chunk
from nltk.tree import Tree

import stanza

stanza.download('en')

from nltk.parse.stanford import StanfordDependencyParser

# !wget https://nlp.stanford.edu/software/stanford-corenlp-4.4.0.zip
# !wget https://nlp.stanford.edu/software/stanford-corenlp-4.4.0-models-english.jar
# !unzip /content/stanford-corenlp-4.4.0.zip

from nltk.parse.stanford import StanfordParser, StanfordDependencyParser

def init_scp(jar_path, models_jar_path):
  return StanfordParser(path_to_jar = jar_path, path_to_models_jar = models_jar_path)

def init_sdp(jar_path, models_jar_path):
  return StanfordDependencyParser(path_to_jar = jar_path, path_to_models_jar = models_jar_path)


def all_features(text, scp, sdp):
      # text = open("3rdMountedDivision.txt").read()
    textB = TextBlob(text)
    nlp=stanza.Pipeline('en',processors='tokenize,mwt,POS')
    doc=nlp(text)
    # Pre-Processing Steps for lexical features
    words = word_tokenize(text)
    T=len(set(words))
    N=len(words)
    tagged_comment = pos_tag(words)
    Total_Words=len(words)
    numVerbs=[]
    numVerbsVB=[]
    numVerbsVBD=[]
    numVerbsVBG=[]
    numVerbsVBN=[]
    numVerbsVBP=[]
    numVerbsVBZ=[]
    perpronouns=[]
    whperpronouns=[]
    numAdj=[]
    numAdverbs=[]
    numPrepositions=[]
    numInterjections=[]
    numConjunct=[]
    numNouns=[]
    numProperNouns=[]
    numModals=[]
    numDeterminers=[]
    for word,tag in tagged_comment:
        if tag=='VB':
            numVerbsVB.append(word)
        elif tag=='VBD':
            numVerbsVBD.append(word)
        elif tag=='VBG':
            numVerbsVBG.append(word)
        elif tag=='VBN':
            numVerbsVBN.append(word)
        elif tag=='VBP':
            numVerbsVBP.append(word)
        elif tag=='VBZ':
            numVerbsVBZ.append(word)
        elif tag=='PRP' or tag=='PRP$':
            perpronouns.append(word)
        elif tag=='WP' or tag=='WP$':
            whperpronouns.append(word)
        elif tag=='JJ' or tag=='JJR' or tag=='JJS':
            numAdj.append(word)
        elif tag=='RB' or tag=='RBR' or tag=='RBS' or tag=='RP':
            numAdverbs.append(word)
        elif tag=='IN':
            numPrepositions.append(word)
        elif tag=='UH':
            numInterjections.append(word)
        elif tag=='CC':
            numConjunct.append(word)
        elif tag=='NN' or tag=='NNS':
            numNouns.append(word)
        elif tag=='NNP' or tag=='NNPS':
            numProperNouns.append(word)
        elif tag=='MD':
            numModals.append(word)
        elif tag=='DT':
            numDeterminers.append(word)
        numVerbs=numVerbsVB+numVerbsVBD+numVerbsVBG+numVerbsVBN+numVerbsVBP+numVerbsVBZ
        Unique_numVerbs=list(set(numVerbs))
        numpronouns=perpronouns+whperpronouns
        numLexicals= numAdj+numNouns+numVerbs+numAdverbs+numProperNouns
        numauxverbs=numModals
        numVerbsOnly=len(numVerbs)-len(numauxverbs)
    tokens = sent_tokenize(text)
# Pre-Processing Steps for sentiment
    sentiments=[sent.sentiment for sent in doc.sentences]
# Pre-processing step for Opinion based
    Num_sentences=len(doc.sentences)
    polarity,subjectivity=0,0
    Number_sentences=len(textB.sentences)
    for t in textB.sentences:
        analysis = t.sentiment
        polarity+=analysis.polarity
        subjectivity+=analysis.subjectivity
# Preprocessing for morphological features
    PronType_Art=0
    PronType_Dem=0
    PronType_Emp=0
    PronType_Exc=0
    PronType_Ind=0
    PronType_Int=0
    PronType_Neg=0
    PronType_Prs=0
    PronType_Rcp=0
    PronType_Rel=0
    PronType_Tot=0
    NumType_Card=0
    NumType_Dist=0
    NumType_Frac=0
    NumType_Mult=0
    NumType_Ord=0
    NumType_Range=0
    NumType_Sets=0
    Poss_Yes=0
    Reflex_Yes=0
    Foreign_Yes=0
    Abbr_Yes=0
    Typo_Yes=0
    Gender_Masc=0
    Gender_Fem=0
    Gender_Neut=0
    Gender_Com=0
    Animacy_Anim=0
    Animacy_Hum=0
    Animacy_Inan=0
    Animacy_Nhum=0
    Number_Coll=0
    Number_Count=0
    Number_Dual=0
    Number_Grpa=0
    Number_Grpl=0
    Number_Inv=0
    Number_Pauc=0
    Number_Plur=0
    Number_Ptan=0
    Number_Sing=0
    Number_Tri=0
    Case_Abs=0
    Case_Acc=0
    Case_Erg=0
    Case_Nom=0
    Case_Abe=0
    Case_Ben=0
    Case_Cau=0
    Case_Cmp=0
    Case_Cns=0
    Case_Com=0
    Case_Dat=0
    Case_Dis=0
    Case_Equ=0
    Case_Gen=0
    Case_Ins=0
    Case_Par=0
    Case_Tem=0
    Case_Tra=0
    Case_Voc=0
    Case_Abl=0
    Case_Add=0
    Case_Ade=0
    Case_All=0
    Case_Del=0
    Case_Ela=0
    Case_Ess=0
    Case_Ill=0
    Case_Ine=0
    Case_Lat=0
    Case_Loc=0
    Case_Per=0
    Case_Sbe=0
    Case_Sbl=0
    Case_Spl=0
    Case_Sub=0
    Case_Sup=0
    Case_Ter=0
    Definite_Com=0
    Definite_Cons=0
    Definite_Def=0
    Definite_Ind=0
    Definite_Spec=0
    Degree_Abs=0
    Degree_Cmp=0
    Degree_Equ=0
    Degree_Pos=0
    Degree_Sup=0
    VerbForm_Conv=0
    VerbForm_Fin=0
    VerbForm_Gdv=0
    VerbForm_Ger=0
    VerbForm_Inf=0
    VerbForm_Part=0
    VerbForm_Sup=0
    VerbForm_Vnoun=0
    Mood_Adm=0
    Mood_Cnd=0
    Mood_Des=0
    Mood_Imp=0
    Mood_Ind=0
    Mood_Irr=0
    Mood_Jus=0
    Mood_Nec=0
    Mood_Opt=0
    Mood_Pot=0
    Mood_Prp=0
    Mood_Qot=0
    Mood_Sub=0
    Tense_Fut=0
    Tense_Imp=0
    Tense_Past=0
    Tense_Pqp=0
    Tense_Pres=0
    Aspect_Hab=0
    Aspect_Imp=0
    Aspect_Iter=0
    Aspect_Perf=0
    Aspect_Prog=0
    Aspect_Prosp=0
    Voice_Act=0
    Voice_Antip=0
    Voice_Bfoc=0
    Voice_Cau=0
    Voice_Dir=0
    Voice_Inv=0
    Voice_Lfoc=0
    Voice_Mid=0
    Voice_Pass=0
    Voice_Rcp=0
    Evident_Fh=0
    Evident_Nfh=0
    Polarity_Neg=0
    Polarity_Pos=0
    Person_0=0
    Person_1=0
    Person_2=0
    Person_3=0
    Person_4=0
    Polite_Elev=0
    Polite_Form=0
    Polite_Humb=0
    Polite_Infm=0
    Clusivity_Ex=0
    Clusivity_In=0
    feature_types=[]
    for sent in doc.sentences:
        for word in sent.words:
            if word.feats is not None:
                feature_types.extend(word.feats.split('|'))
    for f in feature_types:
        f_type=f.split('=')[0]
        if f_type=='PronType':
            if 'Art' in f:
                PronType_Art=PronType_Art+1
            elif 'Dem' in f: 
                PronType_Dem=PronType_Dem+1
            elif 'Emp' in f:
                PronType_Emp=PronType_Emp+1
            elif 'Exc' in f:
                PronType_Exc=PronType_Exc+1
            elif 'Ind' in f:
                PronType_Ind=PronType_Ind+1
            elif 'Int' in f:
                PronType_Int=PronType_Int+1
            elif 'Neg' in f:
                PronType_Neg=PronType_Neg+1
            elif 'Prs'in f:
                PronType_Prs=PronType_Prs+1
            elif 'Rcp' in f:
                PronType_Rcp=PronType_Rcp+1
            elif 'Rel' in f:
                PronType_Rel=PronType_Rel+1
            elif 'Tot' in f:
                PronType_Tot=PronType_Tot+1
        elif f_type=='NumType':
            if 'Card' in f:
                NumType_Card=NumType_Card+1
            elif 'Dist' in f:
                NumType_Dist=NumType_Dist+1
            elif 'Frac' in f:
                NumType_Frac=NumType_Frac+1
            elif 'Mult' in f:
                NumType_Mult=NumType_Mult+1
            elif 'Ord' in f:
                NumType_Ord=NumType_Ord+1
            elif 'Range' in f:
                NumType_Range=NumType_Range+1
            elif 'Sets' in f:
                NumType_Sets=NumType_Sets+1
        elif f_type=='Poss':
            if 'Yes' in f:
                Poss_Yes=Poss_Yes+1
        elif f_type=='Reflex':
            if 'Yes' in f:
                Reflex_Yes=Reflex_Yes+1
        elif f_type=='Foreign':
            if 'Yes' in f:
                Foreign_Yes=Foreign_Yes+1
        elif f_type=='Abbr':
            if 'Yes' in f:
                Abbr_Yes=Abbr_Yes+1
        elif f_type=='Typo':
            if 'Yes' in f:
                Typo_Yes=Typo_Yes+1
        elif f_type=='Gender':
            if 'Masc' in f:
                Gender_Masc=Gender_Masc+1
            elif 'Fem' in f:
                Gender_Fem=Gender_Fem+1
            elif 'Neut' in f:
                Gender_Neut=Gender_Neut+1
            elif 'Com' in f:
                Gender_Com=Gender_Com+1
        elif f_type=='Animacy':
            if 'Anim' in f:
                Animacy_Anim=Animacy_Anim+1
            elif 'Hum' in f:
                Animacy_Hum=Animacy_Hum+1
            elif 'Inan' in f:
                Animacy_Inan=Animacy_Inan+1
            elif 'Nhum' in f:
                Animacy_Nhum=Animacy_Nhum+1
        elif f_type=='Number':
            if 'Coll' in f:
                Number_Coll=Number_Coll+1
            elif 'Count' in f:
                Number_Count=Number_Count+1
            elif 'Dual' in f:
                Number_Dual=Number_Dual+1
            elif 'Grpa' in f:
                Number_Grpa=Number_Grpa+1
            elif 'Grpl' in f:
                Number_Grpl=Number_Grpl+1
            elif 'Inv' in f:
                Number_Inv=Number_Inv+1
            elif 'Pauc' in f:
                Number_Pauc=Number_Pauc+1
            elif 'Plur' in f:
                Number_Plur=Number_Plur+1
            elif 'Ptan' in f:
                Number_Ptan=Number_Ptan+1
            elif 'Sing' in f:
                Number_Sing=Number_Sing+1
            elif 'Tri' in f:
                Number_Tri=Number_Tri+1
        elif f_type=='Case':
            if 'Abs' in f:
                Case_Abs=Case_Abs+1
            elif 'Acc' in f:
                Case_Acc=Case_Acc+1
            elif 'Erg' in f:
                Case_Erg=Case_Erg+1
            elif 'Nom' in f: 
                Case_Nom=Case_Nom+1
            elif 'Abe' in f:
                Case_Abe=Case_Abe+1
            elif 'Ben' in f:
                Case_Ben=Case_Ben+1
            elif 'Cau' in f:
                Case_Cau=Case_Cau+1
            elif 'Cmp' in f:
                Case_Cmp=Case_Cmp+1
            elif 'Cns' in f:
                Case_Cns=Case_Cns+1
            elif 'Com' in f:
                Case_Com=Case_Com+1
            elif 'Dat' in f:
                Case_Dat=Case_Dat+1
            elif 'Dis' in f:
                Case_Dis=Case_Dis+1
            elif 'Equ' in f:
                Case_Equ=Case_Equ+1
            elif 'Gen' in f:
                Case_Gen=Case_Gen+1
            elif 'Ins' in f:
                Case_Ins=Case_Ins+1
            elif 'Par' in f:
                Case_Par=Case_Par+1
            elif 'Tem' in f:
                Case_Tem=Case_Tem+1
            elif 'Tra' in f:
                Case_Tra=Case_Tra+1
            elif 'Voc' in f:
                Case_Voa=Case_Voc+1
            elif 'Abl' in f:
                Case_Abl=Case_Abl+1
            elif 'Add' in f:
                Case_Add=Case_Add+1
            elif 'Ade' in f:
                Case_Ade=Case_Ade+1
            elif 'All' in f:
                Case_All=Case_All+1
            elif 'Del' in f:
                Case_Del=Case_Del+1
            elif 'Ela' in f:
                Case_Ela=Case_Ela+1
            elif 'Ess' in f:
                Case_Ess=Case_Ess+1
            elif 'Ill' in f:
                Case_Ill=Case_Ill+1
            elif 'Ine' in f:
                Case_Ine=Case_Ine+1
            elif 'Lat' in f:
                Case_Lat=Case_Lat+1
            elif 'Loc' in f:
                Case_Loc=Case_Loc+1
            elif 'Per' in f:
                Case_Per=Case_Per+1
            elif 'Sbe' in f:
                Case_Sbe=Case_Sbe+1
            elif 'Sbl' in f:
                Case_Sbl=Case_Sbl+1
            elif 'Spl' in f:
                Case_Spl=Case_Spl+1
            elif 'Sub' in f:
                Case_Sub=Case_Sub+1
            elif 'Sup' in f:
                Case_Sup=Case_Sup+1
            elif 'Ter' in f:
                Case_Ter=Case_Ter+1
        elif f_type=='Definite':
            if 'Com' in f:
                Definite_Com=Definite_Com+1
            elif 'Cons' in f:
                Definite_Cons=Definite_Cons+1
            elif 'Def' in f:
                Definite_Def=Definite_Def+1
            elif 'Ind' in f:
                Definite_Ind=Definite_Ind+1
            elif 'Spec' in f:
                Definite_Spec=Definite_Spec+1
        elif f_type=='Degree':
            if 'Abs' in f:
                Degree_Abs=Degree_Abs+1
            elif 'Cmp' in f:
                Degree_Cmp=Degree_Cmp+1
            elif 'Equ' in f:
                Degree_Equ=Degree_Equ+1
            elif 'Pos' in f:
                Degree_Pos=Degree_Pos+1
            elif 'Sup' in f:
                Degree_Sup=Degree_Sup+1
        elif f_type=='VerbForm':
            if 'Conv' in f:
                VerbForm_Conv=VerbForm_Conv+1
            elif 'Fin' in f:
                VerbForm_Fin=VerbForm_Fin+1
            elif 'Gdv' in f:
                VerbForm_Gdv=VerbForm_Gdv+1
            elif 'Ger' in f:
                VerbForm_Ger=VerbForm_Ger+1
            elif 'Inf' in f:
                VerbForm_Inf=VerbForm_Inf+1
            elif 'Part' in f:
                VerbForm_Part=VerbForm_Part+1
            elif 'Sup' in f:
                VerbForm_Sup=VerbForm_Sup+1
            elif 'Vnoun' in f:
                VerbForm_Vnoun=VerbForm_Vnoun+1
        elif f_type=='Mood':
            if 'Adm' in f:
                Mood_Adm=Mood_Adm+1
            elif 'Cnd' in f:
                Mood_Cnd=Mood_Cnd+1
            elif 'Des' in f:
                Mood_Des=Mood_Des+1
            elif 'Imp' in f:
                Mood_Imp=Mood_Imp+1
            elif 'Ind' in f:
                Mood_Ind=Mood_Ind+1
            elif 'Irr' in f:
                Mood_Irr=Mood_Irr+1
            elif 'Jus' in f:
                Mood_Jus=Mood_Jus+1
            elif 'Nec' in f:
                Mood_Nec=Mood_Nec+1
            elif 'Opt' in f:
                Mood_Opt=Mood_Opt+1                
            elif 'Pot' in f:
                Mood_Pot=Mood_Pot+1
            elif 'Prp' in f:
                Mood_Prp=Mood_Prp+1
            elif 'Qot' in f:
                Mood_Qot=Mood_Qot+1
            elif 'Sub' in f:
                Mood_Sub=Mood_Sub+1
        elif f_type=='Tense':
            if 'Fut' in f:
                Tense_Fut=Tense_Fut+1
            elif 'Imp' in f:
                Tense_Imp=Tense_Imp+1
            elif 'Past' in f:
                Tense_Past=Tense_Past+1
            elif 'Pqp' in f:
                Tense_Pqp=Tense_Pqp+1
            elif 'Pres' in f:
                Tense_Pres=Tense_Pres+1
        elif f_type=='Aspect':
            if 'Hab' in f:
                Aspect_Hab=Aspect_Hab+1
            elif 'Imp' in f:
                Aspect_Imp=Aspect_Imp+1
            elif 'Iter' in f:
                Aspect_Iter=Aspect_Iter+1
            elif 'Perf' in f:
                Aspect_Perf=Aspect_Perf+1
            elif 'Prog' in f:
                Aspect_Prog=Aspect_Prog+1
            elif 'Prosp' in f:
                Aspect_Prosp=Aspect_Prosp+1
        elif f_type=='Voice':
            if 'Act' in f:
                Voice_Act=Voice_Act+1
            elif 'Antip' in f:
                Voice_Antip=Voice_Antip+1
            elif 'Bfoc' in f:
                Voice_Bfoc=Voice_Bfoc+1
            elif 'Cau' in f:
                Voice_Cau=Voice_Cau+1
            elif 'Dir' in f:
                Voice_Dir=Voice_Dir+1
            elif 'Inv' in f:
                Voice_Inv=Voice_Inv+1
            elif 'Lfoc' in f:
                Voice_Lfoc=Voice_Lfoc+1
            elif 'Mid' in f:
                Voice_Mid=Voice_Mid+1
            elif 'Pass' in f:
                Voice_Pass=Voice_Pass+1
            elif 'Rcp' in f:
                Voice_Rcp=Voice_Rcp+1
        elif f_type=='Evident':
            if 'Fh' in f:
                Evident_Fh=Evident_Fh+1
            elif 'Nfh' in f:
                Evident_Nfh=Evident_Nfh+1
        elif f_type=='Polarity':
            if 'Neg' in f:
                Polarity_Neg=Polarity_Neg+1
            elif 'Pos' in f:
                Polarity_Pos=Polarity_Pos+1
        elif f_type=='Person':
            if '0' in f:
                Person_0=Person_0+1
            elif '1' in f:
                Person_1=Person_1+1
            elif '2' in f:
                Person_2=Person_2+1
            elif '3' in f:
                Person_3=Person_3+1
            elif '4' in f:
                Person_4=Person_4+1
        elif f_type=='Polite':
            if 'Elev' in f:
                Polite_Elev=Polite_Elev+1
            elif 'Form' in f:
                Polite_Form=Polite_Form+1
            elif 'Humb' in f:
                Polite_Humb=Polite_Humb+1
            elif 'Infm' in f:
                Polite_Infm=Polite_Infm+1
        elif f_type=='Clusivity':
            if 'Ex' in f:
                Clusivity_Ex=Clusivity_Ex+1
            elif 'In' in f:
                Clusivity_In=Clusivity_In+1
    # Pre-Processing steps for syntactical features
    def clauses(sentences,scp):
        y = scp.raw_parse_sents(sentences)    
        z = list(y)    
        z1 = [list(x) for x in z]
        deps = []
        for sent in z1:
            for subtree in sent[0].subtrees():
                if subtree.label()=="SBAR":
                    deps.append(' '.join(subtree.leaves()))
        
        dep_sents = list(set(deps))
        dependent_sentences = []
        for s in dep_sents:
            temp = s.split(',')
            dependent_sentences.append(temp[0])
        temp = dependent_sentences
        dependent_sentences[:] = [sent.split(".")[0] for sent in dependent_sentences]
        dependent_sentences[:] = [" ".join(sent.split()) for sent in dependent_sentences]
        return dependent_sentences
    
    num_noun_phrases = []
    num_verb_phrases = []
    num_adj_phrases = []
    num_adv_phrases = []
    num_prep_phrases = []
    cl = clauses(tokens,scp)
    dependent_sents= cl    
    for s in tokens: 
      try:           
        tree = parsetree(s)
      except Exception as e:
        print("Exception occured: {}".format(e))
        continue
      chunks = [sentence_tree.chunks for sentence_tree in tree]
      
      noun_phrases_chunks = [chunk.words for chunk in chunks[0] if chunk.type=="NP"]
      noun_phrases= [[(w.string,w.type) for w in word] for word in noun_phrases_chunks]
      
      verb_phrases_chunks = [chunk.words for chunk in chunks[0] if chunk.type=="VP"]
      verb_phrases= [[(w.string,w.type) for w in word] for word in verb_phrases_chunks]
      
      adj_phrases_chunks = [chunk.words for chunk in chunks[0] if chunk.type=="ADJP"]
      adj_phrases= [[(w.string,w.type) for w in word] for word in adj_phrases_chunks]
      
      adverb_phrases_chunks = [chunk.words for chunk in chunks[0] if chunk.type=="ADVP"]
      adverb_phrases= [[(w.string,w.type) for w in word] for word in adverb_phrases_chunks]
      
      prep_phrases_chunks = [chunk.words for chunk in chunks[0] if chunk.type=="PP"]
      prep_phrases= [[(w.string,w.type) for w in word] for word in prep_phrases_chunks]
      
      num_noun_phrases.append(len(noun_phrases))
      num_verb_phrases.append(len(verb_phrases))
      num_adj_phrases.append(len(adj_phrases))
      num_adv_phrases.append(len(adverb_phrases))
      num_prep_phrases.append(len(prep_phrases))


    # Calculating the features
    feats={
        '1.Lexical Features are ........'
        'TypeToken':T/N,
        'Corrected_typeToken':T/(math.sqrt(2*N)),
        'Root_typeToken':T/(math.sqrt(N)),
        'Bilogarithmic_typeToken':(math.log(T))/(math.log(N)),
        'Uber_Index':(math.log(T)*math.log(T))/(math.log(N/T)),
        'POS_numNouns':(len(numNouns)+len(numProperNouns))/Total_Words,
        'POS_numProperNouns':len(numProperNouns)/Total_Words,
        'POS_numPronouns':len(numpronouns)/Total_Words,
        'POS_numConjunct':len(numConjunct)/Total_Words,
        'POS_numAdjectives':len(numAdj)/Total_Words,
        'POS_numVerbs':len(numVerbs)/Total_Words,
        'POS_numAdverbs':len(numAdverbs)/Total_Words,
        'POS_numModals':len(numModals)/Total_Words,
        'POS_numPrepositions':len(numPrepositions)/Total_Words,
        'POS_numInterjections':len(numInterjections)/Total_Words,
        'POS_numPerPronouns':len(perpronouns)/Total_Words,
        'POS_numWhPronouns':len(whperpronouns)/Total_Words,
        'POS_numDeterminers':len(numDeterminers)/Total_Words,
        'POS_numLexicals':len(numLexicals)/Total_Words,
        'POS_advVar':len(numAdverbs)/len(numLexicals),
        'POS_adjVar':len(numAdj)/len(numLexicals),
        'POS_modVar':(len(numAdj)+len(numAdverbs))/len(numLexicals),
        'POS_nounVar':(len(numNouns)+len(numProperNouns))/Total_Words,
        'POS_verbVar1':numVerbsOnly/len(Unique_numVerbs),
        'POS_verbVar2':numVerbsOnly/len(numLexicals),
        'POS_squaredVerbVar1':(numVerbsOnly*numVerbsOnly)/len(Unique_numVerbs),
        'POS_correctedVV1':numVerbsOnly/(math.sqrt(2*len(Unique_numVerbs))),
        'Avg_SentLenghtByWord':np.average([len(token.split()) for token in tokens]),
        'Avg_SentLenghtByCh':np.average([len(token) for token in tokens]),

        '2.Sentiment scores are......'
        '2.1.Positive Sentiment':sentiments.count(0)/Num_sentences,
        '2.2.Neutral Sentiment':sentiments.count(1)/Num_sentences,
        '2.3.Negative Sentiment':sentiments.count(2)/Num_sentences,

        '3''.''Opinion Based Scores are....'
        '3.1.''Polarity':polarity/Number_sentences,
        '3.2.''Subjectivity':subjectivity/Number_sentences,

        '4''.''Syntactical Features are .......'
        '4.1.''noun_phrases_per_corpus':float(sum(num_noun_phrases))/len(num_noun_phrases),
        '4.2.''verb_phrases_per_corpus':float(sum(num_verb_phrases))/len(num_verb_phrases),
        '4.3.''adv_phrases_per_corpus' :float(sum(num_adv_phrases))/len(num_adv_phrases),
        '4.4.''adj_phrases_per_corpus':float(sum(num_adj_phrases))/len(num_adj_phrases),
        '4.5.''prep_phrases_per_corpus':float(sum(num_prep_phrases))/len(num_adj_phrases),
        '4.6.''dep_clauses_per_corpus':float(len(dependent_sents))/len(tokens),

        '5''.''Morphological Features are.....'
        'personal or possessive personal pronoun or determiner - Prs': PronType_Prs,
        'reciprocal pronoun - Rcp':PronType_Rcp,
        'article - Art ':PronType_Art,
        'interrogative pronoun, determiner, numeral or adverb - Int':PronType_Int,
        'relative pronoun, determiner, numeral or adverb - Rel':PronType_Rel,
        'exclamative determiner - Exc':PronType_Exc,
        'demonstrative pronoun, determiner, numeral or adverb - Dem':PronType_Dem,
        'emphatic determiner - Emp':PronType_Emp,
        'total (collective) pronoun, determiner or adverb - Tot':PronType_Tot,
        'negative pronoun, determiner or adverb - Neg':PronType_Neg,
        'indefinite pronoun, determiner, numeral or adverb - Ind':PronType_Ind,
        'cardinal number or corresponding interrogative / relative / indefinite / demonstrative word - Card':NumType_Card,
        'ordinal number or corresponding interrogative / relative / indefinite / demonstrative word - Ord':NumType_Ord,
        'multiplicative numeral or corresponding interrogative / relative / indefinite / demonstrative word - mult':NumType_Mult,
        'fraction - Frac':NumType_Frac,
        'number of sets of things; collective numeral - Sets':NumType_Sets,
        'distributive numeral - Dist':NumType_Dist,
        'range of values - Range':NumType_Range,
        'it is possessive- Yes':Poss_Yes,
        'it is reflexive - Yes': Reflex_Yes,
        'it is foreign - Foreign':Foreign_Yes,
        'it is abbreviation - Abbr':Abbr_Yes,
        'it is typo - Typo' :Typo_Yes,
        'masculine gender - Masc':Gender_Masc,
        'feminine gender - Fem': Gender_Fem,
        'neuter gender - Neut' : Gender_Neut,
        'common gender - Com' : Gender_Com,
        'animate - Anim': Animacy_Anim,
        'inanimate - Inan' : Animacy_Inan,
        'human - Hum' : Animacy_Hum,
        'non-human - Nhum' : Animacy_Nhum,
        'singular number - Sing': Number_Sing,
        'plural number - Plur' : Number_Plur,
        'dual number - Dual':Number_Dual,
        'trial number - Tri':Number_Tri,
        'paucal number - Pauc': Number_Pauc,
        'greater paucal number - Grpa':Number_Grpa,
        'greater plural number - Grpl':Number_Grpl,
        'inverse number - Inv': Number_Inv,
        'count plural - Count' : Number_Count,
        'plurale tantum - Ptan': Number_Ptan,
        'collective / mass / singulare tantum - Coll' : Number_Coll,
        'nominative / direct- Nom': Case_Nom,
        'accusative / oblique - Acc':Case_Acc,
        'absolutive - Abs':Case_Abs,
        'ergative- Erg':Case_Erg,
        'dative - Dat':Case_Dat,
        'genitive - Gen':Case_Gen,
        'vocative - Voc':Case_Voc,
        'instrumental / instructive - Ins':Case_Ins,
        'partitive - Par':Case_Par,
        'distributive - Dis':Case_Dis,
        'essive / prolative - Ess':Case_Ess,
        'translative / factive - Tra':Case_Tra,
        'comitative / associative - Com':Case_Com,
        'abessive / caritive / privative - Abe':Case_Abe,
        'causative / motivative / purposive - Cau':Case_Cau,
        'benefactive / destinative - Ben':Case_Ben,
        'considerative - Cns':Case_Cns,
        'comparative - Cmp':Case_Cmp,
        'equative - Equ':Case_Equ,
        'locative - Loc':Case_Loc,
        'lative / directional allative - Lat':Case_Lat,
        'terminative / terminal allative - Ter':Case_Ter,
        'inessive -Ine':Case_Ine,
        'illative / inlative - Ill':Case_Ill,
        'elative / inelative - Ela':Case_Ela,
        'additive - Add':Case_Add,
        'adessive - Ade':Case_Ade,
        'allative / adlative - All':Case_All,
        'ablative / adelative - Abl':Case_Abl,
        'superessive - Sup':Case_Sup,
        'superlative - Spl':Case_Spl,
        'delative / superelative- Del':Case_Del,
        'subessive - Sub':Case_Sub,
        'sublative - Sbl':Case_Sbl,
        'subelative- Sbe':Case_Sbe,
        'perlative - Per':Case_Per,
        'temporal- Tem':Case_Tem,
        'indefinite - Ind': Definite_Ind,
        'specific indefinite - Spec':Definite_Spec,
        'definite - Def':Definite_Def,
        'construct state / reduced definiteness - Cons': Definite_Cons,
        'complex- Com':Definite_Com,
        'positive, first degree - Pos': Degree_Pos,
        'equative - Equ ': Degree_Equ,
        'comparative, second degree- Cmp': Degree_Cmp,
        'superlative, third degree - Sup':Degree_Sup,
        'absolute superlative - Abs' : Degree_Abs,
        'converb, transgressive, adverbial participle, verbal adverb - Conv':VerbForm_Conv,
        'finite verb- Fin' :VerbForm_Fin,
        'gerundive- Gdv':VerbForm_Gdv,
        'gerund- Ger': VerbForm_Ger,
        'infinitive - Inf':VerbForm_Inf,
        'participle, verbal adjective - Part' :VerbForm_Part,
        'supine - Sup':VerbForm_Sup,
        'verbal noun, masdar- Vnoun':VerbForm_Vnoun,
        'admirative - Adm':Mood_Adm,
        'conditional - Cnd' : Mood_Cnd,
        'desiderative - Des' : Mood_Des,
        'imperative - Imp' :Mood_Imp,
        'indicative or realis -Ind' :Mood_Ind,
        'irrealis - Irr' : Mood_Irr,
        'jussive / injunctive - Jus' : Mood_Jus,
        'necessitative - Nec':Mood_Nec,
        'optative - Opt' :Mood_Opt,
        'potential - Pot ': Mood_Pot,
        'purposive-Prp':Mood_Prp,
        'quotative - Qot' : Mood_Qot,
        'subjunctive / conjunctive- Sub' :Mood_Sub,
        'future tense - Fut' :Tense_Fut,
        'imperfect - Imp' : Tense_Imp,
        'past tense / preterite / aorist - Past':Tense_Past,
        'pluperfect - Pqp' : Tense_Pqp,
        'present / non-past tense / aorist - Pres' :Tense_Pres,
        'habitual aspect - Hab' :Aspect_Hab,
        'imperfect aspect - Imp' :Aspect_Imp,
        'iterative / frequentative aspect - Iter':Aspect_Iter,
        'perfect aspect - Perf':Aspect_Perf,
        'progressive aspect - Prog':Aspect_Prog,
        'prospective aspect - Prosp':Aspect_Prosp,
        'active or actor-focus voice - Act':Voice_Act,
        'antipassive voice - Antip ':Voice_Antip,
        'beneficiary-focus voice - Bfoc':Voice_Bfoc,
        'causative voice - Cau':Voice_Cau,
        'direct voice - Dir':Voice_Dir,
        'inverse voice - Inv':Voice_Inv,
        'location-focus voice - Lfoc':Voice_Lfoc,
        'middle voice - Mid':Voice_Mid,
        'passive or patient-focus voice - Pass':Voice_Pass,
        'reciprocal voice - Rcp':Voice_Rcp,
        'firsthand - Fh' :Evident_Fh,
        'non-firsthand - Nfh':Evident_Nfh,
        'positive, affirmative-Pos':Polarity_Pos,
        'negative - Neg':Polarity_Neg,
        'zero person - 0':Person_0,
        'first person - 1': Person_1,
        'second person - 2': Person_2,
        'third person - 3':Person_3,
        'fourth person - 4': Person_4,
        'referent elevating - Elev' :Polite_Elev,
        'formal register - Form' :Polite_Form,
        'speaker humbling - Humb': Polite_Humb,
        'informal register - Infm':Polite_Infm,
        'inclusive - In': Clusivity_In,
        'exclusive- Ex' : Clusivity_Ex 
    }
    return feats

# x=all_features(text)
# print(x)

