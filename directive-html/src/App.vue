<script setup lang="ts">
import {ref} from "vue";

const htmlStr = ref('<a href="https://vuejs.org//">Vue.jsのTOPページ</a>');

const price = ref(1000);

const hello = ref("奥山に紅葉踏み分け鳴く鹿の声聞く時ぞ秋は悲しき");
</script>

<template>
  <section>{{htmlStr}}</section>
  <section v-html="htmlStr"></section>
  <br>
  <section v-pre>
    <p v-on:click="showHello">{{hello!}}</p>
  </section>
  <br>
  <section>
    <input type="number" v-model="price">円<br>
    <p>金額は{{price}}円です。</p>
    <p v-once>金額は{{price}}円です。</p>
  </section>
  <br>
  <p v-cloak>{{hello}}</p>
</template>

<style>
[v-cloak] {
  display: none;
}
</style>
