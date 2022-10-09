from cgi import print_arguments
import sys
sys.path.append('../')
sys.path.append('../app')

from app.services.ml.evaluator import Evaluator

model = Evaluator(
    path_to_okved='../app/services/ml/okved.json', 
    path_to_tfidf='../app/services/ml/tfidf1.pkl', 
    path_to_logreg='../app/services/ml/classifier.pkl'
    )

texts = ['Каждый отказ представить те же документы по разным требованиям влечет штраф, подтвердил суд',
         'Цены на цветной металл растут из-за опасений прекращения поставок'
         ]

kwords = ['Ресурсы Материалы', 'Налоги Санкции Закон']

def print_similarity(text_1, text_2):

    sm = model.similarity(text_1, text_2)
    print('='*60)
    print(f'similarity between: \n {text_1} \n and \n {text_2}: \n {sm}')

def print_kwords_sim(text, kwords):
    sm = model.compare_text_with_kwords(text, kwords)

    print('='*60)
    print(f'Correspondance of: \n {kwords} \n to \n {text}: \n {sm}')

for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        print_similarity(texts[i], texts[j])

print('='*89)
print('-'*89)
print('='*89)

for i in range(len(texts)):
    for j in range(len(kwords)):
        print_kwords_sim(texts[i], kwords[j])
