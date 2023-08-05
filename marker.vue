<template>
  <div>
    <div ref="text" @mouseup="markText">
      {{ text }}
    </div>
    <ul>
      <li v-for="mark in marks" :key="mark.id">
        {{ mark.text }} ({{ mark.start }} - {{ mark.end }})
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: "ここにテキストを入力してください。",
      marks: []
    };
  },
  methods: {
    markText() {
      const selection = window.getSelection();
      if (selection.toString()) {
        const range = selection.getRangeAt(0);
        const start = range.startOffset;
        const end = range.endOffset;
        const text = range.toString();
        const id = Date.now();
        this.marks.push({ id, start, end, text });
        const span = document.createElement("span");
        span.style.backgroundColor = "green";
        range.surroundContents(span);
      }
    }
  }
};
</script>

<style>
span {
  background-color: green;
}
</style>