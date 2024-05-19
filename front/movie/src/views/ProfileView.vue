<template>
  <div>
    <div v-if="profile !== null" class="content">
      <h1>{{ memberStore.profile.nickname }}님의 프로필 페이지</h1>
      <p>{{ memberStore.profile.like_movie }}</p>
      <p>{{ memberStore.profile.like_genre }}</p>
    </div>
    <p v-else class="content">로딩중...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMemberStore } from '@/stores/member';
import { useRoute } from 'vue-router';
import axios from 'axios';

const memberStore = useMemberStore()

onMounted(() => {
  memberStore.getProfile()
})

</script>

<style scoped>
.content {
  color: white;
}
</style>