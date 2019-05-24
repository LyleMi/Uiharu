<template>
  <div>
    <nav-bar></nav-bar>
      <el-container style="min-height:300px;">
        <el-aside width="140px">
          <side-bar></side-bar>
        </el-aside>
        <el-main>
          <el-form label-width="100px">
            <el-form-item label="Url">
              <el-input v-model="url" auto-complete="off"></el-input>
            </el-form-item>
            <!-- method -->
            <!-- param -->
            <!-- data -->
            <!-- cookie -->
            <!-- header -->
          </el-form>
        </el-main>
      </el-container>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
import { SideBar } from '@/components/tools'
export default {
  name: 'Request',
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

<style scoped>

</style>
