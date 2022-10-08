from model.evaluator import Evaluator
from model.collector import Collector

from datetime import datetime

class News:
    title: str
    text: str
    pub_date: datetime

    def __init__(self, title, text, pub_date) -> None:
        self.title = title
        self.text = text
        self.pub_date = pub_date


class ML:
    evaluator: Evaluator
    collector: Collector
    def __init__(self, okved_ratio):
        '''
        okved_ratio: the ratio of similarity with okved, in whole similarity evaluation
        '''
        self.evaluator = Evaluator()
        self.collector = Collector()

        self.okved_ratio = okved_ratio

    def get_trend(self, news: News):
        self.collector.push(news)
        recent_news = self.collector.get_recent_news()
        return ...

    def score(self, news: News, okved: str, oborot: str, role: str) -> float:
        self.collector.push(news)

        sim_okv = self.evaluator.compare_text_with_kwords(news.title, okved)
        sim_oborot = self.evaluator.compare_text_with_kwords(news.title, oborot)

        return self.okved_ratio * sim_okv + (1-self.okved_ratio)*sim_oborot

    def is_equal(news1: News, news2: News):
        pass