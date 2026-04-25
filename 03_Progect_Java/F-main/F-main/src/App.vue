<template>
  <div id="app">
    <Sidebar />
    <Header />
    <router-view />
  </div>
</template>

<script setup>
// 从 src/ 目录，向上退一级到项目根目录，再进入 public/components
import Sidebar from '../public/components/Sidebar.vue'
import Header from '../public/components/Header.vue'
</script>

<style >
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Microsoft YaHei", sans-serif;
}
body {
  background: #f3f4f6;
}
</style>