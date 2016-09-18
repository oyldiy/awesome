import orm
from models import User, Blog, Comment

def test():
	**kw={}
    yield from orm.create_pool(loop,**kw);
    #  __pool = await aiomysql.create_pool(
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
for x in test():
    pass