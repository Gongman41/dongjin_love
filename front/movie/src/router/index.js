import { useMemberStore } from '@/stores/member'
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DongjinLoveView from '@/views/DongjinLoveView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'

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
    {
      path: '/profile/:username',
      name: 'Profile',
      component: ProfileView
    }
  ]
})

router.beforeEach((to, from) => {
  const memberStore = useMemberStore()
  if (memberStore.token === null && (to.name !== 'Login' && to.name !== 'SignUp')) {
    return { name: 'Login' }
  }
})

export default router
