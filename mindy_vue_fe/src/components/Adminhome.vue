<template>
    <div class="container">
        <el-card :body-style="{ padding: '15px' }" shadow="hover">
            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
            <div style="padding: 14px;" class="filename">
                <span>user management</span>
            </div>
        </el-card>
        <el-card :body-style="{ padding: '15px' }" shadow="hover">
            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
            <div style="padding: 14px;" class="filename">
                <span>mindmap management</span>
            </div>
        </el-card>
    </div>
</template>
<script>
export default {
    
}
</script>
<style lang="less" scoped>
.container{
    display: flex;
    justify-content: space-between;

}
.el-card{
    margin-left: 10%;
    margin-right: 10%;
    margin-top: 10%;
}

</style>