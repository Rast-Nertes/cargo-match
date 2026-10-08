<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <header class="border-b border-slate-200 bg-white shadow-sm">
    <div class="mx-auto flex max-w-6xl items-center justify-between px-4 py-4">
      <RouterLink to="/" class="text-lg font-semibold text-brand-700">
        CargoMatch
      </RouterLink>
      <nav class="flex gap-6 text-sm font-medium text-slate-600">
        <RouterLink to="/cargo-requests" class="hover:text-brand-700">Заявки</RouterLink>
        <RouterLink to="/trips" class="hover:text-brand-700">Рейсы</RouterLink>
        <RouterLink to="/matching" class="hover:text-brand-700">Сопоставление</RouterLink>
      </nav>
    </div>
  </header>
</template>
