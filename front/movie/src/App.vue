<template>
  <nav>
    <RouterLink to="/">홈으로</RouterLink> |
    <RouterLink to="/dongjinlove">동진이게임</RouterLink> |
    <RouterLink to="/moviedetail">영화정보</RouterLink> |
    <RouterLink to="/signup">회원가입</RouterLink> |
    <RouterLink to="/login">로그인</RouterLink>
  </nav>
  <div>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterView, RouterLink } from 'vue-router'


</script>

<style scoped>

</style>