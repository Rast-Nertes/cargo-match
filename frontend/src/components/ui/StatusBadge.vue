<script setup>
defineProps({
  label: { type: String, required: true },
  tone: { type: String, default: 'neutral' },
})

const tones = {
  neutral: 'bg-slate-100 text-slate-700',
  success: 'bg-emerald-100 text-emerald-800',
  warning: 'bg-amber-100 text-amber-800',
  brand: 'bg-brand-100 text-brand-700',
}
</script>

<template>
  <span
    class="inline-flex rounded-full px-2.5 py-0.5 text-xs font-medium"
    :class="tones[tone] || tones.neutral"
  >
    {{ label }}
  </span>
</template>
