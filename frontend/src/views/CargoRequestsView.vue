<script setup>
import { onMounted, ref } from 'vue'
import { fetchCargoRequests } from '@/api/cargoRequests'
import StatusBadge from '@/components/ui/StatusBadge.vue'

const items = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const { data } = await fetchCargoRequests()
    items.value = data
  } catch (e) {
    error.value = 'Не удалось загрузить заявки. Запустите backend и PostgreSQL.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section>
    <h1 class="text-2xl font-bold text-slate-900">Заявки на перевозку</h1>
    <p v-if="loading" class="mt-4 text-slate-500">Загрузка…</p>
    <p v-else-if="error" class="mt-4 text-amber-700">{{ error }}</p>
    <ul v-else class="mt-6 space-y-3">
      <li
        v-for="item in items"
        :key="item.id"
        class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
      >
        <div class="flex flex-wrap items-center justify-between gap-2">
          <span class="font-medium">
            {{ item.origin_city }} → {{ item.destination_city }}
          </span>
          <StatusBadge :label="item.status" tone="brand" />
        </div>
        <p class="mt-1 text-sm text-slate-600">{{ item.cargo_description }}</p>
        <p class="mt-2 text-xs text-slate-500">Вес: {{ item.weight_kg }} кг</p>
      </li>
      <li v-if="!items.length" class="text-sm text-slate-500">Заявок пока нет.</li>
    </ul>
  </section>
</template>
