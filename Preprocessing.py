import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity


class preprocessing:

    def __init__(self,input):
        self.imput=input
        #nltk.download('all')

        
        
    def lowercasing(self,input):
        lower_string=input.lower()        
        return lower_string
        
    def tokenization(self,input):
        token_string=word_tokenize(input)
        
        return token_string
        
    def stopwordemoval(self,input):
        stop_words=set(stopwords.words('english'))
        token_word=self.tokenization(input)
        stop_word_rm=[word for word in token_word if not word in stop_words]
        
        return stop_word_rm
        
    def stemming(self,input):
        ps = PorterStemmer()
        stem_word=ps.stem(input)
        return stem_word
        
    def lemmatization(self,input):
        
        return lemmatization_string
        
    def tfidf(self,input):
        tfid=TfidfVectorizer(max_df=0.90, min_df=2,max_features=1000,stop_words='english')

        tfid_mat=tfid.fit_transform(input)

        df_tf= pd.DataFrame(tfid_mat.todense())
        
        return df_tf
        
    def bagofwords(self,input):
        countvector=CountVectorizer(ngram_vect=(1,1),stop_words='english')

        countvectmat=countvector.fit_transform(input)

        countvectfr= pd.DataFrame(countvectmat.todense())
        
        return countvectfr
        
    def cosinesimilarity(self,vectormatrix,vector1,vector2):
        cosine_matrix = cosine_similarity(vectormatrix)
        return create_dataframe(cosine_matrix,[vector1,vector1])