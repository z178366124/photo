<template>
    <!-- <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
    >
        <el-menu-item index="1">首页</el-menu-item>
        <el-sub-menu index="2">
        <template #title>Workspace</template>
        <el-menu-item index="2-1">item one</el-menu-item>
        <el-menu-item index="2-2">item two</el-menu-item>
        </el-sub-menu>
        <el-menu-item index="3" disabled>Info</el-menu-item>
        <el-menu-item index="4">Orders</el-menu-item>
    </el-menu>
    <div class="h-6" /> -->
    <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        @select="handleSelect"
    >
        <el-menu-item index="1"><RouterLink class="custom-link" to="/">首页</RouterLink></el-menu-item>
        <el-sub-menu index="2">
        <template #title>管理</template>
        <!-- <el-menu-item index="2-1">
            <RouterLink class="custom-link" to="/upload">上传</RouterLink>
        </el-menu-item> -->
        <RouterLink class="custom-link" to="/upload"><el-menu-item index="2-1">上传</el-menu-item></RouterLink>
        <RouterLink class="custom-link" to="/addgroup"><el-menu-item index="2-2">添加分组</el-menu-item></RouterLink>
        </el-sub-menu>
        <!-- <el-menu-item index="3" disabled>Info</el-menu-item> -->
        <el-menu-item index="4"><RouterLink class="custom-link" to="/albums">相册</RouterLink></el-menu-item>
    </el-menu>
    <!-- <header>
        <div>
            <nav>
                <RouterLink to=""><img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="50" height="50" /></RouterLink>
                <RouterLink to="/">首页</RouterLink><span>/</span>
                <RouterLink to="/about">相册</RouterLink>
            </nav>
        </div>
        
    </header> --> 
  </template>
  
  <script setup>
//   import { defineProps } from 'vue';
  import { RouterLink, RouterView } from 'vue-router'
  
  </script>
  

<style>
    .custom-link {
        text-decoration: none; /* 关闭文本链接的下划线 */
        color: inherit; /* 继承父元素的文本颜色 */
        cursor: pointer; /* 显示鼠标指针 */
    }
</style>