import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),
    },
    {
      path: '/cargo-requests',
      name: 'cargo-requests',
      component: () => import('@/views/CargoRequestsView.vue'),
    },
    {
      path: '/trips',
      name: 'trips',
      component: () => import('@/views/TripsView.vue'),
    },
    {
      path: '/matching',
      name: 'matching',
      component: () => import('@/views/MatchingView.vue'),
    },
  ],
})

export default router
