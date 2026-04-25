<template>
  <header class="header">
    <div class="left">量化交易策略管理系统</div>
    <div class="right">
      <i class="fa fa-bell-o"></i>
      <span>管理员</span>
    </div>
  </header>
</template>

<style scoped>
.header {
  height: 60px;
  background: white;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 25px;
  position: fixed;
  top: 0;
  left: 200px;
  right: 0;
  z-index: 99;
}
.left {
  margin-left: 10px;
  font-size: 20px;
  font-weight: 500;
}
.right {
  display: flex;
  gap: 20px;
  align-items: center;
}
</style>