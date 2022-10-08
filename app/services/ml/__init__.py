import abc
from models import ArticleModel


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

    def add_article(self, article: ArticleModel):
        pass

    def score(self, article: ArticleModel, okved: str, oborot: str, role: str) -> float:
        import random
        return random.uniform(0, 1)

    def is_equal(self, article1: ArticleModel, article2: ArticleModel) -> bool:
        return False

    def get_trend(self) -> str:
        return "trend"

    def get_insight(self) -> str:
        return "insight"
