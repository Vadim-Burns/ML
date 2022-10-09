import abc
from models import ArticleModel, ArticleFullModel
from repositories import AbstractScoreRepo, AbstractArticleRepo
from services import AbstractMlService
import inject


class AbstractSkService(abc.ABC):

    @abc.abstractmethod
    def process_article(self, article: ArticleFullModel):
        ...


class SkService(AbstractSkService):

    @inject.autoparams('score_repo', 'article_repo', 'ml_service')
    def __init__(self, score_repo: AbstractScoreRepo, article_repo: AbstractArticleRepo, ml_service: AbstractMlService):
        self._score_repo = score_repo
        self._article_repo = article_repo
        self._ml_service = ml_service

    def process_article(self, article: ArticleFullModel):
        print(article.title)
