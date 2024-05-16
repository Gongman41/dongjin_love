import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const API_KEY = import.meta.env.VITE_TMDB_API_KEY
  const url = `https://api.themoviedb.org/3/movie/top_rated?language=ko-kr&api_key=${API_KEY}`
  const movies = ref([])
  const movie = ref()
  const getMovies = function () {
    axios.get(url).then((response) => {

      movies.value = response.data.results
    }).catch((err) => console.log(err))
  }

  const getMovie = function (movieId) {
    axios.get(`https://api.themoviedb.org/3/movie/${movieId}?language=ko-kr&api_key=${API_KEY}`)
      .then((response) => {
        movie.value = response.data
      })
      .catch((err) => console.log(err))
  }

  return {
    movies, movie,
    getMovies, getMovie,
  }
}, { persist: true })
