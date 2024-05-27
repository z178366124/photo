<template>
    <!-- <el-button plain @click="dialogVisible = true">
        Open a draggable Dialog
    </el-button> -->
    <el-dialog v-model="dialogVisible" title="温馨提示" width="500" draggable @open="handleDialogOpen">
        <span>新增标题命名</span>
        <el-input ref="inputRef" v-model="title" style="width: 240px" placeholder="请输入标题" @keydown.enter="append_ok(select_data)"/>
        <template #footer>
        <div class="dialog-footer">
            <el-button @click="dialogVisible = false;">关闭</el-button>
            <el-button type="primary" @click="append_ok(select_data)">确定</el-button>
        </div>
        </template>
    </el-dialog>

    <div class="custom-tree-container">
      <!-- <p>Using render-content</p> -->
      <el-tree
        style="max-width: 600px"
        :data="groupTree.systree"
        show-checkbox
        node-key="id"
        default-expand-all
        :expand-on-click-node="false"
        :render-content="renderContent"
      />
      <!-- <p>Using scoped slot</p>
      <el-tree
        style="max-width: 600px"
        :data="dataSource"
        show-checkbox
        node-key="id"
        default-expand-all
        :expand-on-click-node="false"
      >
        <template #default="{ node, data }">
          <span class="custom-tree-node">
            <span>{{ node.label }}</span>
            <span>
              <a @click="append(data)"> Append </a>
              <a style="margin-left: 8px" @click="remove(node, data)"> Delete </a>
            </span>
          </span>
        </template>
      </el-tree> -->
    </div>
  </template>

<script lang="js" setup>
    import { ref,toRaw,nextTick  } from 'vue';
    import {systree,sys_group_del } from '../http/Home/index.js';
    import { store, groupTree }  from "../store.js"
    import {sys_group_add_view } from '../http/Home/view.js';

    let id = 1000;
    const title = ref('')
    const dialogVisible = ref(false)
    const select_data = ref([])
    const inputRef = ref(null); // 定义 ref 用于获取 input 元素的引用

    const handleDialogOpen = () => {
      // 在 el-dialog 打开时触发自动获取焦点
        console.log("af")
        console.log(inputRef.value)
        nextTick(() => {
            inputRef.value.focus();
        });
    };

    const append = (data) => {
        title.value = ""
        select_data.value = []
        dialogVisible.value = true
        select_data.value = data;
    };

    const append_ok = (data) =>{
        console.log(data)
        
        sys_group_add_view({"parent" : data.id, "label": title.value}).then(res=>{
            console.log(res);
            const newChild = { id: res.id, label: res.label, children: [] };
            if (!data.children) {
                data.children = [];
            }
            data.children.push(newChild);
            groupTree.systree = [...groupTree.systree];
            dialogVisible.value = false
        }).catch(err => {
            console.log(err)
            // reject(err); // 将异常传递给 Promise 的 reject 函数
        });
        
    }

    const remove = (node, data) => {
        console.log(node)
        console.log(data)
        sys_group_del(data.id);
        const parent = node.parent;
        const children = parent.data.children || parent.data;
        const index = children.findIndex((d) => d.id === data.id);
        children.splice(index, 1);
        groupTree.systree = [...groupTree.systree];
    };

const renderContent = (h, { node, data, store }) => {
  return h(
    'span',
    {
      class: 'custom-tree-node',
    },
    h('span', null, node.label),
    h(
      'span',
      null,
      h(
        'a',
        {
          onClick: () => append(data),
        },
        'Append '
      ),
      h(
        'a',
        {
          style: 'margin-left: 8px',
          onClick: () => remove(node, data),
        },
        'Delete'
      )
    )
  );
};
    const fetchData = async () => {
        await systree(null).then(res=>{
            // responseData.value = res;
            groupTree.systree = toRaw(res);
            console.log(groupTree.systree)
        }).catch(err=>{
            console.log(err)
        })
    };

    fetchData(); // 调用异步函数以获取数据
const dataSource = ref([
  {
    id: 1,
    label: 'Level one 1',
    children: [
      {
        id: 4,
        label: 'Level two 1-1',
        children: [
          {
            id: 9,
            label: 'Level three 1-1-1',
          },
          {
            id: 10,
            label: 'Level three 1-1-2',
          },
        ],
      },
    ],
  },
  {
    id: 2,
    label: 'Level one 2',
    children: [
      {
        id: 5,
        label: 'Level two 2-1',
      },
      {
        id: 6,
        label: 'Level two 2-2',
      },
    ],
  },
  {
    id: 3,
    label: 'Level one 3',
    children: [
      {
        id: 7,
        label: 'Level two 3-1',
      },
      {
        id: 8,
        label: 'Level two 3-2',
      },
    ],
  },
]);


  </script>
  
  <style>
  .custom-tree-node {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 14px;
    padding-right: 8px;
  }

    a{
        font-weight: 500;
        text-decoration: inherit;
        color: #409eff;
    }
  </style>
  