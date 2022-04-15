<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-input placeholder="请输入内容" class="input-with-select">
                    <el-button slot="append" icon="el-icon-search"></el-button>
                </el-input>
            </el-col>
            <el-col :span="4">
                <el-button type="primary" @click="search()">search</el-button>
            </el-col>

        </el-row>

        <el-row :gutter="20">
            <el-col :span="4">
                <div class="grid-content bg-purple">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>文件名</span>
                        </div>
                        <img src="../assets/logo.png" alt="">
                        <!-- <div v-for="o in 4" :key="o" class="text item">
                            {{'列表内容 ' + o }}
                        </div> -->

                    </el-card>
                </div>
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {
    
}
</script>
<style lang="less" scoped>
    .el-row{
        margin: 15px;
    }

</style>