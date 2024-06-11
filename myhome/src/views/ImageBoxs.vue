<script setup>
    import ImageBox from '../components/ImageBox.vue'
    import {gimglists} from '../http/Home/index.js'
    import {get_img_list_view} from '../http/Home/view.js'
    import { ref, toRaw, watchEffect  } from 'vue'
    import AsidePage from '../components/AsidePage.vue'
    import { store, groupTree, imageBoxsSetting }  from "../store.js"

    const aiInput = ref("")
    const isMobile = ref(false);
    watchEffect(() => {
      isMobile.value = window.innerWidth < 768; // 假设手机屏幕宽度小于 768px
    });
    
    
    const fetchData = async () => {
            await get_img_list_view({"sys_group_id": groupTree.select_id })
        };

    fetchData(); // 调用异步函数以获取数据

    function change_page_size(number){
        console.log(number)
        console.log("hello")
        get_img_list_view({"page": number, "sys_group_id": groupTree.select_id})
    }

    const get_ai_class_image = () =>{
        get_img_list_view({"sys_group_id": groupTree.select_id, "ai_name": aiInput.value})
    }
    
</script>

<!-- <template>
    <ImageBox :imgs="store.imgs" :srcList="store.srcList"></ImageBox>
    <el-pagination background layout="prev, pager, next" @current-change="change_page_size" v-model:current-page="store.currPage" v-model:page-size="store.pageSize" :total="store.count" />
</template> -->


<template>
    
    <div v-if="isMobile">
        <el-row :gutter="0">
            <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20"></el-col>
            <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
                <el-input v-model="aiInput" style="width: 100%" placeholder="AI搜索" @keyup.enter="get_ai_class_image"/>
            </el-col>
        </el-row>
        <el-row :gutter="0">
            <div class="grid-content ep-bg-purple-light" />
                <AsidePage ></AsidePage>
        </el-row>
        <el-row :gutter="0">
            <div class="grid-content ep-bg-purple" />
            <ImageBox :imgs="store.imgs" :srcList="store.srcList" style="height: 100%;"></ImageBox>
            <el-pagination background layout="prev, pager, next" @current-change="change_page_size" hide-on-single-page="true" v-model:current-page="store.currPage" v-model:page-size="store.pageSize" :total="store.count" />
        </el-row>
    </div>
    <div v-else>
        <el-row :gutter="0">
            <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20"></el-col>
            <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
                <el-input v-model="aiInput" style="width: 100%;display: inline-block;" placeholder="AI搜索" @keyup.enter="get_ai_class_image"/>
            </el-col>
        </el-row>
        <el-divider border-style="dotted" style="margin: 1px 0;" />
        <el-row :gutter="0">
            <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20">
                <div class="slider-block">
                    <span class="demonstration">图片高度</span>
                    <el-slider style="width: 80%;" v-model="imageBoxsSetting.imageHeight" :min="50" :max="500" show-input/>
                </div>
            </el-col>
            <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
                <el-switch
                    v-model="imageBoxsSetting.openImageInfo"
                    class="ml-2"
                    inline-prompt
                    style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
                    active-text="展开图片详情"
                    inactive-text="图片缩略图"
                />
            </el-col>
            <!-- <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20"></el-col>
            <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
                <el-input v-model="aiInput" style="width: 100%;display: inline-block;" placeholder="AI搜索" @keyup.enter="get_ai_class_image"/>
            </el-col> -->
        </el-row>
        <el-row :gutter="0">
            <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
                <div class="grid-content ep-bg-purple-light" />
                <!-- <el-aside > -->
                    <AsidePage ></AsidePage>
                <!-- </el-aside> -->
            </el-col>
            <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20">
                <div class="grid-content ep-bg-purple" />
                <ImageBox :imgs="store.imgs" :srcList="store.srcList" style="height: 100%;"></ImageBox>
                <el-pagination background layout="prev, pager, next" @current-change="change_page_size" hide-on-single-page="true" v-model:current-page="store.currPage" v-model:page-size="store.pageSize" :total="store.count" />

            </el-col>
        </el-row>
    </div>
    
  </template>



<style scoped>
.slider-block {
  max-width: 600px;
  display: flex;
  align-items: center;
}
.slider-block .el-slider {
  margin-top: 0;
  margin-left: 12px;
}
.slider-block .demonstration {
  font-size: 14px;
  color: var(--el-text-color-secondary);
  line-height: 44px;
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-bottom: 0;
}
</style>