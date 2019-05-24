import Vue from 'vue'
import Router from 'vue-router'
import Project from '@/layouts/project/project'
import Domain from '@/layouts/project/domain'
import Application from '@/layouts/project/application'
import Vuln from '@/layouts/project/vuln'
import IPConv from '@/layouts/tools/ipconv'
import Hash from '@/layouts/tools/hash'
import Encode from '@/layouts/tools/encode'
import Request from '@/layouts/tools/request'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Project',
      component: Project
    },
    {
      path: '/domain',
      name: 'Domain',
      component: Domain
    },
    {
      path: '/application',
      name: 'Application',
      component: Application
    },
    {
      path: '/vuln',
      name: 'Vuln',
      component: Vuln
    },
    {
      path: '/ipconv',
      name: 'IPConv',
      component: IPConv
    },
    {
      path: '/hash',
      name: 'Hash',
      component: Hash
    },
    {
      path: '/encode',
      name: 'Encode',
      component: Encode
    },
    {
      path: '/request',
      name: 'Request',
      component: Request
    }
  ]
})
