import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAppStore = defineStore('app', () => {
  const apiStatus = ref('unknown')

  async function checkHealth() {
    try {
      const { default: client } = await import('@/api/client')
      await client.get('/health')
      apiStatus.value = 'ok'
    } catch {
      apiStatus.value = 'error'
    }
  }

  return { apiStatus, checkHealth }
})
