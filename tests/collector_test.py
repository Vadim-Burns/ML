from datetime import datetime
import sys
sys.path.append('../')
sys.path.append('../app')

from app.services.ml.collector import Collector
from app.models import ArticleModel

col = Collector()
ar1 = ArticleModel(title='a', text='aaa', publish_date=datetime(year=2011, month=1, day=1))
ar2 = ArticleModel(title='b', text='bbb', publish_date=datetime(year=2011, month=1, day=2))
ar3 = ArticleModel(title='c', text='ccc', publish_date=datetime(year=2011, month=2, day=1))

ar4 = ArticleModel(title='c', text='ccc', publish_date=datetime(year=2011, month=2, day=4))

ar5 = ArticleModel(title='d', text='ddd', publish_date=datetime(year=2011, month=2, day=20))

col.push(ar1)
col.push(ar2)
assert len(col.get_recent_news()) == 2

col.push(ar3)

assert len(col.get_recent_news()) == 2

col.push(ar4)

assert len(col.get_recent_news()) == 2
col.push(ar5)

assert len(col.get_recent_news()) == 3
print('='*89,'\n', '='*35, ' ','All tests passed!',' ', '='*35,'\n', '='*89,sep='')