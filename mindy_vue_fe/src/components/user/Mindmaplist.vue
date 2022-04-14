<template>
    <div>
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="user mgt" name="first"></el-tab-pane>
            <el-tab-pane label="mindmap mgt" name="second"></el-tab-pane>
        </el-tabs>
        mindmap mgt
    </div>
</template>
<script>
export default {
    
}
</script>
<style lang="less" scoped>

</style>