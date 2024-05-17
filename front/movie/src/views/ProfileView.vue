<template>
  <div>
    <div v-if="profile !== null" class="content">
      <h1>{{ profile.nickname }}님의 프로필 페이지</h1>
      <p>{{ profile.like_movie }}</p>
      <p>{{ profile.like_genre }}</p>
    </div>
    <p v-else class="content">로딩중...</p>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUpdate } from 'vue'
import { useMemberStore } from '@/stores/member';
import { useRoute } from 'vue-router';
import axios from 'axios';

const profile = ref(null)
const route = useRoute()
const userName = ref(route.params.username)
const memberStore = useMemberStore()

const getProfile = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/profile/${userName.value}`
  })
    .then((response) => {
      profile.value = response.data
    })
    .catch((error) => console.log(error))
}

onMounted(() => {
  getProfile()
})

</script>

<style scoped>
.content {
  color: white;
}
</style>