import Vue from 'vue'
import Router from 'vue-router'
import Project from '@/layouts/project/project'
import Domain from '@/layouts/project/domain'
import Application from '@/layouts/project/application'
import Vuln from '@/layouts/project/vuln'
import IPConv from '@/layouts/tools/ipconv'

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
    }
  ]
})
