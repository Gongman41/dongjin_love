<template>
  <div>
    <nav v-if="memberStore.token !== null" class="navbar">
      <RouterLink to="/" :class="{ 'click': route.path === '/', 'non-click': route.path !== '/' }">
        <img v-if="route.path !== '/'" src="@/assets/home.png" alt="home">
        <img v-if="route.path === '/'" src="@/assets/click_home.png" alt="home">
      </RouterLink>

      <RouterLink to="/dongjinlove"
        :class="{ 'click': route.path === '/dongjinlove', 'non-click': route.path !== '/dongjinlove' }">
        <img v-if="route.path !== '/dongjinlove'" src="@/assets/game.png" alt="game">
        <img v-if="route.path === '/dongjinlove'" src="@/assets/click_game.png" alt="game">
      </RouterLink>

      <RouterLink :to="{ name: 'Profile', params: { username: memberStore.loginUser } }"
        :class="{ 'click': route.name === 'Profile', 'non-click': route.name !== 'Profile' }">
        <img v-if="route.name !== 'Profile'" src="@/assets/profile.png" alt="profile">
        <img v-if="route.name === 'Profile'" src="@/assets/click_profile.png" alt="profile">
      </RouterLink>

      <RouterLink to="">네이버</RouterLink>
      <img src="@/assets/line.png" alt="line">
      <button @click="logout" class="logout-button">로그아웃</button>
    </nav>

    <nav v-else class="navbar">
      <RouterLink to="/signup">회원가입</RouterLink> |
      <RouterLink to="/login">로그인</RouterLink>
    </nav>


    <div class="content">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, RouterView, RouterLink } from 'vue-router'
import { useMemberStore } from '@/stores/member';

const route = useRoute()
console.log(route.path)
const memberStore = useMemberStore()
const logout = function () {
  memberStore.logout()
}

</script>


<style scoped>
img {
  width: 50px;
}

.click {
  background-color: #1a1c26;
  border-top-left-radius: 40%;
  border-bottom-left-radius: 40%;
}

.non-click {
  background: rgba(39, 41, 50, 1);
  border-top-left-radius: 40%;
  border-bottom-left-radius: 40%;
}

.navbar {
  background: rgba(39, 41, 50, 1);
  width: 120px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: end;
  padding-top: 20px;
  z-index: 1;
}

.content {
  margin-left: 220px;
  /* 네비게이션 바 너비 + 여유 공간 만큼 컨텐츠를 오른쪽으로 밀어줌 */
  padding: 20px;
  /* background: rgba(39, 41, 50, 1); */
  height: 100vh;

  /* 여백 추가 */
}

.navbar a,
.navbar button {
  color: white;
  /* 텍스트 색상 */
  text-decoration: none;
  /* 밑줄 제거 */
  padding: 10px;
  /* 패딩 추가 */
}

.navbar a:hover,
.navbar button:hover {
  background-color: #1a1c26;
  /* 마우스 오버 시 배경색 변경 */
}

.logout-button {
  background: linear-gradient(to bottom, #763DCF, #5C24CC);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin: 10px;
  margin-top: 100px;
}

.navbar img:hover {
  filter: brightness(0.8);
}
</style>
