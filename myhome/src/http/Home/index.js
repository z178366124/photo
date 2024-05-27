import request from "../axios.js";
 
export const systree=(params)=>{
  return request({
    url:'/sys/systree/',
    method:'get',
    params
  })
}

export const sys_group_add=(data)=>{
    return request({
      url:'/sys/grouplists/',
      method:'post',
      data: data,
      headers: {
            'Content-Type': 'multipart/form-data' // 设置 Content-Type 为 multipart/form-data
        }
    })
}

export const sys_group_del=(group_id)=>{
    return request({
      url:'/sys/grouplists/' + group_id+ '/',
      method:'DELETE',
    })
}

export const gimglists=(params)=>{
    return request({
      url:'/users/albums/',
      method:'get',
      params
    })
}
  
export const upload_img_list=(params)=>{
    return request({
        url:'/users/albums/upload/',
        method:'post',
        data: params,
        headers: {
            'Content-Type': 'multipart/form-data' // 设置 Content-Type 为 multipart/form-data
        }
    })
}

 
export default {systree, gimglists, upload_img_list, sys_group_add, sys_group_del }