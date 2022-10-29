<script setup lang="ts">
import {ref, computed} from "vue";

const cocktailDataListInit = new Map<number, Cocktail>();
cocktailDataListInit.set(2345, {id: 2345, name: "ホワイトレディ", price: 1200});
cocktailDataListInit.set(4412, {id: 4412, name: "ブルーハワイ", price: 1500});
cocktailDataListInit.set(6792, {id: 6792, name: "ニューヨーク", price: 1100});
cocktailDataListInit.set(8429, {id: 8429, name: "マティーニ", price: 1500});
const cocktailDataList = ref(cocktailDataListInit);
const cocktail1500 = computed(
  (): Map<number, Cocktail> => {
    const newList = new Map<number, Cocktail>();
    cocktailDataList.value.forEach(
      (value: Cocktail, key: number): void => {
        if(value.price === 1500) {
          newList.set(key, value);
        }
      }
    );
    return newList;
  }
);
const changeWhiteLadyPriceInList = (): void => {
  const whiteLady = cocktailDataList.value.get(2345) as Cocktail;
  whiteLady.price = 1500;
};

interface Cocktail {
  id: number;
  name: string;
  price: number
}
</script>

<template>
  <section>
    全てのカクテルリスト
    <ul>
      <li
        v-for="[id, cocktailName] in cocktailDataList"
        v-bind:key="id">
        IDが{{id}}のカクテルは{{cocktailName}}
      </li>
    </ul>
  </section>
  <br>
  <section>
    値段が1500円のリスト
    <ul>
      <li
        v-for="[id, cocktailItem] in cocktail1500"
        v-bind:key="'cocktail1500' + id">
        {{cocktailItem.name}}の値段は{{cocktailItem.price}}円
      </li>
    </ul>
  </section>
  <p>
    cocktailDataList内のホワイトレディの価格を1500円に
    <button v-on:click="changeWhiteLadyPriceInList">変更</button>
  </p>
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
