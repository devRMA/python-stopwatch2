import { defineConfig } from "vitepress";

/*
 * Config based on pinia and vite
 * https://github.com/vuejs/pinia/blob/b6382452030a3b006c5bf61302e699f19d4d88e5/packages/docs/.vitepress/config.js
 * https://github.com/vitejs/vite/blob/344642ad630d8658308dbf707ed805cb04b49d58/docs/.vitepress/config.ts
 */

const ogUrl = "https://stopwatch2.vercel.app/";
const ogTitle = "Python Stopwatch 2 ⏱";
const ogSiteTitle = "Python Stopwatch 2";
const ogDescription = "A simple library to measure code performance.";
const ogImage = "https://stopwatch2.vercel.app/social.png";

export default defineConfig({
    appearance: true,
    title: ogSiteTitle,
    description: ogDescription,

    head: [
        ["link", { rel: "icon", type: "image/svg+xml", href: "/logo.svg" }],
        ["meta", { property: "theme-color", content: "#ffd859" }],
        ["meta", { property: "og:locale", content: "en-US" }],
        ["meta", { property: "og:type", content: "website" }],
        ["meta", { property: "og:url", content: ogUrl }],
        ["meta", { property: "og:site_name", content: ogSiteTitle }],
        ["meta", { property: "og:title", content: ogTitle }],
        ["meta", { property: "og:description", content: ogDescription }],
        ["meta", { property: "og:image", content: ogImage }],
        ["meta", { property: "twitter:card", content: "summary_large_image" }],
        ["meta", { property: "twitter:url", content: ogUrl }],
        ["meta", { property: "twitter:title", content: "ogTitle" }],
        ["meta", { property: "twitter:description", content: ogDescription }],
        ["meta", { property: "twitter:image", content: "ogImage" }],
        [
            "script",
            {
                src: "https://unpkg.com/thesemetrics@latest",
                async: "",
                type: "text/javascript",
            },
        ],
    ],

    lastUpdated: true,

    themeConfig: {
        logo: "/logo.svg",

        editLink: {
            pattern:
                "https://github.com/devRMA/python-stopwatch2/edit/site/docs/:path",
            text: "Suggest changes to this page",
        },

        socialLinks: [
            {
                icon: "github",
                link: "https://github.com/devRMA/python-stopwatch2",
            },
        ],

        algolia: {
            appId: "F1RU66L0F9",
            apiKey: "cc4bbb978df4c275bb825a44705d46e3",
            indexName: "stopwatch2",
        },

        footer: {
            message: "Released under the MIT License.",
            copyright:
                "Copyright © 2021-2022 Jonghwan Hyeon, 2022-present Rafael",
        },

        nav: nav(),
        sidebar: sidebar(),
    },
});

function nav() {
    return [
        {
            text: "Guide",
            link: "/guide/getting-started",
        },
        {
            text: "API",
            link: "/api/stopwatch",
        },
        {
            text: "Links",
            items: [
                {
                    text: "Contributors",
                    link: "/contributors",
                },
                {
                    text: "Issues",
                    link: "https://github.com/devRMA/python-stopwatch2/issues",
                },
                {
                    text: "Changelog",
                    link: "https://github.com/devRMA/python-stopwatch2/blob/main/CHANGELOG.md",
                },
            ],
        },
    ];
}

function sidebar() {
    return [
        {
            text: "Introduction",
            items: [
                {
                    text: "Getting Started",
                    link: "/guide/getting-started",
                },
                {
                    text: "Profiling a function",
                    link: "/guide/profiling-function",
                },
                {
                    text: "With statement",
                    link: "/guide/with-statement",
                },
                {
                    text: "Other libraries",
                    link: "/guide/other-libraries",
                },
            ],
        },
        {
            text: "API Reference",
            items: [
                {
                    text: "Stopwatch",
                    link: "/api/stopwatch",
                },
                {
                    text: "Lap",
                    link: "/api/lap",
                },
                {
                    text: "Statistics",
                    link: "/api/statistics",
                },
                {
                    text: "Decorators",
                    link: "/api/decorators",
                },
                {
                    text: "Utils",
                    link: "/api/utils",
                },
            ],
        },
    ];
}
