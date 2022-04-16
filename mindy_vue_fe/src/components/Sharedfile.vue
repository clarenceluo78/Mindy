<template>
    <div>
                <el-row :gutter="20">
            <el-col :span="8">
                <el-input placeholder="请输入内容" class="input-with-select">
                    <el-button slot="append" icon="el-icon-search"></el-button>
                </el-input>
            </el-col>
            <el-col :span="4">
                <el-button type="primary" @click="search">search</el-button>
            </el-col>

        </el-row>
        <el-breadcrumb separator="/">
            <el-breadcrumb-item><i class="el-icon-sort"></i><a @click="sort_time">sort by time</a></el-breadcrumb-item>
            <el-breadcrumb-item><i class="el-icon-sort"></i><a @click="sort_filename">sort by filename</a></el-breadcrumb-item>
        </el-breadcrumb>
        <el-row :gutter="20">
            <el-col :span="9">
                <div class="grid-content bg-purple">
                    <!-- <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>文件名</span>
                            <el-radio v-model="radio"></el-radio>
                        </div>
                        <img src="../assets/logo.png" alt="">


                    </el-card> -->
                    <el-card :body-style="{ padding: '0px' }">
                        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
                        <div style="padding: 14px;" class="filename">
                            <span>file name</span>
                        </div>
                    </el-card>
                </div>
            </el-col>
        </el-row>

    </div>
</template>
<script>
export default {
    methods:{
        search(){
            console.log('search')
        },
        sort_time(){
            console.log('sort by time')
        },
        sort_filename(){
            console.log('sort by filename')
        }
    }
}
</script>
<style lang="less" scoped>
    .el-row{
        margin: 15px;
    }
</style>