<template>
    <div>
        Your email has been successfully verified. Please wait for automatical jump.
    <div class="biggestBox">
        <!-- <div><input type="text" /></div>
        <div v-if="isShow" :style="{background: msg == '' ? 'cornflowerblue' : '' }" @click="verification">获取验证码</div> -->
        <div v-if="!isShow"><span>{{count}}</span> 秒后跳转</div>
    </div>
    </div>

</template>
<script>
export default {
    data(){
            return{
                count:"",//倒计时
                countt:""
            }
        },

    created(){
        console.log('jump')
        const timejump = 50;
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
        },100)
        }
    },
    methods:{
        
    }
}
</script>
<style lang="less" scoped>

</style>