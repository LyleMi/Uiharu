<template>
    <div>
      <el-menu>
        <el-menu-item index="1" @click="jump('/ipconv')">
          IP格式转换
        </el-menu-item>
        <el-menu-item index="2" @click="jump('/hash')">
          哈希计算
        </el-menu-item>
        <el-menu-item index="3" @click="jump('/encode')">
          编码
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
