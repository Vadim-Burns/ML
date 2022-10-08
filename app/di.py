import inject

from repositories import AbstractScoreRepo, AbstractArticleRepo
from repositories import ScoreRepo, ArticleRepo


def DI():
    def di_configuration(binder):
        binder.bind(AbstractArticleRepo, ArticleRepo())
        binder.bind(AbstractScoreRepo, ScoreRepo())

    inject.configure_once(di_configuration)
