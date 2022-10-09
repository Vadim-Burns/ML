from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

import json
import pickle

class Evaluator:
    model: SentenceTransformer
    def __init__(self,
    path_to_okved='./app/services/ml/okved.json', 
    path_to_tfidf='./app/services/ml/tfidf1.pkl', 
    path_to_logreg='./app/services/ml/classifier.pkl', 
    model_name='paraphrase-multilingual-mpnet-base-v2'
    ) -> None:
        self.model = SentenceTransformer(f"sentence-transformers/{model_name}")
        self.data_okveds = json.load(open(path_to_okved))
        self.tfidf = pickle.load(open(path_to_tfidf, "rb"))
        self.simple_model = pickle.load(open(path_to_logreg, "rb"))


    def similarity(self, text1, text2):
        embd_a = self.model.encode(text1)
        embd_b = self.model.encode(text2)

        sim_score = cos_sim(embd_a, embd_b) 

        return sim_score[0][0]

    def compare_text_with_kwords(self, text, kwords):
        kwords_l = kwords.split()
        sim = 0
        n = len(kwords_l)
        for kword in kwords_l:
            sim += self.similarity(kword, text)
        return sim / n
    