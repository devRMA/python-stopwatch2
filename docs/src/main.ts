import "@varlet/touch-emulator";
import { createApp } from "vue";

import { changeTheme } from "./utils/theme";
import App from "./App.vue";
import './styles/main.sass';

// Setting the theme
if (!localStorage.getItem("theme")) {
    localStorage.setItem("theme", "dark");
}
changeTheme(localStorage.getItem("theme"));

const app = createApp(App);

app.mount("#app");
