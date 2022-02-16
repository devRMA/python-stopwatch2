import vue from "@vitejs/plugin-vue";
import components from "unplugin-vue-components/vite";
import { VarletUIResolver } from "unplugin-vue-components/resolvers";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        components({
            resolvers: [VarletUIResolver()],
        }),
    ],
});
