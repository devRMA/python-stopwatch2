<script setup lang="ts">
import { ref } from 'vue'

const drawer = ref(true)
</script>

<template>
    <v-app>
        <v-navigation-drawer v-model="drawer" app></v-navigation-drawer>

        <v-app-bar app>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

            <v-toolbar-title>Python Stopwatch 2</v-toolbar-title>
        </v-app-bar>

        <v-main></v-main>
    </v-app>
</template>

<style lang="sass">
</style>
