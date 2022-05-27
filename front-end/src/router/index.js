import { createRouter, createWebHistory } from 'vue-router'
import InicioSesion from "@/components/InicioSesion";
import Formulario from "@/components/Formulario";

const routes = [
  {
    path: '/',
    redirect: '/Log_in'
  },
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
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
