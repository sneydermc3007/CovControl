import { createRouter, createWebHistory } from 'vue-router'
import InicioSesion from "@/components/InicioSesion";
import Formulario from "@/components/Formulario";

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
  },
  {
    path: '/Menu_one',
    name: 'Formulario',
    component: Formulario
  },
  {
    path: '/Menu_two',
    name: 'Dashboard',
    component: () => import('../components/Dashboard')
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
