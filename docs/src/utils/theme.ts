import dark from "@varlet/ui/es/themes/dark";
import { StyleProvider } from "@varlet/ui";

export function changeTheme(theme: string | null) {
    StyleProvider(theme === "dark" ? dark : null);
    localStorage.setItem("theme", theme || "light");
}

export function switchTheme() {
    const theme = localStorage.getItem("theme");
    changeTheme(theme === "dark" ? "light" : "dark");
}
