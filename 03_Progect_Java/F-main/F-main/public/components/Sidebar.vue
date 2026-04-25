<template>
  <aside class="sidebar">
    <div class="side-header">量化交易仪表盘</div>
    <div class="menu">
      <router-link to="/dashboard" class="menu-item" :class="{ active: $route.path === '/dashboard' }">
        <i class="fa fa-dashboard"></i> 数据仪表盘
      </router-link>
      <router-link to="/market" class="menu-item" :class="{ active: $route.path === '/market' }">
        <i class="fa fa-line-chart"></i> 实时行情
      </router-link>
      <router-link to="/strategy" class="menu-item" :class="{ active: $route.path === '/strategy' }">
        <i class="fa fa-code"></i> 量化策略
      </router-link>
      <router-link to="/backtest" class="menu-item" :class="{ active: $route.path === '/backtest' }">
        <i class="fa fa-bar-chart"></i> 策略回测
      </router-link>
      <router-link to="/monitor" class="menu-item" :class="{ active: $route.path === '/monitor' }">
        <i class="fa fa-bell"></i> 风险监控
      </router-link>
    </div>
  </aside>
</template>

<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
</script>

<style scoped>
.sidebar {
  width: 200px;
  background: #1f2937;
  color: white;
  height: 100vh;
  padding-left: 40px;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 100;
}
.side-header {
  padding: 20px;
  padding-left:1px;
  font-size: 18px;
  background: #111827;
  text-align: center;
  margin: 15px;
  margin-left: -35px;;
}
.menu {
  margin-top: 20px;
}
.menu-item {
  padding: 14px 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  color: white;
  text-decoration: none;
  margin-left: -38px;
}
.menu-item.active {
  background: #374151;
  border-left: 4px solid #3b82f6;
}
.menu-item:hover {
  background: #374151;
}
</style>