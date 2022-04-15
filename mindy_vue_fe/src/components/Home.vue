<template>

    <el-container class="home-container">
        <el-header>
            <div>
                <img src="" alt="" srcset="">
                <span>
                    Mindy
                </span>
            </div>
            <div>
                <el-avatar class="user-avatar" @click="userinfo"> user </el-avatar>
                <el-button @click="userinfo">
                    INFO
                </el-button>
                <el-button @click="logout">
                    QUIT
                </el-button>
            </div>


        </el-header>

        <el-container>
            <el-aside width="200px">
                <el-button @click="newfile" class="newfile">
                    + NEW
                </el-button>
                <el-menu background-color="#333744" router>
                    <el-menu-item index="/home" class="menu-item">
                        <i class="el-icon-s-home"></i>
                        <span slot="title">HOME</span>
                    </el-menu-item>
                    <el-menu-item index="/file" class="menu-item">
                        <i class="el-icon-document"></i>
                        <span slot="title">MY FILE</span>
                    </el-menu-item>
                    <!-- <el-submenu index="2" class="menu-item">
                        <template slot="title">
                        <i class="el-icon-document"></i>
                        <span class="menu-item">MY FILE</span>
                        </template>
                        <el-menu-item-group>
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
                        </el-submenu>
                    </el-submenu> -->
                    <el-menu-item index="/sharedfile" class="menu-item">
                        <i class="el-icon-files"></i>
                        <span slot="title">SHARED FILE</span>
                    </el-menu-item>
                    <el-menu-item index="/bin" class="menu-item">
                        <i class="el-icon-delete"></i>
                        <span slot="title">RECYCLE BIN</span>
                    </el-menu-item>
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
        userinfo(){
            this.$router.push('/userinfo');
        },
        newfile(){
            console.log('newfile')
            this.$router.push('/mindmap')
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


</style>