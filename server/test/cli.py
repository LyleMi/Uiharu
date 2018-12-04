#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from saker.main import Saker


class Cli(Saker):

    def addProject(self, name="name", target="target", desc="desc"):
        data = {
            "name": name,
            "target": target,
            "desc": desc,
        }
        self.post("project", data=data)
        print(self.lastr.content)

    def getProject(self):
        self.get("project")
        print(self.lastr.content)

    def updateProject(self, uid, name="name2333", target="target", desc="desc"):
        data = {
            "name": name,
            "target": target,
            "desc": desc,
        }
        self.post("project", data=data)
        print(self.lastr.content)

    def deleteProject(self, uid):
        params = {
            "uid": uid
        }
        self.delete("project", params=params)
        print(self.lastr.content)

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

    def addVuln(self, pid="pid", vtype="vtype", data="data", desc="desc"):
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
    url = "http://127.0.0.1:8888/"
    c = Cli(url)
    uid = "c2809c854dc34d969c7d3556b49d3ad8"
    # c.addProject()
    # c.deleteProject()
    c.updateProject(uid)
    c.getProject()
    # c.addAsset()
    # c.getAsset()
    # c.addVuln()
    # c.getVuln()
    # c.addApplication()
    # c.getApplication()
