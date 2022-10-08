from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

class Evaluator:
    model: SentenceTransformer
    def __init__(self, model_name='paraphrase-multilingual-mpnet-base-v2') -> None:
        self.model = SentenceTransformer(f"sentence-transformers/{model_name}")
    
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
    