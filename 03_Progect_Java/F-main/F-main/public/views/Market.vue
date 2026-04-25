<template>
  <div class="market-page">
    <div class="header">
      <h1>实时行情</h1>
      <p>共 {{ total }} 只 · 第 {{ page }} 页</p>
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>代码</th>
            <th>名称</th>
            <th>现价</th>
            <th>涨跌幅</th>
            <th>涨跌额</th>
            <th>成交量(万)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in stockList" :key="item.code">
            <td>{{ item.code }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.price }}</td>
            <td :class="item.rate >= 0 ? 'up' : 'down'">
              {{ item.rate >= 0 ? "+" + item.rate : item.rate }}%
            </td>
            <td :class="item.change >= 0 ? 'up' : 'down'">
              {{ item.change >= 0 ? "+" + item.change : item.change }}
            </td>
            <td>{{ item.vol }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="pagination">
      <button @click="goPage(page - 1)" :disabled="page <= 1">上一页</button>
      <span>第 {{ page }} 页</span>
      <button @click="goPage(page + 1)" :disabled="page >= totalPages">下一页</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";

const stockList = ref([]);
const page = ref(1);
const size = ref(5);
const total = ref(0);
const totalPages = ref(1);

async function fetchData() {
  try {
    const res = await fetch(
      `http://127.0.0.1:5000/api/market?page=${page.value}&size=${size.value}`
    );
    const data = await res.json();

    total.value = data.total || 0;
    totalPages.value = Math.ceil(total.value / size.value);

    stockList.value = data.stocks.map((s) => ({
      code: s["代码"],
      name: s["名称"],
      price: parseFloat(s["最新价"] || 0).toFixed(2),
      rate: parseFloat(s["涨跌幅"] || 0).toFixed(2),
      change: parseFloat(s["涨跌额"] || 0).toFixed(2),
      vol: (parseFloat(s["成交量"] || 0) / 10000).toFixed(2),
    }));
  } catch (e) {
    console.error("请求失败", e);
  }
}

function goPage(p) {
  if (p < 1 || p > totalPages.value) return;
  page.value = p;
}

watch(page, fetchData);

onMounted(() => {
  fetchData();
  setInterval(fetchData, 5000);
});
</script>

<style scoped>
.market-page {
  background: white;
  padding: 50px;
  border-radius: 8px;
  margin-left: 190px;
  margin-top: 30px;
}
.header {
  margin-bottom: 20px;
}
.table-box {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px #00000010;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th,
td {
  padding: 12px;
  text-align: center;
  border-bottom: 1px solid #eee;
}
th {
  background: #f8f9fa;
}
.up {
  color: red;
  font-weight: bold;
}
.down {
  color: green;
  font-weight: bold;
}
.pagination {
  margin-top: 20px;
  display: flex;
  gap: 10px;
  align-items: center;
}
button {
  padding: 6px 14px;
  cursor: pointer;
}
</style>