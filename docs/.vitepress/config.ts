import { defineConfig } from "vitepress";

/*
 * Config based on pinia and vite
 * https://github.com/vuejs/pinia/blob/b6382452030a3b006c5bf61302e699f19d4d88e5/packages/docs/.vitepress/config.js
 * https://github.com/vitejs/vite/blob/344642ad630d8658308dbf707ed805cb04b49d58/docs/.vitepress/config.ts
 */

const ogUrl = "https://stopwatch2.vercel.app/";
const ogTitle = "Python Stopwatch 2 ⏱";
const ogSiteTitle = "Python Stopwatch 2";
const ogDescription =
    "A small, fully typed Python stopwatch and profiler. Time a block, time each iteration with laps, or time every call to a function — with mean, median and standard deviation included.";
const ogImage = "https://stopwatch2.vercel.app/social.png";

export default defineConfig({
    appearance: true,
    title: ogSiteTitle,
    titleTemplate: `:title | ${ogSiteTitle}`,
    description: ogDescription,
    lang: "en-US",

    head: [
        ["link", { rel: "preconnect", href: "https://fonts.googleapis.com" }],
        ["link", { rel: "preconnect", href: "https://fonts.gstatic.com" }],
        [
            "link",
            {
                rel: "stylesheet",
                href: "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono",
            },
        ],
        ["link", { rel: "icon", type: "image/svg+xml", href: "/logo.svg" }],
        ["meta", { property: "theme-color", content: "#ffd859" }],
        ["meta", { property: "og:locale", content: "en-US" }],
        ["meta", { property: "og:type", content: "website" }],
        ["meta", { property: "og:url", content: ogUrl }],
        ["meta", { property: "og:site_name", content: ogSiteTitle }],
        ["meta", { property: "og:title", content: ogTitle }],
        ["meta", { property: "og:description", content: ogDescription }],
        ["meta", { property: "og:image", content: ogImage }],
        ["meta", { property: "og:image:width", content: "1280" }],
        ["meta", { property: "og:image:height", content: "640" }],
        ["meta", { property: "og:image:alt", content: ogTitle }],
        ["meta", { name: "twitter:card", content: "summary_large_image" }],
        ["meta", { name: "twitter:url", content: ogUrl }],
        ["meta", { name: "twitter:title", content: ogTitle }],
        ["meta", { name: "twitter:description", content: ogDescription }],
        ["meta", { name: "twitter:image", content: ogImage }],
        ["meta", { name: "twitter:image:alt", content: ogTitle }],
        [
            "script",
            { type: "application/ld+json" },
            JSON.stringify({
                "@context": "https://schema.org",
                "@type": "SoftwareSourceCode",
                name: ogSiteTitle,
                description: ogDescription,
                codeRepository:
                    "https://github.com/devRMA/python-stopwatch2",
                programmingLanguage: "Python",
                url: ogUrl,
                license: "https://opensource.org/licenses/MIT",
                author: {
                    "@type": "Person",
                    name: "Rafael Alves",
                    url: "https://github.com/devRMA",
                },
            }),
        ],
        // [
        //     "script",
        //     {
        //         src: "https://unpkg.com/thesemetrics@latest",
        //         async: "",
        //         type: "text/javascript",
        //     },
        // ],
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

    sitemap: {
        hostname: 'https://stopwatch2.vercel.app'
      }

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
                    text: "With statement",
                    link: "/guide/with-statement",
                },
                {
                    text: "Measuring laps",
                    link: "/guide/measuring-laps",
                },
                {
                    text: "Profiling a function",
                    link: "/guide/profiling-function",
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
