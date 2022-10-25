<script setup lang="ts">
import {ref} from "vue";

const cocktailListInit: String[] = ["ホワイトレディ", "ブルーハワイ", "ニューヨーク"];
const cocktailList = ref(cocktailListInit);
</script>

<template>
  <ul>
    <li
      v-for="cocktailName in cocktailList"
      v-bind:key="cocktailName">
      {{cocktailName}}
    </li>
  </ul>
  <br>
  <ul>
    <li
      v-for="(cocktailName, index) in cocktailList"
      v-bind:key="cocktailName">
      {{cocktailName}}(インデックス{{index}})
    </li>
  </ul>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
