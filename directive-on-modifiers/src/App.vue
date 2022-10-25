<script setup lang="ts">
import {ref} from "vue";

const msg = ref("まだです！");
const onEnterKey = (): void => {
  msg.value = "エンターキーが押下されました。";
}
const onRightButtonClick = (): void => {
  msg.value = "ボタンが右クリックされました。";
}
const onShiftClick = (): void => {
  msg.value = "シフトを押しながらクリックされました。";
};
</script>

<template>
  <p>{{msg}}</p>
  <input type="text" v-on:keydown.enter="onEnterKey"><br>
  <button v-on:click.right="onRightButtonClick">右クリック</button><br>
  <button v-on:click.shift="onShiftClick">シフトを押しながらクリック</button><br>
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
