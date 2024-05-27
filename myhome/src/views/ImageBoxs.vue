<script setup>
    import ImageBox from '../components/ImageBox.vue'
    import {gimglists} from '../http/Home/index.js'
    import {get_img_list_view} from '../http/Home/view.js'
    import { ref, toRaw, watchEffect  } from 'vue'
    import AsidePage from '../components/AsidePage.vue'
    import { store, groupTree }  from "../store.js"

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
    
</script>

<!-- <template>
    <ImageBox :imgs="store.imgs" :srcList="store.srcList"></ImageBox>
    <el-pagination background layout="prev, pager, next" @current-change="change_page_size" v-model:current-page="store.currPage" v-model:page-size="store.pageSize" :total="store.count" />
</template> -->


<template>
    
    <div v-if="isMobile">
        <el-row :gutter="0">
            <div class="grid-content ep-bg-purple-light" />
                <AsidePage ></AsidePage>
        </el-row>
        <el-row :gutter="0">
            <div class="grid-content ep-bg-purple" />
            <ImageBox :imgs="store.imgs" :srcList="store.srcList"></ImageBox>
            <el-pagination background layout="prev, pager, next" @current-change="change_page_size" hide-on-single-page="true" v-model:current-page="store.currPage" v-model:page-size="store.pageSize" :total="store.count" />
        </el-row>
    </div>
    <div v-else>
        <el-row :gutter="0">
            <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
                <div class="grid-content ep-bg-purple-light" />
                <!-- <el-aside > -->
                    <AsidePage ></AsidePage>
                <!-- </el-aside> -->
            </el-col>
            <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20">
                <div class="grid-content ep-bg-purple" />
                <ImageBox :imgs="store.imgs" :srcList="store.srcList"></ImageBox>
                <el-pagination background layout="prev, pager, next" @current-change="change_page_size" hide-on-single-page="true" v-model:current-page="store.currPage" v-model:page-size="store.pageSize" :total="store.count" />

            </el-col>
        </el-row>
    </div>
    
  </template>