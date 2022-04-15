<template>
    <div>
        <el-button type="text" @click="dialogFormVisible = true" icon="el-icon-connection">INVITE</el-button>
        <el-dialog title="add team member" :visible.sync="dialogFormVisible">
        <el-form :model="form">
            <el-form-item label="ACCOUNT" :label-width="formLabelWidth">
            <el-input v-model="form.name" placeholder="enter the email or cellphone number" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="ROLE" :label-width="formLabelWidth">
            <el-select v-model="form.region" placeholder="select role">
                <el-option label="read only" value="shanghai"></el-option>
                <el-option label="read and edit" value="beijing"></el-option>
            </el-select>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">cancel</el-button>
            <el-button type="primary" @click="submit">submit</el-button>
        </div>
        </el-dialog>
    </div>
</template>
<script>
    export default {
        data(){
            return {
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
            };
        },
        methods:{
            submit(){
                this.$message.success('Successfully login')
                this.dialogFormVisible=false
            }
        }
    }
</script>

<style lang="less" scoped>

</style>