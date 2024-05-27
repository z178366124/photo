import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/albums',
      name: 'ImageBoxs',
      component: () => import('../views/ImageBoxs.vue')
    },
    {
      path: '/upload',
      name: 'UploadImage',
      component: () => import('../views/UploadImage.vue')
    },{
        path: '/addgroup',
        name: 'AddGroup',
        component: () => import('../views/AddGroup.vue')
    }
  ]
})

export default router
