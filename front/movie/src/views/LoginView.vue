<template>
  <div>
    <h1 style="color: white;">로그인</h1>
    <form @submit.prevent="login">
      <div>
        <p><label class="label" for="username">아이디</label></p>
        <input type="text" v-model.trim="username" id="username" class="input-box">
      </div>
      <div>
        <p><label class="label" for="password">비밀번호</label></p>
        <input type="password" v-model.trim="password" id="password" class="input-box">
      </div>
      <input type="submit" value="로그인" class="login-button">
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

<style scoped>
.label {
  font-size: 20px;
  font-weight: bold;
  color: white;
}

.input-box {
  background: rgba(26, 28, 38, 1);
  color: white;
  font-size: 20px;
  width: 511px;
  height: 62px;
  border-radius: 20px;
  padding-left: 20px;
}

.login-button {
  background: linear-gradient(to bottom, #763DCF, #5C24CC);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 100px;
  margin-right: 100px;
}
</style>
