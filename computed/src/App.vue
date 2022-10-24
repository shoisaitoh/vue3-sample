<script setup lang="ts">
import {ref, computed} from "vue";
const radiusInit = Math.round(Math.random() * 10);
const Pl = ref(3.14);
const radius = ref(radiusInit);
const area = computed(
  (): number => {
    return radius.value * radius.value * Pl.value;
  }
);
setInterval(
  ():void => {
    radius.value = Math.round(Math.random() * 10);
  },
  1000
);
</script>

<template>
  <p>半径{{radius}}の円の面積を円周率{{ Pl }}で計算すると、{{area}}</p>
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
