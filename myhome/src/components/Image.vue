<script setup>
defineProps({
    img: {
        type: Object,
        required: true
    },
    srcList: {
        type: Array,
        required: true
    },
    index:{
        type: Number,
        required: true
    }
})


</script>

<template>
    <div :key="img.fit" class="block" width="100px">
        <el-image  style="width: 100px; height: 100px" :src="img.image.img" fit="scale-down" :zoom-rate="1.2"
      :max-scale="7"
      :min-scale="0.2"
      :preview-src-list="srcList"
      lazy
      :initial-index="index"/>
        <div class="button-group">
            <!-- <a class="button" :on-click="look">查看</a> -->
            <a class="button" :href="img.url" download="image.jpg">下载</a>
        </div>
    </div>

    
</template>



<style scoped>
    /* .mode{
        background-color: aqua;
        position: relative;
        width: 100px;
        top: 50px;
        left: 50px;
    } */
    .block{
        position: relative;
        display: inline-block; /* 让容器只占用所需的空间 */
        flex-shrink: 0;
        width: 100px !important;
        height: 100px;
    }

    .block el-image{
        display: block; /* 让图片撑满容器*/
        max-width: 100%; /* 确保图片不超出容器*/
    }

    .button-group{
        position: absolute;
        display: none;
        width: 100%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%); /* 将元素的中心对齐到父元素的中心 */
        background-color: rgba(255, 255, 255, 0.5);
    }

    .button {
      display: block;
      padding: 2px 5px;
      margin-top: 2px;
      /* background-color: #007bff; */
      color: #000;
      border-radius: 5px;
      text-align: center; /* 将文本水平居中 */
    }

    .block:hover .button-group{
        display: block;
    }
</style>