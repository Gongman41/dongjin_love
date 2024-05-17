<template>
  <div class="body-color">
    <nav v-if="memberStore.token !== null" class="navbar">
      <RouterLink to="/"><img src="@/assets/home.png" alt="home"></RouterLink>
      <RouterLink to="/dongjinlove">동진이게임</RouterLink>
      <RouterLink :to="{ name: 'Profile', params: { username: memberStore.loginUser } }">프로필</RouterLink>
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
const memberStore = useMemberStore()
const logout = function () {
  memberStore.logout()
}

</script>

<style scoped>
img {
  width: 50px;
}

.navbar {
  background: rgba(39, 41, 50, 1);
  width: 200px;
  /* 너비 조정 */
  height: 100vh;
  /* 뷰포트의 전체 높이 */
  position: fixed;
  /* 왼쪽에 고정된 위치 */
  top: 0;
  /* 위쪽에 정렬 */
  left: 0;
  /* 왼쪽에 정렬 */
  display: flex;
  /* 플렉스박스를 사용하여 정렬 */
  flex-direction: column;
  /* 항목을 세로로 쌓음 */
  padding-top: 20px;
  /* 위쪽에 패딩 추가 */
  z-index: 1;
  /* 네비게이션 바가 다른 요소 위에 올라오도록 z-index 설정 */
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
  background-color: rgba(0, 0, 0, 0.2);
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
}

.navbar img:hover {
  filter: brightness(0.8);
}
</style>
