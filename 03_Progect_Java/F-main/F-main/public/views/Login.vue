<template>
  <div class="login-page">
    <div class="contains">
      <div class="left">
        <img src="../assets/avatar.jpg" alt="头像" />
        <div class="name">Lcc</div>
      </div>

      <div class="right">
        <h2>量化交易平台</h2>

        <input
          v-model="username"
          type="text"
          placeholder="请设置用户名"
          class="input-item"
        />
        <input
          v-model="password"
          type="password"
          placeholder="请设置密码"
          class="input-item"
        />
        <button class="btn register" @click="register">注册账号</button>

        <input
          v-model="loginUser"
          type="text"
          placeholder="请输入用户名"
          class="input-item"
        />
        <input
          v-model="loginPwd"
          type="password"
          placeholder="请输入密码"
          class="input-item"
        />
        <button class="btn login" @click="login">立即登录</button>

        <p class="tip" :style="{ color: tipColor }">{{ tipText }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 注册
const username = ref('')
const password = ref('')

// 登录
const loginUser = ref('')
const loginPwd = ref('')

// 提示
const tipText = ref('欢迎使用量化交易系统！')
const tipColor = ref('#666')

// 注册
const register = () => {
  if (!username.value || !password.value) {
    tipText.value = '⚠️ 用户名和密码不能为空！'
    tipColor.value = 'red'
    return
  }

  localStorage.setItem('username', username.value)
  localStorage.setItem('password', password.value)
  tipText.value = '✅ 注册成功！请登录'
  tipColor.value = 'green'
}

// 登录
const login = () => {
  const user = localStorage.getItem('username')
  const pwd = localStorage.getItem('password')

  if (!user || !pwd) {
    tipText.value = '⚠️ 您还未注册账号！'
    tipColor.value = 'red'
    return
  }

  if (loginUser.value === user && loginPwd.value === pwd) {
    tipText.value = '✅ 登录成功！正在进入系统...'
    tipColor.value = 'green'

    localStorage.setItem('token', 'LOGIN_SUCCESS')

    setTimeout(() => {
      router.push('/dashboard')
    }, 1200)
  } else {
    tipText.value = '❌ 用户名或密码错误！'
    tipColor.value = 'red'
  }
}
</script>

<style scoped>
.login-page {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f2f5;
  margin: 0;
  padding: 0;
}

.contains {
  display: flex;
  height: 700px;
  width: 1000px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.left {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f8f9fa;
  gap: 20px;
}

.left img {
  width: 260px;
  height: 260px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.left .name {
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.right {
  flex: 1;
  padding: 80px 50px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.right h2 {
  font-size: 28px;
  color: #222;
  text-align: center;
  margin-bottom: 10px;
}

.input-item {
  height: 52px;
  width: 100%;
  border-radius: 8px;
  border: 1px solid #ddd;
  padding: 0 18px;
  font-size: 15px;
  outline: none;
  transition: 0.3s;
}

.input-item:focus {
  border-color: #409eff;
  box-shadow: 0 0 8px rgba(64, 158, 255, 0.2);
}

.btn {
  height: 52px;
  width: 100%;
  border-radius: 8px;
  border: none;
  color: white;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s;
}

.register {
  background-color: #67c23a;
}
.login {
  background-color: #409eff;
}

.btn:hover {
  opacity: 0.9;
}

.tip {
  text-align: center;
  font-size: 14px;
  margin-top: 10px;
}
</style>