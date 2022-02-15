<script setup lang="ts">
import { ref } from 'vue'

const counter = ref(0)
</script>

<template>
    Hello World
    <button @click="counter++">{{ counter }} +</button>
</template>

<style lang="sass">
</style>
