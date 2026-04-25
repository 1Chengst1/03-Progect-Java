import { createRouter, createWebHistory } from 'vue-router'
import Login from '../../public/views/login.vue'
import Dashboard from '../../public/views/Dashboard.vue'
import Market from '../../public/views/Market.vue'
import Backtest from '../../public/views/Backtest.vue'
import Monitor from '../../public/views/Monitor.vue'
import Strategy from '../../public/views/Strategy.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/market',
    name: 'Market',
    component: Market
  },
  {
    path: '/backtest',
    name: 'Backtest',
    component: Backtest
  },
  {
    path: '/monitor',
    name: 'Monitor',
    component: Monitor
  },
  {
    path: '/strategy',
    name: 'Strategy',
    component: Strategy
  },
  {
    path:'/login',
    name:'Login',
    component:Login
  
}
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// 路由守卫：未登录只能访问 login
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.path !== '/login' && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router