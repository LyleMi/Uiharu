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
        self.getObject(Project)

    def post(self):
        self.postObject(Project)

    def put(self):
        self.putObject(Project)

    def delete(self):
        self.deleteObject(Project)


class AssetHandler(BaseHandler):

    def get(self):
        self.getObject(Asset)

    def post(self):
        self.postObject(Asset)

    def put(self):
        self.putObject(Asset)

    def delete(self):
        self.deleteObject(Asset)


class VulnHandler(BaseHandler):

    def get(self):
        self.getObject(Vuln)

    def post(self):
        self.postObject(Vuln)

    def put(self):
        self.putObject(Vuln)

    def delete(self):
        self.deleteObject(Vuln)


class ApplicationHandler(BaseHandler):

    def get(self):
        self.getObject(Application)

    def post(self):
        self.postObject(Application)

    def put(self):
        self.putObject(Application)

    def delete(self):
        self.deleteObject(Application)
