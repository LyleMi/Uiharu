#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT, TIMESTAMP
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid
from common.utils import now


class IP(BaseTable):

    __tablename__ = 'ip'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    pid = Column(VARCHAR(32))
    ip = Column(VARCHAR(200))
    desc = Column(VARCHAR(1000))
    created = Column(TIMESTAMP, default=now)
    required = ['pid', 'ip', 'desc']
