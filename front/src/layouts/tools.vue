<template>
  <div>
    <nav-bar></nav-bar>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
// import { api } from '@/utils/api'
export default {
  name: 'Tools',
  components: {
    NavBar,
    FootBar
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
