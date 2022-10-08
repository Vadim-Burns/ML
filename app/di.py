import inject

from repositories import AbstractScoreRepo, AbstractArticleRepo
from repositories import ScoreRepo, ArticleRepo

from services import AbstractMlService
from services import MlService


def DI():
    def di_configuration(binder):
        binder.bind(AbstractArticleRepo, ArticleRepo())
        binder.bind(AbstractScoreRepo, ScoreRepo())

        binder.bind(AbstractMlService, MlService())

    inject.configure_once(di_configuration)
