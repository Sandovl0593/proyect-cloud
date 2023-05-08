import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/registrar',
    name: 'registrar',
    component: () => import('../views/RegisterView.vue')
  },
  {
    path: '/ventas',
    name: 'ventas',
    component: () => import('../views/VentasView.vue')
  },
  {
    path: '/registrar_producto',
    name: 'registrar_producto',
    component: () => import('../views/RegistrarProductoView.vue')
  },
  {
    path: '/compras',
    name: 'compras',
    component: () => import('../views/ComprasView.vue')
  },
  {
    path: '/inventario',
    name: 'inventario',
    component: () => import('../views/InventarioView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
