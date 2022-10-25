<script setup lang="ts">
import {ref} from "vue";

const cocktailListInit: {[key: number]: string;} = {
  2345: "ホワイトレディ",
  4412: "ブルーハワイ",
  6792: "ニューヨーク"
};
const cocktailList = ref(cocktailListInit);
</script>

<template>
  <ul>
    <li
      v-for="(cocktailName, id) in cocktailList"
      v-bind:key="'cocktailList' + id">
      IDが{{id}}のカクテルは{{cocktailName}}
    </li>
  </ul>
  <br>
  <ul>
    <li
      v-for="(cName, id, index) in cocktailList"
      v-bind:key="'cocktailListWithIdx' + id">
      {{index + 1}}: IDが{{id}}のカクテルは{{cName}}
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
