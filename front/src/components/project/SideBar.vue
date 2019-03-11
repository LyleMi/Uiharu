<template>
    <div>
      <el-menu>
        <el-menu-item index="1" @click="jump('/')">
          <div>
            所有项目
          </div>
        </el-menu-item>
        <el-menu-item index="2" @click="jump('/domain')">
          <div>
            域名列表
          </div>
        </el-menu-item>
        <el-menu-item index="3" @click="jump('/application')">
          <div>
            应用列表
          </div>
        </el-menu-item>
        <el-menu-item index="4" @click="jump('/vuln')">
          <div>
            漏洞列表
          </div>
        </el-menu-item>
      </el-menu>
    </div>
</template>

<script>
export default {
  methods: {
    jump (url) {
      this.$router.push(url)
    }
  }
}
</script>

<style scoped>
a {
  color: grey;
  text-decoration: none;
}
</style>
