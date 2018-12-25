#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from copy import deepcopy

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import as_declarative

from schema.db import engine


@as_declarative()
class BaseTable(object):

    def toStr(self, blist=[]):
        s = deepcopy(self.__dict__)
        del(s['_sa_instance_state'])
        for i in s:
            if isinstance(s[i], datetime.datetime):
                s[i] = str(s[i])
        for b in blist:
            if b in s:
                del s[b]
        return s

    @classmethod
    def getAll(cls, toStr=False, blist=[],
               limit=-1, offset=0,
               sort=None,
               filterKey=None, filterValue=None
               ):
        try:
            cls.db.commit()
            ret = cls.db.query(cls)
            if filterKey and filterValue:
                ret = ret.filter(
                    getattr(cls, filterKey).like('%%%s%%' % filterValue)
                )
            count = ret.count()
            if sort:
                ret = ret.order_by(sort)
            if limit != -1:
                ret = ret.limit(limit).offset(offset)
            else:
                ret = ret.all()
            if toStr:
                return [i.toStr(blist) for i in ret], count
            else:
                return ret, count
        except Exception as e:
            print(repr(e))
            cls.db.rollback()
            return False

    @classmethod
    def count(cls, filterKey=None, filterValue=None):
        ret = cls.db.query(cls)
        if filterKey and filterValue:
            ret = ret.filter(
                getattr(cls, filterKey).like('%%%s%%' % filterValue)
            )
        return ret.count()

    @classmethod
    def get(cls, uid):
        try:
            cls.db.commit()
            obj = cls.db.query(cls).filter(cls.uid == uid)
        except Exception as e:
            print(repr(e))
            cls.db.rollback()
            return False
        if obj.count() < 1:
            return None
        else:
            return obj.one()

    @classmethod
    def add(cls, **kwargs):
        try:
            o = cls()
            for key in kwargs:
                o.__setattr__(key, kwargs[key])
            cls.db.add(o)
            cls.db.commit()
        except Exception as e:
            print(repr(e))
            cls.db.rollback()
            return False
        return True

    @classmethod
    def update(cls, uid, **kwargs):
        try:
            cls.db.query(cls).filter(cls.uid == uid).update(kwargs)
            cls.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            cls.db.rollback()
            return False

    @classmethod
    def delete(cls, uid):
        try:
            obj = cls.db.query(cls).filter(cls.uid == uid).delete()
            cls.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            cls.db.rollback()
            return False


def DBSession(forceNew=False):
    if hasattr(DBSession, "_db") and not forceNew:
        return DBSession._db
    # 初始化数据库
    session_factory = sessionmaker()
    session_factory.configure(bind=engine)
    BaseTable.metadata.create_all(engine)
    DBSession._db = scoped_session(session_factory)
    return DBSession._db


BaseTable.db = DBSession()
