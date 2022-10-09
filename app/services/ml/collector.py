from app.models import ArticleModel
from datetime import date, datetime, timedelta

class Collector:
    recent_news: list
    def __init__(self, history_length=30) -> None:
        """
        @param history_length: количество дней, сохраняемых моделью
        """
        self.recent_news = []
        self.history_lenth = history_length

    def push(self, article: ArticleModel):
        cur_date = article.publish_date
        while len(self.recent_news) != 0 and (cur_date - self.recent_news[0].publish_date) / timedelta(days=1) > self.history_lenth:
            self.recent_news.pop(0)
        self.recent_news.append(article)

    def get_recent_news(self):
        return self.recent_news