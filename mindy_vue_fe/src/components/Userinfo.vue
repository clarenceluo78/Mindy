<template>
    <div>
        <div class="block"><el-avatar :size="200" :src="circleUrl"></el-avatar></div>
        <el-button @click="avatar_edit" class="edit-button">
            EDIT
        </el-button>
        <el-table
        :data="tableData"
        style="width: 100%">
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

        </el-table>
        <el-card class="box-card">
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
            circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
                
            tableData: [{
                username: 'cyy',
                role:'admin',
                email:'118010029@link.cuhk.edu.cn',
                mobile:'13306513527'
            }]
        
      
        }
    },
    methods:{
        avatar_edit(){
            console.log('avatar edit')
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
    .el-card{
        margin-top: 15px;
    }
</style>