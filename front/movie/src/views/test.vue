<template>
  <!-- dirty and sloppy html ahead :) -->
  <main>
    <div class="vs vs-1">
      <div class="one abs">
        <div class="dots abs"></div>
        <div class="conic abs"></div>
      </div>
      <div class="two abs">
        <div class="dots abs"></div>
        <div class="conic abs"></div>
      </div>
      <div class="content">
        <img class="contender" src="https://i.imgur.com/dIXnEra.png" abs="pikachu" />
        <div class="cloud">
          <div class="blob"></div>
          <div class="blob"></div>
          <div class="blob"></div>
          <div class="blob"></div>
          <div class="text">VS</div>
        </div>
        <img class="contender contender--right" src="https://i.imgur.com/BN7jfWU.png" abs="charmeleon" />
      </div>
    </div>

    <div class="vs vs-2">
      <div class="one abs"></div>
      <div class="two abs"></div>

      <div class="content">
        <img class="contender" src="https://i.imgur.com/dIXnEra.png" abs="pikachu" />
        <div class="text">VS</div>
        <img class="contender contender--right" src="https://i.imgur.com/BN7jfWU.png" abs="charmeleon" />
      </div>
    </div>

    <div class="vs vs-3">
      <div class="conic abs"></div>
      <div class="boxes">
        <div class="box">
          <img class="contender" src="https://i.imgur.com/23USGFO.png" alt="bulbasaur" />
        </div>
        <div class="box">
          <img class="contender" src="https://i.imgur.com/mB4sMVG.png" alt="chikorita" />
        </div>
        <div class="text">VS</div>
      </div>
    </div>

    <div class="vs vs-4">
      <div class="boxes">
        <div class="box">
          <img class="contender" src="https://i.imgur.com/23USGFO.png" alt="bulbasaur" />
        </div>
        <div class="box">
          <img class="contender" src="https://i.imgur.com/mB4sMVG.png" alt="chikorita" />
        </div>
      </div>
      <div class="text abs">
        <span>
          <span>V</span><span>S</span>
        </span>
      </div>
    </div>

    <div class="vs vs-5">
      <div class="one abs"></div>
      <div class="one abs"></div>
      <div class="two abs"></div>
      <div class="two abs"></div>

      <div class="content">
        <img class="contender" src="https://i.imgur.com/ssn8cdw.png" abs="pikachu" />
        <div class="text">VS</div>
        <img class="contender contender--right" src="https://i.imgur.com/tucm9wC.png" abs="charmeleon" />
      </div>
    </div>

    <div class="vs vs-6">
      <div class="one abs"></div>
      <div class="two abs"></div>

      <div class="content">
        <img class="contender" src="https://i.imgur.com/ssn8cdw.png" abs="pikachu" />
        <div class="text"><span>V</span><span>S</span></div>
        <img class="contender contender--right" src="https://i.imgur.com/tucm9wC.png" abs="charmeleon" />
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'


</script>

<style scoped>
/* very dirty and sloppy css ahead :) */

@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Passion+One:wght@900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');

:root {
  --cloud-border: 3px;
}

body {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

main {
  min-width: 1470px;
  display: grid;
  grid-template-columns: 50% 50%;
  grid-template-rows: auto;
  border: 1px solid black;
}

.abs {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.vs {
  height: 400px;
  border: 1px solid black;
  position: relative;
  background: black;
}

.contender {
  height: 200px;
}

@media screen and (max-width: 800px) {
  main {
    min-width: 800px;
    grid-template-columns: 100%;
    grid-template-rows: auto;
  }
}

.vs-1 .one {
  background-color: yellow;
  clip-path: polygon(51% 0%,
      47% 27%,
      53% 25%,
      43% 86%,
      47% 85%,
      45% 100%,
      0% 100%,
      0% 0%);
}

.vs-1 .one .dots {
  z-index: -200;
  background-size: 20px 20px;
  background-repeat: repeat;
  background-image: radial-gradient(rgba(255, 153, 0, 0.5) 40%, transparent 16%);
}

.vs-1 .one .conic {
  z-index: -100;
  background-image: repeating-conic-gradient(rgba(255, 217, 0, 0.8) 0 10deg, transparent 0 20deg);
}

.vs-1 .two {
  background: rgb(123, 10, 0);
  clip-path: polygon(57% 0%,
      53% 18%,
      57% 17%,
      45% 83%,
      49% 82%,
      45% 100%,
      100% 100%,
      100% 0%);
}

.vs-1 .two .dots {
  z-index: -200;
  background-size: 20px 20px;
  background-repeat: repeat;
  background-image: radial-gradient(rgba(255, 0, 0, 0.3) 40%, transparent 16%);
}

.vs-1 .two .conic {
  z-index: -100;
  background-image: repeating-conic-gradient(rgba(255, 0, 0, 0.7) 0 10deg, transparent 0 20deg);
}

.vs-1 .cloud {
  width: 100px;
  height: 100px;
  transform: scale(1.2);
}

.vs-1 .blob {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  position: absolute;
  background: white;
}

.vs-1 .blob:nth-child(1) {
  top: 0%;
  left: 0%;
  transform: scale(1.4);
  border-top: calc(var(--cloud-border) - 1px) solid black;
  border-left: calc(var(--cloud-border) - 1px) solid black;
  box-shadow: inset 0px -5px 0px 0px rgb(222, 222, 222);
  z-index: 400;
}

.vs-1 .blob:nth-child(2) {
  top: 0%;
  right: 0%;
  transform: scale(1.2);
  border-top: var(--cloud-border) solid black;
  border-right: var(--cloud-border) solid black;
  z-index: 400;
}

.vs-1 .blob:nth-child(3) {
  bottom: 0%;
  left: 0%;
  transform: scale(1.2);
  border-left: var(--cloud-border) solid black;
  border-bottom: var(--cloud-border) solid black;
  box-shadow: inset 0px -5px 0px 0px rgb(222, 222, 222);
  z-index: 400;
}

.vs-1 .blob:nth-child(4) {
  bottom: 0%;
  right: 0%;
  transform: scale(1.5);
  border-right: var(--cloud-border) solid black;
  border-bottom: var(--cloud-border) solid black;
  box-shadow: inset -8px -8px 0px 0px rgb(222, 222, 222);
  z-index: 400;
}

.vs-1 .text {
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 500;
  font-size: 65px;
  font-family: Anton, Arial, Helvetica, sans-serif;
  transform: translate(-50%, -50%);
  color: rgb(69, 157, 208);
  text-shadow:
    0px -1px white,
    1px -1px white,
    1px 0px white,
    1px 1px white,
    0px 1px white,
    -1px 1px white,
    -1px 0px white,
    -1px -1px white,
    0px -3px black,
    3px -3px black,
    3px 0px black,
    3px 3px black,
    0px 3px black,
    -3px 3px black,
    -3px 0px black,
    -3px -3px black;
}

.vs-1 .content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 100%;
  position: relative;
  z-index: 999;
}

.vs-2 {
  background-color: rgb(251, 225, 84);
}

.vs-2 .one {
  background-color: rgba(244, 180, 76);
  background-image: repeating-linear-gradient(60deg,
      rgb(232, 169, 71),
      rgb(232, 169, 71) 10px,
      transparent 10px,
      transparent 40px);
  clip-path: polygon(0% 0%,
      90% 0%,
      74% 17%,
      76% 23%,
      50% 50%,
      19% 75%,
      21% 81%,
      0% 100%);
}

.vs-2 .two {
  background-color: rgba(234, 87, 68);
  background-image: repeating-linear-gradient(60deg,
      rgb(233, 84, 65),
      rgb(233, 84, 65) 10px,
      transparent 10px,
      transparent 40px);
  clip-path: polygon(100% 0%,
      100% 100%,
      10% 100%,
      26% 83%,
      24% 77%,
      50% 50%,
      81% 25%,
      79% 19%);
}

.vs-2 .content {
  position: relative;
  z-index: 999;
  height: 100%;
  display: flex;
  justify-content: space-around;
}

.vs-2 .text {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background-color: rgb(201, 63, 48);
  align-self: center;
  text-align: center;
  line-height: 150px;
  font-family: Bangers, Arial, Helvetica, sans-serif;
  font-size: 85px;
  color: rgb(251, 225, 84);
  border: 10px solid rgb(103, 22, 22);
}

.vs-2 .contender:first-child {
  margin-top: 25px;
}

.vs-2 .contender--right {
  align-self: flex-end;
  margin-bottom: 20px;
}

.vs-3 .conic {
  background-image: repeating-conic-gradient(#A3EBB1 0 19deg,
      #116530 0 20deg,
      #18A558 0 39deg,
      #116530 0 40deg);
}

.vs-3 .boxes {
  display: grid;
  grid-template-columns: 50% 50%;
  grid-template-rows: auto;
  height: 100%;
  position: relative;
  z-index: 999;
}

.vs-3 .box {
  border: 20px solid white;
  border-radius: 2px;
  box-shadow: inset 2px 2px 0px 5px rgba(0, 0, 0, 0.5),
    2px 2px 0px 5px rgba(0, 0, 0, 0.5);
  margin: 40px;
  background-color: white;
  transform: skewX(-5deg);
  background-image: repeating-linear-gradient(transparent 10px, green 12px);
}

.vs-3 .text {
  position: absolute;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background-color: white;
  z-index: 1000;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) skewX(-5deg);
  box-shadow: inset 2px 2px 0px 5px rgba(0, 0, 0, 0.5),
    2px 2px 0px 5px rgba(0, 0, 0, 0.5);
  border: 10px solid white;
  line-height: 150px;
  font-size: 60px;
  color: red;
  text-align: center;
  text-shadow: 4px 4px rgba(0, 0, 0, 0.5);
  font-family: 'Bebas Neue', Arial, Helvetica, sans-serif;
  -webkit-text-stroke: 1px rgba(0, 0, 0, 0.5);
  background-image: repeating-conic-gradient(transparent 0deg, red 5deg);
}

.vs-3 .contender {
  height: 80%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.vs-4 {
  background: rgba(132, 181, 160);
}

.vs-4 .boxes {
  display: grid;
  grid-template-columns: 50% 50%;
  grid-template-rows: auto;
  height: 100%;
  position: relative;
  z-index: 500;
}

.vs-4 .box {
  border: 5px solid rgb(241, 248, 197);
  border-radius: 5px;
  margin: 20px;
  background-color: rgba(241, 248, 197, 0.5);
  background-image:
    repeating-linear-gradient(transparent, transparent 20px, rgba(0, 0, 0, 0.1) 20px, rgba(0, 0, 0, 0.1) 40px),
    repeating-linear-gradient(to right, transparent, transparent 20px, rgba(0, 0, 0, 0.1) 20px, rgba(0, 0, 0, 0.1) 40px);
  display: flex;
  align-items: center;
  justify-content: center;
}

.vs-4 .box:nth-child(1) {
  border-color: rgb(181, 230, 180);
  background-color: rgba(181, 230, 180, 0.5);
}

.vs-4 .text {
  background-image: linear-gradient(to right,
      rgba(181, 230, 180, 1) 50%,
      rgba(241, 248, 197, 1) 50%);
  clip-path: circle(15%);
  z-index: 999;
  transform: rotateZ(12deg);
}

.vs-4 .text>span {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotateZ(-15deg);
  display: inline-block;
  font-family: 'Balsamiq Sans', Arial, Helvetica, sans-serif;
  font-size: 70px;
  color: rgba(241, 248, 197, 1);
}

.vs-4 .text>span span:first-child {
  display: inline-block;
  transform: rotateZ(-13deg);
}

.vs-4 .text>span span:last-child {
  display: inline-block;
  transform: rotateZ(13deg);
  color: rgba(181, 230, 180, 1);
}

.vs-5 {
  overflow: hidden;
  background: white;
}

.vs-5 .one {
  z-index: 100;
  margin-left: -20px;
  background-color: #00E5FF;
  background-image: repeating-radial-gradient(circle at calc(50% + 20px) center,
      transparent,
      transparent 20px,
      rgba(0, 0, 0, 0.1) 20px,
      rgba(0, 0, 0, 0.1) 40px),
    repeating-radial-gradient(circle at calc(50% + 20px) center,
      transparent 17%,
      rgba(0, 0, 0, 0.5));
  ;
  clip-path: polygon(0% 0%,
      50% 0%,
      52% 10%,
      48% 30%,
      52% 50%,
      48% 70%,
      52% 90%,
      50% 100%,
      0% 100%);
}

.vs-5 .one:nth-child(2) {
  z-index: 50;
  margin-left: -15px;
  background-color: black;
  background-image: none;
}

.vs-5 .two {
  z-index: 100;
  margin-left: 20px;
  background-color: #005EFF;
  background-image: repeating-radial-gradient(circle at calc(50% - 20px) center,
      transparent,
      transparent 20px,
      rgba(0, 0, 0, 0.1) 20px,
      rgba(0, 0, 0, 0.1) 40px),
    repeating-radial-gradient(circle at calc(50% - 20px) center,
      transparent 17%,
      rgba(0, 0, 0, 0.5));
  clip-path: polygon(50% 0%,
      100% 0%,
      100% 100%,
      50% 100%,
      52% 90%,
      48% 70%,
      52% 50%,
      48% 30%,
      52% 10%);
}

.vs-5 .two:nth-child(4) {
  z-index: 50;
  margin-left: 15px;
  background-color: black;
  background-image: none;
}

.vs-5 .content {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-around;
  position: relative;
  z-index: 999;
}

.vs-5 .text {
  width: 100px;
  height: 100px;

  font-size: 85px;
  font-family: 'Passion One', Arial, Helvetica, sans-serif;
  text-align: center;
  line-height: 100px;
  color: white;
  -webkit-text-stroke: 5px rgba(0, 0, 0, 0.9);
}

:root {
  --wall: rgba(0, 0, 0, 0.1);
  --floor: rgba(0, 0, 0, 0.3);
}

.vs-6 .one {
  background-color: #73BEFF;
  clip-path: polygon(0% 0%,
      55% 0%,
      45% 50%,
      55% 50%,
      45% 100%,
      0% 100%);
  background-image: conic-gradient(from 0deg at 25% center,
      transparent,
      transparent 25%,
      var(--floor) 25%,
      var(--floor) 65%,
      var(--wall) 65%,
      var(--wall) 100%);
}

.vs-6 .two {
  background-color: #6894EB;
  background-image: conic-gradient(from 0deg at 75% center,
      var(--wall),
      var(--wall) 35%,
      var(--floor) 25%,
      var(--floor) 75%,
      transparent 75%,
      transparent 100%);
  clip-path: polygon(55% 0%,
      100% 0%,
      100% 100%,
      45% 100%,
      55% 50%,
      45% 50%);
}

.vs-6 .content {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-around;
  position: relative;
  z-index: 999;
}

.vs-6 .text {
  font-size: 90px;
  font-family: Oswald, Arial, Helvetica, sans-serif;
  transform: skewX(-10deg);
}

.vs-6 .text span:nth-child(1) {
  color: white;
  text-shadow: 5px 5px #6894EB;
}

.vs-6 .text span:nth-child(2) {
  color: white;
  text-shadow: 5px 5px #73BEFF;
}
</style>