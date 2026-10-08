<script setup>
import { ref } from 'vue'
import { suggestMatches } from '@/api/cargoRequests'
import StatusBadge from '@/components/ui/StatusBadge.vue'

const requestId = ref('')
const matches = ref([])
const message = ref('')

async function runMatching() {
  message.value = ''
  matches.value = []
  if (!requestId.value) return
  try {
    const { data } = await suggestMatches(Number(requestId.value))
    matches.value = data
    if (!data.length) message.value = 'Подходящих рейсов не найдено.'
  } catch {
    message.value = 'Ошибка сопоставления. Проверьте ID заявки и backend.'
  }
}
</script>

<template>
  <section class="max-w-xl">
    <h1 class="text-2xl font-bold text-slate-900">Автосопоставление</h1>
    <p class="mt-2 text-sm text-slate-600">
      Введите ID опубликованной заявки для подбора рейсов (в т.ч. обратных).
    </p>
    <form class="mt-6 flex gap-2" @submit.prevent="runMatching">
      <input
        v-model="requestId"
        type="number"
        min="1"
        placeholder="ID заявки"
        class="flex-1 rounded-lg border border-slate-300 px-3 py-2 text-sm focus:border-brand-500 focus:outline-none focus:ring-2 focus:ring-brand-100"
      />
      <button
        type="submit"
        class="rounded-lg bg-brand-700 px-4 py-2 text-sm font-medium text-white hover:bg-brand-600"
      >
        Подобрать
      </button>
    </form>
    <p v-if="message" class="mt-4 text-sm text-amber-700">{{ message }}</p>
    <ul class="mt-6 space-y-3">
      <li
        v-for="m in matches"
        :key="m.id"
        class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
      >
        <div class="flex items-center justify-between">
          <span class="font-medium">Рейс #{{ m.trip_id }}</span>
          <StatusBadge :label="`score ${m.score}`" tone="success" />
        </div>
        <p v-if="m.is_backhaul" class="mt-1 text-xs text-amber-700">Обратный рейс</p>
        <p v-if="m.comment" class="mt-2 text-sm text-slate-600">{{ m.comment }}</p>
      </li>
    </ul>
  </section>
</template>
