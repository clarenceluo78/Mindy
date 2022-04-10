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
            prop="date"
            label="日期"
            width="180">
        </el-table-column>
        <el-table-column
            prop="name"
            label="姓名"
            width="180">
        </el-table-column>
        </el-table>
    </div>
</template>
<script>
export default {
    data(){
        return{
            circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
                
            tableData: [{
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-04',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1517 弄'
            }, {
                date: '2016-05-01',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1519 弄'
            }, {
                date: '2016-05-03',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1516 弄'
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
    .edit-button{

    }


</style>