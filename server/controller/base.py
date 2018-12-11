#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import tornado.escape
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def prepare(self):
        super(BaseHandler, self).prepare()
        self.json_data = None
        if self.request.body:
            try:
                self.json_data = tornado.escape.json_decode(self.request.body)
            except ValueError as e:
                print(e)

    def get_argument(self, arg, default=None):
        if self.request.method in ['POST', 'PUT'] and self.json_data:
            return self.json_data.get(arg, default)
        else:
            return super(BaseHandler, self).get_argument(arg, default)

    def on_finish(self):
        self.db.flush()
        self.db.close()

    def ok(self, data):
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.write(json.dumps({"status": "ok", "data": data}))

    def error(self, status_code, msg):
        self.set_status(status_code)
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.write(json.dumps({"msg": msg}))

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PUT, DELETE')

    def getObject(self, cls):
        uid = self.get_argument('uid', None)
        if uid is None:
            return self.ok(cls.getAll(True))
        return cls.get(self.db, uid)

    def postObject(self, cls):
        data = {}
        for r in cls.required:
            data[r] = self.get_argument(r, None)
            if data[r] is None:
                return self.error(404, "%s is required" % r)
        o = cls.add(**data)
        if o:
            return self.ok("suc")
        else:
            return self.ok("fail")

    def putObject(self, cls):
        uid = self.get_argument('uid', None)
        if uid is None:
            return self.error(404, "uid is required")
        data = {}
        for r in cls.required:
            tmp = self.get_argument(r, None)
            if tmp is not None:
                data[r] = tmp
        o = cls.update(uid, **data)
        if o:
            return self.ok("suc")
        else:
            return self.ok("fail")

    def deleteObject(self, cls):
        uid = self.get_argument('uid', None)
        if uid is None:
            return self.error(404, "uid is required")
        if cls.delete(uid):
            return self.ok('suc')
        else:
            return self.ok('fail')
