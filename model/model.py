from email.mime import base
from model.evaluator import Evaluator
from model.collector import Collector

from datetime import date, datetime

class News:
    title: str
    text: str
    pub_date: datetime

    def __init__(self, title, text, pub_date: datetime) -> None:
        self.title = title
        self.text = text
        self.pub_date = pub_date


class ML:
    evaluator: Evaluator
    collector: Collector
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

    def get_trend(self, news: News):
        self.collector.push(news)
        recent_news = self.collector.get_recent_news()
        return ...

    def get_base_score(self, news: News, role: str):
        return self.evaluator.compare_text_with_kwords(news.title, role)

    def score(self, news: News, okved: str, oborot: str, role: str) -> float:
        self.collector.push(news)

        sim_base = self.get_base_score(news, role)
        sim_okv = self.evaluator.compare_text_with_kwords(news.title, okved)
        sim_oborot = self.evaluator.compare_text_with_kwords(news.title, oborot)

        return  self.base_score_ratio * sim_base + \
                self.okved_ratio * sim_okv + \
                (1-self.okved_ratio - self.base_score_ratio)*sim_oborot

    def is_equal(self, news1: News, news2: News):

        # FIXME: may be not the best way. Can be implemented using summarisation

        return self.evaluator.similarity(news1, news2) >= 0.5
        