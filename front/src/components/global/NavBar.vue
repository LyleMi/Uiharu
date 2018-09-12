<template>
  <div>
    <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item>
        <router-link to="/" class="banner" exact>
        Uiharu
        </router-link>
      </el-menu-item>
      <el-menu-item>
        <router-link to="/">
          项目管理
        </router-link>
      </el-menu-item>
      <el-menu-item>
        <router-link to="/tools">
          辅助工具
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
.banner {
  font-size: 28px;
  font-weight: 700;
  background-image: -webkit-gradient(linear,0 0,0 bottom,from(#1890ff),to(#c8c8c8));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

a {
  text-decoration:none;
}
</style>
