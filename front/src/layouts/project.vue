<template>
    <div>
        <nav-bar></nav-bar>
        <el-row class="tac">
        <el-col :span="2">
          <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            >
            <el-menu-item>
              <i class="el-icon-menu"></i>
              <span slot="title">所有项目</span>
            </el-menu-item>
            <el-menu-item>
              <i class="el-icon-document"></i>
              <span slot="title">域名列表</span>
            </el-menu-item>
            <el-menu-item>
              <i class="el-icon-setting"></i>
              <span slot="title">应用列表</span>
            </el-menu-item>
            <el-menu-item>
              <i class="el-icon-setting"></i>
              <span slot="title">漏洞列表</span>
            </el-menu-item>
          </el-menu>
        </el-col>
      </el-row>
        <foot-bar class="footbar"></foot-bar>
    </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
// import { api } from '@/utils/api'
export default {
  name: 'Project',
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
