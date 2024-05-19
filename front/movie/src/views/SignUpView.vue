<template>
  <div class="background-container">
    <h1 class="title">회원가입 페이지</h1>
    <form @submit.prevent="signup" class="signup-form">
      <div>
        <p><label for="username" class="label">아이디</label></p>
        <input type="text" v-model.trim="username" id="username" class="input-box">
      </div>
      <div>
        <p><label for="password1" class="label">비밀번호</label></p>
        <input type="password" v-model.trim="password1" id="password1" class="input-box">
      </div>
      <div>
        <p><label for="password2" class="label">비밀번호 확인</label></p>
        <input type="password" v-model.trim="password2" id="password2" class="input-box">
      </div>
      <div>
        <p><label for="nickname" class="label">닉네임</label></p>
        <input type="text" v-model.trim="nickname" id="nickname" class="input-box">
      </div>
      <input type="submit" value="회원가입" class="signup-button">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMemberStore } from '@/stores/member'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const memberStore = useMemberStore()

const signup = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value
  }
  memberStore.signup(payload)
}
</script>

<style scoped>
.background-container {
  width: 100vw;
  /* 전체 화면 너비 */
  height: 100vh;
  /* 전체 화면 높이 */
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

.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
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
  /* 살짝 투명하게 설정 */
  color: white;
  font-size: 20px;
  width: 300px;
  height: 40px;
  border-radius: 10px;
  padding-left: 10px;
  margin-bottom: 10px;
}

.signup-button {
  background: linear-gradient(to bottom, #763DCF, #5C24CC);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
  text-align: center;
  text-decoration: none;
}
</style>
