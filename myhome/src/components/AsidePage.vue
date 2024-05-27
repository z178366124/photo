<template>
    <el-input
      v-model="filterText"
      placeholder="Filter keyword"
      style="max-width: 100%; width: 100%;"
    />
  
    <el-tree
        ref="treeRef"
        style="max-width: 100%;width: 100%;"
        class="filter-tree"
        :data="groupTree.systree"
        :props="defaultProps"
        default-expand-all
        :filter-node-method="filterNode"
        highlight-current="true"
        @node-click="click_event"
    />
  </template>
      
<script lang="js" setup>
    import { ref, watch, toRaw } from 'vue';
    import axios from 'axios';
    import {systree, gimglists} from '../http/Home/index.js';
    import {get_img_list_view} from '../http/Home/view.js';
    import { store, groupTree }  from "../store.js"


    import { ElTree } from 'element-plus';

    function click_event(data, node, obj, err) {
        groupTree.select_id = data.id
        if(data.children.length === 0){
            get_img_list_view({"sys_group_id" : data.id})
        }
        
    }

    const filterText = ref('');
    const treeRef = ref(null);

    watch(filterText, (val) => {
        treeRef.value.filter(val);
    });

    const filterNode = (value, data) => {
    if (!value) return true;
    return data.label.includes(value);
    };

    // const responseData = ref(null);
    
    // let data = ref([]); // 初始化为一个空数组

    const fetchData = async () => {
        await systree(null).then(res=>{
            // responseData.value = res;
            groupTree.systree = toRaw(res);
            // console.log(data.value)
        }).catch(err=>{
            console.log(err)
        })
    };

    fetchData(); // 调用异步函数以获取数据
</script>
  