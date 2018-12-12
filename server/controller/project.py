#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from server.controller.base import BaseHandler
from schema.tables.application import Application
from schema.tables.project import Project
from schema.tables.domain import Domain
from schema.tables.ip import IP
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

    def options(self):
        pass


class DomainHandler(BaseHandler):

    def get(self):
        self.getObject(Domain)

    def post(self):
        self.postObject(Domain)

    def put(self):
        self.putObject(Domain)

    def delete(self):
        self.deleteObject(Domain)


class IPHandler(BaseHandler):

    def get(self):
        self.getObject(IP)

    def post(self):
        self.postObject(IP)

    def put(self):
        self.putObject(IP)

    def delete(self):
        self.deleteObject(IP)


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
