---
layout: page
title: Contributors
description: The main contributors to the library
---

<script setup>
    import {
        VPTeamPage,
        VPTeamPageTitle,
        VPTeamMembers,
    } from 'vitepress/theme';
    const members = [
        {
            avatar: 'https://www.github.com/devRMA.png',
            name: 'Rafael Alves',
            title: 'Current maintainer of this fork.',
            links: [
                { icon: 'github', link: 'https://github.com/devRMA' },
            ],
        },
        {
            avatar: 'https://www.github.com/jonghwanhyeon.png',
            name: 'Jonghwan Hyeon',
            title: 'Original library creator',
            links: [
                { icon: 'github', link: 'https://github.com/jonghwanhyeon' },
            ],
        },
    ];
</script>

<VPTeamPage>
    <VPTeamPageTitle>
        <template #title>Contributors</template>
        <template #lead>
            The main contributors to the library
        </template>
    </VPTeamPageTitle>
    <VPTeamMembers :members="members" />
</VPTeamPage>
