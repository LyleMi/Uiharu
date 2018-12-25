#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from server.controller.base import JSONBaseHandler
from schema.tables.application import Application
from schema.tables.project import Project
from schema.tables.domain import Domain
from schema.tables.ip import IP
from schema.tables.vuln import Vuln


class ProjectHandler(JSONBaseHandler):

    objcls = Project


class DomainHandler(JSONBaseHandler):

    objcls = Domain


class IPHandler(JSONBaseHandler):

    objcls = IP


class VulnHandler(JSONBaseHandler):

    objcls = Vuln


class ApplicationHandler(JSONBaseHandler):

    objcls = Application
