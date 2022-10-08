import abc
from models import ArticleModel

from app.services.ml.collector import Collector
from app.services.ml.evaluator import Evaluator

class AbstractMlService(abc.ABC):

    @abc.abstractmethod
    def score(self, article: ArticleModel, okved: str, oborot: str, role: str) -> float:
        ...

    @abc.abstractmethod
    def add_article(self, article: ArticleModel):
        ...

    @abc.abstractmethod
    def is_equal(self, article1: ArticleModel, article2: ArticleModel) -> bool:
        ...

    @abc.abstractmethod
    def get_trend(self) -> str:
        ...

    @abc.abstractmethod
    def get_insight(self) -> str:
        ...


class MlService(AbstractMlService):

    collector: Collector
    evaluator: Evaluator

    def __init__(self, base_score_ratio=0.1, okved_ratio=0.5):
        '''
        okved_ratio: the ratio of similarity with okved, in whole similarity evaluation

        base_score_ratio: the ratio of similarity with role, in whole similarity evaluation
        '''

        assert base_score_ratio > 0 and okved_ratio >= 0
        assert base_score_ratio+okved_ratio <= 1

        self.evaluator = Evaluator()
        self.collector = Collector()

        self.okved_ratio = okved_ratio
        self.base_score_ratio = base_score_ratio

    def add_article(self, article: ArticleModel):
        self.collector.push(article)

    def get_base_score(self, article: ArticleModel, role: str):
        return self.evaluator.compare_text_with_kwords(article.title, role)

    def score(self, article: ArticleModel, okved: str, oborot: str, role: str) -> float:
        sim_base = self.get_base_score(article, role)
        sim_okv = self.evaluator.compare_text_with_kwords(article.title, okved)
        sim_oborot = self.evaluator.compare_text_with_kwords(article.title, oborot)

        return  self.base_score_ratio * sim_base + \
                self.okved_ratio * sim_okv + \
                (1-self.okved_ratio - self.base_score_ratio)*sim_oborot

    def is_equal(self, article1: ArticleModel, article2: ArticleModel) -> bool:

        # FIXME: may be not the best way. Can be implemented using summarisation

        return self.evaluator.similarity(article1.title, article2.title) >= 0.5
        

    def get_trend(self) -> list(str):
        recent_news = self.collector.get_recent_news()
        documents = [news.text for news in recent_news]
        
        stoplist = ['счет', 'тонна', 'рынок', 'заявка', 'актив', 'организация', ' ', 'доллар', 'рубль', 'долларов', 'рублей', 'выручка', 'россия', 'президент', 'акция', 'миллиард', 'миллион', 'состояние', 'прибыль', 'составить', 'итог', 'он', 'на', 'процент', "c","а","алло","без", 'этот', 'тот', 'те', 'они', "белый","близко","более","больше","большой","будем","будет","будете","будешь","будто","буду","будут","будь","бы","бывает","бывь","был","была","были","было","быть","в","важная","важное","важные","важный","вам","вами","вас","ваш","ваша","ваше","ваши","вверх","вдали","вдруг","ведь","везде","вернуться","весь","вечер","взгляд","взять","вид","видел","видеть","вместе","вне","вниз","внизу","во","вода","война","вокруг","вон","вообще","вопрос","восемнадцатый","восемнадцать","восемь","восьмой","вот","впрочем","времени","время","все","все еще","всегда","всего","всем","всеми","всему","всех","всею","всю","всюду","вся","всё","второй","вы","выйти","г","где","главный","глаз","говорил","говорит","говорить","год","года","году","голова","голос","город","да","давать","давно","даже","далекий","далеко","дальше","даром","дать","два","двадцатый","двадцать","две","двенадцатый","двенадцать","дверь","двух","девятнадцатый","девятнадцать","девятый","девять","действительно","дел","делал","делать","делаю","дело","день","деньги","десятый","десять","для","до","довольно","долго","должен","должно","должный","дом","дорога","друг","другая","другие","других","друго","другое","другой","думать","душа","е","его","ее","ей","ему","если","есть","еще","ещё","ею","её","ж","ждать","же","жена","женщина","жизнь","жить","за","занят","занята","занято","заняты","затем","зато","зачем","здесь","земля","знать","значит","значить","и","иди","идти","из","или","им","имеет","имел","именно","иметь","ими","имя","иногда","их","к","каждая","каждое","каждые","каждый","кажется","казаться","как","какая","какой","кем","книга","когда","кого","ком","комната","кому","конец","конечно","которая","которого","которой","которые","который","которых","кроме","кругом","кто","куда","лежать","лет","ли","лицо","лишь","лучше","любить","люди","м","маленький","мало","мать","машина","между","меля","менее","меньше","меня","место","миллионов","мимо","минута","мир","мира","мне","много","многочисленная","многочисленное","многочисленные","многочисленный","мной","мною","мог","могу","могут","мож","может","может быть","можно","можхо","мои","мой","мор","москва","мочь","моя","моё","мы","на","наверху","над","надо","назад","наиболее","найти","наконец","нам","нами","народ","нас","начала","начать","наш","наша","наше","наши","не","него","недавно","недалеко","нее","ней","некоторый","нельзя","нем","немного","нему","непрерывно","нередко","несколько","нет","нею","неё","ни","нибудь","ниже","низко","никакой","никогда","никто","никуда","ним","ними","них","ничего","ничто","но","новый","нога","ночь","ну","нужно","нужный","нх","о","об","оба","обычно","один","одиннадцатый","одиннадцать","однажды","однако","одного","одной","оказаться","окно","около","он","она","они","оно","опять","особенно","остаться","от","ответить","отец","откуда","отовсюду","отсюда","очень","первый","перед","писать","плечо","по","под","подойди","подумать","пожалуйста","позже","пойти","пока","пол","получить","помнить","понимать","понять","пор","пора","после","последний","посмотреть","посреди","потом","потому","почему","почти","правда","прекрасно","при","про","просто","против","процентов","путь","пятнадцатый","пятнадцать","пятый","пять","работа","работать","раз","разве","рано","раньше","ребенок","решить","россия","рука","русский","ряд","рядом","с","с кем","сам","сама","сами","самим","самими","самих","само","самого","самой","самом","самому","саму","самый","свет","свое","своего","своей","свои","своих","свой","свою","сделать","сеаой","себе","себя","сегодня","седьмой","сейчас","семнадцатый","семнадцать","семь","сидеть","сила","сих","сказал","сказала","сказать","сколько","слишком","слово","случай","смотреть","сначала","снова","со","собой","собою","советский","совсем","спасибо","спросить","сразу","стал","старый","стать","стол","сторона","стоять","страна","суть","считать","т","та","так","такая","также","таки","такие","такое","такой","там","твои","твой","твоя","твоё","те","тебе","тебя","тем","теми","теперь","тех","то","тобой","тобою","товарищ","тогда","того","тоже","только","том","тому","тот","тою","третий","три","тринадцатый","тринадцать","ту","туда","тут","ты","тысяч","у","увидеть","уж","уже","улица","уметь","утро","хороший","хорошо","хотел бы","хотеть","хоть","хотя","хочешь","час","часто","часть","чаще","чего","человек","чем","чему","через","четвертый","четыре","четырнадцатый","четырнадцать","что","чтоб","чтобы","чуть","шестнадцатый","шестнадцать","шестой","шесть","эта","эти","этим","этими","этих","это","этого","этой","этом","этому","этот","эту","я","являюсь"]
    
        texts = [[re.sub(r'[^а-яА-ЯёЁ ]', '', word) for word in document.split() if word.lower() not in stoplist]
             for document in documents]

        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1

        texts = [[token for token in text if frequency[token] > 1 and len(token.strip()) > 3 and token.isdigit() == False]
                 for text in texts]
        
        # To normal form:
        morph = pymorphy2.MorphAnalyzer()
        texts = [[morph.parse(word)[0].normal_form for word in text] for text in texts]

        texts = [[word for word in text if word.lower() not in stoplist]
             for text in texts]

        bigram = Phrases(texts, min_count=20)
        for idx in range(len(texts)):
            for token in bigram[texts[idx]]:
                if '_' in token:
                    # Token is a bigram, add to document.
                    texts[idx].append(token)
        
        # Create dictionary
        dictionary = corpora.Dictionary(texts)

        # Filter out words that occur less than X documents
        dictionary.filter_extremes(no_below=10)

        # Create the corpus.  This is a Bag of Words representation.
        corpus = [dictionary.doc2bow(text) for text in texts]


        temp = dictionary[0]
        id2word = dictionary.id2token
        num_topics = 3

        model = LdaModel(
            corpus=corpus,
            id2word=id2word,
            chunksize=2000,
            alpha='auto',
            eta='auto',
            iterations=100,
            num_topics=num_topics,
            passes=8,
            eval_every=None
        )
        
        max_sum = 0
        best_index = 0
        for best_count in range(num_topics):
            probabilities = [value[1] for value in model.show_topic(topicid=best_count, topn=10)]
            probabilities_sum = sum(probabilities)
            if probabilities_sum > max_sum:
                max_sum = probabilities_sum
                best_index = best_count

        topics = [value[0] for value in model.show_topic(topicid=best_index, topn=10)]

        info_news = []
        for text in range(len(texts)):
            tf = []
            values = collections.Counter(texts[text])
            tf = sum([values[word] / len(texts[text]) for word in topics])
            info_news.append([text, tf])

        info_news.sort(key=lambda x: x[1], reverse=True)
        index_best_news = [value[0] for value in info_news][:2]
        
        trends = [documents[i] for i in index_best_news]
        return trends

    def get_insight(self) -> str:
        raise NotImplementedError()
