<script setup lang="ts">
import { NButton } from 'naive-ui'
import { ref } from 'vue'

const counter = ref(0)
</script>

<template>
    Hello World
    <n-button @click="counter++">{{ counter }} +</n-button>
</template>

<style lang="sass">
</style>
