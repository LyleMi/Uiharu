<template>
    <div>
      <nav-bar></nav-bar>
      <el-container style="min-height:300px;">
        <el-aside width="140px">
          <side-bar></side-bar>
        </el-aside>
        <el-main>
          <el-row>
            <el-col :span="6">
              <el-input placeholder="过滤"></el-input>
            </el-col>
            <el-col :span="6" :offset="6">
              <el-button type="primary" @click="dialogVisible=true">新增</el-button>
            </el-col>
          </el-row>
          <el-table
            :data="projects"
            style="width: 100%;text-align: left;"
          >
            <el-table-column
              prop="name"
              label="项目名"
              width="180"
            >
            </el-table-column>
            <el-table-column
              prop="target"
              label="目标"
              width="180"
            >
            </el-table-column>
            <el-table-column
              prop="desc"
              label="描述"
              width="500"
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
                  size="small">
                  详情
                </el-button>
                <el-button
                  @click.native.prevent="deleteProject(scope.$index, projects)"
                  size="small">
                  移除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-dialog title="新增应用" :visible.sync="dialogVisible">
          <el-form label-width="80px" :model="form">
            <el-form-item label="项目名称">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="项目目标">
              <el-input v-model="form.target" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="项目描述">
              <el-input v-model="form.desc" rows=10 type="textarea" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button  @click="dialogVisible=false">取 消</el-button>
            <el-button type="primary" @click="createData()">确 定</el-button>
          </div>
        </el-dialog>
        </el-main>
      </el-container>

      <foot-bar></foot-bar>
    </div>
</template>

<script>
import { NavBar, FootBar } from '@/components/global'
import { SideBar } from '@/components/project'
import { getProjects, createProject, deleteProject } from '@/api/project'
export default {
  name: 'Project',
  components: {
    NavBar,
    FootBar,
    SideBar
  },
  created () {
    this.getList()
  },
  data () {
    return {
      projects: [{
        name: '测试项目',
        target: 'google.com',
        desc: 'for test',
        created: '2018-9-30'
      }],
      form: {
        name: '',
        target: '',
        desc: ''
      },
      dialogVisible: false
    }
  },
  methods: {
    getList () {
      getProjects().then(response => {
        this.projects = response.data.data
      })
    },
    createData () {
      createProject(this.form).then(() => {
        this.getList()
      })
      this.dialogVisible = false
    },
    deleteProject (index, rows) {
      deleteProject({'uid': rows[index].uid}).then(() => {
      })
      rows.splice(index, 1)
    }
  }
}
</script>

<style scoped>
</style>
