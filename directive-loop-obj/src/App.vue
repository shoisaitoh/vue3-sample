<script setup lang="ts">
import {ref} from "vue";
const whiteLadyInit: {
  id: number;
  name: string;
  price: number;
  recipe: string;
} = {
  id: 2345,
  name: "ホワイトレディ",
  price: 1200,
  recipe: "ジン30ml+コワントロー15ml+レモン果汁+15ml"
};
const whiteLady = ref(whiteLadyInit);

const cocktailDataListInit: Cocktail[] = [
  {id: 2345, name: "ホワイトレディ", price: 1200},
  {id: 4412, name: "ブルーハワイ", price: 1500},
  {id: 6792, name: "ニューヨーク", price: 1100},
  {id: 8429, name: "マティーニ", price: 1500},
];
const cocktailDataList = ref(cocktailDataListInit);

interface Cocktail {
  id: number;
  name: string;
  price: number;
}

const cocktailDataListInit2 = new Map<number, Cocktail>();
cocktailDataListInit2.set(2345, {id: 2345, name: "ホワイトレディ", price: 1200});
cocktailDataListInit2.set(4412, {id: 4412, name: "ブルーハワイ", price: 1500});
cocktailDataListInit2.set(6792, {id: 6792, name: "ニューヨーク", price: 1100});
cocktailDataListInit2.set(8429, {id: 8429, name: "マティーニ", price: 1500});
const cocktailDataList2 = ref(cocktailDataListInit2);
</script>

<template>
  <dl>
    <template
      v-for="(value, key) in whiteLady"
      v-bind:key="key">
      <dt>{{key}}</dt>
      <dt>{{value}}</dt>
    </template>
  </dl>
  <br>
  <ul>
    <li
      v-for="cocktailItem in cocktailDataList"
      v-bind:key="cocktailItem.id">
      {{cocktailItem.name}}の値段は{{cocktailItem.price}}円
    </li>
  </ul>
  <br>
  <ul>
    <li
      v-for="[id, cocktailItem2] in cocktailDataList2"
      v-bind:key="id">
      {{cocktailItem2.name}}の値段は{{cocktailItem2.price}}円
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
