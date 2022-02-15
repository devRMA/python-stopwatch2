<script lang="ts" setup>
import { ref } from "vue";
import { darkTheme, lightTheme, useOsTheme } from "naive-ui";

let themeToUse = darkTheme;
const themeInLocalStorage = localStorage.getItem("theme");
if (themeInLocalStorage == null) {
    themeToUse = useOsTheme().value === "dark" ? darkTheme : lightTheme;
} else {
    themeToUse = themeInLocalStorage === "dark" ? darkTheme : lightTheme;
}

const theme = ref(themeToUse);
</script>

<template>
    <n-config-provider :theme="theme">
        <n-card>
            <n-space>
                <n-button @click="theme = darkTheme">Dark</n-button>
                <n-button @click="theme = lightTheme">Light</n-button>
            </n-space>
        </n-card>
    </n-config-provider>
</template>

<style lang="sass">

</style>
