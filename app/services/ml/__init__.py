import abc
from models import ArticleModel


class AbstractMlService(abc.ABC):

    @abc.abstractmethod
    def score(self, article: ArticleModel, okved: str, oborot: str) -> float:
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

    def score(self, article: ArticleModel, okved: str, oborot: str) -> float:
        pass

    def is_equal(self, article1: ArticleModel, article2: ArticleModel) -> bool:
        pass

    def get_trend(self) -> str:
        pass

    def get_insight(self) -> str:
        pass
