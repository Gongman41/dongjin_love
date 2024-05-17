import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMemberStore = defineStore('member', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const loginUser = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const router = useRouter()

  const signup = function (payload) {
    const { username, password1, password2, nickname } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
        nickname
      }
    })
      .then((response) => {
        const password = password1
        login({ username, password })
        console.log('회원가입 성공')
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
        loginUser.value = username
        console.log(loginUser.value)
        console.log(token.value)
        console.log('로그인 성공')
        router.push('/')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const logout = function () {

    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`
    })
      .then((response) => {
        token.value = null
        loginUser.value = null
        console.log(loginUser.value)
        console.log(token.value)
        router.push('/login')
        console.log('로그아웃 성공')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return {
    API_URL, token, isLogin, loginUser,
    signup, login, logout
  }
}, { persist: true })
