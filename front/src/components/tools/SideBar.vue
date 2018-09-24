<template>
    <div>
      <el-menu>
        <el-menu-item>
          <router-link to="/ipconv">
            IP格式转换
          </router-link>
        </el-menu-item>
        <el-menu-item>
          <router-link to="/hash">
            哈希计算
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
