from cgi import print_arguments
import sys
sys.path.append('../')


from model.evaluator import Evaluator

model = Evaluator()

texts = ['Люди совершают самоубийства чаще, чем обычно, в России', 
         'В России больше людей стало совершать суицид',
         'Крымский мост частично обрушился после взрыва.', 
         'TAC: Зеленский подводит США на грань ядерной войны',
         'Зеленский призвал НАТО к превентивному удару по России'
         ]

def print_similarity(text_1, text_2):

    sm = model.similarity(text_1, text_2)
    print('='*60)
    print(f'similarity between: \n {text_1} \n and \n {text_2}: \n {sm}')

for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        print_similarity(texts[i], texts[j])
