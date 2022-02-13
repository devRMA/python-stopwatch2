<script setup lang="ts">
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
    <img alt="Vue logo" src="./assets/logo.png" />
    <h2>Counter: {{ count }}</h2>
    <button @click="count++">+</button>
</template>

<style lang="sass">
#app
    font-family: Avenir, Helvetica, Arial, sans-serif
    -webkit-font-smoothing: antialiased
    -moz-osx-font-smoothing: grayscale
    text-align: center
    color: #2c3e50
    margin-top: 60px
</style>
