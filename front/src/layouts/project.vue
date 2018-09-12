<template>
    <div>
      <nav-bar></nav-bar>
      <side-bar></side-bar>
      <foot-bar></foot-bar>
    </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
import { SideBar } from '@/components/project'
// import { api } from '@/utils/api'
export default {
  name: 'Project',
  components: {
    NavBar,
    FootBar,
    SideBar
  },
  created () {
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
