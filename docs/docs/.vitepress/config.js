import { defineConfig } from "vitepress";

export default defineConfig({
    lang: "en-US",
    title: "Python Stopwatch 2",
    description: "A simple stopwatch for measuring code performance.",
    lastUpdated: true,
    themeConfig: {
        repo: "devRMA/python-stopwatch2",
        docsDir: "docs",
        docsBranch: "docs",
        editLinks: true,
        editLinkText: "Edit this page on GitHub",
        lastUpdated: "Last Updated",

        sidebar: {
            "/": [
                {
                    text: "Introduction",
                    children: [
                        {
                            text: "What is Python Stopwatch 2?",
                            link: "/",
                        },
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
                    text: "Advanced",
                    children: [
                        {
                            text: "API Reference",
                            link: "/guide/api",
                        },
                    ],
                },
            ],
        },
    },
});
