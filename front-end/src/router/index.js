import { createRouter, createWebHistory } from 'vue-router'
import InicioSesion from "@/components/InicioSesion";

const routes = [
  {
    path: '/Log_in',
    name: 'InicioSesion',
    component: InicioSesion
  },
  {
    path: "/Sing_up",
    name: 'Registro',
    component: () => import('../components/Registro')
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
