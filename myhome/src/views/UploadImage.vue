<template>
    <div class="mb-2">
        <el-tree-select
            v-model="value"
            :data="data"
            :render-after-expand="false"
            style="width: 240px; margin-right: 20px;"
        />
        <el-button :onclick="click_send" type="primary">发送</el-button>
    </div>
    
    <el-divider />

    <el-upload action="#" list-type="picture-card" :auto-upload="false" multiple="true" drag="true"
    v-model:file-list="fileList" :on-remove="handleRemove" :on-preview="handlePictureCardPreview" :disabled="!value">
      <el-icon><Plus /></el-icon>
    </el-upload>
  
    <el-dialog v-model="dialogVisible">
      <img w-full :src="dialogImageUrl" alt="Preview Image" />
    </el-dialog>
  </template>
  
<script lang="js" setup>
    import { ref,toRaw  } from 'vue'
    import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
    import { groupTree }  from "../store.js"
    import { upload_img_list } from "../http/Home/index.js"
    import { ElLoading } from 'element-plus'
    import {systree} from '../http/Home/index.js';
    
    
    //   import type { UploadFile } from 'element-plus'
    let fileList = ref([])
    let data = ref([])
    const value = ref() // 选择器选择的内容

    const dialogImageUrl = ref('')
    const dialogVisible = ref(false)
    const disabled = ref(false)
    const handleRemove =(file, files) =>{
        console.log(file, files)
    }
    
    const handlePictureCardPreview = (file) => {
        dialogImageUrl.value = file.url
        dialogVisible.value = true
    }

    const fetchData = async () => {
        await systree(null).then(res=>{
            // responseData.value = res;
            groupTree.systree = toRaw(res);
            let jsonString = JSON.stringify(groupTree.systree)
            if(jsonString){
                let modifiedString = jsonString.replace(/"id":/g, '"value":')
                data.value = JSON.parse(modifiedString)
            }
        }).catch(err=>{
            console.log(err)
        })
    };

    fetchData(); // 调用异步函数以获取数据
    
    
    //TODO 图片上传未解决。找不到图片，前后端为结合
    function click_send(){
        const loading = ElLoading.service({
            lock: true,
            text: 'Loading',
            background: 'rgba(0, 0, 0, 0.7)',
        })
        console.log(value.value)
        const formData = new FormData();
        // var img_list = []
        fileList.value.forEach(element => {
            formData.append('img_list', element.raw)
        });
        formData.append("group_id", value.value)
        // formData.append("img_list", img_list)
        upload_img_list(formData).then(res=>{
            alert("上传成功")
            loading.close()
        }).catch(err=>{
            console.log(err)
        })
    }

    
</script>
   