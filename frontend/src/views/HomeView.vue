<script setup>
import { onMounted } from 'vue'
import { useAppStore } from '@/stores/app'
import StatusBadge from '@/components/ui/StatusBadge.vue'

const app = useAppStore()

onMounted(() => {
  app.checkHealth()
})
</script>

<template>
  <section class="space-y-8">
    <div class="rounded-2xl bg-gradient-to-br from-brand-700 to-brand-600 p-8 text-white shadow-lg">
      <h1 class="text-3xl font-bold tracking-tight">
        Платформа сопоставления грузоперевозок
      </h1>
      <p class="mt-3 max-w-2xl text-brand-50/90">
        Агрегация заявок перевозчиков и грузовладельцев с автоматическим подбором рейсов,
        включая обратные (backhaul), для снижения порожних пробегов.
      </p>
      <div class="mt-4 flex items-center gap-2 text-sm">
        <span>API:</span>
        <StatusBadge
          :label="app.apiStatus === 'ok' ? 'доступен' : app.apiStatus === 'error' ? 'недоступен' : 'проверка…'"
          :tone="app.apiStatus === 'ok' ? 'success' : app.apiStatus === 'error' ? 'warning' : 'neutral'"
        />
      </div>
    </div>

    <div class="grid gap-4 md:grid-cols-3">
      <article class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <h2 class="font-semibold text-slate-800">Заявки</h2>
        <p class="mt-2 text-sm text-slate-600">Публикация и управление заявками на перевозку груза.</p>
      </article>
      <article class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <h2 class="font-semibold text-slate-800">Рейсы</h2>
        <p class="mt-2 text-sm text-slate-600">Календарь рейсов перевозчиков, в том числе обратных.</p>
      </article>
      <article class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <h2 class="font-semibold text-slate-800">Сопоставление</h2>
        <p class="mt-2 text-sm text-slate-600">Автоматический scoring заявок и рейсов по маршруту и грузоподъёмности.</p>
      </article>
    </div>
  </section>
</template>
