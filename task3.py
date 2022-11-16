from sqlalchemy import create_engine,Column, String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# 定义Jiker对象:
class DBOperation(Base):
    # 表的名字:
    __tablename__ = 'testtb'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(40))


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:1234@localhost:3306/flaskpythondb?charset=utf8", max_overflow=5)
    # Base.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # # 创建session对象:
    session = DBSession()
    new_data = DBOperation(title="paydays",author="zhangdawei")
    session.add(new_data)
    session.commit()





    # jikers = session.query(DBOperation).all()
    #
    # for item in jikers:
    #     print(item.tostr())
    #
    # # 创建新Jiker对象:
    # new_jiker = DBOperation(title='java project', author='hexter')
    # session.add(new_jiker)
    # # 提交即保存到数据库:
    # session.commit()