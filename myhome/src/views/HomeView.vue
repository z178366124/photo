<!-- <script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <TheWelcome />
  </main> height="400px"
</template> -->

<template>  
    <el-carousel :interval="4000" type="card" height="auto" >
      <el-carousel-item v-for="(item, index) in srcList" :key="item" style="height: 600px;">
        <img :src="item" alt="" class="carousel-image">
      </el-carousel-item>
    </el-carousel>
</template>

<script lang="js" setup>
    const url =
    '1.JPG'
    const srcList = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg',
    '7.jpg',
    ]
</script>

<style scoped>


  .demo-image__error .image-slot {
    font-size: 30px;
    }
    .demo-image__error .image-slot .el-icon {
    font-size: 30px;
    }
    .demo-image__error .el-image {
    width: 100%;
    height: 200px;
    }

    .carousel-container {
        width: 100%; /* 设置父容器宽度 */
        height: 400px; /* 设置父容器高度 */
    }

    .carousel-image {
        width: 100%;
        height: 100%;
        object-fit: cover; /* 中心区域裁剪 */
        object-position: center; /* 图片居中 */
    }
</style>
  

