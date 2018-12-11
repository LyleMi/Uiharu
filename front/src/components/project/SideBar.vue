<template>
    <div>
      <el-menu>
        <el-menu-item index="1">
          <router-link to="/">
            所有项目
          </router-link>
        </el-menu-item>
        <el-menu-item index="2">
          <router-link to="/domain">
            域名列表
          </router-link>
        </el-menu-item>
        <el-menu-item index="3">
          <router-link to="/application">
            应用列表
          </router-link>
        </el-menu-item>
        <el-menu-item index="4">
          <router-link to="/vuln">
            漏洞列表
          </router-link>
        </el-menu-item>
      </el-menu>
    </div>
</template>

<script>
export default {
}
</script>

<style scoped>
a {
  color: grey;
  text-decoration: none;
}
</style>
