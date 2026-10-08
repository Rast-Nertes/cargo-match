<script setup>
import { onMounted, ref } from 'vue'
import { fetchTrips } from '@/api/trips'
import StatusBadge from '@/components/ui/StatusBadge.vue'

const items = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const { data } = await fetchTrips()
    items.value = data
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section>
    <h1 class="text-2xl font-bold text-slate-900">Рейсы перевозчиков</h1>
    <p v-if="loading" class="mt-4 text-slate-500">Загрузка…</p>
    <ul v-else class="mt-6 space-y-3">
      <li
        v-for="trip in items"
        :key="trip.id"
        class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
      >
        <div class="flex flex-wrap items-center justify-between gap-2">
          <span class="font-medium">
            {{ trip.origin_city }} → {{ trip.destination_city }}
          </span>
          <div class="flex gap-2">
            <StatusBadge v-if="trip.is_return_leg" label="обратный рейс" tone="warning" />
            <StatusBadge :label="trip.status" tone="brand" />
          </div>
        </div>
        <p class="mt-2 text-sm text-slate-600">
          Отправление: {{ trip.departure_date }} · Свободно: {{ trip.free_capacity_kg }} кг
        </p>
      </li>
      <li v-if="!items.length" class="text-sm text-slate-500">Рейсов пока нет.</li>
    </ul>
  </section>
</template>
