<template>
  <div>
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="signup">
      <div>
        <p><label for="username">아이디</label></p>
        <input type="text" v-model.trim="username" id="username" class="input-box">
      </div>
      <div>
        <p><label for="password1">비밀번호</label></p>
        <input type="password" v-model.trim="password1" id="password1" class="input-box">
      </div>
      <div>
        <p><label for="password2">비밀번호 확인</label></p>
        <input type="password" v-model.trim="password2" id="password2" class="input-box">
      </div>
      <div>
        <p><label for="nickname">닉네임</label></p>
        <input type="text" v-model.trim="nickname" id="nickname" class="input-box">
      </div>
      <input type="submit" value="회원가입" class="login-button">
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
