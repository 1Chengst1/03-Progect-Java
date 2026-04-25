<template>
  <div class="dashboard">
    <div class="page-title">数据仪表盘</div>

    <!-- 量化核心数据卡片 -->
    <div class="card-row">
      <div class="card blue">
        <div class="title">沪深300</div>
        <div class="num">{{ hs300 }}</div>
        <div class="rate">{{ hs300Rate }}</div>
      </div>
      <div class="card green">
        <div class="title">策略收益</div>
        <div class="num">+12.38%</div>
        <div class="rate">近30日</div>
      </div>
      <div class="card orange">
        <div class="title">最大回撤</div>
        <div class="num">2.15%</div>
        <div class="rate">风险可控</div>
      </div>
      <div class="card red">
        <div class="title">预警次数</div>
        <div class="num">0</div>
        <div class="rate">运行正常</div>
      </div>
    </div>

    <!-- 行情表格 -->
    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>代码</th>
            <th>名称</th>
            <th>收盘价</th>
            <th>涨跌幅</th>
            <th>成交量(万)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in stockList" :key="item.code">
            <td>{{ item.code }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.close }}</td>
            <td :class="item.rate >= 0 ? 'up' : 'down'">
              {{ item.rate >= 0 ? '+' + item.rate : item.rate }}%
            </td>
            <td>{{ item.vol }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 响应式数据
const stockList = ref([])
const hs300 = ref('0.00')
const hs300Rate = ref('0.00%')

// 从后端加载所有数据
async function loadAllData() {
  try {
    const res = await fetch('http://127.0.0.1:5001/api/dashboard')
    const data = await res.json()

    // 更新仪表盘数据
    hs300.value = data.hs300
    hs300Rate.value = data.hs300Rate

    // 更新股票列表
    stockList.value = data.stocks.map(s => ({
      code: s.代码,
      name: s.名称,
      close: Number(s.最新价).toFixed(2),
      rate: Number(s.涨跌幅).toFixed(2),
      vol: (Number(s.成交量) / 10000).toFixed(2)
    }))
  } catch (err) {
    console.error('加载失败', err)
  }
}

onMounted(() => {
  loadAllData()
  setInterval(loadAllData, 3000) // 3秒自动刷新
})
</script>

<style scoped>
.page-title {
  font-size: 22px;
  margin-bottom: 20px;
}
.card-row {
  display: flex;
  gap: 20px;
  margin-top: 50px;
  margin-left: 210px;
  margin-right: 10px;
}
.card {
  flex: 1;
  padding: 20px;
  border-radius: 8px;
  color: white;
}
.card.blue { background: #3b82f6; }
.card.green { background: #10b981; }
.card.orange { background: #f97316; }
.card.red { background: #ef4444; }
.card .title { font-size: 14px; opacity: 0.9; }
.card .num { font-size: 26px; margin: 8px 0; }
.card .rate { font-size: 12px; opacity: 0.8; }

.table-box {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 1px 3px #00000010;
  margin-top: 30px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}
.up { color: #ef4444; font-weight: bold; }
.down { color: #10b981; font-weight: bold; }
</style>