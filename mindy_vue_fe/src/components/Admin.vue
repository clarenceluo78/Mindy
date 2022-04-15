<template>

    <el-container class="home-container">
        <el-header>
            <div>
                <img src="" alt="" srcset="">
                <span>
                    Mindy Admin
                </span>
            </div>
            <div>
                <el-avatar class="user-avatar"> user </el-avatar>
                <el-button @click="admininfo">
                    INFO
                </el-button>
                <el-button @click="logout">
                    QUIT
                </el-button>
            </div>


        </el-header>

        <el-container>
            <el-aside width="200px">
                <el-menu background-color="#333744" router>
                    <el-menu-item index="/adminhome" class="menu-item">
                        <i class="el-icon-s-home"></i>
                        <span slot="title">HOME</span>
                    </el-menu-item>
                    <el-submenu index="2" class="menu-item">
                        <template slot="title">
                        <i class="el-icon-setting"></i>
                        <span class="menu-item">MANAGEMENT</span>
                        </template>
                        <el-menu-item index="/userslist" class="submenu-item">
                            <i class="el-icon-user-solid"></i>
                            USER MGT
                        </el-menu-item>
                        <el-menu-item index="/mindmaplist" class="submenu-item">
                            <i class="el-icon-document-copy"></i>
                            MINDMAP MGT
                        </el-menu-item>
                        <!-- <el-menu-item-group>
                        <template slot="title">分组一</template>
                        <el-menu-item index="1-1">选项1</el-menu-item>
                        <el-menu-item index="1-2">选项2</el-menu-item>
                        </el-menu-item-group>
                        <el-menu-item-group title="分组2">
                        <el-menu-item index="1-3">选项3</el-menu-item>
                        </el-menu-item-group>
                        <el-submenu index="1-4">
                        <template slot="title">选项4</template>
                        <el-menu-item index="1-4-1">选项1</el-menu-item>
                        </el-submenu> -->
                    </el-submenu>
                    <!-- <el-submenu index="3" class="menu-item">
                        <template slot="title">
                        <i class="el-icon-document-copy"></i>
                        <span class="menu-item">MINDMAP MGT</span>
                        </template>
                        <el-menu-item-group>
                        <template slot="title">分组一</template>
                        <el-menu-item index="3-1">选项1</el-menu-item>
                        <el-menu-item index="3-2">选项2</el-menu-item>
                        </el-menu-item-group>
                        <el-menu-item-group title="分组2">
                        <el-menu-item index="3-3">选项3</el-menu-item>
                        </el-menu-item-group>
                        <el-submenu index="3-4">
                        <template slot="title">选项4</template>
                        <el-menu-item index="3-4-1">选项1</el-menu-item>
                        </el-submenu>
                    </el-submenu> -->
                </el-menu>
            </el-aside>
            <el-main>
                <router-view>
                    
                </router-view>
                
            </el-main>
        </el-container>
    </el-container>
</template>
<script>
export default {
    methods:{
        logout(){
            window.sessionStorage.clear();
            this.$router.push('/login');
        },
        admininfo(){
            this.$router.push('/admininfo');
        },
        newfile(){
            console.log('newfile')
        }
    }
}
</script>


<style lang="less" scoped>
.el-header{
    background-color: #373d41;
    display: flex;
    justify-content: space-between;
    padding-left: 0;
    align-items: center;
    color: #fff;
    font-size: 20px;
    >div{
        display: flex;
        align-items: center;
        span{
            margin-left: 15px;
        }
    }
}
.el-aside{
    background-color: #333744;
}
.el-main{
    background-color: #eaedf1;
}
.home-container{
    height: 100%;
}
.newfile{
    margin-top: 15px;
}
.menu-item{
    color: #fff;
    font-size: 15px;

}
.el-submenu{
    >template{
        span{
            color: #fff;
        }
    }
}
.user-avatar{
    margin-right: 15px;
}
.submenu-item{
    color: #fff;
}


</style>