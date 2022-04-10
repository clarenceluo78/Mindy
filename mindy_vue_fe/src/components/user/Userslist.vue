<template>
    <div>
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="role mgt" name="first">ROLE MGT</el-tab-pane>
            <el-tab-pane label="user mgt" name="second">USER MGT</el-tab-pane>
        </el-tabs>
        <el-card class="box-card">
            <div v-for="o in 4" :key="o" class="text item">
                {{'列表内容 ' + o }}
            </div>
        </el-card>
    </div>
</template>
<script>
export default {
    data(){
        return{
            activeName: 'first'
        };
    },
    methods:{
        handleClick(tab, event) {
            console.log(tab, event);
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