<script setup lang="ts">
import {ref, computed} from "vue";

const cocktailDataListInit = new Map<number, Cocktail>();
cocktailDataListInit.set(1, {id: 1, name: "ホワイトレディ", price: 1200});
cocktailDataListInit.set(2, {id: 2, name: "ブルーハワイ", price: 1500});
cocktailDataListInit.set(3, {id: 3, name: "ニューヨーク", price: 1100});
cocktailDataListInit.set(4, {id: 4, name: "マティーニ", price: 1500});
const cocktailDataList = ref(cocktailDataListInit);

const cocktailNo = ref(1);
const priceMsg = computed(
  (): string => {
    const cocktail = cocktailDataListInit.get(cocktailNo.value);
    let msg = "該当カクテルはありません";
    if(cocktail !== undefined) {
      msg = `該当するカクテルは${cocktail.name}で、価格は${cocktail.price}円です。`;
    }
    return msg;
  }
);

setInterval(
  (): void => {
    cocktailNo.value = Math.round(Math.random() * 3) + 1;
  },
  1000
);

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
  <section>
    <p>現在のカクテル番号: {{cocktailNo}}</p>
    <p>{{priceMsg}}</p>
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
