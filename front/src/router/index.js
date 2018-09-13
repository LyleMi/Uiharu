import Vue from 'vue'
import Router from 'vue-router'
import Project from '@/layouts/project'
import Domain from '@/layouts/domain'
import Application from '@/layouts/application'
import Vuln from '@/layouts/vuln'
import Tools from '@/layouts/tools'

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
      path: '/tools',
      name: 'Tools',
      component: Tools
    }
  ]
})
