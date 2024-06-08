<script setup>
import ImageShow from './ImageShow.vue'
import { ref, onMounted } from 'vue'
defineProps({
    imgs: {
        type: Array,
        required: true
    },srcList: {
        type: Array,
        required: true
    }
})

const canvasRef = ref(null)
const isCanvasVisible = ref(false)

const drawImageToCanvas = (event, image) => {
    isCanvasVisible.value = true
    const canvas = canvasRef.value;
    canvas.style.top = '50%';
    canvas.style.left = '50%';
    canvas.style.transform = 'translate(-50%, 0%)'; // 使其居中
    const ctx = canvas.getContext('2d');
    const img = new Image();
    img.onload = () => {
        canvas.width = 400; //img.width;
        canvas.height = 400/img.width *img.height; //img.height;
        console.log(canvas.height)

        const height_b = canvas.height / img.height;
        const width_b = 400.0 / img.width;
        
        // 绘制图片
        // ctx.drawImage(img, 0, 0);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        console.log(image.label)
        image.label.forEach(function(item, index){
            const width = item.locationX2 - item.locationX1;
            const height = item.locationY2 - item.locationY1;
            console.log(item)
            console.log(item.locationX1, width_b)
            console.log(item.locationX1 * width_b, item.locationY1 * height_b, width * width_b, height * height_b)
            // 绘制矩形
            ctx.beginPath();
            ctx.rect(item.locationX1 * width_b, item.locationY1 * height_b, width * width_b, height * height_b); // 矩形的位置和大小
            ctx.lineWidth = 2;
            ctx.strokeStyle = 'red';
            ctx.stroke();
        })
        
    };
    img.src = image.image.img;
};

const hideCanvas = ()=>{
    isCanvasVisible.value = false
}


// console.log(imgs) // 打印出传递给组件的 imgs 数组
</script>



<template>
    <div class="flex-tile-container">
        <div v-for="(image, index) in imgs" :key="index" class="flex-tile-item">
            <ImageShow :img="image" :index="index" :srcList="srcList" class="flex-tile-image" @mouseover="drawImageToCanvas($event, image)"
            @mouseleave="hideCanvas()"/>
        </div>
    </div>
    <canvas ref="canvasRef" :style="{ display: isCanvasVisible ? 'block' : 'none'}" @click="hideCanvas"></canvas>
    <!-- <canvas v-if="isCanvasVisible" ref="canvasRef" width="400" height="300"></canvas> -->
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

canvas {
      position: absolute; /* 设置 Canvas 组件为绝对位置 */
    }
</style>

