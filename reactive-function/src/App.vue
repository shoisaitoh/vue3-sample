<script setup lang="ts">
import {reactive, computed} from "vue";
// リアクティブなテンプレート変数をまとめて用意。
const data = reactive({
  Pl: 3.14,
  radius: Math.round(Math.random() * 10)
});
const area = computed(
  (): number => {
    return data.radius * data.radius * data.Pl;
  }
);
setInterval(
  ():void => {
    data.radius = Math.round(Math.random() * 10);
  },
  1000
);
</script>

<template>
  <p>半径{{data.radius}}の円の面積を円周率{{data.Pl}}で計算すると、{{area}}</p>
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
