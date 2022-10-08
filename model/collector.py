class Collector:
    recent_news: list
    def __init__(self, history_length) -> None:
        self.recent_news = []
        self.history_lenth = history_length

    def push(self, news):
        if len(self.recent_news) == self.history_length:
            self.recent_news.pop(0)
        self.recent_news.append(news)
