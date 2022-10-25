<script setup lang="ts">
import {computed, ref} from "vue";

const number = ref(80);
const showOrNot = computed(
  (): boolean => {
    let showOrNot = false;
    const rand = Math.round(Math.random() * 100);
    if (rand >= 50) {
      showOrNot = true;
    }
    return showOrNot;
  }
);

const randomNumber = computed(
  (): number => {
    return Math.round(Math.random() * 100);
  }
);
</script>

<template>
  <p v-if="number >= 50">
    条件に合致したので表示①
  </p>
  <p v-if="Math.round(Math.random() * 100) >= 50">
    条件に合致したので表示②
  </p>
  <p v-if="showOrNot">
    条件に合致したので表示③
  </p>

  <p>
    点数は{{randomNumber}}点で
    <span v-if="randomNumber >= 80">優です。</span>
    <span v-else-if="randomNumber >= 70">良です。</span>
    <span v-else-if="randomNumber >= 60">可です。</span>
    <span v-else>不可です。</span>
  </p>
  <br>
  <p>
    点数は{{randomNumber}}点で
    <template v-if="randomNumber >= 80">優です。
      <span style="color: red;">すばらしい！</span>
    </template>
  </p>
  <br>
  <section>
    v-ifを利用
    <p v-if="showOrNot">
      条件に合致したので表示
    </p>
  </section>
  <section>
    v-showを利用
    <p v-show="showOrNot">
      条件に合致したので表示
    </p>
  </section>
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
