<script setup>
import Image from './Image.vue'
defineProps({
    imgs: {
        type: Array,
        required: true
    },srcList: {
        type: Array,
        required: true
    }
})

// console.log(imgs) // 打印出传递给组件的 imgs 数组
</script>



<template>
    <div class="flex-tile-container">
        <div v-for="(image, index) in imgs" :key="index" class="flex-tile-item">
            <Image :img="image" :index="index" :srcList="srcList" class="flex-tile-image" />
        </div>
    </div>

</template>




<style scoped>
.flex-tile-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px; /* 图片之间的间隔 */
}

.flex-tile-item {
  flex: 1 0 auto; /* 图片的基本宽度 */
}

.flex-tile-image {
  width: 100%; /* 图片宽度填充父容器 */
  height: auto; /* 根据宽度自适应高度 */
}
</style>

