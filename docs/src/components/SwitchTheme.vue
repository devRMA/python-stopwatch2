<script lang="ts" setup>
import { ref } from "vue";
import { switchTheme } from "../utils/theme";

const darkMode = ref(localStorage.getItem("theme") == "dark");
const changeTheme = () => {
    darkMode.value = !darkMode.value;
    switchTheme();
};
</script>

<template>
    <var-button @click="changeTheme" round>
        <transition name="flip-y" mode="out-in">
            <var-icon v-if="darkMode" name="white-balance-sunny" />
            <var-icon v-else name="weather-night" />
        </transition>
    </var-button>
</template>
