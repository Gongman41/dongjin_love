<template>
  <div>
    <form>
      <div>
        <input type="text" v-model.trim="movie" id="movie" class="input-box" placeholder="영화 검색">
      </div>
    </form>
  </div>

  <div>
    <h1 style="color: white;">회원님을 위한 영화추천</h1>
    <div class="recommend-movie">
      <RouterLink :to="{ name: 'MovieDetail' }">영화1</RouterLink>
      <RouterLink :to="{ name: 'MovieDetail' }">영화2</RouterLink>
      <RouterLink :to="{ name: 'MovieDetail' }">영화3</RouterLink>
      <RouterLink :to="{ name: 'MovieDetail' }">영화4</RouterLink>
    </div>
  </div>

  <div>
    <h1 style="color: white;">코미디</h1>
    <div class="recommend-movie">
      <RouterLink :to="{ name: 'MovieDetail' }">영화1</RouterLink>
      <RouterLink :to="{ name: 'MovieDetail' }">영화2</RouterLink>
      <RouterLink :to="{ name: 'MovieDetail' }">영화3</RouterLink>
      <RouterLink :to="{ name: 'MovieDetail' }">영화4</RouterLink>
    </div>
  </div>

  <div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
const movie = ref(null)

</script>

<style scoped>
.input-box {
  background: rgba(39, 41, 50, 1);
  color: white;
  font-size: 20px;
  width: 511px;
  height: 62px;
  border-radius: 20px;
  padding-left: 20px;
}

.recommend-movie {
  background: rgba(39, 41, 50, 1);
  width: 800px;
  height: 400px;
  border-radius: 20px;
}
</style>