<template>
    <div>
      <nav-bar></nav-bar>
      <el-container style="min-height:300px;">
        <el-aside width="140px">
          <side-bar></side-bar>
        </el-aside>
        <el-main>
          <el-table
            :data="vulns"
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
              prop="vtype"
              label="漏洞类型"
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
                  @click.native.prevent="deleteVuln(scope.$index, vulns)"
                  type="text"
                  size="small">
                  移除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
      <foot-bar></foot-bar>
    </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
import { SideBar } from '@/components/project'
// import { api } from '@/utils/api'
export default {
  name: 'Vuln',
  components: {
    NavBar,
    FootBar,
    SideBar
  },
  created () {
  },
  data () {
    return {
      vulns: [{
        name: '测试项目',
        data: 'google.com',
        vtype: 'rce',
        desc: 'for test',
        created: '2018-9-30'
      }]
    }
  },
  methods: {
    deleteVuln (index, rows) {
      rows.splice(index, 1)
    }
  }
}
</script>

<style scoped>
</style>
