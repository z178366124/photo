import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [
//     vue(),
//   ],
//   resolve: {
//     alias: {
//       '@': fileURLToPath(new URL('./src', import.meta.url))
//     }
//   }
// })


export default defineConfig({
    plugins: [vue()],
    server: {
        disableHostCheck: true,
        host: "0.0.0.0",
        port: 8888,
    //   proxy: {
    //     // 将请求 /api/user 代理到 http://localhost:3000/api/user
    //     '/api': {
    //       target: 'http://192.168.2.104:8000',
    //       changeOrigin: true,
    //       rewrite: (path) => path.replace(/^\/api/, '')
    //     }
    //   }
    proxy: {
        '/api': {
          target: 'http://192.168.2.104:8000', // 目标服务器地址
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '') // 可选的路径重写规则
        }
      }
    }
  })

// module.exports = {
//     devServer: {
//       port: 80,
//       proxy: {
//         '/api': {
//           target: 'http://192.168.2.104:8000',
//           secure: true,
//           changeOrigin: true,
//           pathRewrite: {
//             '^/api': '',
//           },
//         }
//       },
//     },
//   }
  