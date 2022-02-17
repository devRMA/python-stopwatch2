import { switchTheme, changeTheme } from "../../utils/theme";
import { afterEach, describe, it, expect, vi } from "vitest";

describe("changeTheme", () => {
    afterEach(() => {
        vi.restoreAllMocks();
    });

    it("should set in localStorage the theme", () => {
        const spy = vi.spyOn(window.localStorage, "setItem");

        changeTheme("dark");
        expect(spy).toHaveBeenCalledWith("theme", "dark");
        expect(spy).toHaveBeenCalledTimes(1);

        changeTheme("light");
        expect(spy).toHaveBeenCalledWith("theme", "light");
        expect(spy).toHaveBeenCalledTimes(2);

        changeTheme(null);
        expect(spy).toHaveBeenCalledWith("theme", "light");
        expect(spy).toHaveBeenCalledTimes(3);
    });
});

describe("switchTheme", () => {
    afterEach(() => {
        vi.restoreAllMocks();
    });

    it("should set the theme dark if the theme is light, or vice versa", () => {
        window.localStorage.setItem("theme", "dark");

        const spyGetItem = vi.spyOn(window.localStorage, "getItem");
        const spySetItem = vi.spyOn(window.localStorage, "setItem");

        switchTheme();
        expect(spyGetItem).toHaveBeenCalledWith("theme");
        expect(spyGetItem).toHaveBeenCalledTimes(1);
        expect(spyGetItem).toHaveReturnedWith("dark");
        expect(spySetItem).toHaveBeenCalledWith("theme", "light");
        expect(spySetItem).toHaveBeenCalledTimes(1);

        switchTheme();
        expect(spyGetItem).toHaveBeenCalledTimes(2);
        expect(spyGetItem).toHaveReturnedWith("light");
        expect(spySetItem).toHaveBeenCalledWith("theme", "dark");
        expect(spySetItem).toHaveBeenCalledTimes(2);
    });
});
