<template>
    <div>
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="user mgt" name="first"></el-tab-pane>
            <el-tab-pane label="mindmap mgt" name="second"></el-tab-pane>
        </el-tabs>
        <el-card class="box-card">


            <el-row :gutter="20">
                <el-col :span="8">
                    <el-input placeholder="请输入内容" class="input-with-select">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
                <el-col :span="4">
                    <el-button type="primary" @click="add_user()">ADD USER</el-button>
                </el-col>

            </el-row>
                <!-- <el-table
                :data="tableData"
                style="width: 100%">
                <el-table-column
                    prop="date"
                    label="日期"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="name"
                    label="姓名"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="address"
                    label="地址">
                </el-table-column>
                </el-table> -->

            <el-table :data='userlist' stripe=true>
                <el-table-column type="index"></el-table-column>
                <el-table-column width="120" label="username" prop="username"></el-table-column>
                <el-table-column width="300" label="e-mail" prop="email"></el-table-column>
                <el-table-column width="150" label="mobile" prop="mobile"></el-table-column>
                <el-table-column width="100" label="role" prop="role_name"></el-table-column>
                <el-table-column width="100" label="state" prop="mg_state">
                    <template slot-scope="scope">
                        <!-- {{scope.row}} -->
                        <el-switch v-model="scope.row.mg_state">

                        </el-switch>
                    </template>
                </el-table-column>
                <el-table-column label="operations">
                    <template slot-scope="scope">
                        <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisible = true"></el-button>
                        <el-button type="danger" icon="el-icon-delete" @click="delete_user"></el-button>
                        <el-button type="warning" icon="el-icon-setting"></el-button>
                    </template>
                </el-table-column>
            </el-table>
            <el-dialog title="Edit your personal info here" :visible.sync="dialogFormVisible">
            <el-form :model="form">
                <el-form-item label="USERNAME" :label-width="formLabelWidth">
                    <el-input v-model="form.name" placeholder="cyy" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="MOBILE" :label-width="formLabelWidth">
                    <el-input v-model="form.name" placeholder="13306513527" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="E-MAIL" :label-width="formLabelWidth">
                    <el-input v-model="form.name" placeholder="118010029@link.cuhk.edu.cn" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="ROLE" :label-width="formLabelWidth">
                    <el-input v-model="form.name" placeholder="admin" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="STATE" :label-width="formLabelWidth">
                    <el-input v-model="form.name" placeholder="true" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">cancel</el-button>
                <el-button type="primary" @click="submit">submit</el-button>
            </div>
            </el-dialog>
            <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="queryinfo.pagenum" :page-sizes="queryinfo.pagesize" :page-size="[2,5,10]">

            </el-pagination>
        </el-card>
    </div>
</template>
<script>
export default {
    data(){
        return{
            tableData: [{
                username: 'cyy',
                role:'admin',
                email:'118010029@link.cuhk.edu.cn',
                mobile:'13306513527',
                passcode:'******'
            }],
            gridData: [{
                    date: '2016-05-02',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1518 弄'
                }, {
                    date: '2016-05-04',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1518 弄'
                }, {
                    date: '2016-05-01',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1518 弄'
                }, {
                    date: '2016-05-03',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1518 弄'
                }],
                dialogTableVisible: false,
                dialogFormVisible: false,
                form: {
                name: '',
                region: '',
                date1: '',
                date2: '',
                delivery: false,
                type: [],
                resource: '',
                desc: ''
                },
            activeName: 'first',
            queryinfo:{
                query:'',
                pagenum:1,
                pagesize:2
            },
            userlist:[
                {
                    "id":25,
                    "username":'hello',
                    'mobile':'13306513527',
                    'type':1,
                    'create_time':'0',
                    'mg_state':true,
                    'role_name':'admin',
                    'email':'cyy1102@gmail.com'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
                {
                    'id':30,
                    'username':'byebye',
                    'mobile':'17906513529',
                    'type':1,
                    'create_time':'0',
                    'mg_state':false,
                    'role_name':'user',
                    'email':'118010029@link.cuhk.edu.cn'
                },
            ],
            total:0,
        };
    },
    // created(){
    //     this.getUserList()
    // },
    methods:{
        handleClick(tab, event) {
            console.log(tab, event);
        },
        async getUserList(){
            const {data:res}=await this.$http.get('users',{params:this.queryinfo })
        },
        handleSizeChange(newpage){
            console.log(newpage)
        },
        handleCurrentChange(newpage){
            console.log(newpage)
        },
        delete_user(){
            console.log('delete')
        }
    }
}
</script>
<style lang="less" scoped>
    .text {
        font-size: 14px;
    }

    .item {
        padding: 18px 0;
    }

    .box-card {
        width: 480px;
    }

</style>