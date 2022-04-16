<template>
    <div class="login_container">
        <div class="login_box">
            <div class="avatar_box">
                <img src="../assets/mindy_logo.png" alt="">
            </div>
            <div>
                <el-form v-loading="loading" label-width="0px" class="login_form" :model="loginForm" :rules="loginFormRules" ref='loginFormRef'>
                    <el-form-item prop="username">
                        <el-input prefix-icon="el-icon-user" placeholder="请输入用户名" v-model="loginForm.username"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input type='password' prefix-icon="el-icon-lock" placeholder="请输入密码" v-model="loginForm.password"></el-input>
                    </el-form-item>
                    <el-form-item prop="passwordCheck">
                        <el-input type='password' prefix-icon="el-icon-lock" placeholder="请再次输入密码" v-model="loginForm.passwordCheck"></el-input>
                    </el-form-item>
                    <el-form-item prop="phoneNum">
                        <el-input prefix-icon="el-icon-phone" placeholder="请输入手机号" v-model="loginForm.phoneNum"></el-input>
                    </el-form-item>
                    <el-form-item prop="emailAdd">
                        <el-input prefix-icon="el-icon-message" placeholder="请输入邮箱" v-model="loginForm.mailAdd"></el-input>
                    </el-form-item>
                    <el-form-item class="btns">
                        <el-button type="primary" @click="submitRegisterForm">register</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>
<script>
export default {

    data(){
        return{
            loading:false,
            count:"",//倒计时
            countt:"",
            loginForm:{
                username:'',
                password:'',
                passwordCheck:'',
                phoneNum:'',
                mailAdd:'',
            },
            loginFormRules:{
                username:[
                    {required:true, message:'Please enter the username', trigger:'blur'},
                    {min:3,max:10,message:'3 to 10 letters',trigger:'blur'}
                ],
                password:[
                    {required:true, message:'Please enter the password', trigger:'blur'},
                    {min:6,max:12,message:'6 to 12 letters',trigger:'blur'}
                ],
                passwordCheck:[
                    {required:true, message:'Please check the password', trigger:'blur'},
                    {min:6,max:12,message:'6 to 12 letters',trigger:'blur'}
                ],
                phoneNum:[
                    {required:true, message:'Please enter the phone number', trigger:'blur'},
                    {min:11,max:11,message:'11 digit cellphone number',trigger:'blur'}
                ],
                mailAdd:[
                    {required:true, message:'Please enter the email address', trigger:'blur'},
                    // {pattern:}
                ]
            }
        }
    },

    methods:{
        submitRegisterForm(){
            const timejump = 10;
            this.loading=true
            if(!this.timer){
                this.count = timejump /10 ;
                this.countt = timejump;
                this.show = false;
                this.timer = setInterval(()=>{
                if(this.count > 0 && this.count *10 <= timejump ){
                    this.countt--;
                    if(this.countt%10==0){
                        this.count--;
                    }
                }else{
                    this.show = true;
                    clearInterval(this.timer);
                    this.timer = null;
                    //跳转的页面写在此处
                    this.$router.push({path: '/login'});
                }
            },100)}
            console.log('submit')
            this.axios(
                {
                    url:'*******',
                    method:'post',
                    params:{
                        username:this.username,
                        password:this.password,
                    }
                }
            ).then(function(res){
                if(res.data==1)  
                {
                console.log("发送成功")
                }
            }.bind(this))
        }
    },
            

}
</script>

 <style lang="less" scoped>
 .login_form{
     position: absolute;
     bottom: 0;
     width: 100%;
     padding: 0 20px;
    box-sizing: border-box; 
 }
 .btns{
     display: flex;
     justify-content: flex-end;
 }
 .login_container{
     background-color: #2b4b6b;
     height: 100%;
 }
 .login_box{
     width: 450px;
     height: 480px;
     background-color: #fff;
     border-radius: 3px;
     position: absolute;
     left: 50%;
     top: 50%;
     transform: translate(-50%,-50%);
     .avatar_box{
         height: 130px;
         width: 130px;
         border: 1px solid #eee;
         border-radius: 50%;
         box-shadow: 0 0 10px #ddd;
         padding: 10px;
         position: absolute;
         left: 50%;
         transform: translate(-50%,-50%);
         background-color: #fff;
         img{
             height: 100%;
             width:100%;
             border-radius: 50%;
             background-color: #eee;
         }
     }
 }
 </style>
