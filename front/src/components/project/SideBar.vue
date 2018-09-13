<template>
    <div>
      <el-menu
        class="el-menu-vertical-demo"
        >
        <el-menu-item>
          <router-link to="/">
            所有项目
          </router-link>
        </el-menu-item>
        <el-menu-item>
          <router-link to="/domain">
            域名列表
          </router-link>
        </el-menu-item>
        <el-menu-item>
          <router-link to="/application">
            应用列表
          </router-link>
        </el-menu-item>
        <el-menu-item>
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
