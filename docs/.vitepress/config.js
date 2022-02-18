// @ts-check

/*
 * Config based on pinia and vite
 * https://github.com/vuejs/pinia/blob/13d12710da139db8a92ae5509b89d00097f22a8f/packages/docs/.vitepress/config.js
 * https://github.com/vitejs/vite/blob/a7743039f263f41e1c3971e324f893a5ef5e5508/docs/.vitepress/config.js
 */

const META_URL = "https://stopwatch2.vercel.app/";
const META_TITLE = "Python Stopwatch 2 ⏱";
const META_SITE_NAME = "Python Stopwatch 2";
const META_DESCRIPTION = "A simple library to measure code performance.";
const META_IMAGE = "https://stopwatch2.vercel.app/logo_shadow.png";

const isProduction = process.env.NODE_ENV;

/**
 * @type {import('vitepress').UserConfig['head']}
 */
const productionHead = [
    [
        "script",
        {
            src: "https://unpkg.com/thesemetrics@latest",
            async: "",
            type: "text/javascript",
        },
    ],
];

/**
 * @type {import('vitepress').UserConfig}
 */
module.exports = {
    lang: "en-US",
    title: "Python Stopwatch 2",
    description: "A simple library to measure code performance.",
    lastUpdated: true,
    head: [
        ["link", { rel: "icon", type: "image/png", href: "/logo.png" }],
        [
            "meta",
            {
                property: "theme-color",
                content: "#ffd859",
            },
        ],
        [
            "meta",
            {
                property: "og:locale",
                content: "en-US",
            },
        ],
        [
            "meta",
            {
                property: "og:type",
                content: "website",
            },
        ],
        [
            "meta",
            {
                property: "og:url",
                content: META_URL,
            },
        ],
        [
            "meta",
            {
                property: "og:site_name",
                content: META_SITE_NAME,
            },
        ],
        [
            "meta",
            {
                property: "og:title",
                content: META_TITLE,
            },
        ],
        [
            "meta",
            {
                property: "og:description",
                content: META_DESCRIPTION,
            },
        ],
        [
            "meta",
            {
                property: "og:image",
                content: META_IMAGE,
            },
        ],
        [
            "meta",
            {
                property: "twitter:card",
                content: "summary_large_image",
            },
        ],
        [
            "meta",
            {
                property: "twitter:url",
                content: META_URL,
            },
        ],
        [
            "meta",
            {
                property: "twitter:title",
                content: META_TITLE,
            },
        ],
        [
            "meta",
            {
                property: "twitter:description",
                content: META_DESCRIPTION,
            },
        ],
        [
            "meta",
            {
                property: "twitter:image",
                content: META_IMAGE,
            },
        ],

        ...(isProduction ? productionHead : []),
    ],
    themeConfig: {
        repo: "devRMA/python-stopwatch2",
        logo: "/logo.png",
        docsDir: "docs",
        docsBranch: "docs",
        editLinks: true,
        editLinkText: "Suggest changes to this page",
        lastUpdated: "Last Updated",

        nav: [
            { text: "Guide", link: "/guide/getting-started" },
            { text: "API", link: "/guide/api" },
            {
                text: "Links",
                items: [
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
        ],

        sidebar: {
            "/": [
                {
                    text: "Introduction",
                    children: [
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
                    children: [
                        {
                            text: "Stopwatch",
                            link: "/api/stopwatch",
                        },
                    ],
                },
            ],
        },
    },
};
