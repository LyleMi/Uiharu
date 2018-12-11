#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT, TIMESTAMP
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid
from common.utils import now


class Project(BaseTable):

    __tablename__ = 'project'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    name = Column(VARCHAR(200))
    target = Column(VARCHAR(200))
    desc = Column(VARCHAR(4096))
    created = Column(TIMESTAMP, default=now)
    required = ['name', 'target', 'desc']
