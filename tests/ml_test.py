import sys
sys.path.append('./')
sys.path.append('./app')

from app.services.ml import MlService
from app.models import ArticleModel
from datetime import datetime

ar1 = ArticleModel(title='Белоусов прогнозирует нулевую экспортную пошлину на уголь в 2023 году', text='«Высокопоставленный украинский чиновник подтвердил российские сообщения о том, что за нападением стоит Украина. Чиновник на условиях анонимности из-за запрета правительства на обсуждение взрыва добавил, что спецслужбы Украины организовали взрыв, используя бомбу, загруженную в грузовик, который ехал по мосту», — пишет издание.', publish_date=datetime(year=2011, month=1, day=1))
ar2 = ArticleModel(title='О приостановке и возобновлении трудового договора нужно отчитываться в ПФР О приостановке и возобновлении трудового договора нужно отчитываться в ПФР \ Консультант Плюс © КонсультантПлюс, 1997-2022', text='Ранее Украина взяла ответственность за атаку на Крымский мост, однако позже в Киеве обвинили в этом Россию, передает Pravda.Ru. Объект был подорван 8 октября, после чего президент РФ Владимир Путин экстренно собрал правительственную комиссию по этому инциденту. Первые результаты обследования моста ожидаются 9 октября. СК РФ возбудил дело по факту взрыва, пишет РАПСИ.', publish_date=datetime(year=2011, month=1, day=2))
ar3 = ArticleModel(title='В', text='Дедлайн', publish_date=datetime(year=2011, month=2, day=1))

ar4 = ArticleModel(title='Г', text='Хак', publish_date=datetime(year=2011, month=2, day=4))

ar5 = ArticleModel(title='Д', text='Прикол', publish_date=datetime(year=2011, month=2, day=20))

service = MlService()
service.add_article(ar1)
service.add_article(ar2)
print(service.is_equal(ar1, ar2))
print(service.get_trend())
print(service.score(ar1, 'Огород', 'Кухня', 'Прикол'))

print(service.score(ar1, 'Финансы', 'Прогнозы', 'Инвестиции'))
