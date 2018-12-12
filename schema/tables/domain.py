#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT, TIMESTAMP
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid
from common.utils import now


class Domain(BaseTable):

    __tablename__ = 'domain'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    pid = Column(VARCHAR(32))
    domain = Column(VARCHAR(200))
    ips = Column(VARCHAR(200))
    desc = Column(VARCHAR(1024))
    created = Column(TIMESTAMP, default=now)
    required = ['pid', 'domain', 'ips', 'desc']
