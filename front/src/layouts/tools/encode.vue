<template>
  <div>
    <nav-bar></nav-bar>
      <el-container style="min-height:300px;">
        <el-aside width="140px">
          <side-bar></side-bar>
        </el-aside>
        <el-main>
        <el-form label-width="100px">
          <el-form-item label="输入">
            <el-input type="textarea" v-model="input"></el-input>
          </el-form-item>
          <el-form-item label="编码">
            <el-button type="primary" @click="hexEncode">hex</el-button>
            <el-button type="primary" @click="urlEncode">url</el-button>
            <el-button type="primary" @click="mysqlEncode">mysql</el-button>
          </el-form-item>
          <el-form-item label="解码">
            <el-button type="primary" @click="urlDecode">url</el-button>
          </el-form-item>
          <el-form-item label="输出">
            <el-input type="textarea" v-model="output"></el-input>
          </el-form-item>
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
  name: 'Encode',
  components: {
    NavBar,
    FootBar,
    SideBar
  },
  created () {
  },
  data () {
    return {
      input: '',
      output: ''
    }
  },
  computed: {
  },
  methods: {
    hexEncode () {
      this.output = ''
      for (let i = 0; i < this.input.length; i++) {
        this.output += '\\x' + (this.input.charCodeAt(i).toString(16))
      }
    },
    urlEncode () {
      this.output = encodeURI(this.input)
    },
    mysqlEncode () {
      this.output = "concat('" + this.input.split('').join("','") + "')"
    },
    urlDecode () {
      this.input = decodeURI(this.output)
    }
  }
}
</script>

<style scoped>

</style>
