<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">아이디 : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password">비밀번호 : </label>
        <input type="password" v-model.trim="password" id="password">
      </div>
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMemberStore } from '@/stores/member'

const username = ref(null)
const password = ref(null)
const memberStore = useMemberStore()

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  memberStore.login(payload)
}
</script>

<style></style>
