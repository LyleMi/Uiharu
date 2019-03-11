<template>
  <div>
    <nav-bar></nav-bar>
      <el-container style="min-height:300px;">
        <el-aside width="140px">
          <side-bar></side-bar>
        </el-aside>
        <el-main>
        <!-- ip convert -->
        <h3>IP 转换</h3>
        <el-form label-width="100px">
          <el-form-item label="普通形式">
            <el-input v-model="rawip" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="八进制格式">
            <el-input v-model="octip" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="十进制格式">
            <el-input v-model="decip" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="十六进制格式">
            <el-input v-model="hexip" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="十六进制整数">
            <el-input v-model="hexintip" auto-complete="off"></el-input>
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
  name: 'IPConv',
  components: {
    NavBar,
    FootBar,
    SideBar
  },
  created () {
  },
  data () {
    return {
      rawip: ''
    }
  },
  computed: {
    octip: function () {
      var octip = this.rawip.split('.')
      if (octip.length !== 4) {
        return ''
      }
      return octip.map(
        item => '0' + parseInt(item).toString(8)
      ).join('.')
    },
    decip: function () {
      var decip = this.rawip.split('.')
      if (decip.length !== 4) {
        return ''
      }
      var ret = 0
      for (var i in decip) {
        ret = ret << 8
        ret += parseInt(decip[i])
      }
      ret = ret >>> 0
      return ret
    },
    hexip: function () {
      var hexip = this.rawip.split('.')
      if (hexip.length !== 4) {
        return ''
      }
      return hexip.map(
        item => '0x' + parseInt(item).toString(16)
      ).join('.')
    },
    hexintip: function () {
      var hexintip = this.rawip.split('.')
      if (hexintip.length !== 4) {
        return ''
      }
      var ret = 0
      for (var i in hexintip) {
        ret = ret << 8
        ret += parseInt(hexintip[i])
      }
      ret = ret >>> 0
      return '0x' + ret.toString(16)
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
