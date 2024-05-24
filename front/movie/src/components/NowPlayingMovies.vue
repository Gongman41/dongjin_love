<template>
  <h2 style="color: black; padding-left: 2%;">현재 상영중인 영화</h2>
  <div class="user-ranking">
    <table class="ranking-table">
      <tbody>
        <tr v-for="movie in movies" :key="movie.rank">
          <td>{{ movie.rank }}</td>
          <td>{{ movie.movieNm }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'
import axios from 'axios';

export default {
  setup() {
    const movies = ref([]);
    const API_KEY = import.meta.env.VITE_KOBIS_API_KEY
    onMounted(() => {
      const dt = new Date();
      const m = dt.getMonth() + 1 < 10 ? '0' + (dt.getMonth() + 1) : dt.getMonth() + 1
      const d = dt.getDate() - 1 < 10 ? '0' + (dt.getDate() - 1) : dt.getDate() - 1
      const y = dt.getFullYear()
      const result = y + m + d
      console.log(result)
      axios({
        method: 'get',
        url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=${API_KEY}&targetDt=${result}&itemPerPage=5`,
      })
        .then(response => {
          const parser = new DOMParser()
          const xmlDoc = parser.parseFromString(response.data, 'text/xml')
          const dailyBoxOfficeList = xmlDoc.getElementsByTagName('dailyBoxOffice')
          for (let i = 0; i < dailyBoxOfficeList.length; i++) {
            const movie = {
              rank: dailyBoxOfficeList[i].getElementsByTagName('rank')[0].childNodes[0].nodeValue,
              movieNm: dailyBoxOfficeList[i].getElementsByTagName('movieNm')[0].childNodes[0].nodeValue,
              openDt: dailyBoxOfficeList[i].getElementsByTagName('openDt')[0].childNodes[0].nodeValue,
              audiAcc: dailyBoxOfficeList[i].getElementsByTagName('audiAcc')[0].childNodes[0].nodeValue
            }
            movies.value.push(movie)
          }
        })
        .catch(error => console.log(error))
    });

    // 3자리씩 끊어서 출력하는 함수
    function formatAudiAcc(acc) {
      const regex = /\B(?=(\d{3})+(?!\d))/g;
      return acc.toString().replace(regex, ",");
    }

    return {
      movies,
      formatAudiAcc
    };
  }
}
</script>

<style scoped>
.user-ranking {
  max-width: 800px;
  margin: 3% auto;
  border: 1px solid #ddd;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  background-color: #fff;
}

.ranking-table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif;
}

.ranking-table thead {
  background-color: #4CAF50;
  color: white;
  font-weight: bold;
}

.ranking-table td,
.ranking-table th {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.ranking-table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.ranking-table tbody tr:hover {
  background-color: #f1f1f1;
  cursor: pointer;
}


.ranking-table td.rank {
  width: 10%;
  font-weight: bold;
}

.ranking-table td.movieNm {
  width: 70%;
}

.ranking-table td.lovepoint {
  width: 20%;
  color: #555;
}
</style>