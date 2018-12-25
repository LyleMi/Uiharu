#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import tornado.escape
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def set_default_headers(self):
        self.set_header('Server', 'PHP')


class JSONBaseHandler(BaseHandler):

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
        self.write(json.dumps({'status': 'ok', 'data': data}))

    def error(self, status_code, msg):
        self.set_status(status_code)
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.write(json.dumps({'status': 'error', 'msg': msg}))

    def set_default_headers(self):
        super(JSONBaseHandler, self).set_default_headers()
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.set_header('Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PUT, DELETE')

    def get(self):
        cls = self.objcls
        uid = self.get_argument('uid', None)
        if uid is not None:
            return self.ok(cls.get(uid).toStr())
        sort = self.get_argument('sort', None)
        limit = int(self.get_argument('limit', 10))
        page = int(self.get_argument('page', 1))
        offset = limit * (page - 1)
        filterKey = self.get_argument('filterKey', None)
        filterValue = self.get_argument('filterValue', None)
        items = cls.getAll(
            True,
            limit=limit,
            offset=offset,
            sort=sort,
            filterKey=filterKey,
            filterValue=filterValue
        )
        if items is False:
            return self.error(500, 'database error')
        items, count = items
        return self.ok({
            'items': items,
            'total': count
        })

    def post(self):
        cls = self.objcls
        data = {}
        for r in cls.required:
            data[r] = self.get_argument(r, None)
            if data[r] is None:
                return self.error(404, '%s is required' % r)
        if cls.add(**data):
            return self.ok('suc')
        else:
            return self.error(500, 'add data fail')

    def put(self):
        cls = self.objcls
        uid = self.get_argument('uid', None)
        if uid is None:
            return self.error(404, 'uid is required')
        data = {}
        for r in cls.required:
            tmp = self.get_argument(r, None)
            if tmp is not None:
                data[r] = tmp
        if cls.update(uid, **data):
            return self.ok('suc')
        else:
            return self.error(500, 'update data fail')

    def delete(self):
        cls = self.objcls
        uid = self.get_argument('uid', None)
        if uid is None:
            return self.error(404, 'uid is required')
        if cls.delete(uid):
            return self.ok('suc')
        else:
            return self.error(500, 'delete data fail')

    def options(self):
        pass
