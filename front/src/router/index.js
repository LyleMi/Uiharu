import Vue from 'vue'
import Router from 'vue-router'
import Project from '@/layouts/project'
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
      path: '/tools',
      name: 'Tools',
      component: Tools
    }
  ]
})
