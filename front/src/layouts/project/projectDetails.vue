<template>
    <div>
      <nav-bar></nav-bar>
      <foot-bar></foot-bar>
    </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
import { SideBar } from '@/components/project'
export default {
  name: 'ProjectDetails',
  components: {
    NavBar,
    FootBar,
    SideBar
  },
  created () {
    this.getDetails()
  },
  data () {
    return {
      data: {
        name: '',
        target: '',
        desc: ''
      },
      dialogVisible: false
    }
  },
  methods: {
    getDetails () {
    }
  }
</script>

<style scoped>
</style>
