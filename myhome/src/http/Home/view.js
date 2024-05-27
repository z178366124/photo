import {gimglists, sys_group_add} from "./index.js";
import { store }  from "../../store.js"

export const get_img_list_view=(data)=>{
    gimglists(data).then(res=>{
        store.imgs = res["results"]
        store.count = res.count
        store.pageSize = res.page_size
        store.currPage = res.page
        store.previous = res.previous
        store.next = res.next
        console.log("count", store.count)
        console.log(store.pageSize)
        store.imgs.forEach(element => {
            store.srcList.push(element.image.img)
        });
        console.log(store.imgs)
    }).catch(err=>{
        console.log(err)
    })
}

export const sys_group_add_view=(data)=>{
    return new Promise((resolve, reject) => {
        const formData = new FormData();
        console.log(data)
        for (let key in data) {
            formData.append(key, data[key])
        }
        sys_group_add(formData).then(res => {
            console.log("sys_group_add", res)
            resolve(res); // 将异步操作的结果传递给 Promise 的 resolve 函数
        }).catch(err => {
            console.log(err)
            reject(err); // 将异常传递给 Promise 的 reject 函数
        });
    });
}

export default {get_img_list_view, sys_group_add_view, }