<template>
  <div>
    <!-- <iframe frameborder="0" src="https://itch.io/embed-upload/10418501?color=333333" allowfullscreen="" width="640"
      height="380"><a :href="url">Play test on itch.io</a></iframe> -->
    <iframe frameborder="0" src="https://itch.io/embed-upload/10494887?color=333333" allowfullscreen="" width="100%"
      height="600"><a :href="url">Play test on itch.io</a></iframe>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useMemberStore } from '@/stores/member';

const memberStore = useMemberStore()
const userId = ref(null)
const url = ref(null)
onMounted(() => {
  memberStore.getProfile()
  userId.value = memberStore.profile.id
  url.value = `https://lkm98401.itch.io/test?user_id=${userId}`
})

</script>

<style scoped></style>