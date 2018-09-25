<template>
  <div>
    <nav-bar></nav-bar>
      <el-container style="min-height:300px;">
        <el-aside width="140px">
          <side-bar></side-bar>
        </el-aside>
        <el-main>
        <h3>哈希计算</h3>
        <el-form label-width="100px">
          <el-form-item label="输入">
            <el-input v-model="str" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密钥">
            <el-input v-model="key" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="md5">
            <el-input v-model="md5" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="sha1">
            <el-input v-model="sha1" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="sha256">
            <el-input v-model="sha256" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="sha512">
            <el-input v-model="sha512" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="hmac(md5)">
            <el-input v-model="hmd5" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="hmac(sha1)">
            <el-input v-model="hsha1" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="hmac(sha256)">
            <el-input v-model="hsha256" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="hmac(sha512)">
            <el-input v-model="hsha512" autocomplete="off"></el-input>
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
const Hashes = require('jshashes')
export default {
  name: 'Hash',
  components: {
    NavBar,
    FootBar,
    SideBar,
    Hashes
  },
  created () {
    this.hashes = {
      md5: new Hashes.MD5(),
      sha1: new Hashes.SHA1(),
      sha256: new Hashes.SHA256(),
      sha512: new Hashes.SHA512()
    }
  },
  data () {
    return {
      str: '',
      key: ''
    }
  },
  computed: {
    md5: function () {
      return this.hashes.md5.hex(this.str)
    },
    sha1: function () {
      return this.hashes.sha1.hex(this.str)
    },
    sha256: function () {
      return this.hashes.sha256.hex(this.str)
    },
    sha512: function () {
      return this.hashes.sha512.hex(this.str)
    },
    hmd5: function () {
      return this.hashes.md5.hex_hmac(this.key, this.str)
    },
    hsha1: function () {
      return this.hashes.sha1.hex_hmac(this.key, this.str)
    },
    hsha256: function () {
      return this.hashes.sha256.hex_hmac(this.key, this.str)
    },
    hsha512: function () {
      return this.hashes.sha512.hex_hmac(this.key, this.str)
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
