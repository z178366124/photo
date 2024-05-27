import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'
import axios from 'axios'
 


const app = createApp(App)

app.use(router).use(ElementPlus)
app.config.globalProperties.$http=axios;

app.mount('#app')
