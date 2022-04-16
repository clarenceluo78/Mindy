<template>
    <div>
        <div class="block"><el-avatar :size="200" :src="circleUrl"></el-avatar></div>
        <!-- <el-button @click="avatar_edit" class="edit-button">
            EDIT
        </el-button> -->

        <el-button @click="dialogFormVisible = true" >EDIT</el-button>
        <el-dialog title="Edit your personal info here" :visible.sync="dialogFormVisible">
        <el-form :model="form">
            <el-form-item label="USERNAME" :label-width="formLabelWidth">
                <el-input v-model="form.name" placeholder="cyy" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="OLD PASSWD" :label-width="formLabelWidth">
                <el-input v-model="form.name" placeholder="enter your old passcode" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="NEW PASSWD" :label-width="formLabelWidth">
                <el-input v-model="form.name" placeholder="enter your new passcode" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="VERIFY PASSWD" :label-width="formLabelWidth">
                <el-input v-model="form.name" placeholder="verify your new passcode" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="MOBILE" :label-width="formLabelWidth">
                <el-input v-model="form.name" placeholder="13306513527" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="E-MAIL" :label-width="formLabelWidth">
                <el-input v-model="form.name" placeholder="118010029@link.cuhk.edu.cn" autocomplete="off"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">cancel</el-button>
            <el-button type="primary" @click="submit">submit</el-button>
        </div>
        </el-dialog>

        <el-table
        :data="tableData"
        style="width: 100%"
        :colspan=colspan>
        <el-table-column
            prop="username"
            label="name">
        </el-table-column>
        <el-table-column
            prop="role"
            label="role">
        </el-table-column>
        <el-table-column
            prop="mobile"
            label="mobile">
        </el-table-column>        
        <el-table-column
            prop="email"
            label="e-mail">
        </el-table-column>        
        <el-table-column
            prop="passcode"
            label="passcode">
        </el-table-column>

        </el-table>
        <el-card class="box-card" shadow="always">
            <div>
                <el-row>
                    <el-col :span="4"><div class="grid-content bg-purple">INVITE LINK:</div></el-col>
                    <el-col :span="16"><div class="grid-content bg-purple"></div></el-col>
                </el-row>

            </div>
        </el-card>
    </div>
</template>
<script>
export default {
    data(){
        return{
            colspan:1,
            circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
                
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
                formLabelWidth: '120px'
            
        
      
        }
    },
    methods:{
        avatar_edit(){
            console.log('avatar edit')
        },
        submit(){
            console.log('submit')
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
    .el-card{
        margin-top: 15px;
        width: 240px;
    }
</style>