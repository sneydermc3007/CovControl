import { createRouter, createWebHistory } from 'vue-router'
import InicioSesion from "@/components/InicioSesion";

const routes = [
  {
    path: '/Log_in',
    name: 'InicioSesion',
    component: InicioSesion
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
