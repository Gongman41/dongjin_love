import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DongjinLoveView from '@/views/DongjinLoveView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/dongjinlove',
    name: 'DongjinLove',
    component: DongjinLoveView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView 
  },
  {
    path: '/moviedetail',
    name: 'MovieDetail',
    component: MovieDetailView
  },
  ]
})

export default router
