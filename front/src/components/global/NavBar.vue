<template>
  <div>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1" @click="jump('/')">
        <div class="banner">
          Uiharu
        </div>
      </el-menu-item>
      <el-menu-item index="2" @click="jump('/')">
        项目管理
      </el-menu-item>
      <el-menu-item index="3" @click="jump('/ipconv')">
        辅助工具
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
