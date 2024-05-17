<template>
  <div class="background-container">
    <h1 class="title">로그인</h1>
    <form @submit.prevent="login" class="login-form">
      <div>
        <p><label class="label" for="username">아이디</label></p>
        <input type="text" v-model.trim="username" id="username" class="input-box">
      </div>
      <div>
        <p><label class="label" for="password">비밀번호</label></p>
        <input type="password" v-model.trim="password" id="password" class="input-box">
      </div>
      <div class="button-container">
        <input type="submit" value="로그인" class="login-button">
        <RouterLink :to="{ name: 'SignUp' }" class="signup-button">회원가입</RouterLink>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
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
.background-container {
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/background.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
}

.title {
  color: white;
  font-size: 32px;
  margin-bottom: 20px;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* 중앙 정렬 */
  background-color: rgba(0, 0, 0, 0.2);
  padding: 20px;
  border-radius: 10px;
}

.label {
  font-size: 20px;
  font-weight: bold;
  color: white;
}

.input-box {
  background: rgba(26, 28, 38, 0.8);
  color: white;
  font-size: 20px;
  width: 300px;
  height: 40px;
  border-radius: 10px;
  padding-left: 10px;
  margin-bottom: 10px;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-button,
.signup-button {
  width: 110px;
  background: linear-gradient(to bottom, #763DCF, #5C24CC);
  color: white;
  border: none;
  padding: 10px 0;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
  margin-top: 10px;
}
</style>
