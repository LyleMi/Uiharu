<template>
  <div>
    <nav-bar></nav-bar>
    <!-- ip convert -->
    <h3>IP 转换</h3>
    <el-form label-width="100px">
      <el-form-item label="普通形式">
        <el-input v-model="rawip" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="八进制格式">
        <el-input v-model="octip" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="十进制格式">
        <el-input v-model="decip" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="十六进制格式">
        <el-input v-model="hexip" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="十六进制整数">
        <el-input v-model="hexintip" autocomplete="off"></el-input>
      </el-form-item>
    </el-form>

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
      return '0x' + ret.toString(16)
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
