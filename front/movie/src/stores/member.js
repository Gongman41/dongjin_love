import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMemberStore = defineStore('member', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  
  const router = useRouter()

  const signup = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then((response) => {
        const password = password1
        login({ username, password })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const login = function (payload) {

    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then((response) => {
        token.value = response.data.key
        router.push('/')
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return {
    API_URL, token, isLogin,
    signup, login
  }
}, { persist: true })
