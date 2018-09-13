<template>
    <div>
      <nav-bar></nav-bar>
      <div>
      <el-container>
        <el-aside width="140px">
          <side-bar></side-bar>
        </el-aside>
        <el-main>
          <el-table
            :data="applications"
            style="width: 100%;text-align: left;"
          >
            <el-table-column
              prop="name"
              label="项目名"
              width="180"
            >
            </el-table-column>
            <el-table-column
              prop="data"
              label="数据"
              width="180"
            >
            </el-table-column>
            <el-table-column
              prop="desc"
              label="描述"
              width="180"
            >
            </el-table-column>
            <el-table-column
              prop="created"
              label="创建日期"
              width="180"
            >
            </el-table-column>
            <el-table-column
              label="操作"
              width="180"
            >
              <template slot-scope="scope">
                <el-button
                  type="text"
                  size="small">
                  详情
                </el-button>
                <el-button
                  @click.native.prevent="deleteApplication(scope.$index, applications)"
                  type="text"
                  size="small">
                  移除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
      </div>
      <foot-bar></foot-bar>
    </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
import { SideBar } from '@/components/project'
// import { api } from '@/utils/api'
export default {
  name: 'Application',
  components: {
    NavBar,
    FootBar,
    SideBar
  },
  created () {
  },
  data () {
    return {
      applications: [{
        name: '测试项目',
        data: 'google.com',
        desc: 'for test',
        created: '2018-9-30'
      }]
    }
  },
  methods: {
    deleteApplication (index, rows) {
      rows.splice(index, 1)
    }
  }
}
</script>

<style scoped>
</style>
