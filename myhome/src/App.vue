<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ContextPage from './components/ContextPage.vue'
import HeaderPage from './components/HeaderPage.vue'

</script>

<!-- <template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template> -->
  
  <!-- <template>
    <div class="common-layout">
        <el-container>
            <el-aside>
                <AsidePage wd></AsidePage>
            </el-a side>
                <el-container>
                    <el-header>
                        <HeaderPage></HeaderPage>
                    </el-header>
                    <el-main>
                        <RouterView />
                    </el-main>
                    <el-footer>
                        <div width="100%" style="background-color: bisque;">footer</div>
                    </el-footer>
                </el-container>
        </el-container>
    </div>
</template> -->

<template>
    <el-row :gutter="0">
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="1">
        <div class="grid-content ep-bg-purple" />
      </el-col>
      <el-col :xs="24" :sm="22" :md="20" :lg="18" :xl="22">
        <div class="grid-content ep-bg-purple-light" />
        <el-container>
            <el-header>
                <HeaderPage></HeaderPage>
            </el-header>
            <el-main>
                <RouterView style="min-height: 400px;" />
            </el-main>
            <el-footer>
                <!-- <div width="100%" style="background-color: bisque;">
                    
                </div> -->
                <div class="footer-content">
                    <!-- 页脚链接 -->
                    <a href="#">关于我们</a>
                    <a href="#">联系我们</a>
                    <a href="#">帮助中心</a>
                    <!-- 版权信息 -->
                    <span>© 2024 您的公司名称</span>
                </div>
            </el-footer>
        </el-container>
      </el-col>
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="1">
        <div class="grid-content ep-bg-purple-light" />
      </el-col>
    </el-row>
  </template>


<style scoped>
.footer {
  background-color: #f5f7fa;
  color: #606266;
}

.footer-content {
  text-align: center;
  line-height: 60px;
}

.footer-content a {
  margin: 0 10px;
  color: #606266;
  text-decoration: none;
}

.footer-content a:hover {
  color: #409eff;
}

.footer-content span {
  margin-left: 20px;
}
</style>
