<template>
  <div class="item-list-container">
    <!-- 加载状态 -->
    <div v-if="loading" class="loading">加载中...</div>
    
    <!-- 错误提示 -->
    <div v-else-if="error" class="error">
      数据加载失败: {{ error }}
      <button @click="fetchItems">重试</button>
    </div>

    <!-- 正常表格 -->
    <div v-else>
      <table class="item-table">
        <!-- 表头（保持原有逻辑） -->
        <thead>
          <tr>
            <th v-for="col in columns" :key="col.key" @click="sortBy(col.key)">
              {{ col.label }}
              <span v-if="sortKey === col.key">
                {{ sortOrder === 'asc' ? '▲' : '▼' }}
              </span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in paginatedData" :key="item.id">
            <td>{{ item.title }}</td>
            <td>{{ item.author }}</td>
            <td>{{ item.type }}</td>
            <td>{{ formatDate(item.create_date) }}</td>
            <td>{{ formatDate(item.update_date) }}</td>
            <td>{{ item.description }}</td>
          </tr>
        </tbody>
      </table>

      <!-- 分页（保持原有逻辑） -->
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
        <span>{{ currentPage }} / {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">下一页</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

// ---------------------- 状态管理 ----------------------
const loading = ref(true)    // 加载状态
const error = ref(null)      // 错误信息
const items = ref([])        // 后端返回的原始数据
const sortKey = ref('')      // 当前排序字段
const sortOrder = ref('asc') // 排序顺序
const currentPage = ref(1)   // 当前页码

// ---------------------- 配置项 ----------------------
const columns = [
  { key: 'title', label: '标题' },
  { key: 'author', label: '作者' },
  { key: 'type', label: '类型' },
  { key: 'create_date', label: '创建时间' },
  { key: 'update_date', label: '更新时间' },
  { key: 'description', label: '描述' }
]
const itemsPerPage = 10      // 每页显示数量
const API_URL = 'http://47.108.254.185:8000/' // 后端接口地址（根据实际情况调整）

// ---------------------- 计算属性 ----------------------
// 排序后的数据
const sortedItems = computed(() => {
  if (!sortKey.value) return [...items.value]
  return [...items.value].sort((a, b) => {
    const aVal = a[sortKey.value]
    const bVal = b[sortKey.value]
    return sortOrder.value === 'asc' 
      ? (aVal < bVal ? -1 : 1) 
      : (aVal > bVal ? -1 : 1)
  })
})

// 总页数
const totalPages = computed(() => Math.ceil(sortedItems.value.length / itemsPerPage))

// 分页后的数据
const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return sortedItems.value.slice(start, end)
})

// ---------------------- 核心方法 ----------------------
// 获取后端数据
const fetchItems = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await axios.get(API_URL)
    items.value = response.data // 假设后端返回数组格式数据
    currentPage.value = 1       // 重置到第一页
  } catch (err) {
    error.value = err.message || '未知错误'
  } finally {
    loading.value = false
  }
}

// 排序逻辑（保持原有）
const sortBy = (key) => {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortOrder.value = 'asc'
  }
}

// 分页逻辑（保持原有）
const prevPage = () => { if (currentPage.value > 1) currentPage.value-- }
const nextPage = () => { if (currentPage.value < totalPages.value) currentPage.value++ }

// 日期格式化（保持原有）
const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// ---------------------- 生命周期钩子 ----------------------
onMounted(() => {
  fetchItems() // 组件挂载时自动获取数据
})
</script>

<style scoped>
/* 保持原有样式，新增加载/错误状态样式 */
.loading, .error {
  padding: 20px;
  text-align: center;
  color: #666;
}
.error {
  color: #f56c6c;
}
.error button {
  margin-left: 10px;
  padding: 4px 8px;
  background: #fff;
  border: 1px solid #f56c6c;
  border-radius: 4px;
  cursor: pointer;
}
</style>