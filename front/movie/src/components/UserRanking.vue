<template>
  <h2 style="color: black; padding-left: 2%;">TOP5 유저 랭킹</h2>
  <div class="user-ranking">

    <table class="ranking-table">
      <tbody>
        <tr v-for="(user, index) in users" :key="user.id"
          :class="{ 'highlighted-row': user.username === memberStore.loginUser }">
          <td class="rank">{{ index + 1 }}</td>
          <td class="nickname">{{ user.nickname }}</td>
          <td class="lovepoint">{{ user.lovepoint }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useMemberStore } from '@/stores/member';
import axios from 'axios';

const users = ref([]);
const memberStore = useMemberStore()

async function fetchUserRanking() {
  try {
    const response = await axios.get(`${memberStore.API_URL}/user_ranking/`);
    users.value = response.data.slice(0, 5);
  } catch (error) {
    console.error('Error fetching user ranking:', error);
  }
}

onMounted(() => {
  fetchUserRanking();
});
</script>

<style scoped>
.user-ranking {
  max-width: 800px;
  /* 전체적으로 크기를 키웁니다 */
  margin-top: 4%;
}

.ranking-table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif;
}

.ranking-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.ranking-table tr:hover {
  background-color: #ddd;
}

.ranking-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

.ranking-table .rank {
  width: 10%;
  font-weight: bold;
  color: #333;
}

.ranking-table .nickname {
  width: 60%;
  font-weight: bold;
  color: #555;
}

.ranking-table .lovepoint {
  width: 30%;
  color: #777;
}

.highlighted-row {
  background-color: rgb(204, 233, 40) !important;
}

.ranking-table tr {
  transition: background-color 0.3s;
}
</style>
