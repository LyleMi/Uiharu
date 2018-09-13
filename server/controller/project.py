#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from server.controller.base import BaseHandler
from schema.tables.application import Application
from schema.tables.project import Project
from schema.tables.asset import Asset
from schema.tables.vuln import Vuln


class ProjectHandler(BaseHandler):

    def get(self):
        return self.ok(Project.getAll(True))

    def post(self):
        name = self.get_argument('name', '')
        if not name:
            return self.error(404, "name is required")
        target = self.get_argument('target', '')
        if not target:
            return self.error(404, "target is required")
        desc = self.get_argument('desc', '')
        if not desc:
            return self.error(404, "desc is required")
        o = Project.add(name, target, desc)
        return self.ok("suc")


class AssetHandler(BaseHandler):

    def get(self):
        return self.ok(Asset.getAll(True))

    def post(self):
        pid = self.get_argument('pid', '')
        if not pid:
            return self.error(404, "pid is required")
        atype = self.get_argument('atype', '')
        if not atype:
            return self.error(404, "atype is required")
        data = self.get_argument('data', '')
        if not data:
            return self.error(404, "data is required")
        desc = self.get_argument('desc', '')
        if not desc:
            return self.error(404, "desc is required")
        o = Asset.add(pid, atype, data, desc)
        return self.ok("suc")


class VulnHandler(BaseHandler):

    def get(self):
        return self.ok(Vuln.getAll(True))

    def post(self):
        pid = self.get_argument('pid', '')
        if not pid:
            return self.error(404, "pid is required")
        vtype = self.get_argument('vtype', '')
        if not vtype:
            return self.error(404, "vtype is required")
        data = self.get_argument('data', '')
        if not data:
            return self.error(404, "data is required")
        desc = self.get_argument('desc', '')
        if not desc:
            return self.error(404, "desc is required")
        o = Vuln.add(pid, name, vtype, desc)
        return self.ok("suc")


class ApplicationHandler(BaseHandler):

    def get(self):
        return self.ok(Application.getAll(True))

    def post(self):
        pid = self.get_argument('pid', '')
        if not pid:
            return self.error(404, "pid is required")
        data = self.get_argument('data', '')
        if not data:
            return self.error(404, "data is required")
        desc = self.get_argument('desc', '')
        if not desc:
            return self.error(404, "desc is required")
        o = Application.add(pid, data, desc)
        return self.ok("suc")
