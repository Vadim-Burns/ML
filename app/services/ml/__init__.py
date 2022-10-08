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
        

    def get_trend(self) -> str:
        recent_news = self.collector.get_recent_news()
        news_texts = [news.text for news in recent_news]
        raise NotImplementedError()

    def get_insight(self) -> str:
        raise NotImplementedError()
