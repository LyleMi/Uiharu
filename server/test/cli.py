#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests


class Cli(object):

    def __init__(self, url):
        super(Cli, self).__init__()
        self.url = url
        self.s = requests.session()

    def addProject(self, name="name", target="target", desc="desc"):
        data = {
            "name": name,
            "target": target,
            "desc": desc,
        }
        self.post("project", data=data)

    def getProject(self):
        self.get("project")

    def addAsset(self, pid="pid", atype="atype", data="data", desc="desc"):
        data = {
            "pid": pid,
            "data": data,
            "atype": atype,
            "desc": desc,
        }
        self.post("asset", data=data)

    def getAsset(self):
        self.get("asset")

    def addVuln(self, pid="pid",  vtype="vtype", data="data", desc="desc"):
        data = {
            "pid": pid,
            "data": data,
            "atype": atype,
            "desc": desc,
        }
        self.post("vuln", data=data)

    def getVuln(self):
        self.get("vuln")

    def addApplication(self, pid="pid", data="data", desc="desc"):
        data = {
            "pid": pid,
            "data": data,
            "desc": desc,
        }
        self.post("application", data=data)

    def getApplication(self):
        self.get("application")


if __name__ == '__main__':
    url = "http://127.0.0.1/"
    c = Cli(url)
    c.addProject()
    c.getProject()
    c.addAsset()
    c.getAsset()
    c.addVuln()
    c.getVuln()
    c.addApplication()
    c.getApplication()
