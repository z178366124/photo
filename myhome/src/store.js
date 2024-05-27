import { reactive } from 'vue'

export const store = reactive({
    srcList: [],
    imgs: [],
    count: 0,
    pageSize: 20,
    currPage: 0,
    next: 0,
    previous: 0,
})

export const groupTree = reactive({
    sysTree: [],
    select_id: 1,
    // imgs: []
})

export default {store, groupTree}