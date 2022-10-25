<script setup lang="ts">
import {ref} from "vue";

const imgAttributes = ref({
  src: "/images/logo.svg",
  alt: "Vueのロゴ",
  width: 75,
  height: 75
});
</script>

<template>
  <p><img v-bind="imgAttributes"></p>
  <p><img v-bind="imgAttributes" title="ロゴです！"></p>
  <p><img v-bind="imgAttributes" alt="ロゴです！"></p>
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
