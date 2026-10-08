<script setup>
import AppHeader from '@/components/layout/AppHeader.vue'
import AppFooter from '@/components/layout/AppFooter.vue'
</script>

<template>
  <div class="flex min-h-screen flex-col">
    <AppHeader />
    <main class="mx-auto w-full max-w-6xl flex-1 px-4 py-8">
      <RouterView />
    </main>
    <AppFooter />
  </div>
</template>
