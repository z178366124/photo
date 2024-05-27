<script setup>
      import HeaderPage from './HeaderPage.vue'

      // 导航链接数据
    const navigationLinks = [
    {
        id: 1,
        icon: 'el-icon-globe',
        title: 'Website',
        description: 'Visit our website for more information.',
        url: '/'
    },
    {
        id: 2,
        icon: 'el-icon-document',
        title: 'Documentation',
        description: 'Read our documentation to learn more.',
        url: '/'
    },
    // 添加更多链接...
    ];
</script>

<template>
    <div class="common-layout">
        <el-container>
            <el-aside width="200px">Aside</el-aside>
                <el-container>
                    <el-header>
                        <HeaderPage links="navigationLinks"></HeaderPage>
                    </el-header>
                    <el-main>Main</el-main>
                    <el-footer>Footer</el-footer>
                </el-container>
        </el-container>
    </div>
</template>
  
  

<style scoped>

</style>
