<template>
  <div>
    <!-- <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" class="poster-img"> -->
    <div class="movie-box" v-if="movie !== null">
      <!-- 
      <div v-if="videoId" class="video-wrapper">
        <iframe
          :src="`https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1&controls=1&loop=1&playlist=${videoId}&playsinline=1`"
          frameborder="0" allowfullscreen class="video-frame"></iframe>
      </div> -->
      <h1 style="text-align: center; margin-top: 5%; " v-if="movie !== null">{{ movie.title }}</h1>

      <div class="movie-detail">
        <iframe v-if="videoId" style="width: 64vw; height: 60vh;"
          :src="`https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1&controls=1&loop=1&playlist=${videoId}&playsinline=1`"
          frameborder="0" allowfullscreen></iframe>
        <p style="display: flex; flex-direction: row; justify-content: space-between;">
          <p>장르 : {{ genres }}</p>
          <img v-if="liked" @click="liked = !liked" src="@/assets/heart.png" alt="like">
          <img v-else @click="liked = !liked" src="@/assets/dislike.png" alt="dislike">
        </p>
        <p>개봉일 : {{ movie.release_date }}</p>
        <p>평점 : {{ movie.vote_average }}</p>
        <p>인기도 : {{ movie.popularity }}</p>
        <p @click="addLikeMovie(movie.id)">
        </p>
        <p style="text-indent: 10px;">{{ movie.overview }}</p>

        <p>출연 :
          <span v-for="actor in actors" :key="actor.id" class="person-item">
            <img v-if="actor.poster_path" :src="`https://image.tmdb.org/t/p/w500${actor.poster_path}`" alt="" class="person-img">
            <img v-else src="@/assets/profile.png" alt="" class="person-img">
            <p>{{ actor.name }}</p>
          </span>
        </p>
        <p>제작 :
          <span v-for="producer in crews" :key="producer.id" class="person-item">
            <img v-if="producer.poster_path" :src="`https://image.tmdb.org/t/p/w500${producer.poster_path}`" alt="" class="person-img">
            <img v-else src="@/assets/profile.png" alt="" class="person-img">
            <p>{{ producer.name }}</p>
          </span>
        </p>
      </div>
      <div class="review-container">
        <h2>리뷰 리스트</h2>
        <div class="review-list">
          <div v-if="reviews.length > 0">
            <div v-for="(review) in reviews" :key="review.id">
              <div class="review-info">
                <p>작성자 : {{ review.user.nickname }}</p>
                <p>작성일 : {{ format(review.updated_at, 'yyyy-MM-dd') }}</p>
              </div>
              <div class="review-item">
                <p>{{ review.content }}</p>
                <div>
                  <p class="star">
                    <img v-for="i in review.rank" src="@/assets/star.png" alt="star" class="rank">
                  </p>
                </div>
              </div>
              

            </div>
          </div>
          <!-- 리뷰가 없는 경우 -->
          <p v-else>리뷰가 없습니다.</p>
        </div>

        <!-- 리뷰 작성 폼 -->
        <div class="review-form">
          <form @submit.prevent="submitReview">
            <label for="review-rating">평점</label><br>
            <input type="number" id="review-rating" v-model="newReview.rank" min="1" max="5" class="rate-box"
              placeholder="별점 1 ~ 5"><br>
            <label for="review-content">리뷰</label><br>
            <input id="review-content" v-model="newReview.content" class="input-box" placeholder="댓글을 입력해주세요"></input><br>
            <button class="create-button" type="submit">작성 하기</button>
          </form>
        </div>
      </div>
    </div>
    <p v-else>로딩중...</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useMemberStore } from '@/stores/member'
import { useMovieStore } from '@/stores/movie';
import { format } from 'date-fns';

const store = useMemberStore()
const movieStore = useMovieStore()
// const user = store.loginUser
// const reviews = ref([]); // 리뷰 리스트
const reviews = ref([])


const newReview = ref({ // 새로운 리뷰를 위한 데이터
  content: '',
  rank: ''
});
const route = useRoute()
const movieId = ref(null)
const movie = ref(null)
const videoId = ref(null)
const genres = ref('')
const actors = ref([])
const crews = ref([])
const liked = ref(false)

onMounted(() => {
  movieId.value = route.params.movie_id;
  axios({
    method: 'get',
    url: `${movieStore.url}/${movieId.value}/`
  })
    .then((response) => {
      movie.value = response.data;
      console.log(movie.value.liked_users)
      submitQuery();
      return axios.get(`${movieStore.url}/${movieId.value}/review/`); // 리뷰 목록 가져오기
    })
    .then((reviewsResponse) => {
      reviews.value = reviewsResponse.data;
      console.log(reviews.value)
      movie.value.liked_users.forEach(user => {
        if (user.username === store.loginUser) {
          liked.value = true
        }
      })
    })
    .catch(error => console.error(error));
});

const addLikeMovie = function (movieId) {
  axios({
    method: 'put',
    url: `${movieStore.url}/likemovie/${movieId}/`,
    headers: {
      'Authorization': `Token ${store.token}`
    }
  })
    .then(response => console.log(response))
    .catch(error => console.log(error))
}

const submitReview = async function () {
  try {
    const response = await axios.post(`${movieStore.url}}/${movieId.value}/review/`, {
      content: newReview.value.content,
      rank: newReview.value.rank,
    }, {
      headers: {
        'Authorization': `Token ${store.token}` // 인증 토큰 추가. Token으로 붙여야됨
      }
    });
    console.log(response)
    console.log(reviews.value)
    reviews.value.push(response.data);

    newReview.value.content = '';
    newReview.value.rank = '';
    console.log(reviews.value)
  } catch (error) {
    console.error(error.response ? error.response.data : error.message);
  }
}
// 같은 유저가 같은 작품에 리뷰 남겼을 때 문제발생

const submitQuery = async function () {
  try {
    const response = await axios({
      method: 'get',
      url: 'https://www.googleapis.com/youtube/v3/search',
      params: {
        part: 'snippet',
        q: `${movie.value.title} official trailer`,
        type: 'video',
        key: 'AIzaSyDskhfMipluROAa1aw94rdNHj4WrrIKHY4',
      }
      // key 갱신 문제
    });
    if (response.data.items.length > 0) {
      videoId.value = response.data.items[0].id.videoId
    } else {
      console.log('No video found')
    }

    const genresResponse = await Promise.all(movie.value.genres.map(getGenreName));
    genres.value = genresResponse.join(', ');

    const actorResponse = await Promise.all(movie.value.cast.map(getPerson));
    actors.value = actorResponse;

    const crewResponse = await Promise.all(movie.value.crew.map(getPerson));
    crews.value = crewResponse;
  } catch (error) {
    console.error(error);
  }
}

const getPerson = async function (PersonId) {
  try {
    const response = await axios.get(`${movieStore.url}/${PersonId}/person/`);
    return response.data
  } catch (error) {
    console.log(error);
    return ''; // 에러가 발생하면 빈 문자열 반환
  }
}

const getGenreName = async function (genreId) {
  try {
    const response = await axios.get(`${movieStore.url}/${genreId}/genre/`);
    return response.data.name;
  } catch (error) {
    console.log(error);
    return ''; // 에러가 발생하면 빈 문자열 반환
  }
}


</script>

<style scoped>
.create-button {
  background-color: #5E31A6;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-right: 10px;
  margin-top: 10px;
  float: right;
}

.star {
  display: flex;
  align-items: center;
  justify-content: end;
}

.rank {
  width: 20px;
  height: 20px;
}

.review-list {
  display: flex;
  flex-direction: row;
  width: 100%;
}

.review-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.input-box {
  background: #0a141e;
  color: white;
  font-size: 15px;
  width: 100%;
  height: 40px;
  padding-left: 20px;
  border-radius: 20px;
  margin-top: 5px;
}

.rate-box {
  width: 20%;
  height: 40px;
  background: #0a141e;
  text-align: center;
  color: white;
  border-radius: 20px;
  margin-top: 5px;
}

.movie-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.video-wrapper {
  position: absolute;
  width: 64vw;
  /* 브라우저 창 너비의 80% */
  padding-top: 36%;
  /* 가로 너비의 50%인 세로 비율 */
  margin: 0 auto;
  /* 가운데 정렬 */
}

.video-frame {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.movie-detail {
  width: 64vw;
  /* 브라우저 창 너비의 80% */
  padding-top: 5%;
  /* 가로 너비의 50%인 세로 비율 */
  margin: 0 auto;
  /* 가운데 정렬 */
}

.movie-detail>p {
  background: rgba(39, 41, 50, 1);
  color: white;
  font-size: 20px;
  padding: 15px 20px;
  /* 상하 15px, 좌우 20px */
  display: flex;
  flex-wrap: wrap;
  /* Flex wrap을 사용하여 요소들을 줄 바꿈 */
  line-height: 1.5;
  /* 줄 간격을 1.5로 설정 */

}


.person-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px;
  /* 적당한 거리 */
}

.person-img {
  width: 120px;
  height: 130px;
  border-radius: 10px;
}

.review-container {
  position: relative;
  width: 64vw;
  /* 브라우저 창 너비의 80% */
  margin: 20px auto;
  /* 위아래 여백을 조정하여 가깝게 배치 */
  background: rgba(39, 41, 50, 1);
  color: white;
  font-size: 20px;
  /* border-radius: 20px; */
  padding: 15px 20px;
  /* 상하 15px, 좌우 20px */
  display: flex;
  line-height: 1.5;
  /* 줄 간격을 1.5로 설정 */
  flex-direction: column;
}


.review-item {
  border: 1px solid #ccc;
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  
}

</style>
