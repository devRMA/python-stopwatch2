<script lang="ts" setup>
import { changeTheme } from "./utils/theme";

if (!localStorage.getItem("theme")) {
    localStorage.setItem("theme", "dark");
}

changeTheme(localStorage.getItem("theme"));
</script>

<template>
    <var-button type="success" @click="changeTheme('dark')"> Dark </var-button>
    <var-button type="success" @click="changeTheme('light')">
        Light
    </var-button>
</template>

<style lang="sass">
body
    transition: background-color .25s
    color: var(--color-text)
    background-color: var(--color-body)
</style>
