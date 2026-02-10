# karakeep - Markdown Content

Repository: https://github.com/karakeep-app/karakeep
Branch: main

==================================================
File: AGENTS.md
==================================================
# Karakeep Project Overview

This document provides context about the Karakeep project for the different agents.

## Project Overview

Karakeep is a monorepo project managed with Turborepo. It appears to be a web application with a focus on collecting and organizing information, possibly a bookmarking or "read-it-later" service. The project is built with a modern tech stack, including:

- **Frontend:** Next.js, React, TypeScript, Tailwind CSS
- **Backend:** Hono (a lightweight web framework), tRPC
- **Database:** Drizzle ORM (likely with a relational database like PostgreSQL or SQLite)
- **Tooling:** Prettier,oxlint, Vitest, pnpm

## Project Structure

The project is organized into `apps` and `packages`:

### Applications (`apps/`)

- **`web`:** The main web application, built with Next.js.
- **`browser-extension`:** A browser extension, likely for saving content to karakeep.
- **`cli`:** A command-line interface for interacting with the service.
- **`landing`:** A landing page for the project.
- **`mobile`:** A mobile application (details unknown).
- **`mcp`:** The Model Context Protocol (MCP) server to communicate with Karakeep.
- **`workers`:** Background workers for processing tasks.

### Packages (`packages/`)

- **`api`:** The main API, built with Hono and tRPC.
- **`db`:** Database schema and migrations, using Drizzle ORM.
- **`e2e_tests`:** End-to-end tests for the project.
- **`open-api`:** OpenAPI specifications for the API.
- **`sdk`:** A software development kit for interacting with the API.
- **`shared`:** Shared code and types between packages.
- **`shared-react`:** Shared React components and hooks.
- **`shared-server`:** Shared logic that's meant to be used on the server-side.
- **`trpc`:** tRPC router and procedures. Most of the business logic is here.

### Docs

- **docs/docs/03-configuration.md**: Explains configuration options for the project.

## Development Workflow

- **Package Manager:** pnpm
- **Build System:** Turborepo
- **Code Formatting:** Prettier
- **Linting:** oxlint
- **Testing:** Vitest

## Other info

- This project uses shadcn/ui. The shadcn components in the web app are in `packages/web/components/ui`.
- This project uses Tailwind CSS.
- For the mobile app, we use [expo](https://expo.dev/).

### Common Commands

- `pnpm typecheck`: Typecheck the codebase.
- `pnpm lint`: Lint the codebase.
- `pnpm lint:fix`: Fix linting issues.
- `pnpm format`: Format the codebase.
- `pnpm format:fix`: Fix formatting issues.
- `pnpm test`: Run tests.
- `pnpm db:generate --name description_of_schema_change`: db migration after making schema changes

Starting services:
- `pnpm web`: Start the web application (this doesn't return, unless you kill it).
- `pnpm workers`: Starts the background workers (this doesn't return, unless you kill it).


==================================================
File: CLAUDE.md
==================================================
# Karakeep Project Overview

This document provides context about the Karakeep project for the different agents.

## Project Overview

Karakeep is a monorepo project managed with Turborepo. It appears to be a web application with a focus on collecting and organizing information, possibly a bookmarking or "read-it-later" service. The project is built with a modern tech stack, including:

- **Frontend:** Next.js, React, TypeScript, Tailwind CSS
- **Backend:** Hono (a lightweight web framework), tRPC
- **Database:** Drizzle ORM (likely with a relational database like PostgreSQL or SQLite)
- **Tooling:** Prettier,oxlint, Vitest, pnpm

## Project Structure

The project is organized into `apps` and `packages`:

### Applications (`apps/`)

- **`web`:** The main web application, built with Next.js.
- **`browser-extension`:** A browser extension, likely for saving content to karakeep.
- **`cli`:** A command-line interface for interacting with the service.
- **`landing`:** A landing page for the project.
- **`mobile`:** A mobile application (details unknown).
- **`mcp`:** The Model Context Protocol (MCP) server to communicate with Karakeep.
- **`workers`:** Background workers for processing tasks.

### Packages (`packages/`)

- **`api`:** The main API, built with Hono and tRPC.
- **`db`:** Database schema and migrations, using Drizzle ORM.
- **`e2e_tests`:** End-to-end tests for the project.
- **`open-api`:** OpenAPI specifications for the API.
- **`sdk`:** A software development kit for interacting with the API.
- **`shared`:** Shared code and types between packages.
- **`shared-react`:** Shared React components and hooks.
- **`shared-server`:** Shared logic that's meant to be used on the server-side.
- **`trpc`:** tRPC router and procedures. Most of the business logic is here.

### Docs

- **docs/docs/03-configuration.md**: Explains configuration options for the project.

## Development Workflow

- **Package Manager:** pnpm
- **Build System:** Turborepo
- **Code Formatting:** Prettier
- **Linting:** oxlint
- **Testing:** Vitest

## Other info

- This project uses shadcn/ui. The shadcn components in the web app are in `packages/web/components/ui`.
- This project uses Tailwind CSS.
- For the mobile app, we use [expo](https://expo.dev/).

### Common Commands

- `pnpm typecheck`: Typecheck the codebase.
- `pnpm lint`: Lint the codebase.
- `pnpm lint:fix`: Fix linting issues.
- `pnpm format`: Format the codebase.
- `pnpm format:fix`: Fix formatting issues.
- `pnpm test`: Run tests.
- `pnpm db:generate --name description_of_schema_change`: db migration after making schema changes

Starting services:
- `pnpm web`: Start the web application (this doesn't return, unless you kill it).
- `pnpm workers`: Starts the background workers (this doesn't return, unless you kill it).


==================================================
File: CONTRIBUTING.md
==================================================
# Contributing to Karakeep

First off, thank you for considering contributing to our project! This document outlines our contribution process and guidelines to make it easy for you to help improve this project.

## How Can I Contribute?


### Asking Questions

If you have questions:

* Use the GitHub Discussions Q&A section
* Search existing discussions to see if your question has been answered
* If not found, create a new discussion with a clear, descriptive title


### Reporting Bugs

If in doubt, about whether a problem you're seeing is a bug or not, use the discussions Q&A section instead. If it turns out to be a bug, we'll promote it into an issue. If you're sure it's a bug:
* Create a new issue using the bug report template
* Include a clear description and steps to reproduce
* Wait for triage and labeling by maintainers


### Suggesting Features

For feature requests:

* If you find a similar feature request, upvote it instead of creating a new one to help us prioritize it
* Create a new issue using the feature request template
* New features start with the `status/untriaged` label
  * If the feature request is approved, the maintainers will add the `status/approved` label and assign a priority to the issue
  * Other issues will get labeled with `status/icebox`. Issues in the icebox are not prioritized, until there's enough interest from the community


### Working on Issues

Before starting to work on an issue:

* Prefer working on `status/approved` issues to make sure they get prioritized for the review
* Comment on the issue to let others know you're working on it
* Read the [development documentation](https://docs.karakeep.app/Development/setup) to get started
* If you need help, you can find us in the #development channel in the [Karakeep Discord](https://discord.com/invite/NrgeYywsFh).
* Once you're done, open a PR and wait for review. Try to include a screenshot of the change in the PR description.

Please note that we're all volunteers. We'll aim to review your PR within a week from when they are opened.


==================================================
File: GEMINI.md
==================================================
# Karakeep Project Overview

This document provides context about the Karakeep project for the different agents.

## Project Overview

Karakeep is a monorepo project managed with Turborepo. It appears to be a web application with a focus on collecting and organizing information, possibly a bookmarking or "read-it-later" service. The project is built with a modern tech stack, including:

- **Frontend:** Next.js, React, TypeScript, Tailwind CSS
- **Backend:** Hono (a lightweight web framework), tRPC
- **Database:** Drizzle ORM (likely with a relational database like PostgreSQL or SQLite)
- **Tooling:** Prettier,oxlint, Vitest, pnpm

## Project Structure

The project is organized into `apps` and `packages`:

### Applications (`apps/`)

- **`web`:** The main web application, built with Next.js.
- **`browser-extension`:** A browser extension, likely for saving content to karakeep.
- **`cli`:** A command-line interface for interacting with the service.
- **`landing`:** A landing page for the project.
- **`mobile`:** A mobile application (details unknown).
- **`mcp`:** The Model Context Protocol (MCP) server to communicate with Karakeep.
- **`workers`:** Background workers for processing tasks.

### Packages (`packages/`)

- **`api`:** The main API, built with Hono and tRPC.
- **`db`:** Database schema and migrations, using Drizzle ORM.
- **`e2e_tests`:** End-to-end tests for the project.
- **`open-api`:** OpenAPI specifications for the API.
- **`sdk`:** A software development kit for interacting with the API.
- **`shared`:** Shared code and types between packages.
- **`shared-react`:** Shared React components and hooks.
- **`shared-server`:** Shared logic that's meant to be used on the server-side.
- **`trpc`:** tRPC router and procedures. Most of the business logic is here.

### Docs

- **docs/docs/03-configuration.md**: Explains configuration options for the project.

## Development Workflow

- **Package Manager:** pnpm
- **Build System:** Turborepo
- **Code Formatting:** Prettier
- **Linting:** oxlint
- **Testing:** Vitest

## Other info

- This project uses shadcn/ui. The shadcn components in the web app are in `packages/web/components/ui`.
- This project uses Tailwind CSS.
- For the mobile app, we use [expo](https://expo.dev/).

### Common Commands

- `pnpm typecheck`: Typecheck the codebase.
- `pnpm lint`: Lint the codebase.
- `pnpm lint:fix`: Fix linting issues.
- `pnpm format`: Format the codebase.
- `pnpm format:fix`: Fix formatting issues.
- `pnpm test`: Run tests.
- `pnpm db:generate --name description_of_schema_change`: db migration after making schema changes

Starting services:
- `pnpm web`: Start the web application (this doesn't return, unless you kill it).
- `pnpm workers`: Starts the background workers (this doesn't return, unless you kill it).


==================================================
File: README.md
==================================================
<div align="center">
    <a href="https://github.com/karakeep-app/karakeep/actions/workflows/ci.yml">
        <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/karakeep-app/karakeep/ci.yml" />
    </a>
    <a href="https://github.com/karakeep-app/karakeep/releases">
        <img alt="GitHub Release" src="https://img.shields.io/github/v/release/karakeep-app/karakeep" />
    </a>
    <a href="https://discord.gg/NrgeYywsFh">
        <img alt="Discord" src="https://img.shields.io/discord/1223681308962721802?label=chat%20on%20discord" />
    </a>
    <a href="https://hosted.weblate.org/engage/hoarder/">
        <img src="https://hosted.weblate.org/widget/hoarder/hoarder/svg-badge.svg" alt="Translation status" />
    </a>
</div>

# <img height="50px" src="./screenshots/logo.png" />

Karakeep (previously Hoarder) is a self-hostable bookmark-everything app with a touch of AI for the data hoarders out there.

![homepage screenshot](https://github.com/karakeep-app/karakeep/blob/main/screenshots/homepage.png?raw=true)

## Features

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 👥 Collaborate with others on the same list.
- 🔎 Full text search of all the content stored.
- ✨ AI-based (aka chatgpt) automatic tagging and summarization. With supports for local models using ollama!
- 🤖 Rule-based engine for customized management.
- 🎆 OCR for extracting text from images.
- 🔖 [Chrome plugin](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje) and [Firefox addon](https://addons.mozilla.org/en-US/firefox/addon/karakeep/) for quick bookmarking.
- 📱 An [iOS app](https://apps.apple.com/us/app/karakeep-app/id6479258022), and an [Android app](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).
- 📰 Auto hoarding from RSS feeds.
- 🔌 REST API and multiple clients.
- 🌐 Multi-language support.
- 🖍️ Mark and store highlights from your hoarded content.
- 🗄️ Full page archival (using [monolith](https://github.com/Y2Z/monolith)) to protect against link rot.
- ▶️ Auto video archiving using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- ☑️ Bulk actions support.
- 🔐 SSO support.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
- 🔄 Automatic sync with browser bookmarks via [floccus](https://floccus.org/).
- [Planned] Offline reading on mobile, semantic search across bookmarks, ...

**⚠️ This app is under heavy development.**

## Documentation

- [Installation](https://docs.karakeep.app/Installation/docker)
- [Configuration](https://docs.karakeep.app/configuration)
- [Screenshots](https://docs.karakeep.app/screenshots)
- [Security Considerations](https://docs.karakeep.app/security-considerations)
- [Development](https://docs.karakeep.app/Development/setup)

## Demo

You can access the demo at [https://try.karakeep.app](https://try.karakeep.app). Login with the following creds:

```
email: demo@karakeep.app
password: demodemo
```

The demo is seeded with some content, but it's in read-only mode to prevent abuse.

## About the name

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).

## Stack

- [NextJS](https://nextjs.org/) for the web app. Using app router.
- [Drizzle](https://orm.drizzle.team/) for the database and its migrations.
- [NextAuth](https://next-auth.js.org) for authentication.
- [tRPC](https://trpc.io) for client->server communication.
- [Puppeteer](https://pptr.dev/) for crawling the bookmarks.
- [OpenAI](https://openai.com/) because AI is so hot right now.
- [Meilisearch](https://meilisearch.com) for the full content search.

## Why did I build it?

I browse reddit, twitter and hackernews a lot from my phone. I frequently find interesting stuff (articles, tools, etc) that I'd like to bookmark and read later when I'm in front of a laptop. Typical read-it-later apps usecase. Initially, I was using [Pocket](https://getpocket.com) for that. Then I got into self-hosting and I wanted to self-host this usecase. I used [memos](https://github.com/usememos/memos) for those quick notes and I loved it but it was lacking some features that I found important for that usecase such as link previews and automatic tagging (more on that in the next section).

I'm a systems engineer in my day job (and have been for the past 7 years). I didn't want to get too detached from the web development world. I decided to build this app as a way to keep my hand dirty with web development, and at the same time, build something that I care about and use every day.

## Alternatives

- [memos](https://github.com/usememos/memos): I love memos. I have it running on my home server and it's one of my most used self-hosted apps. It doesn't, however, archive or preview the links shared in it. It's just that I dump a lot of links there and I'd have loved if I'd be able to figure which link is that by just looking at my timeline. Also, given the variety of things I dump there, I'd have loved if it does some sort of automatic tagging for what I save there. This is exactly the usecase that I'm trying to tackle with Karakeep.
- [mymind](https://mymind.com/): Mymind is the closest alternative to this project and from where I drew a lot of inspirations. It's a commercial product though.
- [raindrop](https://raindrop.io): A polished open source bookmark manager that supports links, images and files. It's not self-hostable though.
- Bookmark managers (mostly focused on bookmarking links):
    - [Pocket](https://getpocket.com) (Dead): Pocket is what hooked me into the whole idea of read-it-later apps. I used it [a lot](https://blog.mbassem.com/2019/01/27/favorite-articles-2018/). However, I recently got into home-labbing and became obsessed with the idea of running my services in my home server. Karakeep is meant to be a self-hosting first app. Mozilla recently announced that it's shutting down pocket.
    - [Linkwarden](https://linkwarden.app/): An open-source self-hostable bookmark manager that I ran for a bit in my homelab. It's focused mostly on links and supports collaborative collections.
    - [Wallabag](https://wallabag.it): Wallabag is a well-established open source read-it-later app written in php.
    - [Shiori](https://github.com/go-shiori/shiori): Shiori is meant to be an open source pocket clone written in Go.

## Translations

Karakeep uses Weblate for managing translations. If you want to help translate Karakeep, you can do so [here](https://hosted.weblate.org/engage/hoarder/).

## Karakeep Cloud ☁️

If you're not comfortable with self-hosting, you can use our managed Karakeep cloud at [cloud.karakeep.app](https://cloud.karakeep.app). Cloud subscriptions support the development of Karakeep.

## Support

If you're enjoying using Karakeep, drop a ⭐️ on the repo!

<a href="https://www.buymeacoffee.com/mbassem" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## Community Channels

- Join us on [Discord](https://discord.gg/NrgeYywsFh).
- Follow us on Twitter: [@karakeep_app](https://x.com/karakeep_app).

## License

Karakeep is licensed under [AGPL-3.0](https://github.com/karakeep-app/karakeep/blob/main/LICENSE) and owned by [Localhost Labs Ltd](https://localhostlabs.co.uk).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=karakeep-app/karakeep&type=Date)](https://star-history.com/#karakeep-app/karakeep&Date)


==================================================
File: SECURITY.md
==================================================
# Security Policy

## Reporting a Vulnerability

Please report security issues to `security@karakeep.app`


==================================================
File: apps/landing/README.md
==================================================
This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.


==================================================
File: apps/mcp/README.md
==================================================
# Karakeep MCP Server

This is the Karakeep MCP server, which is a server that can be used to interact
with Karakeep from other tools.

## Supported Tools

- Searching bookmarks
- Adding and removing bookmarks from lists
- Attaching and detaching tags to bookmarks
- Creating new lists
- Creating text and URL bookmarks

Currently, the MCP server only exposes tools (no resources).

## Usage with Claude Desktop

From NPM:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "npx",
      "args": [
        "@karakeep/mcp"
      ],
      "env": {
        "KARAKEEP_API_ADDR": "https://<YOUR_SERVER_ADDR>",
        "KARAKEEP_API_KEY": "<YOUR_TOKEN>",
        "KARAKEEP_CUSTOM_HEADERS": "{\"CF-Access-Client-Id\": \"...\", \"CF-Access-Client-Secret\": \"...\"}"
      }
    }
  }
}
```

From Docker:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "docker",
      "args": [
        "run",
        "-e",
        "KARAKEEP_API_ADDR=https://<YOUR_SERVER_ADDR>",
        "-e",
        "KARAKEEP_API_KEY=<YOUR_TOKEN>",
        "-e",
        "KARAKEEP_CUSTOM_HEADERS={\"CF-Access-Client-Id\": \"...\", \"CF-Access-Client-Secret\": \"...\"}",
        "ghcr.io/karakeep-app/karakeep-mcp:latest"
      ]
    }
  }
}
```


==================================================
File: apps/web/README.md
==================================================
This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.


==================================================
File: apps/web/components/dashboard/preview/content-renderers/README.md
==================================================
# Content-Aware Renderers

This directory contains the content-aware rendering system for LinkContentPreview. It allows for special rendering of different types of links based on their URL patterns.

## Architecture

The system consists of:

1. **Types** (`types.ts`): Defines the `ContentRenderer` interface
2. **Registry** (`registry.ts`): Manages registration and retrieval of renderers
3. **Individual Renderers**: Each renderer handles a specific type of content

## Creating a New Renderer

To add support for a new website or content type:

1. Create a new file (e.g., `MyWebsiteRenderer.tsx`)
2. Implement the `ContentRenderer` interface:

```typescript
import { ContentRenderer } from "./types";
import { BookmarkTypes, ZBookmark } from "@karakeep/shared/types/bookmarks";
import { MyIcon } from "lucide-react";

function canRenderMyWebsite(bookmark: ZBookmark): boolean {
  if (bookmark.content.type !== BookmarkTypes.LINK) {
    return false;
  }

  // Add your URL pattern matching logic here
  return bookmark.content.url.includes("mywebsite.com");
}

function MyWebsiteRendererComponent({ bookmark }: { bookmark: ZBookmark }) {
  // Your custom rendering logic here
  return <div>Custom content for MyWebsite</div>;
}

export const myWebsiteRenderer: ContentRenderer = {
  id: "mywebsite",
  name: "My Website",
  icon: MyIcon,
  canRender: canRenderMyWebsite,
  component: MyWebsiteRendererComponent,
  priority: 10, // Higher priority = appears first in dropdown
};
```

3. Register your renderer in `index.ts`:

```typescript
import { myWebsiteRenderer } from "./MyWebsiteRenderer";

contentRendererRegistry.register(myWebsiteRenderer);
```


==================================================
File: charts/README.md
==================================================
The helm charts got moved to a separate repo: https://github.com/karakeep-app/helm-charts


==================================================
File: docs/README.md
==================================================
# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ yarn
```

### Local Development

```
$ yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
$ yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.


==================================================
File: docs/docs/01-getting-started/01-intro.md
==================================================
---
slug: /
---

# Introduction

Karakeep (previously Hoarder) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

![Screenshot](https://raw.githubusercontent.com/karakeep-app/karakeep/main/screenshots/homepage.png)


## Features

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 👥 Collaborate with others on the same list.
- 🔎 Full text search of all the content stored.
- ✨ AI-based (aka chatgpt) automatic tagging and summarization. With supports for local models using ollama!
- 🤖 Rule-based engine for customized management.
- 🎆 OCR for extracting text from images.
- 🔖 [Chrome plugin](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje) and [Firefox addon](https://addons.mozilla.org/en-US/firefox/addon/karakeep/) for quick bookmarking.
- 📱 An [iOS app](https://apps.apple.com/us/app/karakeep-app/id6479258022), and an [Android app](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).
- 📰 Auto hoarding from RSS feeds.
- 🔌 REST API and multiple clients.
- 🌐 Multi-language support.
- 🖍️ Mark and store highlights from your hoarded content.
- 🗄️ Full page archival (using [monolith](https://github.com/Y2Z/monolith)) to protect against link rot.
- ▶️ Auto video archiving using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- ☑️ Bulk actions support.
- 🔐 SSO support.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
- 🔄 Automatic sync with browser bookmarks via [floccus](https://floccus.org/).
- [Planned] Offline reading on mobile, semantic search across bookmarks, ...

**⚠️ This app is under heavy development.**


## Demo

You can access the demo at [https://try.karakeep.app](https://try.karakeep.app). Login with the following creds:

```
email: demo@karakeep.app
password: demodemo
```

The demo is seeded with some content, but it's in read-only mode to prevent abuse.

## About the name

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).


==================================================
File: docs/docs/01-getting-started/02-screenshots.md
==================================================
# Screenshots

## Homepage

![Homepage](/img/screenshots/homepage.png)

## Homepage (Dark Mode)

![Homepage](/img/screenshots/homepage-dark.png)

## Tags

![All Tags](/img/screenshots/all-tags.png)

## Lists

![All Lists](/img/screenshots/all-lists.png)

## Bookmark Preview

![Bookmark Preview](/img/screenshots/bookmark-preview.png)

## Settings

![Settings](/img/screenshots/settings.png)


## Sharing

<img src="/img/screenshots/share-sheet.png" width="400px"  />


==================================================
File: docs/docs/02-installation/01-docker.md
==================================================
# Docker

### Requirements

- Docker
- Docker Compose

### 1. Create a new directory

Create a new directory to host the compose file and env variables.

This is where you’ll place the `docker-compose.yml` file from the next step and the environment variables.

For example you could make a new directory called "karakeep-app" with the following command:
```
mkdir karakeep-app
```


### 2. Download the compose file

Download the docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml) directly into your new directory.

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/docker/docker-compose.yml
```

### 3. Populate the environment variables

To configure the app, create a `.env` file in the directory and add this minimal env file:

```
KARAKEEP_VERSION=release
NEXTAUTH_SECRET=super_random_string
MEILI_MASTER_KEY=another_random_string
NEXTAUTH_URL=http://localhost:3000
```

You **should** change the random strings. You can use `openssl rand -base64 36` in a seperate terminal window to generate the random strings. You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

Persistent storage and the wiring between the different services is already taken care of in the docker compose file.

Keep in mind that every time you change the `.env` file, you'll need to re-run `docker compose up`.

If you want more config params, check the config documentation [here](../03-configuration/01-environment-variables.md).

### 4. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the env file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](../06-administration/03-openai.md).

If you want to use a different AI provider (e.g. Ollama for local inference), check out the [different AI providers](../03-configuration/02-different-ai-providers.md) guide.

### 5. Start the service

Start the service by running:

```
docker compose up -d
```

Then visit `http://localhost:3000` and you should be greeted with the Sign In page.

### [Optional] 6. Enable optional features

Check the [configuration docs](../03-configuration/01-environment-variables.md) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.

### [Optional] 7. Setup quick sharing extensions

Go to the [quick sharing page](../04-using-karakeep/quick-sharing.md) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Updating Karakeep will depend on what you used for the `KARAKEEP_VERSION` env variable.

- If you pinned the app to a specific version, bump the version and re-run `docker compose up -d`. This should pull the new version for you.
- If you used `KARAKEEP_VERSION=release`, you'll need to force docker to pull the latest version by running `docker compose up --pull always -d`.

Note that if you want to upgrade/migrate `Meilisearch` versions, refer to the [troubleshooting](../06-administration/05-troubleshooting.md) page.


==================================================
File: docs/docs/02-installation/02-unraid.md
==================================================
# Unraid

## Docker Compose Manager Plugin (Recommended)

You can use [Docker Compose Manager](https://forums.unraid.net/topic/114415-plugin-docker-compose-manager/) plugin to deploy Karakeep using the official docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml). After creating the stack, you'll need to setup some env variables similar to that from the docker compose installation docs [here](/installation/docker#3-populate-the-environment-variables).

## Community Apps

:::info
The community application template is maintained by the community.
:::

Karakeep can be installed on Unraid using the community application plugins. Karakeep is a multi-container service, and because unraid doesn't natively support that, you'll have to install the different pieces as separate applications and wire them manually together.

Here's a high level overview of the services you'll need:

- **Karakeep** ([Support post](https://forums.unraid.net/topic/165108-support-collectathon-karakeep/)): Karakeep's main web app.
- **Browserless** ([Support post](https://forums.unraid.net/topic/130163-support-template-masterwishxbrowserless/)): The chrome headless service used for fetching the content. Karakeep's official docker compose doesn't use browserless, but it's currently the only headless chrome service available on unraid, so you'll have to use it.
- **MeiliSearch** ([Support post](https://forums.unraid.net/topic/164847-support-collectathon-meilisearch/)): The search engine used by Karakeep. It's optional but highly recommended. If you don't have it set up, search will be disabled.


==================================================
File: docs/docs/02-installation/03-archlinux.md
==================================================
# Arch Linux

## Installation

> [Karakeep on AUR](https://aur.archlinux.org/packages/karakeep) is not maintained by the karakeep official.

1. Install karakeep

    ```shell
    paru -S karakeep
    ```

2. (**Optional**) Install optional dependencies

    ```shell
    # karakeep-cli: karakeep cli tool
    paru -S karakeep-cli

    # ollama: for automatic tagging
    sudo pacman -S ollama

    # yt-dlp: for download video
    sudo pacman -S yt-dlp
    ```

    You can use Open-AI instead of `ollama`. If you use `ollama`, you need to download the ollama model. Please refer to: [https://ollama.com/library](https://ollama.com/library).

3. Set up

    Environment variables can be set in `/etc/karakeep/karakeep.env` according to [configuration page](../03-configuration/01-environment-variables.md). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

4. Enable service

    ```shell
    sudo systemctl enable --now karakeep.target
    ```

    Then visit `http://localhost:3000` and you should be greated with the sign in page.

## Services and Ports

`karakeep.target` include 3 services: `karakeep-web.service`, `karakeep-works.service`, `karakeep-browser.service`.

- `karakeep-web.service`: Provide karakeep webui service, uses `3000` port by default.

- `karakeep-workers.service`: Provide karakeep workers service, no port.

- `karakeep-browser.service`: Provide browser headless service, uses `9222` port by default.

Now `karakeep` depends on `meilisearch`, and `karakeep-workers.service` wants `meilisearch.service`, starting `karakeep.target` will start `meilisearch.service` at the same time.

## How to Migrate from Hoarder to Karakeep

The PKGBUILD has been fully updated to replace all references to `hoarder` with `karakeep`. If you want to preserve your existing `hoarder` data during the upgrade, please follow the steps below:

**1. Stop the old services**

```shell
sudo systemctl stop hoarder-web.service hoarder-worker.service hoarder-browser.service
sudo systemctl disable --now hoarder.target
```

**2. Uninstall Hoarder**  
After uninstalling, you can manually remove the old `hoarder` user and group if needed.
```shell
paru -R hoarder
```

**3. Rename the old data directory**
```shell
sudo mv /var/lib/hoarder /var/lib/karakeep
```

**4. Install Karakeep**
```shell
paru -S karakeep
```

**5. Fix ownership of the data directory**
```shell
sudo chown -R karakeep:karakeep /var/lib/karakeep
```

**6. Set Karakeep**  
Edit `/etc/karakeep/karakeep.env` according to [configuration page](../03-configuration/01-environment-variables.md). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

Or you can copy old hoarder env file to karakeep:
```shell
sudo cp -f /etc/hoarder/hoarder.env /etc/karakeep/karakeep.env
```

**7. Start Karakeep**
```shell
sudo systemctl enable --now karakeep.target
```


==================================================
File: docs/docs/02-installation/04-kubernetes.md
==================================================
# Kubernetes

### Requirements

- A kubernetes cluster
- kubectl
- kustomize

### 1. Get the deployment manifests

You can clone the repository and copy the `/kubernetes` directory into another directory of your choice.

### 2. Populate the environment variables and secrets

To configure the app, copy the `.env_sample` to `.env` and change to your specific needs.

You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

To see all available configuration options check the [documentation](../03-configuration/01-environment-variables.md).

To configure the neccessary secrets for the application copy the `.secrets_sample` file to `.secrets` and change the sample secrets to your generated secrets.

> Note: You **should** change the random strings. You can use `openssl rand -base64 36` to generate the random strings.

### 3. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](../06-administration/03-openai.md).

If you want to use a different AI provider (e.g. Ollama for local inference), check out the [different AI providers](../03-configuration/02-different-ai-providers.md) guide.

### 4. Deploy the service

Deploy the service by running:

```
make deploy
```

### 5. Access the service

#### via LoadBalancer IP

By default, these manifests expose the application as a LoadBalancer Service. You can run `kubectl get services` to identify the IP of the loadbalancer for your service.

Then visit `http://<loadbalancer-ip>:3000` and you should be greated with the Sign In page.

> Note: Depending on your setup you might want to expose the service via an Ingress, or have a different means to access it.

#### Via Ingress

If you want to use an ingress, you can customize the sample ingress in the kubernetes folder and change the host to the DNS name of your choice.

After that you have to configure the web service to the type ClusterIP so it is only reachable via the ingress.

If you have already deployed the service you can patch the web service to the type ClusterIP with the following command:

` kubectl -n karakeep patch service web -p '{"spec":{"type":"ClusterIP"}}' `

Afterwards you can apply the ingress and access the service via your chosen URL.

#### Setting up HTTPS access to the Service

To access karakeep securely you can configure the ingress to use a preconfigured TLS certificate. This requires that you already have the needed files, namely your .crt and .key file, on hand.

After you have deployed the karakeep manifests you can deploy your certificate for karakeep in the `karakeep` namespace with this example command. You can name the secret however you want. But be aware that the secret name in the ingress definition has to match the secret name.

` $ kubectl --namespace karakeep create secret tls karakeep-web-tls --cert=/path/to/crt --key=/path/to/key `

If the secret is successfully created you can now configure the Ingress to use TLS via this changes to the spec:

```` yaml
 spec:
  tls:
  - hosts:
      - karakeep.example.com
    secretName: karakeep-web-tls
````

> Note: Be aware that the hosts have to match between the tls spec and the HTTP spec.

### [Optional] 6. Setup quick sharing extensions

Go to the [quick sharing page](../04-using-karakeep/quick-sharing.md) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Edit the `KARAKEEP_VERSION` variable in the `kustomization.yaml` file and run `make clean deploy`.

If you have chosen `release` as the image tag you can also destroy the web pod, since the deployment has an ImagePullPolicy set to always the pod always pulls the image from the registry, this way we can ensure that the newest release image is pulled.


==================================================
File: docs/docs/02-installation/06-debuntu.md
==================================================
# Debian 12/Ubuntu 24.04

:::warning
This script is a stripped-down version of those found in the [Proxmox Community Scripts](https://github.com/community-scripts/ProxmoxVE) repo. It has been adapted to work on baremetal Debian 12 or Ubuntu 24.04 installs **only**. Any other use is not supported and you use this script at your own risk.
:::

### Requirements

- **Debian 12** (Buster) or
- **Ubuntu 24.04** (Noble Numbat)

The script will download and install all dependencies (except for Ollama), install Karakeep, do a basic configuration of Karakeep and Meilisearch (the search app used by Karakeep), and create and enable the systemd service files needed to run Karakeep on startup. Karakeep and Meilisearch are run in the context of their low-privilege user environments for more security.

The script functions as an update script in addition to an installer. See **[Updating](#updating)**.

### 1. Download the script from the [Karakeep repository](https://github.com/karakeep-app/karakeep/blob/main/karakeep-linux.sh)

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/karakeep-linux.sh
```

### 2. Run the script

> This script must be run as `root`, or as a user with `sudo` privileges.

    If this is a fresh install, then run the installer by using the following command:

    ```shell
    bash karakeep-linux.sh install
    ```

### 3. Create an account/sign in

    Then visit `http://localhost:3000` and you should be greated with the Sign In page.

## Updating

> This script must be run as `root`, or as a user with `sudo` privileges.

    If Karakeep has previously been installed using this script, then run the updater like so:

    ```shell
     bash karakeep-linux.sh update
    ```

## Services and Ports

`karakeep.target` includes 4 services: `meilisearch.service`, `karakeep-web.service`, `karakeep-workers.service`, `karakeep-browser.service`.

- `meilisearch.service`: Provides full-text search, Karakeep Workers service connects to it, uses port `7700` by default.

- `karakeep-web.service`: Provides the karakeep web service, uses `3000` port by default.

- `karakeep-workers.service`: Provides the karakeep workers service, no port.

- `karakeep-browser.service`: Provides the headless browser service, uses `9222` port by default.

## Configuration, ENV file, database locations

During installation, the script created a configuration file for `meilisearch`, an `ENV` file for Karakeep, and located config paths and database paths separate from the installation path of Karakeep, so as to allow for easier updating. Their names/locations are as follows:

- `/etc/meilisearch.toml` - a basic configuration for meilisearch, that contains configs for the database location, disabling analytics, and using a master key, which prevents unauthorized connections.
- `/var/lib/meilisearch` - Meilisearch DB location.
- `/etc/karakeep/karakeep.env` - The Karakeep `ENV` file. Edit this file to configure Karakeep beyond the default. The web service and the workers service need to be restarted after editing this file:

    ```shell
    sudo systemctl restart karakeep-workers karakeep-web
    ```

- `/var/lib/karakeep` - The Karakeep database location. If you delete the contents of this folder you will lose all your data.

## Still Running Hoarder?

There is a way to upgrade. Please see [Hoarder to Karakeep Migration](../06-administration/08-hoarder-to-karakeep-migration.md)


==================================================
File: docs/docs/02-installation/07-minimal-install.md
==================================================
# Minimal Installation

:::warning
Unless necessary, prefer the [full installation](/installation/docker) to leverage all the features of Karakeep. You'll be sacrificing a lot of functionality if you go with the minimal installation route.
:::

Karakeep's default installation has a dependency on Meilisearch for the full text search, Chrome for crawling and OpenAI/Ollama for AI tagging. You can however run Karakeep without those dependencies if you're willing to sacrifice those features.

- If you run without meilisearch, the search functionality will be completely disabled.
- If you run without chrome, crawling will still work, but you'll lose ability to take screenshots of websites and websites with javascript content won't get crawled correctly.
- If you don't setup OpenAI/Ollama, AI tagging will be disabled.

Those features are important for leveraging Karakeep's full potential, but if you're running in constrained environments, you can use the following minimal docker compose to skip all those dependencies:

```yaml
services:
  web:
    image: ghcr.io/karakeep-app/karakeep:release
    restart: unless-stopped
    volumes:
      - data:/data
    ports:
      - 3000:3000
    environment:
      DATA_DIR: /data
      NEXTAUTH_SECRET: super_random_string
volumes:
  data:
```

Or just with the following docker command:

```base
docker run -d \
  --restart unless-stopped \
  -v data:/data \
  -p 3000:3000 \
  -e DATA_DIR=/data \
  -e NEXTAUTH_SECRET=super_random_string \
  ghcr.io/karakeep-app/karakeep:release
```

:::warning
You **MUST** change the `super_random_string` to a true random string which you can generate with `openssl rand -hex 32`.
:::

Check the [configuration docs](../03-configuration/01-environment-variables.md) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.


==================================================
File: docs/docs/02-installation/08-truenas.md
==================================================
# TrueNAS

Karakeep is available directly from TrueNAS's app catalog ([link](https://apps.truenas.com/catalog/karakeep/)).


==================================================
File: docs/docs/02-installation/09-cloud-hosting.md
==================================================
# Karakeep Cloud

:::tip
If you want to use Karakeep without running your own servers, the hosted cloud option is the fastest way to start.
:::

[Karakeep Cloud](https://cloud.karakeep.app) is the fully managed version of Karakeep operated by the core team. It handles hosting, updates, monitoring, and backups for you, so you can focus on saving content instead of maintaining infrastructure.

### Get started

1. Visit [cloud.karakeep.app](https://cloud.karakeep.app) and create an account.
2. Follow the onboarding flow to create your workspace.
3. Install the browser extension or mobile apps from the [quick sharing page](../04-using-karakeep/quick-sharing.md) and start saving links immediately.


==================================================
File: docs/docs/02-installation/10-pikapods.md
==================================================
# PikaPods

:::info
Note: PikaPods shares some of its revenue from hosting Karakeep with the maintainer of this project.
:::

[PikaPods](https://www.pikapods.com/) offers managed paid hosting for many open source apps, including Karakeep.
Server administration, updates, migrations and backups are all taken care of, which makes it well suited
for less technical users. As of Nov 2024, running Karakeep there will cost you ~$3 per month.

### Requirements

- A _PikaPods_ account. Can be created for free [here](https://www.pikapods.com/register). You get an initial welcome credit of $5.

### 1. Choose app

Choose _Karakeep_ from their [list of apps](https://www.pikapods.com/apps) or use this [direct link](https://www.pikapods.com/pods?run=hoarder). This will either
open a new dialog to add a new _Karakeep_ pod or ask you to log in.

### 2. Add settings

There are a few settings to configure in the dialog:

- **Basics**: Give the pod a name and choose a region that's near you.
- **Env Vars**: Here you can disable signups or set an OpenAI API key. All settings are optional.
- **Resources**: The resources your _Karakeep_ pod can use. The defaults are fine, unless you have a very large collection.

### 3. Start pod and add user

After hitting _Add pod_ it will take about a minute for the app to fully start. After this you can visit
the pod's URL and add an initial user under _Sign Up_. After this you may want to disable further sign-ups
by setting the pod's `DISABLE_SIGNUPS` _Env Var_ to `true`.


==================================================
File: docs/docs/03-configuration/01-environment-variables.md
==================================================
# Configuration

The app is mainly configured by environment variables. All the used environment variables are listed in [packages/shared/config.ts](https://github.com/karakeep-app/karakeep/blob/main/packages/shared/config.ts). The most important ones are:

| Name                                   | Required                              | Default         | Description                                                                                                                                                                                                                                                            |
| -------------------------------------- | ------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PORT                                   | No                                    | 3000            | The port on which the web server will listen. DON'T CHANGE THIS IF YOU'RE USING DOCKER, instead changed the docker bound external port.                                                                                                                                |
| WORKERS_PORT                           | No                                    | 0 (Random Port) | The port on which the worker will export its prometheus metrics on `/metrics`. By default it's a random unused port. If you want to utilize those metrics, fix the port to a value (and export it in docker if you're using docker).                                   |
| WORKERS_HOST                           | No                                    | 127.0.0.1       | Host to listen to for requests to WORKERS_PORT. You will need to set this if running in a container, since localhost will not be reachable from outside                                                                                                                |
| WORKERS_ENABLED_WORKERS                | No                                    | Not set         | Comma separated list of worker names to enable. If set, only these workers will run. Valid values: crawler,inference,search,adminMaintenance,video,feed,assetPreprocessing,webhook,ruleEngine.                                                                         |
| WORKERS_DISABLED_WORKERS               | No                                    | Not set         | Comma separated list of worker names to disable. Takes precedence over `WORKERS_ENABLED_WORKERS`.                                                                                                                                                                      |
| LOG_LEVEL                              | No                                    | debug           | The application log level as defined in the [winston documentation](https://github.com/winstonjs/winston?tab=readme-ov-file#logging-levels). You may want to set this to `notice` or `warning` when running Karakeep in a production environment.                      |
| DATA_DIR                               | Yes                                   | Not set         | The path for the persistent data directory. This is where the db lives. Assets are stored here by default unless `ASSETS_DIR` is set.                                                                                                                                  |
| ASSETS_DIR                             | No                                    | Not set         | The path where crawled assets will be stored. If not set, defaults to `${DATA_DIR}/assets`.                                                                                                                                                                            |
| NEXTAUTH_URL                           | Yes                                   | Not set         | Should point to the address of your server. The app will function without it, but will redirect you to wrong addresses on signout for example.                                                                                                                         |
| NEXTAUTH_SECRET                        | Yes                                   | Not set         | Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`.                                                                                                                                                                                |
| MEILI_ADDR                             | No                                    | Not set         | The address of meilisearch. If not set, Search will be disabled. E.g. (`http://meilisearch:7700`)                                                                                                                                                                      |
| MEILI_MASTER_KEY                       | Only in Prod and if search is enabled | Not set         | The master key configured for meilisearch. Not needed in development environment. Generate one with `openssl rand -base64 36 \| tr -dc 'A-Za-z0-9'`                                                                                                                    |
| MAX_ASSET_SIZE_MB                      | No                                    | 50              | Sets the maximum allowed asset size (in MB) to be uploaded                                                                                                                                                                                                             |
| DISABLE_NEW_RELEASE_CHECK              | No                                    | false           | If set to true, latest release check will be disabled in the admin panel.                                                                                                                                                                                              |
| RATE_LIMITING_ENABLED                  | No                                    | false           | If set to true, API rate limiting will be enabled.                                                                                                                                                                                                                     |
| CRAWLER_DOMAIN_RATE_LIMIT_WINDOW_MS    | No                                    | Not set         | Time window in milliseconds for per-domain crawler rate limiting.                                                                                                                                                                                                      |
| CRAWLER_DOMAIN_RATE_LIMIT_MAX_REQUESTS | No                                    | Not set         | Maximum crawler requests allowed per domain inside the configured window.                                                                                                                                                                                              |
| DB_WAL_MODE                            | No                                    | false           | Enables WAL mode for the sqlite database. This should improve the performance of the database. There's no reason why you shouldn't set this to true unless you're running the db on a network attached drive. This will become the default at some time in the future. |
| SEARCH_NUM_WORKERS                     | No                                    | 1               | Number of concurrent workers for search indexing tasks. Increase this if you have a high volume of content being indexed for search.                                                                                                                                   |
| SEARCH_JOB_TIMEOUT_SEC                 | No                                    | 30              | How long to wait for a search indexing job to finish before timing out. Increase this if you have large bookmarks with extensive content that takes longer to index.                                                                                                   |
| WEBHOOK_NUM_WORKERS                    | No                                    | 1               | Number of concurrent workers for webhook delivery. Increase this if you have multiple webhook endpoints or high webhook traffic.                                                                                                                                       |
| ASSET_PREPROCESSING_NUM_WORKERS        | No                                    | 1               | Number of concurrent workers for asset preprocessing tasks (image processing, OCR, etc.). Increase this if you have many images or documents that need processing.                                                                                                     |
| ASSET_PREPROCESSING_JOB_TIMEOUT_SEC    | No                                    | 60              | How long to wait for an asset preprocessing job to finish before timing out. Increase this if you have large images or PDFs that take longer to process.                                                                                                               |
| RULE_ENGINE_NUM_WORKERS                | No                                    | 1               | Number of concurrent workers for rule engine processing. Increase this if you have complex automation rules that need to be processed quickly.                                                                                                                         |
| MAX_RSS_FEEDS_PER_USER                 | No                                    | 1000            | The maximum number of RSS feeds a user can create.                                                                                                                                                                                                                     |
| MAX_WEBHOOKS_PER_USER                  | No                                    | 100             | The maximum number of webhooks a user can create.                                                                                                                                                                                                                      |

## Asset Storage

Karakeep supports two storage backends for assets: local filesystem (default) and S3-compatible object storage. S3 storage is automatically detected when an S3 endpoint is passed.

| Name                             | Required          | Default | Description                                                                                               |
| -------------------------------- | ----------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| ASSET_STORE_S3_ENDPOINT          | No                | Not set | The S3 endpoint URL. Required for S3-compatible services like MinIO. **Setting this enables S3 storage**. |
| ASSET_STORE_S3_REGION            | No                | Not set | The S3 region to use.                                                                                     |
| ASSET_STORE_S3_BUCKET            | Yes when using S3 | Not set | The S3 bucket name where assets will be stored.                                                           |
| ASSET_STORE_S3_ACCESS_KEY_ID     | Yes when using S3 | Not set | The S3 access key ID for authentication.                                                                  |
| ASSET_STORE_S3_SECRET_ACCESS_KEY | Yes when using S3 | Not set | The S3 secret access key for authentication.                                                              |
| ASSET_STORE_S3_FORCE_PATH_STYLE  | No                | false   | Whether to force path-style URLs for S3 requests. Set to true for MinIO and other S3-compatible services. |

:::info
When using S3 storage, make sure the bucket exists and the provided credentials have the necessary permissions to read, write, and delete objects in the bucket.
:::

:::warning
Switching between storage backends after data has been stored will require manual migration of existing assets. Plan your storage backend choice carefully before deploying.
:::

## Authentication / Signup

By default, Karakeep uses the database to store users, but it is possible to also use OAuth.
The flags need to be provided to the `web` container.

:::info
Only OIDC compliant OAuth providers are supported! For information on how to set it up, consult the documentation of your provider.
:::

:::info
When setting up OAuth, the allowed redirect URLs configured at the provider should be set to `<KARAKEEP_ADDRESS>/api/auth/callback/custom` where `<KARAKEEP_ADDRESS>` is the address you configured in `NEXTAUTH_URL` (for example: `https://try.karakeep.app/api/auth/callback/custom`).
:::

| Name                                        | Required | Default                | Description                                                                                                                                                                                           |
| ------------------------------------------- | -------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DISABLE_SIGNUPS                             | No       | false                  | If enabled, no new signups will be allowed and the signup button will be disabled in the UI                                                                                                           |
| DISABLE_PASSWORD_AUTH                       | No       | false                  | If enabled, only signups and logins using OAuth are allowed and the signup button and login form for local accounts will be disabled in the UI                                                        |
| EMAIL_VERIFICATION_REQUIRED                 | No       | false                  | Whether email verification is required during user signup. If enabled, users must verify their email address before they can use their account. If you enable this, you must configure SMTP settings. |
| OAUTH_WELLKNOWN_URL                         | No       | Not set                | The "wellknown Url" for openid-configuration as provided by the OAuth provider                                                                                                                        |
| OAUTH_CLIENT_SECRET                         | No       | Not set                | The "Client Secret" as provided by the OAuth provider                                                                                                                                                 |
| OAUTH_CLIENT_ID                             | No       | Not set                | The "Client ID" as provided by the OAuth provider                                                                                                                                                     |
| OAUTH_SCOPE                                 | No       | "openid email profile" | "Full list of scopes to request (space delimited)"                                                                                                                                                    |
| OAUTH_PROVIDER_NAME                         | No       | "Custom Provider"      | The name of your provider. Will be shown on the signup page as "Sign in with `<name>`"                                                                                                                |
| OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING | No       | false                  | Whether existing accounts in karakeep stored in the database should automatically be linked with your OAuth account. Only enable it if you trust the OAuth provider!                                  |
| OAUTH_TIMEOUT                               | No       | 3500                   | The wait time in milliseconds for the OAuth provider response. Increase this if you are having `outgoing request timed out` errors                                                                    |

For more information on `OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING`, check the [next-auth.js documentation](https://next-auth.js.org/configuration/providers/oauth#allowdangerousemailaccountlinking-option).

## Inference Configs (For automatic tagging)

Either `OPENAI_API_KEY` or `OLLAMA_BASE_URL` need to be set for automatic tagging to be enabled. Otherwise, automatic tagging will be skipped.

:::warning

- The quality of the tags you'll get will depend on the quality of the model you choose.
- You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be (money-wise on OpenAI and resource-wise on ollama).
  :::

| Name                                 | Required | Default                | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAI_API_KEY                       | No       | Not set                | The OpenAI key used for automatic tagging. More on that in [here](../06-administration/03-openai.md).                                                                                                                                                                                                                                                                                            |
| OPENAI_BASE_URL                      | No       | Not set                | If you just want to use OpenAI you don't need to pass this variable. If, however, you want to use some other openai compatible API (e.g. azure openai service), set this to the url of the API.                                                                                                                                                                                       |
| OPENAI_PROXY_URL                     | No       | Not set                | HTTP proxy server URL for OpenAI API requests (e.g., `http://proxy.example.com:8080`).                                                                                                                                                                                                                                                                                                |
| OPENAI_SERVICE_TIER                  | No       | Not set                | Set to `auto`, `default`, or `flex`. Flex processing provides lower costs in exchange for slower response times and occasional resource unavailability. See [OpenAI Flex Processing](https://platform.openai.com/docs/guides/flex-processing) and [Chat Service Tier](https://platform.openai.com/docs/api-reference/chat/object#chat-object-service_tier) for more details.          |
| OLLAMA_BASE_URL                      | No       | Not set                | If you want to use ollama for local inference, set the address of ollama API here.                                                                                                                                                                                                                                                                                                    |
| OLLAMA_KEEP_ALIVE                    | No       | Not set                | Controls how long the model will stay loaded into memory following the request (examples: "5m" for 5 minutes, "-1m" to keep the model loaded indefinitely, "0" to unload the model instantly after processing is complete).                                                                                                                                                                                                                                                                                 |
| INFERENCE_TEXT_MODEL                 | No       | gpt-4.1-mini           | The model to use for text inference. You'll need to change this to some other model if you're using ollama.                                                                                                                                                                                                                                                                           |
| INFERENCE_IMAGE_MODEL                | No       | gpt-4o-mini            | The model to use for image inference. You'll need to change this to some other model if you're using ollama and that model needs to support vision APIs (e.g. llava).                                                                                                                                                                                                                 |
| EMBEDDING_TEXT_MODEL                 | No       | text-embedding-3-small | The model to be used for generating embeddings for the text.                                                                                                                                                                                                                                                                                                                          |
| INFERENCE_CONTEXT_LENGTH             | No       | 2048                   | The max number of tokens that we'll pass to the inference model. If your content is larger than this size, it'll be truncated to fit. The larger this value, the more of the content will be used in tag inference, but the more expensive the inference will be (money-wise on openAI and resource-wise on ollama). Check the model you're using for its max supported content size. |
| INFERENCE_MAX_OUTPUT_TOKENS          | No       | 2048                   | The maximum number of tokens that the inference model is allowed to generate in its response. This controls the length of AI-generated content like tags and summaries. Increase this if you need longer responses, but be aware that higher values will increase costs (for OpenAI) and processing time.                                                                             |
| INFERENCE_USE_MAX_COMPLETION_TOKENS  | No       | false                  | \[OpenAI Only\] Whether to use the newer `max_completion_tokens` parameter instead of the deprecated `max_tokens` parameter. Set to `true` if using GPT-5 or o-series models which require this. Will become the default in a future release.                                                                                                                                         |
| INFERENCE_LANG                       | No       | english                | The language in which the tags will be generated.                                                                                                                                                                                                                                                                                                                                     |
| INFERENCE_NUM_WORKERS                | No       | 1                      | Number of concurrent workers for AI inference tasks (tagging and summarization). Increase this if you have multiple AI inference requests and want to process them in parallel.                                                                                                                                                                                                       |
| INFERENCE_ENABLE_AUTO_TAGGING        | No       | true                   | Whether automatic AI tagging is enabled or disabled.                                                                                                                                                                                                                                                                                                                                  |
| INFERENCE_ENABLE_AUTO_SUMMARIZATION  | No       | false                  | Whether automatic AI summarization is enabled or disabled.                                                                                                                                                                                                                                                                                                                            |
| INFERENCE_JOB_TIMEOUT_SEC            | No       | 30                     | How long to wait for the inference job to finish before timing out. If you're running ollama without powerful GPUs, you might want to increase the timeout a bit.                                                                                                                                                                                                                     |
| INFERENCE_FETCH_TIMEOUT_SEC          | No       | 300                    | \[Ollama Only\] The timeout of the fetch request to the ollama server. If your inference requests take longer than the default 5mins, you might want to increase this timeout.                                                                                                                                                                                                        |
| INFERENCE_SUPPORTS_STRUCTURED_OUTPUT | No       | Not set                | \[DEPRECATED\] Whether the inference model supports structured output or not. Use INFERENCE_OUTPUT_SCHEMA instead. Setting this to true translates to INFERENCE_OUTPUT_SCHEMA=structured, and to false translates to INFERENCE_OUTPUT_SCHEMA=plain.                                                                                                                                   |
| INFERENCE_OUTPUT_SCHEMA              | No       | structured             | Possible values are "structured", "json", "plain". Structured is the preferred option, but if your model doesn't support it, you can use "json" if your model supports JSON mode, otherwise "plain" which should be supported by all the models but the model might not output the data in the correct format.                                                                        |

:::info

- You can append additional instructions to the prompt used for automatic tagging, in the `AI Settings` (in the `User Settings` screen)
- You can use the placeholders `$tags`, `$aiTags`, `$userTags` in the prompt. These placeholders will be replaced with all tags, ai generated tags or human created tags when automatic tagging is performed (e.g. `[karakeep, computer, ai]`)
  :::

## Crawler Configs

| Name                                     | Required | Default   | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_NUM_WORKERS                      | No       | 1         | Number of allowed concurrent crawling jobs. By default, we're only doing one crawling request at a time to avoid consuming a lot of resources.                                                                                                                                                                                                                                |
| BROWSER_WEB_URL                          | No       | Not set   | The browser's http debugging address. The worker will talk to this endpoint to resolve the debugging console's websocket address. If you already have the websocket address, use `BROWSER_WEBSOCKET_URL` instead. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution. |
| BROWSER_WEBSOCKET_URL                    | No       | Not set   | The websocket address of browser's debugging console. If you want to use [browserless](https://browserless.io), use their websocket address here. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution.                                                                 |
| BROWSER_CONNECT_ONDEMAND                 | No       | false     | If set to false, the crawler will proactively connect to the browser instance and always maintain an active connection. If set to true, the browser will be launched on demand only whenever a crawling is requested. Set to true if you're using a service that provides you with browser instances on demand.                                                               |
| CRAWLER_DOWNLOAD_BANNER_IMAGE            | No       | true      | Whether to cache the banner image used in the cards locally or fetch it each time directly from the website. Caching it consumes more storage space, but is more resilient against link rot and rate limits from websites.                                                                                                                                                    |
| CRAWLER_STORE_SCREENSHOT                 | No       | true      | Whether to store a screenshot from the crawled website or not. Screenshots act as a fallback for when we fail to extract an image from a website. You can also view the stored screenshots for any link.                                                                                                                                                                      |
| CRAWLER_FULL_PAGE_SCREENSHOT             | No       | false     | Whether to store a screenshot of the full page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, the screenshot will only include the visible part of the page                                                                                                                                                                              |
| CRAWLER_SCREENSHOT_TIMEOUT_SEC           | No       | 5         | How long to wait for the screenshot finish before timing out. If you are capturing full-page screenshots of long webpages, consider increasing this value.                                                                                                                                                                                                                    |
| CRAWLER_STORE_PDF                        | No       | false     | Whether to store a PDF snapshot of the crawled page. Disabled by default, as it can lead to much higher disk usage. When enabled, a PDF version of each crawled page will be captured and stored as an asset, which can be viewed in the bookmark preview.                                                                                                                    |
| CRAWLER_FULL_PAGE_ARCHIVE                | No       | false     | Whether to store a full local copy of the page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, only the readable text of the page is archived.                                                                                                                                                                                            |
| CRAWLER_JOB_TIMEOUT_SEC                  | No       | 60        | How long to wait for the crawler job to finish before timing out. If you have a slow internet connection or a low powered device, you might want to bump this up a bit                                                                                                                                                                                                        |
| CRAWLER_NAVIGATE_TIMEOUT_SEC             | No       | 30        | How long to spend navigating to the page (along with its redirects). Increase this if you have a slow internet connection                                                                                                                                                                                                                                                     |
| CRAWLER_VIDEO_DOWNLOAD                   | No       | false     | Whether to download videos from the page or not (using yt-dlp)                                                                                                                                                                                                                                                                                                                |
| CRAWLER_VIDEO_DOWNLOAD_MAX_SIZE          | No       | 50        | The maximum file size for the downloaded video. The quality will be chosen accordingly. Use -1 to disable the limit.                                                                                                                                                                                                                                                          |
| CRAWLER_VIDEO_DOWNLOAD_TIMEOUT_SEC       | No       | 600       | How long to wait for the video download to finish                                                                                                                                                                                                                                                                                                                             |
| CRAWLER_ENABLE_ADBLOCKER                 | No       | true      | Whether to enable an adblocker in the crawler or not. If you're facing troubles downloading the adblocking lists on worker startup, you can disable this.                                                                                                                                                                                                                     |
| CRAWLER_YTDLP_ARGS                       | No       | []        | Include additional yt-dlp arguments to be passed at crawl time separated by %%: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#general-options                                                                                                                                                                                                                           |
| BROWSER_COOKIE_PATH                      | No       | Not set   | Path to a JSON file containing cookies to be loaded into the browser context. The file should be an array of cookie objects, each with name and value (required), and optional fields like domain, path, expires, httpOnly, secure, and sameSite (e.g., `[{"name": "session", "value": "xxx", "domain": ".example.com"}`]).                                                   |
| HTML_CONTENT_SIZE_INLINE_THRESHOLD_BYTES | No       | 5 \* 1024 | The thresholds in bytes after which larger assets will be stored in the assetdb (folder/s3) instead of inline in the database.                                                                                                                                                                                                                                                |

<details>

  <summary>More info on BROWSER_COOKIE_PATH</summary>

BROWSER_COOKIE_PATH specifies the path to a JSON file containing cookies to be loaded into the browser context for crawling.

The JSON file must be an array of cookie objects, each with:

- name: The cookie name (required).
- value: The cookie value (required).
- Optional fields: domain, path, expires, httpOnly, secure, sameSite (values: "Strict", "Lax", or "None").

Example JSON file:

```json
[
  {
    "name": "session",
    "value": "xxx",
    "domain": ".example.com",
    "path": "/",
    "expires": 1735689600,
    "httpOnly": true,
    "secure": true,
    "sameSite": "Lax"
  }
]
```

</details>

## OCR Configs

Karakeep uses [tesseract.js](https://github.com/naptha/tesseract.js) to extract text from images by default. Alternatively, you can use an LLM-based OCR by enabling the `OCR_USE_LLM` flag. LLM-based OCR uses the configured inference model (OpenAI or Ollama) to extract text from images, which can provide better results for complex images but requires a configured inference provider.

| Name                     | Required | Default   | Description                                                                                                                                                                                                                               |
| ------------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OCR_CACHE_DIR            | No       | $TEMP_DIR | The dir where tesseract will download its models. By default, those models are not persisted and stored in the OS' temp dir.                                                                                                              |
| OCR_LANGS                | No       | eng       | Comma separated list of the language codes that you want tesseract to support. You can find the language codes [here](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html). Set to empty string to disable OCR. |
| OCR_CONFIDENCE_THRESHOLD | No       | 50        | A number between 0 and 100 indicating the minimum acceptable confidence from tessaract. If tessaract's confidence is lower than this value, extracted text won't be stored.                                                               |
| OCR_USE_LLM              | No       | false     | If set to true, uses the configured inference model (OpenAI or Ollama) for OCR instead of Tesseract. This can provide better results for complex images but requires a configured inference provider (`OPENAI_API_KEY` or `OLLAMA_BASE_URL`). Falls back to Tesseract if no inference provider is configured. |

## Webhook Configs

You can use webhooks to trigger actions when bookmarks are created, changed or crawled.

| Name                | Required | Default | Description                                       |
| ------------------- | -------- | ------- | ------------------------------------------------- |
| WEBHOOK_TIMEOUT_SEC | No       | 5       | The timeout for the webhook request in seconds.   |
| WEBHOOK_RETRY_TIMES | No       | 3       | The number of times to retry the webhook request. |

:::info

- The WEBHOOK_TOKEN is used for authentication. It will appear in the Authorization header as Bearer token.
  ```
  Authorization: Bearer <WEBHOOK_TOKEN>
  ```
- The webhook will be triggered with the job id (used for idempotence), bookmark id, bookmark type, the user id, the url and the operation in JSON format in the body.

  ```json
  {
    "jobId": "123",
    "type": "link",
    "bookmarkId": "exampleBookmarkId",
    "userId": "exampleUserId",
    "url": "https://example.com",
    "operation": "crawled"
  }
  ```

  :::

## SMTP Configuration

Karakeep can send emails for various purposes such as email verification during signup. Configure these settings to enable email functionality.

| Name          | Required | Default | Description                                                                                     |
| ------------- | -------- | ------- | ----------------------------------------------------------------------------------------------- |
| SMTP_HOST     | No       | Not set | The SMTP server hostname or IP address. Required if you want to enable email functionality.     |
| SMTP_PORT     | No       | 587     | The SMTP server port. Common values are 587 (STARTTLS), 465 (SSL/TLS), or 25 (unencrypted).     |
| SMTP_SECURE   | No       | false   | Whether to use SSL/TLS encryption. Set to true for port 465, false for port 587 with STARTTLS.  |
| SMTP_USER     | No       | Not set | The username for SMTP authentication. Usually your email address.                               |
| SMTP_PASSWORD | No       | Not set | The password for SMTP authentication. For services like Gmail, use an app-specific password.    |
| SMTP_FROM     | No       | Not set | The "from" email address that will appear in sent emails. This should be a valid email address. |

## Proxy Configuration

If your Karakeep instance needs to connect through a proxy server, you can configure the following settings:

| Name                               | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_HTTP_PROXY                 | No       | Not set | HTTP proxy server URL for outgoing HTTP requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                                                           |
| CRAWLER_HTTPS_PROXY                | No       | Not set | HTTPS proxy server URL for outgoing HTTPS requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                                                         |
| CRAWLER_NO_PROXY                   | No       | Not set | Comma-separated list of hostnames/IPs that should bypass the proxy (e.g., `localhost,127.0.0.1,.local`)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CRAWLER_ALLOWED_INTERNAL_HOSTNAMES | No       | Not set | By default, Karakeep blocks worker-initiated requests whose DNS resolves to private, loopback, link-local, or Tailscale CGNAT IP addresses. Use this to allowlist specific hostnames for internal access (e.g., `internal.company.com`, `app-name.local`). Supports domain wildcards by prefixing with a dot (e.g., `.internal.company.com`, `.<tailnet-name>.ts.net`). Passing `.` allowlists all domains. Note: Internal IP validation is bypassed when a proxy is configured for the URL as the local DNS resolver won't necessarily be the same as the one used by the proxy. |

:::info
These proxy settings will be used by the crawler and other components that make outgoing HTTP requests.
:::

## Monitoring

Karakeep supports distributed tracing via OpenTelemetry. When enabled, traces are collected for tRPC API calls, background worker operations, and other key workflows. Karakeep also exports prometheus-based metrics.

| Name                        | Required | Default  | Description                                                                                                                                                                                                                                                                                                             |
| --------------------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OTEL_TRACING_ENABLED        | No       | false    | Set to `true` to enable OpenTelemetry tracing. When disabled, all tracing operations are no-ops.                                                                                                                                                                                                                        |
| OTEL_EXPORTER_OTLP_ENDPOINT | No       | Not set  | The OTLP HTTP endpoint to send traces to (e.g., `http://jaeger:4318/v1/traces` or `http://otel-collector:4318/v1/traces`). If not set, traces are logged to the console.                                                                                                                                                |
| OTEL_SERVICE_NAME           | No       | karakeep | The service name that will appear in your tracing backend. The actual service name will include a suffix (e.g., `karakeep-api`, `karakeep-workers`).                                                                                                                                                                    |
| OTEL_SAMPLE_RATE            | No       | 1.0      | The sampling rate for traces, between 0.0 and 1.0. A value of 1.0 means all traces are sampled, while 0.1 means only 10% of traces are sampled. Lower values reduce overhead and storage costs in production.                                                                                                           |
| PROMETHEUS_AUTH_TOKEN       | No       | Random   | Enable a prometheus metrics endpoint at `/api/metrics`. This endpoint will require this token being passed in the Authorization header as a Bearer token. If not set, a new random token is generated everytime at startup. This cannot contain any special characters or you may encounter a 400 Bad Request response. |


==================================================
File: docs/docs/03-configuration/02-different-ai-providers.md
==================================================
# Configuring different AI Providers

Karakeep uses LLM providers for AI tagging and summarization. We support OpenAI-compatible providers and ollama. This guide will show you how to configure different providers.

## OpenAI

If you want to use OpenAI itself, you just need to pass in the OPENAI_API_KEY environment variable.

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# You can change the default models by uncommenting the following lines, and choosing your model.
# INFERENCE_TEXT_MODEL=gpt-4.1-mini
# INFERENCE_IMAGE_MODEL=gpt-4o-mini
```

## Ollama

Ollama is a local LLM provider that you can use to run your own LLM server. You'll need to pass ollama's address to karakeep and you need to ensure that it's accessible from within the karakeep container (e.g. no localhost addresses).

Ollama provides two API endpoints:

1. **OpenAI-compatible API (Recommended)** - Uses the `/v1` chat endpoint which handles message formatting automatically
2. **Native Ollama API** - Requires manual formatting for some models

### Option 1: OpenAI-compatible API (Recommended)

This approach uses Ollama's OpenAI-compatible endpoint and is more reliable with various models:

```
OPENAI_API_KEY=ollama
OPENAI_BASE_URL=http://ollama.mylab.com:11434/v1

# Make sure to pull the models in ollama first. Example models:
INFERENCE_TEXT_MODEL=gemma3
INFERENCE_IMAGE_MODEL=llava
```

### Option 2: Native Ollama API

Alternatively, you can use the native Ollama API:

```
# MAKE SURE YOU DON'T HAVE OPENAI_API_KEY set, otherwise it takes precedence.

OLLAMA_BASE_URL=http://ollama.mylab.com:11434

# Make sure to pull the models in ollama first. Example models:
INFERENCE_TEXT_MODEL=gemma3
INFERENCE_IMAGE_MODEL=llava

# If the model you're using doesn't support structured output, you also need:
# INFERENCE_OUTPUT_SCHEMA=plain
```

:::tip
If you experience issues with certain models (especially OpenAI's gpt-oss models or other models requiring specific chat formats), try using the OpenAI-compatible API endpoint instead.
:::

## Gemini

Gemini has an OpenAI-compatible API. You need to get an api key from Google AI Studio.

```

OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=gemini-2.0-flash
INFERENCE_IMAGE_MODEL=gemini-2.0-flash
```

## OpenRouter

```
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=meta-llama/llama-4-scout
INFERENCE_IMAGE_MODEL=meta-llama/llama-4-scout
```

## Perplexity

```
OPENAI_BASE_URL: https://api.perplexity.ai
OPENAI_API_KEY: Your Perplexity API Key
INFERENCE_TEXT_MODEL: sonar-pro
INFERENCE_IMAGE_MODEL: sonar-pro
```

## Azure

Azure has an OpenAI-compatible API.

You can get your API key from the Overview page of the Azure AI Foundry Portal or via "Keys + Endpoints" on the resource in the Azure Portal.

:::warning
The [model name is the deployment name](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/switching-endpoints#keyword-argument-for-model) you specified when deploying the model, which may differ from the base model name.
:::

```
# Deployed via Azure AI Foundry:
OPENAI_BASE_URL=https://{your-azure-ai-foundry-resource-name}.cognitiveservices.azure.com/openai/v1/

# Deployed via Azure OpenAI Service:
OPENAI_BASE_URL=https://{your-azure-openai-resource-name}.openai.azure.com/openai/v1/

OPENAI_API_KEY=YOUR_API_KEY
INFERENCE_TEXT_MODEL=YOUR_DEPLOYMENT_NAME
INFERENCE_IMAGE_MODEL=YOUR_DEPLOYMENT_NAME
```


==================================================
File: docs/docs/04-using-karakeep/advanced-workflows.md
==================================================
---
sidebar_position: 10
slug: advanced-workflows
---

# Advanced workflows

Push Karakeep further with automation and integrations.

## Rule engine

- Create if-this-then-that style rules to auto-tag, favourite, or route bookmarks into lists based on metadata or content.
- Useful for keeping inboxes tidy (e.g. auto-archive newsletters, auto-tag domains, or flag videos).

## API

- Use the API to script imports, syncs, or custom tools. Same surface area the apps use.
- Great for integrating with personal scripts, cron jobs, or other services.

## Webhooks

- Subscribe to bookmark events and trigger your own systems when something is added, updated, or archived.
- Pair with the API to build end-to-end automations (e.g. push new saves into a writing queue or a team chat).


==================================================
File: docs/docs/04-using-karakeep/bookmarking.md
==================================================
---
sidebar_position: 1
slug: bookmarking
---

# Bookmarking

Everything in Karakeep starts as a bookmark. Here’s how the different types work and how to keep your home view tidy with favourites and archive.

## Favourites

- Star bookmarks you like so they sit in their own dedicated favourites view for quick return visits.
- Handy for saved gems you want to re-open often like articles you enjoyed, references you come back to, or things worth sharing.

## Archiving

- Archive hides a bookmark from the homepage without deleting it.
- Archived items stay searchable and keep all tags, highlights, and attachments.
- Ideal for achieving inbox-zero style for your homepage.

## Bookmark types

- **Links**: URLs saved from the web or extension. Karakeep grabs metadata, previews, screenshots, and archives when configured.
- **Text**: Quick notes or snippets you paste in. Great for ideas, quotes, or saving context alongside links.
- **Media**: Images or PDFs you want to save for later. Karakeep automatically extracts content out of those files and makes them searchable.

## Notes

- Attach personal notes to any bookmark to capture context, reminders, or next steps.
- Notes live with the bookmark and are searchable, so you can recall why something mattered.

## Highlights

- Save quotes, summaries, or TODOs while reading.
- Highlights show up in the bookmark detail view/reader and are searchable, so you can jump straight to the key ideas.

## Attachments

- Store extra context alongside a bookmark: screenshots, page captures, videos, and files you upload.
- **Screenshots & archives**: fallback when the original page changes or disappear.
- **Uploaded files**: keep PDFs, notes, or supporting assets right with the link.
- Manage attachments from the bookmark detail view: upload, download, or detach as needed.


==================================================
File: docs/docs/04-using-karakeep/import.md
==================================================
---
sidebar_position: 8
slug: import
---

# Import your library


Karakeep supports importing bookmarks using the Netscape HTML Format, Pocket's new CSV format & Omnivore's JSONs. Titles, tags and addition date will be preserved during the import. An automatically created list will contain all the imported bookmarks.

:::info
All the URLs in the bookmarks file will be added automatically, you will not be able to pick and choose which bookmarks to import!
:::

## Import from Chrome

- Open Chrome and go to `chrome://bookmarks`
- Click on the three dots on the top right corner and choose `Export bookmarks`
- This will download an html file with all of your bookmarks.
- To import the bookmark file, go to the settings and click "Import Bookmarks from HTML file".

## Import from Firefox
- Open Firefox and click on the menu button (☰) in the top right corner.
- Navigate to Bookmarks > Manage bookmarks (or press Ctrl + Shift + O / Cmd + Shift + O to open the Bookmarks Library).
- In the Bookmarks Library, click the Import and Backup button at the top. Select Export Bookmarks to HTML... to save your bookmarks as an HTML file.
- To import a bookmark file, go back to the Import and Backup menu, then select Import Bookmarks from HTML... and choose your saved HTML file.

## Import from Pocket

- Go to the [Pocket export page](https://getpocket.com/export) and follow the instructions to export your bookmarks.
- Pocket after a couple of minutes will mail you a zip file with all the bookmarks.
- Unzip the file and you'll get a CSV file.
- To import the bookmark file, go to the settings and click "Import Bookmarks from Pocket export".

## Import from Omnivore

- Follow Omnivore's [documentation](https://docs.omnivore.app/using/exporting.html) to export your bookmarks.
- This will give you a zip file with all your data.
- The zip file contains a lot of JSONs in the format `metadata_*.json`. You can either import every JSON file manually, or merge the JSONs into a single JSON file and import that.
- To  merge the JSONs into a single JSON file, you can use the following command in the unzipped directory: `jq -r '.[]' metadata_*.json | jq -s > omnivore.json` and then import the `omnivore.json` file. You'll need to have the [jq](https://github.com/jqlang/jq) tool installed.

## Import using the CLI

:::warning
Importing bookmarks using the CLI requires some technical knowledge and might not be very straightforward for non-technical users. Don't hesitate to ask questions in github discussions or discord though.
:::

If you can get your bookmarks in a text file with one link per line, you can use the following command to import them using the [karakeep cli](../05-integrations/02-command-line.md):

```
while IFS= read -r url; do
    karakeep --api-key "<KEY>" --server-addr "<SERVER_ADDR>" bookmarks add --link "$url"
done < all_links.txt
```


==================================================
File: docs/docs/04-using-karakeep/lists.md
==================================================
---
sidebar_position: 2
---

# Lists

Lists are the core organizational layer in Karakeep. Every saved item can sit in multiple lists so you can group links by project, topic, or audience without duplicating them.

## Manual lists

- Curated sets you add bookmarks to by hand. Great for projects, reading queues, or hand-picked collections.
- Can be **private** (visible only to you) or **public** (share a read-only link).
- Can be **collaborative**: invite people by email as viewers or editors. Editors can add their own bookmarks; viewers can browse. Your personal states (favourite/archive) stay yours even inside a shared list.

## Smart lists

- Auto-updating lists powered by a saved search query (e.g. `#ai -archived`).
- Best for dynamic views like `Youtube links added last week` or `All reddit links from r/selfhosted`.


==================================================
File: docs/docs/04-using-karakeep/quick-sharing.md
==================================================
---
sidebar_position: 7
slug: quick-sharing
---

# Quick capture and sharing

The whole point of Karakeep is making it easy to hoard the content. That's why there are a couple of 

## Mobile Apps

<img src="/img/quick-sharing/mobile.png" alt="mobile screenshot" width="300"/>


- **iOS app**: [App Store Link](https://apps.apple.com/us/app/karakeep-app/id6479258022).
- **Android App**: [Play Store link](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).

## Browser Extensions

<img src="/img/quick-sharing/extension.png" alt="mobile screenshot" width="300"/>

- **Chrome extension**: [here](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje).
- **Firefox addon**: [here](https://addons.mozilla.org/en-US/firefox/addon/karakeep/).

- ## Community Extensions
- **Safari extension**: [App Store Link](https://apps.apple.com/us/app/karakeeper-bookmarker/id6746722790).  For macOS and iOS to allow a simple way to add your bookmarks to your self hosted karakeep instance.


==================================================
File: docs/docs/04-using-karakeep/search-query-language.md
==================================================
---
sidebar_position: 9
slug: search-query-language
---

# Search Query Language

Karakeep provides a search query language to filter and find bookmarks. Here are all the supported qualifiers and how to use them:

## Basic Syntax

- Use spaces to separate multiple conditions (implicit AND)
- Use `and`/`or` keywords for explicit boolean logic
- Prefix qualifiers with `-` or `!` to negate them (e.g., `-is:archived` or `!is:archived`)
- Use parentheses `()` for grouping conditions (note that groups can't be negated)

## Qualifiers

Here's a comprehensive table of all supported qualifiers:

| Qualifier                        | Description                                                                                                                                                                                               | Example Usage                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `is:fav`                         | Favorited bookmarks                                                                                                                                                                                       | `is:fav`                                     |
| `is:archived`                    | Archived bookmarks                                                                                                                                                                                        | `-is:archived`                               |
| `is:tagged`                      | Bookmarks that has one or more tags                                                                                                                                                                       | `is:tagged`                                  |
| `is:inlist`                      | Bookmarks that are in one or more lists                                                                                                                                                                   | `is:inlist`                                  |
| `is:link`, `is:text`, `is:media` | Bookmarks that are of type link, text or media                                                                                                                                                            | `is:link`                                    |
| `is:broken`                      | Bookmarks with broken/failed links (crawl failures or non-2xx status codes)                                                                                                                               | `is:broken`                                  |
| `url:<value>`                    | Match bookmarks with URL substring                                                                                                                                                                        | `url:example.com`                            |
| `title:<value>`                  | Match bookmarks with title substring                                                                                                               | `title:example`                              |
|                                  | Supports quoted strings for titles with spaces                                                                                                   | `title:"my title"`                           |
| `#<tag>` or `tag:<tag>`          | Match bookmarks with specific tag                                                                                                                                                                         | `#important` or `tag:important`              |
|                                  | Supports quoted strings for tags with spaces                                                                                                                                                              | `#"work in progress"` or `tag:"work in progress"` |
| `list:<name>`                    | Match bookmarks in specific list                                                                                                                                                                          | `list:reading`                               |
|                                  | Supports quoted strings for list names with spaces                                                                                                                                                        | `list:"to review"`                           |
| `after:<date>`                   | Bookmarks created on or after date (YYYY-MM-DD)                                                                                                                                                           | `after:2023-01-01`                           |
| `before:<date>`                  | Bookmarks created on or before date (YYYY-MM-DD)                                                                                                                                                          | `before:2023-12-31`                          |
| `feed:<name>`                    | Bookmarks imported from a particular rss feed                                                                                                                                                             | `feed:Hackernews`                            |
| `source:<value>`                 | Match bookmarks from a specific source. Valid values: `api`, `web`, `cli`, `mobile`, `extension`, `singlefile`, `rss`, `import`                                                                          | `source:rss` `-source:web`                   |
| `age:<time-range>`               | Match bookmarks based on how long ago they were created. Use `<` or `>` to indicate the maximum / minimum age of the bookmarks. Supported units: `d` (days), `w` (weeks), `m` (months), `y` (years). | `age:<1d` `age:>2w` `age:<6m` `age:>3y` |

### Examples

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not tagged or not in any list
-is:tagged or -is:inlist
# Find bookmarks with "React" in the title
title:React
```

## Combining Conditions

You can combine multiple conditions using boolean logic:

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not favorited and not archived
-is:fav -is:archived

# Using ! as an alias for negation
!is:fav !is:archived

# Using tag: as an alias for #
tag:important tag:"work in progress"
```

## Text Search

Any text not part of a qualifier will be treated as a full-text search:

```plaintext
# Search for "machine learning" in bookmark content
machine learning

# Combine text search with qualifiers
machine learning is:fav
```


==================================================
File: docs/docs/04-using-karakeep/tags.md
==================================================
---
sidebar_position: 3
---

# Tags

Tags are lightweight labels you can attach to any bookmark to add meaning without rigid folders.

- Use tags to capture topics, sources, people, or workflow states (e.g. `ai`, `design`, `to-read`).
- Combine multiple tags to filter or build smart lists; tags travel with a bookmark wherever it appears.
- AI tags might look a little messy, but the extra labels make finding things easier. Use tags for broad discovery and lists when you want a clean, hand-picked setup.


==================================================
File: docs/docs/05-integrations/02-command-line.md
==================================================
# Command Line Tool (CLI)

Karakeep comes with a simple CLI for those users who want to do more advanced manipulation.

## Features

- Manipulate bookmarks, lists and tags
- Mass import/export of bookmarks

## Installation (NPM)

```
npm install -g @karakeep/cli
```


## Installation (Docker)

```
docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help
```

## Usage

```
karakeep
```

```
Usage: karakeep [options] [command]

A CLI interface to interact with the karakeep api

Options:
  --api-key <key>       the API key to interact with the API (env: KARAKEEP_API_KEY)
  --server-addr <addr>  the address of the server to connect to (env: KARAKEEP_SERVER_ADDR)
  -V, --version         output the version number
  -h, --help            display help for command

Commands:
  bookmarks             manipulating bookmarks
  lists                 manipulating lists
  tags                  manipulating tags
  whoami                returns info about the owner of this API key
  help [command]        display help for command
```

And some of the subcommands:

```
karakeep bookmarks
```

```
Usage: karakeep bookmarks [options] [command]

Manipulating bookmarks

Options:
  -h, --help             display help for command

Commands:
  add [options]          creates a new bookmark
  get <id>               fetch information about a bookmark
  update [options] <id>  updates bookmark
  list [options]         list all bookmarks
  delete <id>            delete a bookmark
  help [command]         display help for command

```

```
karakeep lists
```

```
Usage: karakeep lists [options] [command]

Manipulating lists

Options:
  -h, --help                 display help for command

Commands:
  list                       lists all lists
  delete <id>                deletes a list
  add-bookmark [options]     add a bookmark to list
  remove-bookmark [options]  remove a bookmark from list
  help [command]             display help for command
```

## Obtaining an API Key

To use the CLI, you'll need to get an API key from your karakeep settings. You can validate that it's working by running:

```
karakeep --api-key <key> --server-addr <addr> whoami
```

For example:

```
karakeep --api-key mysupersecretkey --server-addr https://try.karakeep.app whoami
{
  id: 'j29gnbzxxd01q74j2lu88tnb',
  name: 'Test User',
  email: 'test@gmail.com'
}
```


## Other clients

There also exists a **non-official**, community-maintained, python package called [karakeep-python-api](https://github.com/thiswillbeyourgithub/karakeep_python_api) that can be accessed from the CLI, but is **not** official.


==================================================
File: docs/docs/05-integrations/03-mcp.md
==================================================
# Model Context Protocol Server (MCP)

Karakeep comes with a Model Context Protocol server that can be used to interact with it through LLMs.

## Supported Tools

- Searching bookmarks
- Adding and removing bookmarks from lists
- Attaching and detaching tags to bookmarks
- Creating new lists
- Creating text and URL bookmarks


## Usage with Claude Desktop

From NPM:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "npx",
      "args": [
        "@karakeep/mcp"
      ],
      "env": {
        "KARAKEEP_API_ADDR": "https://<YOUR_SERVER_ADDR>",
        "KARAKEEP_API_KEY": "<YOUR_TOKEN>"
      }
    }
  }
}
```

From Docker:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "docker",
      "args": [
        "run",
        "-e",
        "KARAKEEP_API_ADDR=https://<YOUR_SERVER_ADDR>",
        "-e",
        "KARAKEEP_API_KEY=<YOUR_TOKEN>",
        "ghcr.io/karakeep-app/karakeep-mcp:latest"
      ]
    }
  }
}
```


### Demo

#### Search
![mcp-1](/img/mcp-1.gif)

#### Adding Text Bookmarks
![mcp-2](/img/mcp-2.gif)

#### Adding URL Bookmarks
![mcp-2](/img/mcp-3.gif)


==================================================
File: docs/docs/05-integrations/05-singlefile.md
==================================================
# Using Karakeep with SingleFile Extension

Karakeep supports being a destination for the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile). This has the benefit of allowing you to use the singlefile extension to hoard links as you're seeing them in the browser. This is perfect for websites that don't like to get crawled, has annoying cookie banner or require authentication.

## Setup

1. Install the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile).
2. In the extension settings, select `Destinations`.
3. Select `upload to a REST Form API`.
4. In the URL, insert the address: `https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile`.
5. In the `authorization token` field, paste an API key that you can get from your karakeep settings.
6. Set `data field name` to `file`.
7. Set `URL field name` to `url`.
8. (Optional) Add `&ifexists=MODE` to the URL where MODE is one of `skip`, `overwrite`, `overwrite-recrawl`, `append`, or `append-recrawl`. See "Handling Existing Bookmarks" section below for details.

Now, go to any page and click the singlefile extension icon. Once it's done with the upload, the bookmark should show up in your karakeep instance. Note that the singlefile extension doesn't show any progress on the upload. Given that archives are typically large, it might take 30+ seconds until the upload is done and starts showing up in Karakeep.

## Handling Existing Bookmarks

When uploading a page that already exists in your archive (same URL), you can control the behavior by setting the `ifexists` query parameter in the upload URL. The available modes are:

- `skip` (default): If the bookmark already exists, skip creating a new one
- `overwrite`: Replace existing precrawled archive (only the most recent archive is kept)
- `overwrite-recrawl`: Replace existing archive and queue a recrawl to update content
- `append`: Add new archive version alongside existing ones
- `append-recrawl`: Add new archive and queue a recrawl

To use these modes, append `?ifexists=MODE` to your upload URL, replacing `MODE` with your desired behavior.

For example:  
`https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile?ifexists=overwrite`


## Recommended settings

In the singlefile extension, you probably will want to change the following settings for better experience:
* Stylesheets > compress CSS content: on
* Stylesheets > group duplicate stylesheets together: on
* HTML content > remove frames: on

Also, you most likely will want to change the default `MAX_ASSET_SIZE_MB` in karakeep to something higher, for example `100`.

:::info
Currently, we don't support screenshots for singlefile uploads, but this will change in the future.
:::



==================================================
File: docs/docs/05-integrations/06-rss-feeds.md
==================================================
# RSS Feeds

Karakeep offers RSS feed integration, allowing you to both consume RSS feeds from external sources and publish your lists as RSS feeds for others to subscribe to.

## Publishing RSS Feeds

You can publish any of your lists as an RSS feed, making it easy to share your bookmarks with others or integrate them into RSS readers.

### Enabling RSS for a List

1. Navigate to one of your lists
2. Click on the list settings (three dots menu)
3. Toggle the "RSS Feed" switch to enable it
4. Copy the generated RSS feed URL

### What Gets Published

RSS feeds include:
- **Links**: Bookmarks of type "link" with their URL, title, description, and author
- **Assets**: Uploaded files (PDFs, images) are included with a link to view them
- **Tags**: Bookmark tags are exported as RSS categories
- **Dates**: The bookmark creation date is used as the publication date

Note: Text notes are not included in RSS feeds as they don't have an associated URL.

### Security Considerations

- Each RSS feed requires a unique token for access
- Tokens can be regenerated at any time, which will invalidate the old URL
- Disabling RSS for a list immediately revokes access

## Consuming RSS Feeds

Karakeep can automatically monitor RSS feeds and create bookmarks from new entries, making it perfect for staying up to date with blogs, news sites, and other content sources.

### Adding an RSS Feed

1. Go to **Settings** → **RSS Feeds**
2. Click **Add Feed**
3. Enter the feed details:
   - **Name**: A friendly name for the feed
   - **URL**: The RSS/Atom feed URL
   - **Enabled**: Toggle to enable/disable the feed
   - **Import Tags**: Enable to import RSS categories as bookmark tags

### How It Works

- Karakeep checks enabled RSS feeds **every hour**
- New entries are automatically created as bookmarks
- Duplicate entries are automatically detected and skipped


==================================================
File: docs/docs/06-administration/01-security-considerations.md
==================================================
# Security Considerations

If you're going to give app access to untrusted users, there's some security considerations that you'll need to be aware of given how the crawler works. The crawler is basically running a browser to fetch the content of the bookmarks. Any untrusted user can submit bookmarks to be crawled from your server and they'll be able to see the crawling result. This can be abused in multiple ways:

1. Untrusted users can submit crawl requests to websites that you don't want to be coming out of your IPs.
2. Crawling user controlled websites can expose your origin IP (and location) even if your service is hosted behind cloudflare for example.
3. The crawling requests will be coming out from your own network, which untrusted users can leverage to crawl internal non-internet exposed endpoints.

To mitigate those risks, you can do one of the following:

1. Limit access to trusted users
2. Let the browser traffic go through some VPN with restricted network policies.
3. Host the browser container outside of your network.
4. Use a hosted browser as a service (e.g. [browserless](https://browserless.io)). Note: I've never used them before.


==================================================
File: docs/docs/06-administration/02-FAQ.md
==================================================
# Frequently Asked Questions (FAQ)

## User Management

### Lost password

#### If you are not an administrator

Administrators can reset the password of any user. Contact an administrator to reset the password for you.

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to reset the password
- Enter a new password and press `Reset`
- The new password is now set
- If required, you can change your password again (so the admin does not know your password) in the `User Settings`

#### If you are an administrator

If you are an administrator and lost your password, you have to reset the password in the database.

To reset the password:

- Acquire some kind of tools that helps you to connect to the database:
  - `sqlite3` on Linux: run `apt-get install sqlite3` (depending on your package manager)
  - e.g. `dbeaver` on Windows
- Shut down Karakeep
- Connect to the `db.db` database, which is located in the `data` directory you have mounted to your docker container:
  - by e.g. running `sqlite3 db.db` (in your `data` directory)
  - or going through e.g. the `dbeaver` UI to locate the file in the data directory and connecting to it
- Update the password in the database by running:
  - `update user set password='$2a$10$5u40XUq/cD/TmLdCOyZ82ePENE6hpkbodJhsp7.e/BgZssUO5DDTa', salt='' where email='<YOUR_EMAIL_HERE>';`
  - (don't forget to put your email address into the command)
- The new password for your user is now `adminadmin`.
- Start Karakeep again
- Log in with your email address and the password `adminadmin` and change the password to whatever you want in the `User Settings`

### Adding another administrator

By default, the first user to sign up gets promoted to administrator automatically.

In case you want to grant those permissions to another user:

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to change the Role
- Change the Role to `Admin`
- Press `Change`
- The new administrator has to log out and log in again to get the new role assigned

### Adding new users, when signups are disabled

Administrators can create new accounts any time:

- Navigate to the `Admin Settings` page
- Go to the `Users List`
- Press the `Create User` Button.
- Enter the information for the user
- Press `create`
- The new user can now log in


==================================================
File: docs/docs/06-administration/03-openai.md
==================================================
# Tagging Costs

This service uses OpenAI for automatic tagging. This means that you'll incur some costs if automatic tagging is enabled. There are two type of inferences that we do:

## Text Tagging

For text tagging, we use the `gpt-4.1-mini` model. This model is [extremely cheap](https://openai.com/api/pricing). Cost per inference varies depending on the content size per article. Though, roughly, You'll be able to generate tags for almost 3000+ bookmarks for less than $1.

## Image Tagging

For image uploads, we use the `gpt-4o-mini` model for extracting tags from the image. You can learn more about the costs of using this model [here](https://platform.openai.com/docs/guides/images?api-mode=chat#calculating-costs). To lower the costs, we're using the low resolution mode (fixed number of tokens regardless of image size). You'll be able to run inference for 1000+ images for less than a $1.


==================================================
File: docs/docs/06-administration/05-troubleshooting.md
==================================================
# Troubleshooting

## SqliteError: no such table: user

This usually means that there's something wrong with the database setup (more concretely, it means that the database is not initialized). This can be caused by multiple problems:
1. **Wiped DATA_DIR:** Your `DATA_DIR` got wiped (or the backing storage dir changed). If you did this intentionally, restart the container so that it can re-initalize the database.
2. **Missing DATA_DIR**: You're not using the default docker compose file, and you forgot to configure the `DATA_DIR` env var. This will result into the database getting set up in a different directory than the one used by the service.

## Chrome Failed to Read DnsConfig

If you see this error in the logs of the chrome container, it's a benign error and you can safely ignore it. Whatever problems you're having, is unrelated to this error.

## AI Tagging not working (when using OpenAI)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OPENAI_API_KEY` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring open ai.
3. OpenAI requires pre-charging the account with credits before using it, otherwise you'll get an error like "insufficient funds".

## AI Tagging not working (when using Ollama)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OLLAMA_BASE_URL` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring ollama.
3. You didn't change the `INFERENCE_TEXT_MODEL` env variable, resulting into karakeep attempting to use gpt models with ollama which won't work.
4. Ollama server is not reachable by the karakeep container. This can be caused by:
    1. Ollama server being in a different docker network than the karakeep container.
    2. You're using `localhost` as the `OLLAMA_BASE_URL` instead of the actual address of the ollama server. `localhost` points to the container itself, not the docker host. Check this [stackoverflow answer](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) to find how to correctly point to the docker host address instead.

## Crawling not working

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. You changed the name of the chrome container but didn't change the `BROWSER_WEB_URL` env variable.

## Upgrading Meilisearch - Migrating the Meilisearch db version

[Meilisearch](https://www.meilisearch.com/) is the database used by karakeep for searching in your bookmarks. The version used by karakeep is `1.13.3` and it is advised not to upgrade it without good reasons. If you do, you might see errors like `Your database version (1.11.1) is incompatible with your current engine version (1.13.3). To migrate data between Meilisearch versions, please follow our guide on https://www.meilisearch.com/docs/learn/update_and_migration/updating.`.

Luckily we can easily workaround this:
1. Stop the Meilisearch container.
2. Inside the Meilisearch volume bound to `/meili_data`, erase/rename the folder called `data.ms`.
3. Launch Meilisearch again.
4. Login to karakeep as administrator and go to (as of v0.24.1) `Admin Settings > Background Jobs` then click on `Reindex All Bookmarks`.
5. When the reindexing has finished, Meilisearch should be working as usual.

If you run into issues, the official documentation can be found [there](https://www.meilisearch.com/docs/learn/update_and_migration/updating).


==================================================
File: docs/docs/06-administration/06-server-migration.md
==================================================
# Migrating Between Servers

This guide explains how to migrate all of your data from one Karakeep server to another using the official CLI.

## What the command does

The migration copies user-owned data from a source server to a destination server in this order:

- User settings
- Lists (preserving hierarchy and settings)
- RSS feeds
- AI prompts (custom prompts and their enabled state)
- Webhooks (URL and events)
- Tags (ensures tags by name exist)
- Rule engine rules (IDs remapped to destination equivalents)
- Bookmarks (links, text, and assets)
  - After creation, attaches the correct tags and adds to the correct lists

Notes:
- Webhook tokens cannot be read via the API, so tokens are not migrated. Re‑add them on the destination if needed.
- Asset bookmarks are migrated by downloading the original asset and re‑uploading it to the destination. Only images and PDFs are supported for asset bookmarks.
- Link bookmarks on the destination may be de‑duplicated if the same URL already exists.

## Prerequisites

- Install the CLI:
  - NPM: `npm install -g @karakeep/cli`
  - Docker: `docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help`
- Collect API keys and base URLs for both servers:
  - Source: `--server-addr`, `--api-key`
  - Destination: `--dest-server`, `--dest-api-key`

## Quick start

```
karakeep --server-addr https://src.example.com --api-key <SOURCE_API_KEY> migrate \
  --dest-server https://dest.example.com \
  --dest-api-key <DEST_API_KEY>
```

The command is long‑running and shows live progress for each phase. You will be prompted for confirmation; pass `--yes` to skip the prompt.

### Options

- `--server-addr <url>`: Source server base URL
- `--api-key <key>`: API key for the source server
- `--dest-server <url>`: Destination server base URL
- `--dest-api-key <key>`: API key for the destination server
- `--batch-size <n>`: Page size for bookmark migration (default 50, max 100)
- `-y`, `--yes`: Skip the confirmation prompt

## What to expect

- Lists are recreated parent‑first and retain their hierarchy.
- Feeds, prompts, webhooks, and tags are recreated by value.
- Rules are recreated after IDs (tags, lists, feeds) are remapped to their corresponding destination IDs.
- After each bookmark is created, the command attaches the correct tags and adds it to the correct lists.

## Caveats and tips

- Webhook auth tokens must be re‑entered on the destination after migration.
- If your destination already contains data, duplicate links may be de‑duplicated; tags and list membership are still applied to the existing bookmark.

## Troubleshooting

- If the command exits early, you can re‑run it, but note:
  - Tags and lists that already exist are reused.
  - Link de‑duplication avoids duplicate link bookmarks. Notes and assets will get re-created.
  - Rules, webhooks, rss feeds will get re-created and you'll have to manually clean them up afterwards.
  - The progress log indicates how far it got.
- Use a smaller `--batch-size` if your source or destination is under heavy load.


==================================================
File: docs/docs/06-administration/07-legacy-container-upgrade.md
==================================================
# Legacy Container Upgrade

Karakeep's 0.16 release consolidated the web and worker containers into a single container and also dropped the need for the redis container. The legacy containers will stop being supported soon, to upgrade to the new container do the following:

1. Remove the redis container and its volume if it had one.
2. Move the environment variables that you've set exclusively to the `workers` container to the `web` container.
3. Delete the `workers` container.
4. Rename the web container image from `hoarder-app/hoarder-web` to `hoarder-app/hoarder`.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder-web:${KARAKEEP_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${KARAKEEP_VERSION:-release}
     restart: unless-stopped
     volumes:
       - data:/data
@@ -10,14 +10,10 @@ services:
     env_file:
       - .env
     environment:
-      REDIS_HOST: redis
       MEILI_ADDR: http://meilisearch:7700
+      BROWSER_WEB_URL: http://chrome:9222
+      # OPENAI_API_KEY: ...
       DATA_DIR: /data
-  redis:
-    image: redis:7.2-alpine
-    restart: unless-stopped
-    volumes:
-      - redis:/data
   chrome:
     image: gcr.io/zenika-hub/alpine-chrome:123
     restart: unless-stopped
@@ -37,24 +33,7 @@ services:
       MEILI_NO_ANALYTICS: "true"
     volumes:
       - meilisearch:/meili_data
-  workers:
-    image: ghcr.io/hoarder-app/hoarder-workers:${KARAKEEP_VERSION:-release}
-    restart: unless-stopped
-    volumes:
-      - data:/data
-    env_file:
-      - .env
-    environment:
-      REDIS_HOST: redis
-      MEILI_ADDR: http://meilisearch:7700
-      BROWSER_WEB_URL: http://chrome:9222
-      DATA_DIR: /data
-      # OPENAI_API_KEY: ...
-    depends_on:
-      web:
-        condition: service_started

 volumes:
-  redis:
   meilisearch:
   data:
```


==================================================
File: docs/docs/06-administration/08-hoarder-to-karakeep-migration.md
==================================================
# Hoarder to Karakeep Migration

Hoarder is rebranding to Karakeep. Due to github limitations, the old docker image might not be getting new updates after the rebranding. You might need to update your docker image to point to the new karakeep image instead by applying the following change in the docker compose file.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder:${HOARDER_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${HOARDER_VERSION:-release}
```

You can also change the `HOARDER_VERSION` environment variable but if you do so remember to change it in the `.env` file as well.

## Migrating a Baremetal Installation

If you previously used the [Debian/Ubuntu install script](../02-installation/06-debuntu.md) to install Hoarder, there is an option to migrate your installation to Karakeep.

```bash
bash karakeep-linux.sh migrate
```

This will migrate your installation with no user input required. After the migration, the script will also check for an update.


==================================================
File: docs/docs/07-community/01-community-projects.md
==================================================
# Community Projects

This page lists community projects that are built around Karakeep, but not officially supported by the development team.

:::warning
This list comes with no guarantees about security, performance, reliability, or accuracy. Use at your own risk.
:::

### Raycast Extension

_By [@luolei](https://github.com/foru17)._

A user-friendly Raycast extension that seamlessly integrates with Karakeep, bringing powerful bookmark management to your fingertips. Quickly save, search, and organize your bookmarks, texts, and images—all through Raycast's intuitive interface.

Get it [here](https://www.raycast.com/luolei/karakeep).

### Alfred Workflow

_By [@yinan-c](https://github.com/yinan-c)_

An Alfred workflow to quickly hoard stuff or access your hoarded bookmarks!

Get it [here](https://www.alfredforum.com/topic/22528-hoarder-workflow-for-self-hosted-bookmark-management/).

### Obsidian Plugin

_By [@jhofker](https://github.com/jhofker)_

An Obsidian plugin that syncs your Karakeep bookmarks with Obsidian, creating markdown notes for each bookmark in a designated folder.

Get it [here](https://github.com/jhofker/obsidian-hoarder/), or install it directly from Obsidian's community plugin store ([link](https://obsidian.md/plugins?id=hoarder-sync)).

### Telegram Bot

_By [@Madh93](https://github.com/Madh93)_

A Telegram Bot for saving bookmarks to Karakeep directly through Telegram.

Get it [here](https://github.com/Madh93/karakeepbot).

### Hoarder's Pipette

_By [@DanSnow](https://github.com/DanSnow)_

A chrome extension that injects karakeep's bookmarks into your search results.

Get it [here](https://dansnow.github.io/hoarder-pipette/guides/installation/).

### Karakeep-Python-API

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python package to simplify access to the karakeep API. Can be used as a library or from the CLI. Aims for feature completeness and high test coverage but do check its feature matrix before relying too much on it.

Its repository also hosts the [Community Script](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts), for example:

| Community Script | Description | Documentation |
|----------------|-------------|---------------|
| **Karakeep-Time-Tagger** | Automatically adds time-to-read tags (`0-5m`, `5-10m`, etc.) to bookmarks based on content length analysis. Includes systemd service and timer files for automated periodic execution. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-time-tagger) |
| **Karakeep-List-To-Tag** | Converts a Karakeep list into tags by adding a specified tag to all bookmarks within that list. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-list-to-tag) |
| **Omnivore2Karakeep-Highlights** | Imports highlights from Omnivore export data to Karakeep, with intelligent position detection and bookmark matching. Supports dry-run mode for testing. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/omnivore2karakeep-highlights) |


Get it [here](https://github.com/thiswillbeyourgithub/karakeep_python_api).

### FreshRSS_to_Karakeep

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python script to automatically create Karakeep bookmarks from your [FreshRSS](https://github.com/FreshRSS/FreshRSS) *favourites/saved* RSS item. Made to be called periodically. Based on the community project `Karakeep-Python-API` above, by the same author.

Get it [here](https://github.com/thiswillbeyourgithub/freshrss_to_karakeep).

### karakeep-sync
_By [@sidoshi](https://github.com/sidoshi/)_

Sync links from Hacker News upvotes, Reddit Saves to Karakeep for centralized bookmark management.

Get it [here](https://github.com/sidoshi/karakeep-sync)

### Home Assistant Integration

_By [@sli-cka](https://github.com/sli-cka)_

A custom integration that brings Karakeep data into Home Assistant. It exposes your Karakeep statistics data (like lists, bookmarks, tag, etc.) as Home Assistant entities, enabling dashboards, automations, and notifications based on your Karakeep data.

Get it [here](https://github.com/sli-cka/karakeep-homeassistant)


==================================================
File: docs/docs/07-community/02-community-channels.md
==================================================
# Community Channels

Stay connected with the Karakeep team and community for updates, support, and feature discussions.

## Discord

- Join the official server: [discord.gg/NrgeYywsFh](https://discord.gg/NrgeYywsFh)
- Great for getting help, sharing setups, and chatting with the team and other users.

## Twitter / X

- Follow [@karakeep_app](https://twitter.com/karakeep_app) for release announcements, tips, and product news.
- DM or tag us with feedback or things you'd like to see next.


==================================================
File: docs/docs/08-development/01-setup.md
==================================================
# Setup

## Quick Start

For the fastest way to get started with development, use the one-command setup script:

```bash
./start-dev.sh
```

This script will automatically:
- Start Meilisearch in Docker (on port 7700)
- Start headless Chrome in Docker (on port 9222) 
- Install dependencies with `pnpm install` if needed
- Start both the web app and workers in parallel
- Provide cleanup when you stop with Ctrl+C

**Prerequisites:**
- Docker installed and running
- pnpm installed (see manual setup below for installation instructions)

The script will output the running services:
- Web app: http://localhost:3000
- Meilisearch: http://localhost:7700  
- Chrome debugger: http://localhost:9222

Press Ctrl+C to stop all services and clean up Docker containers.

## Manual Setup

Karakeep uses `node` version 24. To install it, you can use `nvm` [^1]

```
$ nvm install  24
```

Verify node version using this command:
```
$ node --version
v24.14.0
```

Karakeep also makes use of `corepack`[^2]. If you have `node` installed, then `corepack` should already be
installed on your machine, and you don't need to do anything. To verify the `corepack` is installed run:

```
$ command -v corepack
/home/<user>/.nvm/versions/node/v24.14.0/bin/corepack
```

To enable `corepack` run the following command:

```
$ corepack enable
```

Then, from the root of the repository, install the packages and dependencies using:

```
$ pnpm install
```

Output of a successful `pnpm install` run should look something like:

```
Scope: all 20 workspace projects
Lockfile is up to date, resolution step is skipped
Packages: +3129
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 0, reused 2699, downloaded 0, added 3129, done

devDependencies:
+ @karakeep/prettier-config 0.1.0 <- tooling/prettier

. prepare$ husky
└─ Done in 45ms
Done in 5.5s
```

You can now continue with the rest of this documentation.

### First Setup

- You'll need to prepare the environment variables for the dev env.
- Easiest would be to set it up once in the root of the repo and then symlink it in each app directory (e.g. `/apps/web`, `/apps/workers`) and also `/packages/db`.
- Start by copying the template by `cp .env.sample .env`.
- The most important env variables to set are:
  - `DATA_DIR`: Where the database and assets will be stored. This is the only required env variable. You can use an absolute path so that all apps point to the same dir.
  - `NEXTAUTH_SECRET`: Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`. Logging in will not work if this is missing!
  - `MEILI_ADDR`: If not set, search will be disabled. You can set it to `http://127.0.0.1:7700` if you run meilisearch using the command below.
  - `OPENAI_API_KEY`: If you want to enable auto tag inference in the dev env.
- run `pnpm run db:migrate` in the root of the repo to set up the database.

### Dependencies

#### Meilisearch

Meilisearch is the provider for the full text search (and at some point embeddings search too). You can get it running with `docker run -p 7700:7700 getmeili/meilisearch:v1.13.3`.

Mount persistent volume if you want to keep index data across restarts. You can trigger a re-index for the entire items collection in the admin panel in the web app.

#### Chrome

The worker app will automatically start headless chrome on startup for crawling pages. You don't need to do anything there.

### Web App

- Run `pnpm web` in the root of the repo.
- Go to `http://localhost:3000`.

> NOTE: The web app kinda works without any dependencies. However, search won't work unless meilisearch is running. Also, new items added won't get crawled/indexed unless workers are running.

### Workers

- Run `pnpm workers` in the root of the repo.

### Mobile App (iOS & Android)

#### Prerequisites

To build and run the mobile app locally, you'll need:

- **For iOS development**: 
  - macOS computer
  - Xcode installed from the App Store
  - iOS Simulator (comes with Xcode)

- **For Android development**:
  - Android Studio installed
  - Android SDK configured
  - Android Emulator or physical device

For detailed setup instructions, refer to the [Expo documentation](https://docs.expo.dev/guides/local-app-development/).

#### Running the app

- `cd apps/mobile`
- `pnpm exec expo prebuild --no-install` to build the app.

**For iOS:**
- `pnpm exec expo run:ios`
- The app will be installed and started in the simulator.

**Troubleshooting iOS Setup:**
If you encounter an error like `xcrun: error: SDK "iphoneos" cannot be located`, you may need to set the correct Xcode developer directory:
```bash
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

**For Android:**
- Start the Android emulator or connect a physical device.
- `pnpm exec expo run:android`
- The app will be installed and started on the emulator/device.

Changing the code will hot reload the app. However, installing new packages requires restarting the expo server.

### Browser Extension

- `cd apps/browser-extension`
- `pnpm dev`
- This will generate a `dist` package
- Go to extension settings in chrome and enable developer mode.
- Press `Load unpacked` and point it to the `dist` directory.
- The plugin will pop up in the plugin list.

In dev mode, opening and closing the plugin menu should reload the code.


## Docker Dev Env

If the manual setup is too much hassle for you. You can use a docker based dev environment by running `docker compose -f docker/docker-compose.dev.yml up` in the root of the repo. This setup wasn't super reliable for me though.


[^1]: [nvm](https://github.com/nvm-sh/nvm) is a node version manager. You can install it following [these
instructions](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

[^2]: [corepack](https://nodejs.org/api/corepack.html) is an experimental tool to help with managing versions of your
package managers.


==================================================
File: docs/docs/08-development/02-directories.md
==================================================
# Directory Structure

## Apps

| Directory                | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| `apps/web`               | The main web app                                       |
| `apps/workers`           | The background workers logic                           |
| `apps/mobile`            | The react native based mobile app                      |
| `apps/browser-extension` | The browser extension                                  |
| `apps/landing`           | The landing page of [karakeep.app](https://karakeep.app) |

## Shared Packages

| Directory         | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `packages/db`     | The database schema and migrations                                           |
| `packages/trpc`   | Where most of the business logic lies built as TRPC routes                   |
| `packages/shared` | Some shared code between the different apps (e.g. loggers, configs, assetdb) |

## Toolings

| Directory            | Description             |
| -------------------- | ----------------------- |
| `tooling/typescript` | The shared tsconfigs    |
| `tooling/eslint`     | ESlint configs          |
| `tooling/prettier`   | Prettier configs        |
| `tooling/tailwind`   | Shared tailwind configs |


==================================================
File: docs/docs/08-development/03-database.md
==================================================
# Database Migrations

- The database schema lives in `packages/db/schema.ts`.
- Changing the schema, requires a migration.
- You can generate the migration by running `pnpm run db:generate --name description_of_schema_change` in the root dir.
- You can then apply the migration by running `pnpm run db:migrate`.

## Drizzle Studio

You can start the drizzle studio by running `pnpm run db:studio` in the root of the repo.


==================================================
File: docs/docs/08-development/04-architecture.md
==================================================
# Architecture

![Architecture Diagram](/img/architecture/arch.png)

- Webapp: NextJS based using sqlite for data storage.
- Workers: Consume the jobs from sqlite based job queue and executes them, there are three job types:
  1. Crawling: Fetches the content of links using a headless chrome browser running in the workers container.
  2. OpenAI: Uses OpenAI APIs to infer the tags of the content.
  3. Indexing: Indexes the content in meilisearch for faster retrieval during search.


==================================================
File: docs/versioned_docs/version-v0.27.0/01-intro.md
==================================================
---
slug: /
---

# Introduction

Karakeep (previously Hoarder) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

![Screenshot](https://raw.githubusercontent.com/karakeep-app/karakeep/main/screenshots/homepage.png)


## Features

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 🔎 Full text search of all the content stored.
- ✨ AI-based (aka chatgpt) automatic tagging and summarization. With supports for local models using ollama!
- 🤖 Rule-based engine for customized management.
- 🎆 OCR for extracting text from images.
- 🔖 [Chrome plugin](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje) and [Firefox addon](https://addons.mozilla.org/en-US/firefox/addon/karakeep/) for quick bookmarking.
- 📱 An [iOS app](https://apps.apple.com/us/app/karakeep-app/id6479258022), and an [Android app](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).
- 📰 Auto hoarding from RSS feeds.
- 🔌 REST API and multiple clients.
- 🌐 Multi-language support.
- 🖍️ Mark and store highlights from your hoarded content.
- 🗄️ Full page archival (using [monolith](https://github.com/Y2Z/monolith)) to protect against link rot.
- ▶️ Auto video archiving using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- ☑️ Bulk actions support.
- 🔐 SSO support.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
- 🔄 Automatic sync with browser bookmarks via [floccus](https://floccus.org/).
- [Planned] Offline reading on mobile, semantic search across bookmarks, ...

**⚠️ This app is under heavy development.**


## Demo

You can access the demo at [https://try.karakeep.app](https://try.karakeep.app). Login with the following creds:

```
email: demo@karakeep.app
password: demodemo
```

The demo is seeded with some content, but it's in read-only mode to prevent abuse.

## About the name

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).


==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/01-docker.md
==================================================
# Docker Compose [Recommended]

### Requirements

- Docker
- Docker Compose

### 1. Create a new directory

Create a new directory to host the compose file and env variables.

This is where you’ll place the `docker-compose.yml` file from the next step and the environment variables.

For example you could make a new directory called "karakeep-app" with the following command:
```
mkdir karakeep-app
```


### 2. Download the compose file

Download the docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml) directly into your new directory.

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/docker/docker-compose.yml
```

### 3. Populate the environment variables

To configure the app, create a `.env` file in the directory and add this minimal env file:

```
KARAKEEP_VERSION=release
NEXTAUTH_SECRET=super_random_string
MEILI_MASTER_KEY=another_random_string
NEXTAUTH_URL=http://localhost:3000
```

You **should** change the random strings. You can use `openssl rand -base64 36` in a seperate terminal window to generate the random strings. You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

Persistent storage and the wiring between the different services is already taken care of in the docker compose file.

Keep in mind that every time you change the `.env` file, you'll need to re-run `docker compose up`.

If you want more config params, check the config documentation [here](/configuration).

### 4. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the env file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](/openai).

<details>
    <summary>If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose.

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `llama3.1`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.
    - You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be.

</details>

### 5. Start the service

Start the service by running:

```
docker compose up -d
```

Then visit `http://localhost:3000` and you should be greeted with the Sign In page.

### [Optional] 6. Enable optional features

Check the [configuration docs](/configuration) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.

### [Optional] 7. Setup quick sharing extensions

Go to the [quick sharing page](/quick-sharing) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Updating Karakeep will depend on what you used for the `KARAKEEP_VERSION` env variable.

- If you pinned the app to a specific version, bump the version and re-run `docker compose up -d`. This should pull the new version for you.
- If you used `KARAKEEP_VERSION=release`, you'll need to force docker to pull the latest version by running `docker compose up --pull always -d`.

Note that if you want to upgrade/migrate `Meilisearch` versions, refer to the [troubleshooting](/troubleshooting) page.


==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/02-unraid.md
==================================================
# Unraid

## Docker Compose Manager Plugin (Recommended)

You can use [Docker Compose Manager](https://forums.unraid.net/topic/114415-plugin-docker-compose-manager/) plugin to deploy Karakeep using the official docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml). After creating the stack, you'll need to setup some env variables similar to that from the docker compose installation docs [here](/installation/docker#3-populate-the-environment-variables).

## Community Apps

:::info
The community application template is maintained by the community.
:::

Karakeep can be installed on Unraid using the community application plugins. Karakeep is a multi-container service, and because unraid doesn't natively support that, you'll have to install the different pieces as separate applications and wire them manually together.

Here's a high level overview of the services you'll need:

- **Karakeep** ([Support post](https://forums.unraid.net/topic/165108-support-collectathon-karakeep/)): Karakeep's main web app.
- **Browserless** ([Support post](https://forums.unraid.net/topic/130163-support-template-masterwishxbrowserless/)): The chrome headless service used for fetching the content. Karakeep's official docker compose doesn't use browserless, but it's currently the only headless chrome service available on unraid, so you'll have to use it.
- **MeiliSearch** ([Support post](https://forums.unraid.net/topic/164847-support-collectathon-meilisearch/)): The search engine used by Karakeep. It's optional but highly recommended. If you don't have it set up, search will be disabled.


==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/03-archlinux.md
==================================================
# Arch Linux

## Installation

> [Karakeep on AUR](https://aur.archlinux.org/packages/karakeep) is not maintained by the karakeep official.

1. Install karakeep

    ```shell
    paru -S karakeep
    ```

2. (**Optional**) Install optional dependencies

    ```shell
    # karakeep-cli: karakeep cli tool
    paru -S karakeep-cli

    # ollama: for automatic tagging
    sudo pacman -S ollama

    # yt-dlp: for download video
    sudo pacman -S yt-dlp
    ```

    You can use Open-AI instead of `ollama`. If you use `ollama`, you need to download the ollama model. Please refer to: [https://ollama.com/library](https://ollama.com/library).

3. Set up

    Environment variables can be set in `/etc/karakeep/karakeep.env` according to [configuration page](/configuration). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

4. Enable service

    ```shell
    sudo systemctl enable --now karakeep.target
    ```

    Then visit `http://localhost:3000` and you should be greated with the sign in page.

## Services and Ports

`karakeep.target` include 3 services: `karakeep-web.service`, `karakeep-works.service`, `karakeep-browser.service`.

- `karakeep-web.service`: Provide karakeep webui service, uses `3000` port by default.

- `karakeep-workers.service`: Provide karakeep workers service, no port.

- `karakeep-browser.service`: Provide browser headless service, uses `9222` port by default.

Now `karakeep` depends on `meilisearch`, and `karakeep-workers.service` wants `meilisearch.service`, starting `karakeep.target` will start `meilisearch.service` at the same time.

## How to Migrate from Hoarder to Karakeep

The PKGBUILD has been fully updated to replace all references to `hoarder` with `karakeep`. If you want to preserve your existing `hoarder` data during the upgrade, please follow the steps below:

**1. Stop the old services**

```shell
sudo systemctl stop hoarder-web.service hoarder-worker.service hoarder-browser.service
sudo systemctl disable --now hoarder.target
```

**2. Uninstall Hoarder**  
After uninstalling, you can manually remove the old `hoarder` user and group if needed.
```shell
paru -R hoarder
```

**3. Rename the old data directory**
```shell
sudo mv /var/lib/hoarder /var/lib/karakeep
```

**4. Install Karakeep**
```shell
paru -S karakeep
```

**5. Fix ownership of the data directory**
```shell
sudo chown -R karakeep:karakeep /var/lib/karakeep
```

**6. Set Karakeep**  
Edit `/etc/karakeep/karakeep.env` according to [configuration page](/configuration). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

Or you can copy old hoarder env file to karakeep:
```shell
sudo cp -f /etc/hoarder/hoarder.env /etc/karakeep/karakeep.env
```

**7. Start Karakeep**
```shell
sudo systemctl enable --now karakeep.target
```


==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/04-kubernetes.md
==================================================
# Kubernetes

### Requirements

- A kubernetes cluster
- kubectl
- kustomize

### 1. Get the deployment manifests

You can clone the repository and copy the `/kubernetes` directory into another directory of your choice.

### 2. Populate the environment variables and secrets

To configure the app, copy the `.env_sample` to `.env` and change to your specific needs.

You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

To see all available configuration options check the [documentation](https://docs.karakeep.app/configuration).

To configure the neccessary secrets for the application copy the `.secrets_sample` file to `.secrets` and change the sample secrets to your generated secrets.

> Note: You **should** change the random strings. You can use `openssl rand -base64 36` to generate the random strings. 

### 3. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](/openai).

<details>
    <summary>[EXPERIMENTAL] If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose. Running local models is a recent addition and not as battle tested as using openai, so proceed with care (and potentially expect a bunch of inference failures).

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `mistral`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.


</details>

### 4. Deploy the service

Deploy the service by running:

```
make deploy
```

### 5. Access the service

#### via LoadBalancer IP

By default, these manifests expose the application as a LoadBalancer Service. You can run `kubectl get services` to identify the IP of the loadbalancer for your service.

Then visit `http://<loadbalancer-ip>:3000` and you should be greated with the Sign In page.

> Note: Depending on your setup you might want to expose the service via an Ingress, or have a different means to access it.

#### Via Ingress

If you want to use an ingress, you can customize the sample ingress in the kubernetes folder and change the host to the DNS name of your choice.

After that you have to configure the web service to the type ClusterIP so it is only reachable via the ingress.

If you have already deployed the service you can patch the web service to the type ClusterIP with the following command:

` kubectl -n karakeep patch service web -p '{"spec":{"type":"ClusterIP"}}' `

Afterwards you can apply the ingress and access the service via your chosen URL.

#### Setting up HTTPS access to the Service

To access karakeep securely you can configure the ingress to use a preconfigured TLS certificate. This requires that you already have the needed files, namely your .crt and .key file, on hand.

After you have deployed the karakeep manifests you can deploy your certificate for karakeep in the `karakeep` namespace with this example command. You can name the secret however you want. But be aware that the secret name in the ingress definition has to match the secret name.

` $ kubectl --namespace karakeep create secret tls karakeep-web-tls --cert=/path/to/crt --key=/path/to/key `

If the secret is successfully created you can now configure the Ingress to use TLS via this changes to the spec:

```` yaml
 spec:
  tls:
  - hosts:
      - karakeep.example.com
    secretName: karakeep-web-tls
````

> Note: Be aware that the hosts have to match between the tls spec and the HTTP spec.

### [Optional] 6. Setup quick sharing extensions

Go to the [quick sharing page](/quick-sharing) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Edit the `KARAKEEP_VERSION` variable in the `kustomization.yaml` file and run `make clean deploy`.

If you have chosen `release` as the image tag you can also destroy the web pod, since the deployment has an ImagePullPolicy set to always the pod always pulls the image from the registry, this way we can ensure that the newest release image is pulled.


==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/05-pikapods.md
==================================================
# PikaPods [Paid Hosting]

:::info
Note: PikaPods shares some of its revenue from hosting Karakeep with the maintainer of this project.
:::

[PikaPods](https://www.pikapods.com/) offers managed paid hosting for many open source apps, including Karakeep.
Server administration, updates, migrations and backups are all taken care of, which makes it well suited
for less technical users. As of Nov 2024, running Karakeep there will cost you ~$3 per month.

### Requirements

- A _PikaPods_ account. Can be created for free [here](https://www.pikapods.com/register). You get an initial welcome credit of $5.

### 1. Choose app

Choose _Karakeep_ from their [list of apps](https://www.pikapods.com/apps) or use this [direct link](https://www.pikapods.com/pods?run=hoarder). This will either
open a new dialog to add a new _Karakeep_ pod or ask you to log in.

### 2. Add settings

There are a few settings to configure in the dialog:

- **Basics**: Give the pod a name and choose a region that's near you.
- **Env Vars**: Here you can disable signups or set an OpenAI API key. All settings are optional.
- **Resources**: The resources your _Karakeep_ pod can use. The defaults are fine, unless you have a very large collection.

### 3. Start pod and add user

After hitting _Add pod_ it will take about a minute for the app to fully start. After this you can visit
the pod's URL and add an initial user under _Sign Up_. After this you may want to disable further sign-ups
by setting the pod's `DISABLE_SIGNUPS` _Env Var_ to `true`.


==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/06-debuntu.md
==================================================
# Debian 12/Ubuntu 24.04

:::warning
This script is a stripped-down version of those found in the [Proxmox Community Scripts](https://github.com/community-scripts/ProxmoxVE) repo. It has been adapted to work on baremetal Debian 12 or Ubuntu 24.04 installs **only**. Any other use is not supported and you use this script at your own risk.
:::

### Requirements

- **Debian 12** (Buster) or
- **Ubuntu 24.04** (Noble Numbat)

The script will download and install all dependencies (except for Ollama), install Karakeep, do a basic configuration of Karakeep and Meilisearch (the search app used by Karakeep), and create and enable the systemd service files needed to run Karakeep on startup. Karakeep and Meilisearch are run in the context of their low-privilege user environments for more security.

The script functions as an update script in addition to an installer. See **[Updating](#updating)**.

### 1. Download the script from the [Karakeep repository](https://github.com/karakeep-app/karakeep/blob/main/karakeep-linux.sh)

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/karakeep-linux.sh
```

### 2. Run the script

> This script must be run as `root`, or as a user with `sudo` privileges.

    If this is a fresh install, then run the installer by using the following command:

    ```shell
    bash karakeep-linux.sh install
    ```

### 3. Create an account/sign in

    Then visit `http://localhost:3000` and you should be greated with the Sign In page.

## Updating

> This script must be run as `root`, or as a user with `sudo` privileges.

    If Karakeep has previously been installed using this script, then run the updater like so:

    ```shell
     bash karakeep-linux.sh update
    ```

## Services and Ports

`karakeep.target` includes 4 services: `meilisearch.service`, `karakeep-web.service`, `karakeep-workers.service`, `karakeep-browser.service`.

- `meilisearch.service`: Provides full-text search, Karakeep Workers service connects to it, uses port `7700` by default.

- `karakeep-web.service`: Provides the karakeep web service, uses `3000` port by default.

- `karakeep-workers.service`: Provides the karakeep workers service, no port.

- `karakeep-browser.service`: Provides the headless browser service, uses `9222` port by default.

## Configuration, ENV file, database locations

During installation, the script created a configuration file for `meilisearch`, an `ENV` file for Karakeep, and located config paths and database paths separate from the installation path of Karakeep, so as to allow for easier updating. Their names/locations are as follows:

- `/etc/meilisearch.toml` - a basic configuration for meilisearch, that contains configs for the database location, disabling analytics, and using a master key, which prevents unauthorized connections.
- `/var/lib/meilisearch` - Meilisearch DB location.
- `/etc/karakeep/karakeep.env` - The Karakeep `ENV` file. Edit this file to configure Karakeep beyond the default. The web service and the workers service need to be restarted after editing this file:

    ```shell
    sudo systemctl restart karakeep-workers karakeep-web
    ```

- `/var/lib/karakeep` - The Karakeep database location. If you delete the contents of this folder you will lose all your data.

## Still Running Hoarder?

There is a way to upgrade. Please see [Guides > Hoarder to Karakeep Migration](https://docs.karakeep.app/Guides/hoarder-to-karakeep-migration)


==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/07-minimal-install.md
==================================================
# Minimal Installation

:::warning
Unless necessary, prefer the [full installation](/installation/docker) to leverage all the features of Karakeep. You'll be sacrificing a lot of functionality if you go with the minimal installation route.
:::

Karakeep's default installation has a dependency on Meilisearch for the full text search, Chrome for crawling and OpenAI/Ollama for AI tagging. You can however run Karakeep without those dependencies if you're willing to sacrifice those features.

- If you run without meilisearch, the search functionality will be completely disabled.
- If you run without chrome, crawling will still work, but you'll lose ability to take screenshots of websites and websites with javascript content won't get crawled correctly.
- If you don't setup OpenAI/Ollama, AI tagging will be disabled.

Those features are important for leveraging Karakeep's full potential, but if you're running in constrained environments, you can use the following minimal docker compose to skip all those dependencies:

```yaml
services:
  web:
    image: ghcr.io/karakeep-app/karakeep:release
    restart: unless-stopped
    volumes:
      - data:/data
    ports:
      - 3000:3000
    environment:
      DATA_DIR: /data
      NEXTAUTH_SECRET: super_random_string
volumes:
  data:
```

Or just with the following docker command:

```base
docker run -d \
  --restart unless-stopped \
  -v data:/data \
  -p 3000:3000 \
  -e DATA_DIR=/data \
  -e NEXTAUTH_SECRET=super_random_string \
  ghcr.io/karakeep-app/karakeep:release
```

:::warning
You **MUST** change the `super_random_string` to a true random string which you can generate with `openssl rand -hex 32`.
:::

Check the [configuration docs](/configuration) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.




==================================================
File: docs/versioned_docs/version-v0.27.0/02-installation/08-truenas.md
==================================================
# TrueNAS

Karakeep is available directly from TrueNAS's app catalog ([link](https://apps.truenas.com/catalog/karakeep/)).


==================================================
File: docs/versioned_docs/version-v0.27.0/03-configuration.md
==================================================
# Configuration

The app is mainly configured by environment variables. All the used environment variables are listed in [packages/shared/config.ts](https://github.com/karakeep-app/karakeep/blob/main/packages/shared/config.ts). The most important ones are:

| Name                            | Required                              | Default         | Description                                                                                                                                                                                                                                                            |
| ------------------------------- | ------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PORT                            | No                                    | 3000            | The port on which the web server will listen. DON'T CHANGE THIS IF YOU'RE USING DOCKER, instead changed the docker bound external port.                                                                                                                                |
| WORKERS_PORT                    | No                                    | 0 (Random Port) | The port on which the worker will export its prometheus metrics on `/metrics`. By default it's a random unused port. If you want to utilize those metrics, fix the port to a value (and export it in docker if you're using docker).                                   |
| WORKERS_ENABLED_WORKERS         | No                                    | Not set         | Comma separated list of worker names to enable. If set, only these workers will run. Valid values: crawler,inference,search,tidyAssets,video,feed,assetPreprocessing,webhook,ruleEngine.                                                                               |
| WORKERS_DISABLED_WORKERS        | No                                    | Not set         | Comma separated list of worker names to disable. Takes precedence over `WORKERS_ENABLED_WORKERS`.                                                                                                                                                                      |
| DATA_DIR                        | Yes                                   | Not set         | The path for the persistent data directory. This is where the db lives. Assets are stored here by default unless `ASSETS_DIR` is set.                                                                                                                                  |
| ASSETS_DIR                      | No                                    | Not set         | The path where crawled assets will be stored. If not set, defaults to `${DATA_DIR}/assets`.                                                                                                                                                                            |
| NEXTAUTH_URL                    | Yes                                   | Not set         | Should point to the address of your server. The app will function without it, but will redirect you to wrong addresses on signout for example.                                                                                                                         |
| NEXTAUTH_SECRET                 | Yes                                   | Not set         | Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`.                                                                                                                                                                                |
| MEILI_ADDR                      | No                                    | Not set         | The address of meilisearch. If not set, Search will be disabled. E.g. (`http://meilisearch:7700`)                                                                                                                                                                      |
| MEILI_MASTER_KEY                | Only in Prod and if search is enabled | Not set         | The master key configured for meilisearch. Not needed in development environment. Generate one with `openssl rand -base64 36 \| tr -dc 'A-Za-z0-9'`                                                                                                                    |
| MAX_ASSET_SIZE_MB               | No                                    | 50              | Sets the maximum allowed asset size (in MB) to be uploaded                                                                                                                                                                                                             |
| DISABLE_NEW_RELEASE_CHECK       | No                                    | false           | If set to true, latest release check will be disabled in the admin panel.                                                                                                                                                                                              |
| PROMETHEUS_AUTH_TOKEN           | No                                    | Random          | Enable a prometheus metrics endpoint at `/api/metrics`. This endpoint will require this token being passed in the Authorization header as a Bearer token. If not set, a new random token is generated everytime at startup.                                            |
| RATE_LIMITING_ENABLED           | No                                    | false           | If set to true, API rate limiting will be enabled.                                                                                                                                                                                                                     |
| DB_WAL_MODE                     | No                                    | false           | Enables WAL mode for the sqlite database. This should improve the performance of the database. There's no reason why you shouldn't set this to true unless you're running the db on a network attached drive. This will become the default at some time in the future. |
| SEARCH_NUM_WORKERS              | No                                    | 1               | Number of concurrent workers for search indexing tasks. Increase this if you have a high volume of content being indexed for search.                                                                                                                                   |
| WEBHOOK_NUM_WORKERS             | No                                    | 1               | Number of concurrent workers for webhook delivery. Increase this if you have multiple webhook endpoints or high webhook traffic.                                                                                                                                       |
| ASSET_PREPROCESSING_NUM_WORKERS | No                                    | 1               | Number of concurrent workers for asset preprocessing tasks (image processing, OCR, etc.). Increase this if you have many images or documents that need processing.                                                                                                     |
| RULE_ENGINE_NUM_WORKERS         | No                                    | 1               | Number of concurrent workers for rule engine processing. Increase this if you have complex automation rules that need to be processed quickly.                                                                                                                         |

## Asset Storage

Karakeep supports two storage backends for assets: local filesystem (default) and S3-compatible object storage. S3 storage is automatically detected when an S3 endpoint is passed.

| Name                             | Required          | Default | Description                                                                                               |
| -------------------------------- | ----------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| ASSET_STORE_S3_ENDPOINT          | No                | Not set | The S3 endpoint URL. Required for S3-compatible services like MinIO. **Setting this enables S3 storage**. |
| ASSET_STORE_S3_REGION            | No                | Not set | The S3 region to use.                                                                                     |
| ASSET_STORE_S3_BUCKET            | Yes when using S3 | Not set | The S3 bucket name where assets will be stored.                                                           |
| ASSET_STORE_S3_ACCESS_KEY_ID     | Yes when using S3 | Not set | The S3 access key ID for authentication.                                                                  |
| ASSET_STORE_S3_SECRET_ACCESS_KEY | Yes when using S3 | Not set | The S3 secret access key for authentication.                                                              |
| ASSET_STORE_S3_FORCE_PATH_STYLE  | No                | false   | Whether to force path-style URLs for S3 requests. Set to true for MinIO and other S3-compatible services. |

:::info
When using S3 storage, make sure the bucket exists and the provided credentials have the necessary permissions to read, write, and delete objects in the bucket.
:::

:::warning
Switching between storage backends after data has been stored will require manual migration of existing assets. Plan your storage backend choice carefully before deploying.
:::

## Authentication / Signup

By default, Karakeep uses the database to store users, but it is possible to also use OAuth.
The flags need to be provided to the `web` container.

:::info
Only OIDC compliant OAuth providers are supported! For information on how to set it up, consult the documentation of your provider.
:::

:::info
When setting up OAuth, the allowed redirect URLs configured at the provider should be set to `<KARAKEEP_ADDRESS>/api/auth/callback/custom` where `<KARAKEEP_ADDRESS>` is the address you configured in `NEXTAUTH_URL` (for example: `https://try.karakeep.app/api/auth/callback/custom`).
:::

| Name                                        | Required | Default                | Description                                                                                                                                                                                           |
| ------------------------------------------- | -------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DISABLE_SIGNUPS                             | No       | false                  | If enabled, no new signups will be allowed and the signup button will be disabled in the UI                                                                                                           |
| DISABLE_PASSWORD_AUTH                       | No       | false                  | If enabled, only signups and logins using OAuth are allowed and the signup button and login form for local accounts will be disabled in the UI                                                        |
| EMAIL_VERIFICATION_REQUIRED                 | No       | false                  | Whether email verification is required during user signup. If enabled, users must verify their email address before they can use their account. If you enable this, you must configure SMTP settings. |
| OAUTH_WELLKNOWN_URL                         | No       | Not set                | The "wellknown Url" for openid-configuration as provided by the OAuth provider                                                                                                                        |
| OAUTH_CLIENT_SECRET                         | No       | Not set                | The "Client Secret" as provided by the OAuth provider                                                                                                                                                 |
| OAUTH_CLIENT_ID                             | No       | Not set                | The "Client ID" as provided by the OAuth provider                                                                                                                                                     |
| OAUTH_SCOPE                                 | No       | "openid email profile" | "Full list of scopes to request (space delimited)"                                                                                                                                                    |
| OAUTH_PROVIDER_NAME                         | No       | "Custom Provider"      | The name of your provider. Will be shown on the signup page as "Sign in with `<name>`"                                                                                                                |
| OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING | No       | false                  | Whether existing accounts in karakeep stored in the database should automatically be linked with your OAuth account. Only enable it if you trust the OAuth provider!                                  |
| OAUTH_TIMEOUT                               | No       | 3500                   | The wait time in milliseconds for the OAuth provider response. Increase this if you are having `outgoing request timed out` errors                                                                    |

For more information on `OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING`, check the [next-auth.js documentation](https://next-auth.js.org/configuration/providers/oauth#allowdangerousemailaccountlinking-option).

## Inference Configs (For automatic tagging)

Either `OPENAI_API_KEY` or `OLLAMA_BASE_URL` need to be set for automatic tagging to be enabled. Otherwise, automatic tagging will be skipped.

:::warning

- The quality of the tags you'll get will depend on the quality of the model you choose.
- You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be (money-wise on OpenAI and resource-wise on ollama).
  :::

| Name                                 | Required | Default                | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAI_API_KEY                       | No       | Not set                | The OpenAI key used for automatic tagging. More on that in [here](/openai).                                                                                                                                                                                                                                                                                                           |
| OPENAI_BASE_URL                      | No       | Not set                | If you just want to use OpenAI you don't need to pass this variable. If, however, you want to use some other openai compatible API (e.g. azure openai service), set this to the url of the API.                                                                                                                                                                                       |
| OLLAMA_BASE_URL                      | No       | Not set                | If you want to use ollama for local inference, set the address of ollama API here.                                                                                                                                                                                                                                                                                                    |
| OLLAMA_KEEP_ALIVE                    | No       | Not set                | Controls how long the model will stay loaded into memory following the request (example value: "5m").                                                                                                                                                                                                                                                                                 |
| INFERENCE_TEXT_MODEL                 | No       | gpt-4.1-mini           | The model to use for text inference. You'll need to change this to some other model if you're using ollama.                                                                                                                                                                                                                                                                           |
| INFERENCE_IMAGE_MODEL                | No       | gpt-4o-mini            | The model to use for image inference. You'll need to change this to some other model if you're using ollama and that model needs to support vision APIs (e.g. llava).                                                                                                                                                                                                                 |
| EMBEDDING_TEXT_MODEL                 | No       | text-embedding-3-small | The model to be used for generating embeddings for the text.                                                                                                                                                                                                                                                                                                                          |
| INFERENCE_CONTEXT_LENGTH             | No       | 2048                   | The max number of tokens that we'll pass to the inference model. If your content is larger than this size, it'll be truncated to fit. The larger this value, the more of the content will be used in tag inference, but the more expensive the inference will be (money-wise on openAI and resource-wise on ollama). Check the model you're using for its max supported content size. |
| INFERENCE_MAX_OUTPUT_TOKENS          | No       | 2048                   | The maximum number of tokens that the inference model is allowed to generate in its response. This controls the length of AI-generated content like tags and summaries. Increase this if you need longer responses, but be aware that higher values will increase costs (for OpenAI) and processing time.                                                                             |
| INFERENCE_LANG                       | No       | english                | The language in which the tags will be generated.                                                                                                                                                                                                                                                                                                                                     |
| INFERENCE_NUM_WORKERS                | No       | 1                      | Number of concurrent workers for AI inference tasks (tagging and summarization). Increase this if you have multiple AI inference requests and want to process them in parallel.                                                                                                                                                                                                       |
| INFERENCE_ENABLE_AUTO_TAGGING        | No       | true                   | Whether automatic AI tagging is enabled or disabled.                                                                                                                                                                                                                                                                                                                                  |
| INFERENCE_ENABLE_AUTO_SUMMARIZATION  | No       | false                  | Whether automatic AI summarization is enabled or disabled.                                                                                                                                                                                                                                                                                                                            |
| INFERENCE_JOB_TIMEOUT_SEC            | No       | 30                     | How long to wait for the inference job to finish before timing out. If you're running ollama without powerful GPUs, you might want to increase the timeout a bit.                                                                                                                                                                                                                     |
| INFERENCE_FETCH_TIMEOUT_SEC          | No       | 300                    | \[Ollama Only\] The timeout of the fetch request to the ollama server. If your inference requests take longer than the default 5mins, you might want to increase this timeout.                                                                                                                                                                                                        |
| INFERENCE_SUPPORTS_STRUCTURED_OUTPUT | No       | Not set                | \[DEPRECATED\] Whether the inference model supports structured output or not. Use INFERENCE_OUTPUT_SCHEMA instead. Setting this to true translates to INFERENCE_OUTPUT_SCHEMA=structured, and to false translates to INFERENCE_OUTPUT_SCHEMA=plain.                                                                                                                                   |
| INFERENCE_OUTPUT_SCHEMA              | No       | structured             | Possible values are "structured", "json", "plain". Structured is the preferred option, but if your model doesn't support it, you can use "json" if your model supports JSON mode, otherwise "plain" which should be supported by all the models but the model might not output the data in the correct format.                                                                        |

:::info

- You can append additional instructions to the prompt used for automatic tagging, in the `AI Settings` (in the `User Settings` screen)
- You can use the placeholders `$tags`, `$aiTags`, `$userTags` in the prompt. These placeholders will be replaced with all tags, ai generated tags or human created tags when automatic tagging is performed (e.g. `[karakeep, computer, ai]`)
  :::

## Crawler Configs

| Name                               | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_NUM_WORKERS                | No       | 1       | Number of allowed concurrent crawling jobs. By default, we're only doing one crawling request at a time to avoid consuming a lot of resources.                                                                                                                                                                                                                                |
| BROWSER_WEB_URL                    | No       | Not set | The browser's http debugging address. The worker will talk to this endpoint to resolve the debugging console's websocket address. If you already have the websocket address, use `BROWSER_WEBSOCKET_URL` instead. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution. |
| BROWSER_WEBSOCKET_URL              | No       | Not set | The websocket address of browser's debugging console. If you want to use [browserless](https://browserless.io), use their websocket address here. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution.                                                                 |
| BROWSER_CONNECT_ONDEMAND           | No       | false   | If set to false, the crawler will proactively connect to the browser instance and always maintain an active connection. If set to true, the browser will be launched on demand only whenever a crawling is requested. Set to true if you're using a service that provides you with browser instances on demand.                                                               |
| CRAWLER_DOWNLOAD_BANNER_IMAGE      | No       | true    | Whether to cache the banner image used in the cards locally or fetch it each time directly from the website. Caching it consumes more storage space, but is more resilient against link rot and rate limits from websites.                                                                                                                                                    |
| CRAWLER_STORE_SCREENSHOT           | No       | true    | Whether to store a screenshot from the crawled website or not. Screenshots act as a fallback for when we fail to extract an image from a website. You can also view the stored screenshots for any link.                                                                                                                                                                      |
| CRAWLER_FULL_PAGE_SCREENSHOT       | No       | false   | Whether to store a screenshot of the full page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, the screenshot will only include the visible part of the page                                                                                                                                                                              |
| CRAWLER_SCREENSHOT_TIMEOUT_SEC     | No       | 5       | How long to wait for the screenshot finish before timing out. If you are capturing full-page screenshots of long webpages, consider increasing this value.                                                                                                                                                                                                                    |
| CRAWLER_FULL_PAGE_ARCHIVE          | No       | false   | Whether to store a full local copy of the page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, only the readable text of the page is archived.                                                                                                                                                                                            |
| CRAWLER_JOB_TIMEOUT_SEC            | No       | 60      | How long to wait for the crawler job to finish before timing out. If you have a slow internet connection or a low powered device, you might want to bump this up a bit                                                                                                                                                                                                        |
| CRAWLER_NAVIGATE_TIMEOUT_SEC       | No       | 30      | How long to spend navigating to the page (along with its redirects). Increase this if you have a slow internet connection                                                                                                                                                                                                                                                     |
| CRAWLER_VIDEO_DOWNLOAD             | No       | false   | Whether to download videos from the page or not (using yt-dlp)                                                                                                                                                                                                                                                                                                                |
| CRAWLER_VIDEO_DOWNLOAD_MAX_SIZE    | No       | 50      | The maximum file size for the downloaded video. The quality will be chosen accordingly. Use -1 to disable the limit.                                                                                                                                                                                                                                                          |
| CRAWLER_VIDEO_DOWNLOAD_TIMEOUT_SEC | No       | 600     | How long to wait for the video download to finish                                                                                                                                                                                                                                                                                                                             |
| CRAWLER_ENABLE_ADBLOCKER           | No       | true    | Whether to enable an adblocker in the crawler or not. If you're facing troubles downloading the adblocking lists on worker startup, you can disable this.                                                                                                                                                                                                                     |
| CRAWLER_YTDLP_ARGS                 | No       | []      | Include additional yt-dlp arguments to be passed at crawl time separated by %%: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#general-options                                                                                                                                                                                                                           |
| BROWSER_COOKIE_PATH                | No       | Not set | Path to a JSON file containing cookies to be loaded into the browser context. The file should be an array of cookie objects, each with name and value (required), and optional fields like domain, path, expires, httpOnly, secure, and sameSite (e.g., `[{"name": "session", "value": "xxx", "domain": ".example.com"}`]).                                                   |

<details>

  <summary>More info on BROWSER_COOKIE_PATH</summary>

BROWSER_COOKIE_PATH specifies the path to a JSON file containing cookies to be loaded into the browser context for crawling.

The JSON file must be an array of cookie objects, each with:
- name: The cookie name (required).
- value: The cookie value (required).
- Optional fields: domain, path, expires, httpOnly, secure, sameSite (values: "Strict", "Lax", or "None").

Example JSON file:

```json
[
  {
    "name": "session",
    "value": "xxx",
    "domain": ".example.com",
    "path": "/",
    "expires": 1735689600,
    "httpOnly": true,
    "secure": true,
    "sameSite": "Lax"
  }
]
```

</details>

## OCR Configs

Karakeep uses [tesseract.js](https://github.com/naptha/tesseract.js) to extract text from images.

| Name                     | Required | Default   | Description                                                                                                                                                                                                                               |
| ------------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OCR_CACHE_DIR            | No       | $TEMP_DIR | The dir where tesseract will download its models. By default, those models are not persisted and stored in the OS' temp dir.                                                                                                              |
| OCR_LANGS                | No       | eng       | Comma separated list of the language codes that you want tesseract to support. You can find the language codes [here](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html). Set to empty string to disable OCR. |
| OCR_CONFIDENCE_THRESHOLD | No       | 50        | A number between 0 and 100 indicating the minimum acceptable confidence from tessaract. If tessaract's confidence is lower than this value, extracted text won't be stored.                                                               |

## Webhook Configs

You can use webhooks to trigger actions when bookmarks are created, changed or crawled.

| Name                | Required | Default | Description                                       |
| ------------------- | -------- | ------- | ------------------------------------------------- |
| WEBHOOK_TIMEOUT_SEC | No       | 5       | The timeout for the webhook request in seconds.   |
| WEBHOOK_RETRY_TIMES | No       | 3       | The number of times to retry the webhook request. |

:::info

- The WEBHOOK_TOKEN is used for authentication. It will appear in the Authorization header as Bearer token.
  ```
  Authorization: Bearer <WEBHOOK_TOKEN>
  ```
- The webhook will be triggered with the job id (used for idempotence), bookmark id, bookmark type, the user id, the url and the operation in JSON format in the body.

  ```json
  {
    "jobId": "123",
    "type": "link",
    "bookmarkId": "exampleBookmarkId",
    "userId": "exampleUserId",
    "url": "https://example.com",
    "operation": "crawled"
  }
  ```

  :::

## SMTP Configuration

Karakeep can send emails for various purposes such as email verification during signup. Configure these settings to enable email functionality.

| Name          | Required | Default | Description                                                                                     |
| ------------- | -------- | ------- | ----------------------------------------------------------------------------------------------- |
| SMTP_HOST     | No       | Not set | The SMTP server hostname or IP address. Required if you want to enable email functionality.     |
| SMTP_PORT     | No       | 587     | The SMTP server port. Common values are 587 (STARTTLS), 465 (SSL/TLS), or 25 (unencrypted).     |
| SMTP_SECURE   | No       | false   | Whether to use SSL/TLS encryption. Set to true for port 465, false for port 587 with STARTTLS.  |
| SMTP_USER     | No       | Not set | The username for SMTP authentication. Usually your email address.                               |
| SMTP_PASSWORD | No       | Not set | The password for SMTP authentication. For services like Gmail, use an app-specific password.    |
| SMTP_FROM     | No       | Not set | The "from" email address that will appear in sent emails. This should be a valid email address. |

## Proxy Configuration

If your Karakeep instance needs to connect through a proxy server, you can configure the following settings:

| Name                | Required | Default | Description                                                                                             |
| ------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------- |
| CRAWLER_HTTP_PROXY  | No       | Not set | HTTP proxy server URL for outgoing HTTP requests (e.g., `http://proxy.example.com:8080`)                |
| CRAWLER_HTTPS_PROXY | No       | Not set | HTTPS proxy server URL for outgoing HTTPS requests (e.g., `http://proxy.example.com:8080`)              |
| CRAWLER_NO_PROXY    | No       | Not set | Comma-separated list of hostnames/IPs that should bypass the proxy (e.g., `localhost,127.0.0.1,.local`) |

:::info
These proxy settings will be used by the crawler and other components that make outgoing HTTP requests.
:::


==================================================
File: docs/versioned_docs/version-v0.27.0/04-screenshots.md
==================================================
# Screenshots

## Homepage

![Homepage](/img/screenshots/homepage.png)

## Homepage (Dark Mode)

![Homepage](/img/screenshots/homepage-dark.png)

## Tags

![All Tags](/img/screenshots/all-tags.png)

## Lists

![All Lists](/img/screenshots/all-lists.png)

## Bookmark Preview

![Bookmark Preview](/img/screenshots/bookmark-preview.png)

## Settings

![Settings](/img/screenshots/settings.png)

## Admin Panel

![Ammin](/img/screenshots/admin.png)


## iOS Sharing

<img src="/img/screenshots/share-sheet.png" width="400px"  />


==================================================
File: docs/versioned_docs/version-v0.27.0/05-quick-sharing.md
==================================================
# Quick Sharing Extensions

The whole point of Karakeep is making it easy to hoard the content. That's why there are a couple of 

## Mobile Apps

<img src="/img/quick-sharing/mobile.png" alt="mobile screenshot" width="300"/>


- **iOS app**: [App Store Link](https://apps.apple.com/us/app/karakeep-app/id6479258022).
- **Android App**: [Play Store link](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).

## Browser Extensions

<img src="/img/quick-sharing/extension.png" alt="mobile screenshot" width="300"/>

- **Chrome extension**: [here](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje).
- **Firefox addon**: [here](https://addons.mozilla.org/en-US/firefox/addon/karakeep/).

- ## Community Extensions
- **Safari extension**: [App Store Link](https://apps.apple.com/us/app/karakeeper-bookmarker/id6746722790).  For macOS and iOS to allow a simple way to add your bookmarks to your self hosted karakeep instance.


==================================================
File: docs/versioned_docs/version-v0.27.0/06-openai.md
==================================================
# OpenAI Costs

This service uses OpenAI for automatic tagging. This means that you'll incur some costs if automatic tagging is enabled. There are two type of inferences that we do:

## Text Tagging

For text tagging, we use the `gpt-4.1-mini` model. This model is [extremely cheap](https://openai.com/api/pricing). Cost per inference varies depending on the content size per article. Though, roughly, You'll be able to generate tags for almost 3000+ bookmarks for less than $1.

## Image Tagging

For image uploads, we use the `gpt-4o-mini` model for extracting tags from the image. You can learn more about the costs of using this model [here](https://platform.openai.com/docs/guides/images?api-mode=chat#calculating-costs). To lower the costs, we're using the low resolution mode (fixed number of tokens regardless of image size). You'll be able to run inference for 1000+ images for less than a $1.


==================================================
File: docs/versioned_docs/version-v0.27.0/07-development/01-setup.md
==================================================
# Setup

## Quick Start

For the fastest way to get started with development, use the one-command setup script:

```bash
./start-dev.sh
```

This script will automatically:
- Start Meilisearch in Docker (on port 7700)
- Start headless Chrome in Docker (on port 9222) 
- Install dependencies with `pnpm install` if needed
- Start both the web app and workers in parallel
- Provide cleanup when you stop with Ctrl+C

**Prerequisites:**
- Docker installed and running
- pnpm installed (see manual setup below for installation instructions)

The script will output the running services:
- Web app: http://localhost:3000
- Meilisearch: http://localhost:7700  
- Chrome debugger: http://localhost:9222

Press Ctrl+C to stop all services and clean up Docker containers.

## Manual Setup

Karakeep uses `node` version 22. To install it, you can use `nvm` [^1]

```
$ nvm install  22
```

Verify node version using this command:
```
$ node --version
v22.14.0
```

Karakeep also makes use of `corepack`[^2]. If you have `node` installed, then `corepack` should already be
installed on your machine, and you don't need to do anything. To verify the `corepack` is installed run:

```
$ command -v corepack
/home/<user>/.nvm/versions/node/v22.14.0/bin/corepack
```

To enable `corepack` run the following command:

```
$ corepack enable
```

Then, from the root of the repository, install the packages and dependencies using:

```
$ pnpm install
```

Output of a successful `pnpm install` run should look something like:

```
Scope: all 20 workspace projects
Lockfile is up to date, resolution step is skipped
Packages: +3129
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 0, reused 2699, downloaded 0, added 3129, done

devDependencies:
+ @karakeep/prettier-config 0.1.0 <- tooling/prettier

. prepare$ husky
└─ Done in 45ms
Done in 5.5s
```

You can now continue with the rest of this documentation.

### First Setup

- You'll need to prepare the environment variables for the dev env.
- Easiest would be to set it up once in the root of the repo and then symlink it in each app directory (e.g. `/apps/web`, `/apps/workers`) and also `/packages/db`.
- Start by copying the template by `cp .env.sample .env`.
- The most important env variables to set are:
  - `DATA_DIR`: Where the database and assets will be stored. This is the only required env variable. You can use an absolute path so that all apps point to the same dir.
  - `NEXTAUTH_SECRET`: Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`. Logging in will not work if this is missing!
  - `MEILI_ADDR`: If not set, search will be disabled. You can set it to `http://127.0.0.1:7700` if you run meilisearch using the command below.
  - `OPENAI_API_KEY`: If you want to enable auto tag inference in the dev env.
- run `pnpm run db:migrate` in the root of the repo to set up the database.

### Dependencies

#### Meilisearch

Meilisearch is the provider for the full text search (and at some point embeddings search too). You can get it running with `docker run -p 7700:7700 getmeili/meilisearch:v1.13.3`.

Mount persistent volume if you want to keep index data across restarts. You can trigger a re-index for the entire items collection in the admin panel in the web app.

#### Chrome

The worker app will automatically start headless chrome on startup for crawling pages. You don't need to do anything there.

### Web App

- Run `pnpm web` in the root of the repo.
- Go to `http://localhost:3000`.

> NOTE: The web app kinda works without any dependencies. However, search won't work unless meilisearch is running. Also, new items added won't get crawled/indexed unless workers are running.

### Workers

- Run `pnpm workers` in the root of the repo.

### Mobile App (iOS & Android)

#### Prerequisites

To build and run the mobile app locally, you'll need:

- **For iOS development**: 
  - macOS computer
  - Xcode installed from the App Store
  - iOS Simulator (comes with Xcode)

- **For Android development**:
  - Android Studio installed
  - Android SDK configured
  - Android Emulator or physical device

For detailed setup instructions, refer to the [Expo documentation](https://docs.expo.dev/guides/local-app-development/).

#### Running the app

- `cd apps/mobile`
- `pnpm exec expo prebuild --no-install` to build the app.

**For iOS:**
- `pnpm exec expo run:ios`
- The app will be installed and started in the simulator.

**Troubleshooting iOS Setup:**
If you encounter an error like `xcrun: error: SDK "iphoneos" cannot be located`, you may need to set the correct Xcode developer directory:
```bash
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

**For Android:**
- Start the Android emulator or connect a physical device.
- `pnpm exec expo run:android`
- The app will be installed and started on the emulator/device.

Changing the code will hot reload the app. However, installing new packages requires restarting the expo server.

### Browser Extension

- `cd apps/browser-extension`
- `pnpm dev`
- This will generate a `dist` package
- Go to extension settings in chrome and enable developer mode.
- Press `Load unpacked` and point it to the `dist` directory.
- The plugin will pop up in the plugin list.

In dev mode, opening and closing the plugin menu should reload the code.


## Docker Dev Env

If the manual setup is too much hassle for you. You can use a docker based dev environment by running `docker compose -f docker/docker-compose.dev.yml up` in the root of the repo. This setup wasn't super reliable for me though.


[^1]: [nvm](https://github.com/nvm-sh/nvm) is a node version manager. You can install it following [these
instructions](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

[^2]: [corepack](https://nodejs.org/api/corepack.html) is an experimental tool to help with managing versions of your
package managers.


==================================================
File: docs/versioned_docs/version-v0.27.0/07-development/02-directories.md
==================================================
# Directory Structure

## Apps

| Directory                | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| `apps/web`               | The main web app                                       |
| `apps/workers`           | The background workers logic                           |
| `apps/mobile`            | The react native based mobile app                      |
| `apps/browser-extension` | The browser extension                                  |
| `apps/landing`           | The landing page of [karakeep.app](https://karakeep.app) |

## Shared Packages

| Directory         | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `packages/db`     | The database schema and migrations                                           |
| `packages/trpc`   | Where most of the business logic lies built as TRPC routes                   |
| `packages/shared` | Some shared code between the different apps (e.g. loggers, configs, assetdb) |

## Toolings

| Directory            | Description             |
| -------------------- | ----------------------- |
| `tooling/typescript` | The shared tsconfigs    |
| `tooling/eslint`     | ESlint configs          |
| `tooling/prettier`   | Prettier configs        |
| `tooling/tailwind`   | Shared tailwind configs |


==================================================
File: docs/versioned_docs/version-v0.27.0/07-development/03-database.md
==================================================
# Database Migrations

- The database schema lives in `packages/db/schema.ts`.
- Changing the schema, requires a migration.
- You can generate the migration by running `pnpm run db:generate --name description_of_schema_change` in the root dir.
- You can then apply the migration by running `pnpm run db:migrate`.

## Drizzle Studio

You can start the drizzle studio by running `pnpm run db:studio` in the root of the repo.


==================================================
File: docs/versioned_docs/version-v0.27.0/07-development/04-architecture.md
==================================================
# Architecture

![Architecture Diagram](/img/architecture/arch.png)

- Webapp: NextJS based using sqlite for data storage.
- Workers: Consume the jobs from sqlite based job queue and executes them, there are three job types:
  1. Crawling: Fetches the content of links using a headless chrome browser running in the workers container.
  2. OpenAI: Uses OpenAI APIs to infer the tags of the content.
  3. Indexing: Indexes the content in meilisearch for faster retrieval during search.


==================================================
File: docs/versioned_docs/version-v0.27.0/08-security-considerations.md
==================================================
# Security Considerations

If you're going to give app access to untrusted users, there's some security considerations that you'll need to be aware of given how the crawler works. The crawler is basically running a browser to fetch the content of the bookmarks. Any untrusted user can submit bookmarks to be crawled from your server and they'll be able to see the crawling result. This can be abused in multiple ways:

1. Untrusted users can submit crawl requests to websites that you don't want to be coming out of your IPs.
2. Crawling user controlled websites can expose your origin IP (and location) even if your service is hosted behind cloudflare for example.
3. The crawling requests will be coming out from your own network, which untrusted users can leverage to crawl internal non-internet exposed endpoints.

To mitigate those risks, you can do one of the following:

1. Limit access to trusted users
2. Let the browser traffic go through some VPN with restricted network policies.
3. Host the browser container outside of your network.
4. Use a hosted browser as a service (e.g. [browserless](https://browserless.io)). Note: I've never used them before.


==================================================
File: docs/versioned_docs/version-v0.27.0/09-command-line.md
==================================================
# Command Line Tool (CLI)

Karakeep comes with a simple CLI for those users who want to do more advanced manipulation.

## Features

- Manipulate bookmarks, lists and tags
- Mass import/export of bookmarks

## Installation (NPM)

```
npm install -g @karakeep/cli
```


## Installation (Docker)

```
docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help
```

## Usage

```
karakeep
```

```
Usage: karakeep [options] [command]

A CLI interface to interact with the karakeep api

Options:
  --api-key <key>       the API key to interact with the API (env: KARAKEEP_API_KEY)
  --server-addr <addr>  the address of the server to connect to (env: KARAKEEP_SERVER_ADDR)
  -V, --version         output the version number
  -h, --help            display help for command

Commands:
  bookmarks             manipulating bookmarks
  lists                 manipulating lists
  tags                  manipulating tags
  whoami                returns info about the owner of this API key
  help [command]        display help for command
```

And some of the subcommands:

```
karakeep bookmarks
```

```
Usage: karakeep bookmarks [options] [command]

Manipulating bookmarks

Options:
  -h, --help             display help for command

Commands:
  add [options]          creates a new bookmark
  get <id>               fetch information about a bookmark
  update [options] <id>  updates bookmark
  list [options]         list all bookmarks
  delete <id>            delete a bookmark
  help [command]         display help for command

```

```
karakeep lists
```

```
Usage: karakeep lists [options] [command]

Manipulating lists

Options:
  -h, --help                 display help for command

Commands:
  list                       lists all lists
  delete <id>                deletes a list
  add-bookmark [options]     add a bookmark to list
  remove-bookmark [options]  remove a bookmark from list
  help [command]             display help for command
```

## Obtaining an API Key

To use the CLI, you'll need to get an API key from your karakeep settings. You can validate that it's working by running:

```
karakeep --api-key <key> --server-addr <addr> whoami
```

For example:

```
karakeep --api-key mysupersecretkey --server-addr https://try.karakeep.app whoami
{
  id: 'j29gnbzxxd01q74j2lu88tnb',
  name: 'Test User',
  email: 'test@gmail.com'
}
```


## Other clients

There also exists a **non-official**, community-maintained, python package called [karakeep-python-api](https://github.com/thiswillbeyourgithub/karakeep_python_api) that can be accessed from the CLI, but is **not** official.


==================================================
File: docs/versioned_docs/version-v0.27.0/09-mcp.md
==================================================
# Model Context Protocol Server (MCP)

Karakeep comes with a Model Context Protocol server that can be used to interact with it through LLMs.

## Supported Tools

- Searching bookmarks
- Adding and removing bookmarks from lists
- Attaching and detaching tags to bookmarks
- Creating new lists
- Creating text and URL bookmarks


## Usage with Claude Desktop

From NPM:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "npx",
      "args": [
        "@karakeep/mcp"
      ],
      "env": {
        "KARAKEEP_API_ADDR": "https://<YOUR_SERVER_ADDR>",
        "KARAKEEP_API_KEY": "<YOUR_TOKEN>"
      }
    }
  }
}
```

From Docker:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "docker",
      "args": [
        "run",
        "-e",
        "KARAKEEP_API_ADDR=https://<YOUR_SERVER_ADDR>",
        "-e",
        "KARAKEEP_API_KEY=<YOUR_TOKEN>",
        "ghcr.io/karakeep-app/karakeep-mcp:latest"
      ]
    }
  }
}
```


### Demo

#### Search
![mcp-1](/img/mcp-1.gif)

#### Adding Text Bookmarks
![mcp-2](/img/mcp-2.gif)

#### Adding URL Bookmarks
![mcp-2](/img/mcp-3.gif)


==================================================
File: docs/versioned_docs/version-v0.27.0/10-import.md
==================================================
# Importing Bookmarks


Karakeep supports importing bookmarks using the Netscape HTML Format, Pocket's new CSV format & Omnivore's JSONs. Titles, tags and addition date will be preserved during the import. An automatically created list will contain all the imported bookmarks.

:::info
All the URLs in the bookmarks file will be added automatically, you will not be able to pick and choose which bookmarks to import!
:::

## Import from Chrome

- Open Chrome and go to `chrome://bookmarks`
- Click on the three dots on the top right corner and choose `Export bookmarks`
- This will download an html file with all of your bookmarks.
- To import the bookmark file, go to the settings and click "Import Bookmarks from HTML file".

## Import from Firefox
- Open Firefox and click on the menu button (☰) in the top right corner.
- Navigate to Bookmarks > Manage bookmarks (or press Ctrl + Shift + O / Cmd + Shift + O to open the Bookmarks Library).
- In the Bookmarks Library, click the Import and Backup button at the top. Select Export Bookmarks to HTML... to save your bookmarks as an HTML file.
- To import a bookmark file, go back to the Import and Backup menu, then select Import Bookmarks from HTML... and choose your saved HTML file.

## Import from Pocket

- Go to the [Pocket export page](https://getpocket.com/export) and follow the instructions to export your bookmarks.
- Pocket after a couple of minutes will mail you a zip file with all the bookmarks.
- Unzip the file and you'll get a CSV file.
- To import the bookmark file, go to the settings and click "Import Bookmarks from Pocket export".

## Import from Omnivore

- Follow Omnivore's [documentation](https://docs.omnivore.app/using/exporting.html) to export your bookmarks.
- This will give you a zip file with all your data.
- The zip file contains a lot of JSONs in the format `metadata_*.json`. You can either import every JSON file manually, or merge the JSONs into a single JSON file and import that.
- To  merge the JSONs into a single JSON file, you can use the following command in the unzipped directory: `jq -r '.[]' metadata_*.json | jq -s > omnivore.json` and then import the `omnivore.json` file. You'll need to have the [jq](https://github.com/jqlang/jq) tool installed.

## Import using the CLI

:::warning
Importing bookmarks using the CLI requires some technical knowledge and might not be very straightforward for non-technical users. Don't hesitate to ask questions in github discussions or discord though.
:::

If you can get your bookmarks in a text file with one link per line, you can use the following command to import them using the [karakeep cli](https://docs.karakeep.app/command-line):

```
while IFS= read -r url; do
    karakeep --api-key "<KEY>" --server-addr "<SERVER_ADDR>" bookmarks add --link "$url"
done < all_links.txt
```


==================================================
File: docs/versioned_docs/version-v0.27.0/11-FAQ.md
==================================================
# Frequently Asked Questions (FAQ)

## User Management

### Lost password

#### If you are not an administrator

Administrators can reset the password of any user. Contact an administrator to reset the password for you.

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to reset the password
- Enter a new password and press `Reset`
- The new password is now set
- If required, you can change your password again (so the admin does not know your password) in the `User Settings`

#### If you are an administrator

If you are an administrator and lost your password, you have to reset the password in the database.

To reset the password:

- Acquire some kind of tools that helps you to connect to the database:
  - `sqlite3` on Linux: run `apt-get install sqlite3` (depending on your package manager)
  - e.g. `dbeaver` on Windows
- Shut down Karakeep
- Connect to the `db.db` database, which is located in the `data` directory you have mounted to your docker container:
  - by e.g. running `sqlite3 db.db` (in your `data` directory)
  - or going through e.g. the `dbeaver` UI to locate the file in the data directory and connecting to it
- Update the password in the database by running:
  - `update user set password='$2a$10$5u40XUq/cD/TmLdCOyZ82ePENE6hpkbodJhsp7.e/BgZssUO5DDTa', salt='' where email='<YOUR_EMAIL_HERE>';`
  - (don't forget to put your email address into the command)
- The new password for your user is now `adminadmin`.
- Start Karakeep again
- Log in with your email address and the password `adminadmin` and change the password to whatever you want in the `User Settings`

### Adding another administrator

By default, the first user to sign up gets promoted to administrator automatically.

In case you want to grant those permissions to another user:

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to change the Role
- Change the Role to `Admin`
- Press `Change`
- The new administrator has to log out and log in again to get the new role assigned

### Adding new users, when signups are disabled

Administrators can create new accounts any time:

- Navigate to the `Admin Settings` page
- Go to the `Users List`
- Press the `Create User` Button.
- Enter the information for the user
- Press `create`
- The new user can now log in


==================================================
File: docs/versioned_docs/version-v0.27.0/12-troubleshooting.md
==================================================
# Troubleshooting

## SqliteError: no such table: user

This usually means that there's something wrong with the database setup (more concretely, it means that the database is not initialized). This can be caused by multiple problems:
1. **Wiped DATA_DIR:** Your `DATA_DIR` got wiped (or the backing storage dir changed). If you did this intentionally, restart the container so that it can re-initalize the database.
2. **Missing DATA_DIR**: You're not using the default docker compose file, and you forgot to configure the `DATA_DIR` env var. This will result into the database getting set up in a different directory than the one used by the service.

## Chrome Failed to Read DnsConfig

If you see this error in the logs of the chrome container, it's a benign error and you can safely ignore it. Whatever problems you're having, is unrelated to this error.

## AI Tagging not working (when using OpenAI)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OPENAI_API_KEY` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring open ai.
3. OpenAI requires pre-charging the account with credits before using it, otherwise you'll get an error like "insufficient funds".

## AI Tagging not working (when using Ollama)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OLLAMA_BASE_URL` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring ollama.
3. You didn't change the `INFERENCE_TEXT_MODEL` env variable, resulting into karakeep attempting to use gpt models with ollama which won't work.
4. Ollama server is not reachable by the karakeep container. This can be caused by:
    1. Ollama server being in a different docker network than the karakeep container.
    2. You're using `localhost` as the `OLLAMA_BASE_URL` instead of the actual address of the ollama server. `localhost` points to the container itself, not the docker host. Check this [stackoverflow answer](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) to find how to correctly point to the docker host address instead.

## Crawling not working

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. You changed the name of the chrome container but didn't change the `BROWSER_WEB_URL` env variable.

## Upgrading Meilisearch - Migrating the Meilisearch db version

[Meilisearch](https://www.meilisearch.com/) is the database used by karakeep for searching in your bookmarks. The version used by karakeep is `1.13.3` and it is advised not to upgrade it without good reasons. If you do, you might see errors like `Your database version (1.11.1) is incompatible with your current engine version (1.13.3). To migrate data between Meilisearch versions, please follow our guide on https://www.meilisearch.com/docs/learn/update_and_migration/updating.`.

Luckily we can easily workaround this:
1. Stop the Meilisearch container.
2. Inside the Meilisearch volume bound to `/meili_data`, erase/rename the folder called `data.ms`.
3. Launch Meilisearch again.
4. Login to karakeep as administrator and go to (as of v0.24.1) `Admin Settings > Background Jobs` then click on `Reindex All Bookmarks`.
5. When the reindexing has finished, Meilisearch should be working as usual.

If you run into issues, the official documentation can be found [there](https://www.meilisearch.com/docs/learn/update_and_migration/updating).


==================================================
File: docs/versioned_docs/version-v0.27.0/13-community-projects.md
==================================================
# Community Projects

This page lists community projects that are built around Karakeep, but not officially supported by the development team.

:::warning
This list comes with no guarantees about security, performance, reliability, or accuracy. Use at your own risk.
:::

### Raycast Extension

_By [@luolei](https://github.com/foru17)._

A user-friendly Raycast extension that seamlessly integrates with Karakeep, bringing powerful bookmark management to your fingertips. Quickly save, search, and organize your bookmarks, texts, and images—all through Raycast's intuitive interface.

Get it [here](https://www.raycast.com/luolei/hoarder).

### Alfred Workflow

_By [@yinan-c](https://github.com/yinan-c)_

An Alfred workflow to quickly hoard stuff or access your hoarded bookmarks!

Get it [here](https://www.alfredforum.com/topic/22528-hoarder-workflow-for-self-hosted-bookmark-management/).

### Obsidian Plugin

_By [@jhofker](https://github.com/jhofker)_

An Obsidian plugin that syncs your Karakeep bookmarks with Obsidian, creating markdown notes for each bookmark in a designated folder.

Get it [here](https://github.com/jhofker/obsidian-hoarder/), or install it directly from Obsidian's community plugin store ([link](https://obsidian.md/plugins?id=hoarder-sync)).

### Telegram Bot

_By [@Madh93](https://github.com/Madh93)_

A Telegram Bot for saving bookmarks to Karakeep directly through Telegram.

Get it [here](https://github.com/Madh93/karakeepbot).

### Hoarder's Pipette

_By [@DanSnow](https://github.com/DanSnow)_

A chrome extension that injects karakeep's bookmarks into your search results.

Get it [here](https://dansnow.github.io/hoarder-pipette/guides/installation/).

### Karakeep-Python-API

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python package to simplify access to the karakeep API. Can be used as a library or from the CLI. Aims for feature completeness and high test coverage but do check its feature matrix before relying too much on it.

Its repository also hosts the [Community Script](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts), for example:

| Community Script | Description | Documentation |
|----------------|-------------|---------------|
| **Karakeep-Time-Tagger** | Automatically adds time-to-read tags (`0-5m`, `5-10m`, etc.) to bookmarks based on content length analysis. Includes systemd service and timer files for automated periodic execution. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-time-tagger) |
| **Karakeep-List-To-Tag** | Converts a Karakeep list into tags by adding a specified tag to all bookmarks within that list. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-list-to-tag) |
| **Omnivore2Karakeep-Highlights** | Imports highlights from Omnivore export data to Karakeep, with intelligent position detection and bookmark matching. Supports dry-run mode for testing. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/omnivore2karakeep-highlights) |


Get it [here](https://github.com/thiswillbeyourgithub/karakeep_python_api).

### FreshRSS_to_Karakeep

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python script to automatically create Karakeep bookmarks from your [FreshRSS](https://github.com/FreshRSS/FreshRSS) *favourites/saved* RSS item. Made to be called periodically. Based on the community project `Karakeep-Python-API` above, by the same author.

Get it [here](https://github.com/thiswillbeyourgithub/freshrss_to_karakeep).


==================================================
File: docs/versioned_docs/version-v0.27.0/14-guides/01-legacy-container-upgrade.md
==================================================
# Legacy Container Upgrade

Karakeep's 0.16 release consolidated the web and worker containers into a single container and also dropped the need for the redis container. The legacy containers will stop being supported soon, to upgrade to the new container do the following:

1. Remove the redis container and its volume if it had one.
2. Move the environment variables that you've set exclusively to the `workers` container to the `web` container.
3. Delete the `workers` container.
4. Rename the web container image from `hoarder-app/hoarder-web` to `hoarder-app/hoarder`.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder-web:${KARAKEEP_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${KARAKEEP_VERSION:-release}
     restart: unless-stopped
     volumes:
       - data:/data
@@ -10,14 +10,10 @@ services:
     env_file:
       - .env
     environment:
-      REDIS_HOST: redis
       MEILI_ADDR: http://meilisearch:7700
+      BROWSER_WEB_URL: http://chrome:9222
+      # OPENAI_API_KEY: ...
       DATA_DIR: /data
-  redis:
-    image: redis:7.2-alpine
-    restart: unless-stopped
-    volumes:
-      - redis:/data
   chrome:
     image: gcr.io/zenika-hub/alpine-chrome:123
     restart: unless-stopped
@@ -37,24 +33,7 @@ services:
       MEILI_NO_ANALYTICS: "true"
     volumes:
       - meilisearch:/meili_data
-  workers:
-    image: ghcr.io/hoarder-app/hoarder-workers:${KARAKEEP_VERSION:-release}
-    restart: unless-stopped
-    volumes:
-      - data:/data
-    env_file:
-      - .env
-    environment:
-      REDIS_HOST: redis
-      MEILI_ADDR: http://meilisearch:7700
-      BROWSER_WEB_URL: http://chrome:9222
-      DATA_DIR: /data
-      # OPENAI_API_KEY: ...
-    depends_on:
-      web:
-        condition: service_started

 volumes:
-  redis:
   meilisearch:
   data:
```


==================================================
File: docs/versioned_docs/version-v0.27.0/14-guides/02-search-query-language.md
==================================================
# Search Query Language

Karakeep provides a search query language to filter and find bookmarks. Here are all the supported qualifiers and how to use them:

## Basic Syntax

- Use spaces to separate multiple conditions (implicit AND)
- Use `and`/`or` keywords for explicit boolean logic
- Prefix qualifiers with `-` to negate them
- Use parentheses `()` for grouping conditions (note that groups can't be negated)

## Qualifiers

Here's a comprehensive table of all supported qualifiers:

| Qualifier                        | Description                                                                                                                                                                                               | Example Usage                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `is:fav`                         | Favorited bookmarks                                                                                                                                                                                       | `is:fav`                                     |
| `is:archived`                    | Archived bookmarks                                                                                                                                                                                        | `-is:archived`                               |
| `is:tagged`                      | Bookmarks that has one or more tags                                                                                                                                                                       | `is:tagged`                                  |
| `is:inlist`                      | Bookmarks that are in one or more lists                                                                                                                                                                   | `is:inlist`                                  |
| `is:link`, `is:text`, `is:media` | Bookmarks that are of type link, text or media                                                                                                                                                            | `is:link`                                    |
| `url:<value>`                    | Match bookmarks with URL substring                                                                                                                                                                        | `url:example.com`                            |
| `#<tag>`                         | Match bookmarks with specific tag                                                                                                                                                                         | `#important`                                 |
|                                  | Supports quoted strings for tags with spaces                                                                                                                                                              | `#"work in progress"`                        |
| `list:<name>`                    | Match bookmarks in specific list                                                                                                                                                                          | `list:reading`                               |
|                                  | Supports quoted strings for list names with spaces                                                                                                                                                        | `list:"to review"`                           |
| `after:<date>`                   | Bookmarks created on or after date (YYYY-MM-DD)                                                                                                                                                           | `after:2023-01-01`                           |
| `before:<date>`                  | Bookmarks created on or before date (YYYY-MM-DD)                                                                                                                                                          | `before:2023-12-31`                          |
| `feed:<name>`                    | Bookmarks imported from a particular rss feed                                                                                                                                                             | `feed:Hackernews`                            |
| `age:<time-range>`               | Match bookmarks based on how long ago they were created. Use `<` or `>` to indicate the maximum / minimum age of the bookmarks. Supported units: `d` (days), `w` (weeks), `m` (months), `y` (years). | `age:<1d` `age:>2w` `age:<6m` `age:>3y` |

### Examples

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not tagged or not in any list
-is:tagged or -is:inlist
```

## Combining Conditions

You can combine multiple conditions using boolean logic:

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not favorited and not archived
-is:fav -is:archived
```

## Text Search

Any text not part of a qualifier will be treated as a full-text search:

```plaintext
# Search for "machine learning" in bookmark content
machine learning

# Combine text search with qualifiers
machine learning is:fav
```


==================================================
File: docs/versioned_docs/version-v0.27.0/14-guides/03-singlefile.md
==================================================
# Using Karakeep with SingleFile Extension

Karakeep supports being a destination for the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile). This has the benefit of allowing you to use the singlefile extension to hoard links as you're seeing them in the browser. This is perfect for websites that don't like to get crawled, has annoying cookie banner or require authentication.

## Setup

1. Install the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile).
2. In the extension settings, select `Destinations`.
3. Select `upload to a REST Form API`.
4. In the URL, insert the address: `https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile`.
5. In the `authorization token` field, paste an API key that you can get from your karakeep settings.
6. Set `data field name` to `file`.
7. Set `URL field name` to `url`.
8. (Optional) Add `&ifexists=MODE` to the URL where MODE is one of `skip`, `overwrite`, `overwrite-recrawl`, `append`, or `append-recrawl`. See "Handling Existing Bookmarks" section below for details.

Now, go to any page and click the singlefile extension icon. Once it's done with the upload, the bookmark should show up in your karakeep instance. Note that the singlefile extension doesn't show any progress on the upload. Given that archives are typically large, it might take 30+ seconds until the upload is done and starts showing up in Karakeep.

## Handling Existing Bookmarks

When uploading a page that already exists in your archive (same URL), you can control the behavior by setting the `ifexists` query parameter in the upload URL. The available modes are:

- `skip` (default): If the bookmark already exists, skip creating a new one
- `overwrite`: Replace existing precrawled archive (only the most recent archive is kept)
- `overwrite-recrawl`: Replace existing archive and queue a recrawl to update content
- `append`: Add new archive version alongside existing ones
- `append-recrawl`: Add new archive and queue a recrawl

To use these modes, append `?ifexists=MODE` to your upload URL, replacing `MODE` with your desired behavior.

For example:  
`https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile?ifexists=overwrite`


## Recommended settings

In the singlefile extension, you probably will want to change the following settings for better experience:
* Stylesheets > compress CSS content: on
* Stylesheets > group duplicate stylesheets together: on
* HTML content > remove frames: on

Also, you most likely will want to change the default `MAX_ASSET_SIZE_MB` in karakeep to something higher, for example `100`.

:::info
Currently, we don't support screenshots for singlefile uploads, but this will change in the future.
:::



==================================================
File: docs/versioned_docs/version-v0.27.0/14-guides/04-hoarder-to-karakeep-migration.md
==================================================
# Hoarder to Karakeep Migration

Hoarder is rebranding to Karakeep. Due to github limitations, the old docker image might not be getting new updates after the rebranding. You might need to update your docker image to point to the new karakeep image instead by applying the following change in the docker compose file.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder:${HOARDER_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${HOARDER_VERSION:-release}
```

You can also change the `HOARDER_VERSION` environment variable but if you do so remember to change it in the `.env` file as well.

## Migrating a Baremetal Installation

If you previously used the [Debian/Ubuntu install script](https://docs.karakeep.app/Installation/debuntu) to install Hoarder, there is an option to migrate your installation to Karakeep.

```bash
bash karakeep-linux.sh migrate
```

This will migrate your installation with no user input required. After the migration, the script will also check for an update.


==================================================
File: docs/versioned_docs/version-v0.27.0/14-guides/05-different-ai-providers.md
==================================================
# Configuring different AI Providers

Karakeep uses LLM providers for AI tagging and summarization. We support OpenAI-compatible providers and ollama. This guide will show you how to configure different providers.

## OpenAI

If you want to use OpenAI itself, you just need to pass in the OPENAI_API_KEY environment variable.

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# You can change the default models by uncommenting the following lines, and choosing your model.
# INFERENCE_TEXT_MODEL=gpt-4.1-mini
# INFERENCE_IMAGE_MODEL=gpt-4o-mini
```

## Ollama

Ollama is a local LLM provider that you can use to run your own LLM server. You'll need to pass ollama's address to karakeep and you need to ensure that it's accessible from within the karakeep container (e.g. no localhost addresses).

```
# MAKE SURE YOU DON'T HAVE OPENAI_API_KEY set, otherwise it takes precedence.

OLLAMA_BASE_URL=http://ollama.mylab.com:11434

# Make sure to pull the models in ollama first. Example models:
INFERENCE_TEXT_MODEL=gemma3
INFERENCE_IMAGE_MODEL=llava

# If the model you're using doesn't support structured output, you also need:
# INFERENCE_OUTPUT_SCHEMA=plain
```

## Gemini

Gemini has an OpenAI-compatible API. You need to get an api key from Google AI Studio.

```

OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=gemini-2.0-flash
INFERENCE_IMAGE_MODEL=gemini-2.0-flash
```

## OpenRouter

```
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=meta-llama/llama-4-scout
INFERENCE_IMAGE_MODEL=meta-llama/llama-4-scout
```

## Perplexity

```
OPENAI_BASE_URL: https://api.perplexity.ai
OPENAI_API_KEY: Your Perplexity API Key
INFERENCE_TEXT_MODEL: sonar-pro
INFERENCE_IMAGE_MODEL: sonar-pro
```


==================================================
File: docs/versioned_docs/version-v0.28.0/01-intro.md
==================================================
---
slug: /
---

# Introduction

Karakeep (previously Hoarder) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

![Screenshot](https://raw.githubusercontent.com/karakeep-app/karakeep/main/screenshots/homepage.png)


## Features

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 🔎 Full text search of all the content stored.
- ✨ AI-based (aka chatgpt) automatic tagging and summarization. With supports for local models using ollama!
- 🤖 Rule-based engine for customized management.
- 🎆 OCR for extracting text from images.
- 🔖 [Chrome plugin](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje) and [Firefox addon](https://addons.mozilla.org/en-US/firefox/addon/karakeep/) for quick bookmarking.
- 📱 An [iOS app](https://apps.apple.com/us/app/karakeep-app/id6479258022), and an [Android app](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).
- 📰 Auto hoarding from RSS feeds.
- 🔌 REST API and multiple clients.
- 🌐 Multi-language support.
- 🖍️ Mark and store highlights from your hoarded content.
- 🗄️ Full page archival (using [monolith](https://github.com/Y2Z/monolith)) to protect against link rot.
- ▶️ Auto video archiving using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- ☑️ Bulk actions support.
- 🔐 SSO support.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
- 🔄 Automatic sync with browser bookmarks via [floccus](https://floccus.org/).
- [Planned] Offline reading on mobile, semantic search across bookmarks, ...

**⚠️ This app is under heavy development.**


## Demo

You can access the demo at [https://try.karakeep.app](https://try.karakeep.app). Login with the following creds:

```
email: demo@karakeep.app
password: demodemo
```

The demo is seeded with some content, but it's in read-only mode to prevent abuse.

## About the name

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).


==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/01-docker.md
==================================================
# Docker Compose [Recommended]

### Requirements

- Docker
- Docker Compose

### 1. Create a new directory

Create a new directory to host the compose file and env variables.

This is where you’ll place the `docker-compose.yml` file from the next step and the environment variables.

For example you could make a new directory called "karakeep-app" with the following command:
```
mkdir karakeep-app
```


### 2. Download the compose file

Download the docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml) directly into your new directory.

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/docker/docker-compose.yml
```

### 3. Populate the environment variables

To configure the app, create a `.env` file in the directory and add this minimal env file:

```
KARAKEEP_VERSION=release
NEXTAUTH_SECRET=super_random_string
MEILI_MASTER_KEY=another_random_string
NEXTAUTH_URL=http://localhost:3000
```

You **should** change the random strings. You can use `openssl rand -base64 36` in a seperate terminal window to generate the random strings. You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

Persistent storage and the wiring between the different services is already taken care of in the docker compose file.

Keep in mind that every time you change the `.env` file, you'll need to re-run `docker compose up`.

If you want more config params, check the config documentation [here](/configuration).

### 4. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the env file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](/openai).

<details>
    <summary>If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose.

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `llama3.1`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.
    - You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be.

</details>

### 5. Start the service

Start the service by running:

```
docker compose up -d
```

Then visit `http://localhost:3000` and you should be greeted with the Sign In page.

### [Optional] 6. Enable optional features

Check the [configuration docs](/configuration) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.

### [Optional] 7. Setup quick sharing extensions

Go to the [quick sharing page](/quick-sharing) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Updating Karakeep will depend on what you used for the `KARAKEEP_VERSION` env variable.

- If you pinned the app to a specific version, bump the version and re-run `docker compose up -d`. This should pull the new version for you.
- If you used `KARAKEEP_VERSION=release`, you'll need to force docker to pull the latest version by running `docker compose up --pull always -d`.

Note that if you want to upgrade/migrate `Meilisearch` versions, refer to the [troubleshooting](/troubleshooting) page.


==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/02-unraid.md
==================================================
# Unraid

## Docker Compose Manager Plugin (Recommended)

You can use [Docker Compose Manager](https://forums.unraid.net/topic/114415-plugin-docker-compose-manager/) plugin to deploy Karakeep using the official docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml). After creating the stack, you'll need to setup some env variables similar to that from the docker compose installation docs [here](/installation/docker#3-populate-the-environment-variables).

## Community Apps

:::info
The community application template is maintained by the community.
:::

Karakeep can be installed on Unraid using the community application plugins. Karakeep is a multi-container service, and because unraid doesn't natively support that, you'll have to install the different pieces as separate applications and wire them manually together.

Here's a high level overview of the services you'll need:

- **Karakeep** ([Support post](https://forums.unraid.net/topic/165108-support-collectathon-karakeep/)): Karakeep's main web app.
- **Browserless** ([Support post](https://forums.unraid.net/topic/130163-support-template-masterwishxbrowserless/)): The chrome headless service used for fetching the content. Karakeep's official docker compose doesn't use browserless, but it's currently the only headless chrome service available on unraid, so you'll have to use it.
- **MeiliSearch** ([Support post](https://forums.unraid.net/topic/164847-support-collectathon-meilisearch/)): The search engine used by Karakeep. It's optional but highly recommended. If you don't have it set up, search will be disabled.


==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/03-archlinux.md
==================================================
# Arch Linux

## Installation

> [Karakeep on AUR](https://aur.archlinux.org/packages/karakeep) is not maintained by the karakeep official.

1. Install karakeep

    ```shell
    paru -S karakeep
    ```

2. (**Optional**) Install optional dependencies

    ```shell
    # karakeep-cli: karakeep cli tool
    paru -S karakeep-cli

    # ollama: for automatic tagging
    sudo pacman -S ollama

    # yt-dlp: for download video
    sudo pacman -S yt-dlp
    ```

    You can use Open-AI instead of `ollama`. If you use `ollama`, you need to download the ollama model. Please refer to: [https://ollama.com/library](https://ollama.com/library).

3. Set up

    Environment variables can be set in `/etc/karakeep/karakeep.env` according to [configuration page](/configuration). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

4. Enable service

    ```shell
    sudo systemctl enable --now karakeep.target
    ```

    Then visit `http://localhost:3000` and you should be greated with the sign in page.

## Services and Ports

`karakeep.target` include 3 services: `karakeep-web.service`, `karakeep-works.service`, `karakeep-browser.service`.

- `karakeep-web.service`: Provide karakeep webui service, uses `3000` port by default.

- `karakeep-workers.service`: Provide karakeep workers service, no port.

- `karakeep-browser.service`: Provide browser headless service, uses `9222` port by default.

Now `karakeep` depends on `meilisearch`, and `karakeep-workers.service` wants `meilisearch.service`, starting `karakeep.target` will start `meilisearch.service` at the same time.

## How to Migrate from Hoarder to Karakeep

The PKGBUILD has been fully updated to replace all references to `hoarder` with `karakeep`. If you want to preserve your existing `hoarder` data during the upgrade, please follow the steps below:

**1. Stop the old services**

```shell
sudo systemctl stop hoarder-web.service hoarder-worker.service hoarder-browser.service
sudo systemctl disable --now hoarder.target
```

**2. Uninstall Hoarder**  
After uninstalling, you can manually remove the old `hoarder` user and group if needed.
```shell
paru -R hoarder
```

**3. Rename the old data directory**
```shell
sudo mv /var/lib/hoarder /var/lib/karakeep
```

**4. Install Karakeep**
```shell
paru -S karakeep
```

**5. Fix ownership of the data directory**
```shell
sudo chown -R karakeep:karakeep /var/lib/karakeep
```

**6. Set Karakeep**  
Edit `/etc/karakeep/karakeep.env` according to [configuration page](/configuration). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

Or you can copy old hoarder env file to karakeep:
```shell
sudo cp -f /etc/hoarder/hoarder.env /etc/karakeep/karakeep.env
```

**7. Start Karakeep**
```shell
sudo systemctl enable --now karakeep.target
```


==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/04-kubernetes.md
==================================================
# Kubernetes

### Requirements

- A kubernetes cluster
- kubectl
- kustomize

### 1. Get the deployment manifests

You can clone the repository and copy the `/kubernetes` directory into another directory of your choice.

### 2. Populate the environment variables and secrets

To configure the app, copy the `.env_sample` to `.env` and change to your specific needs.

You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

To see all available configuration options check the [documentation](https://docs.karakeep.app/configuration).

To configure the neccessary secrets for the application copy the `.secrets_sample` file to `.secrets` and change the sample secrets to your generated secrets.

> Note: You **should** change the random strings. You can use `openssl rand -base64 36` to generate the random strings. 

### 3. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](/openai).

<details>
    <summary>[EXPERIMENTAL] If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose. Running local models is a recent addition and not as battle tested as using openai, so proceed with care (and potentially expect a bunch of inference failures).

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `mistral`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.


</details>

### 4. Deploy the service

Deploy the service by running:

```
make deploy
```

### 5. Access the service

#### via LoadBalancer IP

By default, these manifests expose the application as a LoadBalancer Service. You can run `kubectl get services` to identify the IP of the loadbalancer for your service.

Then visit `http://<loadbalancer-ip>:3000` and you should be greated with the Sign In page.

> Note: Depending on your setup you might want to expose the service via an Ingress, or have a different means to access it.

#### Via Ingress

If you want to use an ingress, you can customize the sample ingress in the kubernetes folder and change the host to the DNS name of your choice.

After that you have to configure the web service to the type ClusterIP so it is only reachable via the ingress.

If you have already deployed the service you can patch the web service to the type ClusterIP with the following command:

` kubectl -n karakeep patch service web -p '{"spec":{"type":"ClusterIP"}}' `

Afterwards you can apply the ingress and access the service via your chosen URL.

#### Setting up HTTPS access to the Service

To access karakeep securely you can configure the ingress to use a preconfigured TLS certificate. This requires that you already have the needed files, namely your .crt and .key file, on hand.

After you have deployed the karakeep manifests you can deploy your certificate for karakeep in the `karakeep` namespace with this example command. You can name the secret however you want. But be aware that the secret name in the ingress definition has to match the secret name.

` $ kubectl --namespace karakeep create secret tls karakeep-web-tls --cert=/path/to/crt --key=/path/to/key `

If the secret is successfully created you can now configure the Ingress to use TLS via this changes to the spec:

```` yaml
 spec:
  tls:
  - hosts:
      - karakeep.example.com
    secretName: karakeep-web-tls
````

> Note: Be aware that the hosts have to match between the tls spec and the HTTP spec.

### [Optional] 6. Setup quick sharing extensions

Go to the [quick sharing page](/quick-sharing) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Edit the `KARAKEEP_VERSION` variable in the `kustomization.yaml` file and run `make clean deploy`.

If you have chosen `release` as the image tag you can also destroy the web pod, since the deployment has an ImagePullPolicy set to always the pod always pulls the image from the registry, this way we can ensure that the newest release image is pulled.


==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/05-pikapods.md
==================================================
# PikaPods [Paid Hosting]

:::info
Note: PikaPods shares some of its revenue from hosting Karakeep with the maintainer of this project.
:::

[PikaPods](https://www.pikapods.com/) offers managed paid hosting for many open source apps, including Karakeep.
Server administration, updates, migrations and backups are all taken care of, which makes it well suited
for less technical users. As of Nov 2024, running Karakeep there will cost you ~$3 per month.

### Requirements

- A _PikaPods_ account. Can be created for free [here](https://www.pikapods.com/register). You get an initial welcome credit of $5.

### 1. Choose app

Choose _Karakeep_ from their [list of apps](https://www.pikapods.com/apps) or use this [direct link](https://www.pikapods.com/pods?run=hoarder). This will either
open a new dialog to add a new _Karakeep_ pod or ask you to log in.

### 2. Add settings

There are a few settings to configure in the dialog:

- **Basics**: Give the pod a name and choose a region that's near you.
- **Env Vars**: Here you can disable signups or set an OpenAI API key. All settings are optional.
- **Resources**: The resources your _Karakeep_ pod can use. The defaults are fine, unless you have a very large collection.

### 3. Start pod and add user

After hitting _Add pod_ it will take about a minute for the app to fully start. After this you can visit
the pod's URL and add an initial user under _Sign Up_. After this you may want to disable further sign-ups
by setting the pod's `DISABLE_SIGNUPS` _Env Var_ to `true`.


==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/06-debuntu.md
==================================================
# Debian 12/Ubuntu 24.04

:::warning
This script is a stripped-down version of those found in the [Proxmox Community Scripts](https://github.com/community-scripts/ProxmoxVE) repo. It has been adapted to work on baremetal Debian 12 or Ubuntu 24.04 installs **only**. Any other use is not supported and you use this script at your own risk.
:::

### Requirements

- **Debian 12** (Buster) or
- **Ubuntu 24.04** (Noble Numbat)

The script will download and install all dependencies (except for Ollama), install Karakeep, do a basic configuration of Karakeep and Meilisearch (the search app used by Karakeep), and create and enable the systemd service files needed to run Karakeep on startup. Karakeep and Meilisearch are run in the context of their low-privilege user environments for more security.

The script functions as an update script in addition to an installer. See **[Updating](#updating)**.

### 1. Download the script from the [Karakeep repository](https://github.com/karakeep-app/karakeep/blob/main/karakeep-linux.sh)

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/karakeep-linux.sh
```

### 2. Run the script

> This script must be run as `root`, or as a user with `sudo` privileges.

    If this is a fresh install, then run the installer by using the following command:

    ```shell
    bash karakeep-linux.sh install
    ```

### 3. Create an account/sign in

    Then visit `http://localhost:3000` and you should be greated with the Sign In page.

## Updating

> This script must be run as `root`, or as a user with `sudo` privileges.

    If Karakeep has previously been installed using this script, then run the updater like so:

    ```shell
     bash karakeep-linux.sh update
    ```

## Services and Ports

`karakeep.target` includes 4 services: `meilisearch.service`, `karakeep-web.service`, `karakeep-workers.service`, `karakeep-browser.service`.

- `meilisearch.service`: Provides full-text search, Karakeep Workers service connects to it, uses port `7700` by default.

- `karakeep-web.service`: Provides the karakeep web service, uses `3000` port by default.

- `karakeep-workers.service`: Provides the karakeep workers service, no port.

- `karakeep-browser.service`: Provides the headless browser service, uses `9222` port by default.

## Configuration, ENV file, database locations

During installation, the script created a configuration file for `meilisearch`, an `ENV` file for Karakeep, and located config paths and database paths separate from the installation path of Karakeep, so as to allow for easier updating. Their names/locations are as follows:

- `/etc/meilisearch.toml` - a basic configuration for meilisearch, that contains configs for the database location, disabling analytics, and using a master key, which prevents unauthorized connections.
- `/var/lib/meilisearch` - Meilisearch DB location.
- `/etc/karakeep/karakeep.env` - The Karakeep `ENV` file. Edit this file to configure Karakeep beyond the default. The web service and the workers service need to be restarted after editing this file:

    ```shell
    sudo systemctl restart karakeep-workers karakeep-web
    ```

- `/var/lib/karakeep` - The Karakeep database location. If you delete the contents of this folder you will lose all your data.

## Still Running Hoarder?

There is a way to upgrade. Please see [Guides > Hoarder to Karakeep Migration](https://docs.karakeep.app/Guides/hoarder-to-karakeep-migration)


==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/07-minimal-install.md
==================================================
# Minimal Installation

:::warning
Unless necessary, prefer the [full installation](/installation/docker) to leverage all the features of Karakeep. You'll be sacrificing a lot of functionality if you go with the minimal installation route.
:::

Karakeep's default installation has a dependency on Meilisearch for the full text search, Chrome for crawling and OpenAI/Ollama for AI tagging. You can however run Karakeep without those dependencies if you're willing to sacrifice those features.

- If you run without meilisearch, the search functionality will be completely disabled.
- If you run without chrome, crawling will still work, but you'll lose ability to take screenshots of websites and websites with javascript content won't get crawled correctly.
- If you don't setup OpenAI/Ollama, AI tagging will be disabled.

Those features are important for leveraging Karakeep's full potential, but if you're running in constrained environments, you can use the following minimal docker compose to skip all those dependencies:

```yaml
services:
  web:
    image: ghcr.io/karakeep-app/karakeep:release
    restart: unless-stopped
    volumes:
      - data:/data
    ports:
      - 3000:3000
    environment:
      DATA_DIR: /data
      NEXTAUTH_SECRET: super_random_string
volumes:
  data:
```

Or just with the following docker command:

```base
docker run -d \
  --restart unless-stopped \
  -v data:/data \
  -p 3000:3000 \
  -e DATA_DIR=/data \
  -e NEXTAUTH_SECRET=super_random_string \
  ghcr.io/karakeep-app/karakeep:release
```

:::warning
You **MUST** change the `super_random_string` to a true random string which you can generate with `openssl rand -hex 32`.
:::

Check the [configuration docs](/configuration) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.




==================================================
File: docs/versioned_docs/version-v0.28.0/02-installation/08-truenas.md
==================================================
# TrueNAS

Karakeep is available directly from TrueNAS's app catalog ([link](https://apps.truenas.com/catalog/karakeep/)).


==================================================
File: docs/versioned_docs/version-v0.28.0/03-configuration.md
==================================================
# Configuration

The app is mainly configured by environment variables. All the used environment variables are listed in [packages/shared/config.ts](https://github.com/karakeep-app/karakeep/blob/main/packages/shared/config.ts). The most important ones are:

| Name                            | Required                              | Default         | Description                                                                                                                                                                                                                                                                                                             |
| ------------------------------- | ------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PORT                            | No                                    | 3000            | The port on which the web server will listen. DON'T CHANGE THIS IF YOU'RE USING DOCKER, instead changed the docker bound external port.                                                                                                                                                                                 |
| WORKERS_PORT                    | No                                    | 0 (Random Port) | The port on which the worker will export its prometheus metrics on `/metrics`. By default it's a random unused port. If you want to utilize those metrics, fix the port to a value (and export it in docker if you're using docker).                                                                                    |
| WORKERS_HOST                    | No                                    | 127.0.0.1       | Host to listen to for requests to WORKERS_PORT. You will need to set this if running in a container, since localhost will not be reachable from outside                                                                                                                                                                 |
| WORKERS_ENABLED_WORKERS         | No                                    | Not set         | Comma separated list of worker names to enable. If set, only these workers will run. Valid values: crawler,inference,search,adminMaintenance,video,feed,assetPreprocessing,webhook,ruleEngine.                                                                                                                          |
| WORKERS_DISABLED_WORKERS        | No                                    | Not set         | Comma separated list of worker names to disable. Takes precedence over `WORKERS_ENABLED_WORKERS`.                                                                                                                                                                                                                       |
| DATA_DIR                        | Yes                                   | Not set         | The path for the persistent data directory. This is where the db lives. Assets are stored here by default unless `ASSETS_DIR` is set.                                                                                                                                                                                   |
| ASSETS_DIR                      | No                                    | Not set         | The path where crawled assets will be stored. If not set, defaults to `${DATA_DIR}/assets`.                                                                                                                                                                                                                             |
| NEXTAUTH_URL                    | Yes                                   | Not set         | Should point to the address of your server. The app will function without it, but will redirect you to wrong addresses on signout for example.                                                                                                                                                                          |
| NEXTAUTH_SECRET                 | Yes                                   | Not set         | Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`.                                                                                                                                                                                                                                 |
| MEILI_ADDR                      | No                                    | Not set         | The address of meilisearch. If not set, Search will be disabled. E.g. (`http://meilisearch:7700`)                                                                                                                                                                                                                       |
| MEILI_MASTER_KEY                | Only in Prod and if search is enabled | Not set         | The master key configured for meilisearch. Not needed in development environment. Generate one with `openssl rand -base64 36 \| tr -dc 'A-Za-z0-9'`                                                                                                                                                                     |
| MAX_ASSET_SIZE_MB               | No                                    | 50              | Sets the maximum allowed asset size (in MB) to be uploaded                                                                                                                                                                                                                                                              |
| DISABLE_NEW_RELEASE_CHECK       | No                                    | false           | If set to true, latest release check will be disabled in the admin panel.                                                                                                                                                                                                                                               |
| PROMETHEUS_AUTH_TOKEN           | No                                    | Random          | Enable a prometheus metrics endpoint at `/api/metrics`. This endpoint will require this token being passed in the Authorization header as a Bearer token. If not set, a new random token is generated everytime at startup. This cannot contain any special characters or you may encounter a 400 Bad Request response. |
| RATE_LIMITING_ENABLED           | No                                    | false           | If set to true, API rate limiting will be enabled.                                                                                                                                                                                                                                                                      |
| DB_WAL_MODE                     | No                                    | false           | Enables WAL mode for the sqlite database. This should improve the performance of the database. There's no reason why you shouldn't set this to true unless you're running the db on a network attached drive. This will become the default at some time in the future.                                                  |
| SEARCH_NUM_WORKERS              | No                                    | 1               | Number of concurrent workers for search indexing tasks. Increase this if you have a high volume of content being indexed for search.                                                                                                    |
| SEARCH_JOB_TIMEOUT_SEC          | No                                    | 30              | How long to wait for a search indexing job to finish before timing out. Increase this if you have large bookmarks with extensive content that takes longer to index.                                                                    |
| WEBHOOK_NUM_WORKERS             | No                                    | 1               | Number of concurrent workers for webhook delivery. Increase this if you have multiple webhook endpoints or high webhook traffic.                                                                                                        |
| ASSET_PREPROCESSING_NUM_WORKERS | No                                    | 1               | Number of concurrent workers for asset preprocessing tasks (image processing, OCR, etc.). Increase this if you have many images or documents that need processing.                                                                                                                                                      |
| RULE_ENGINE_NUM_WORKERS         | No                                    | 1               | Number of concurrent workers for rule engine processing. Increase this if you have complex automation rules that need to be processed quickly.                                                                                                                                                                          |

## Asset Storage

Karakeep supports two storage backends for assets: local filesystem (default) and S3-compatible object storage. S3 storage is automatically detected when an S3 endpoint is passed.

| Name                             | Required          | Default | Description                                                                                               |
| -------------------------------- | ----------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| ASSET_STORE_S3_ENDPOINT          | No                | Not set | The S3 endpoint URL. Required for S3-compatible services like MinIO. **Setting this enables S3 storage**. |
| ASSET_STORE_S3_REGION            | No                | Not set | The S3 region to use.                                                                                     |
| ASSET_STORE_S3_BUCKET            | Yes when using S3 | Not set | The S3 bucket name where assets will be stored.                                                           |
| ASSET_STORE_S3_ACCESS_KEY_ID     | Yes when using S3 | Not set | The S3 access key ID for authentication.                                                                  |
| ASSET_STORE_S3_SECRET_ACCESS_KEY | Yes when using S3 | Not set | The S3 secret access key for authentication.                                                              |
| ASSET_STORE_S3_FORCE_PATH_STYLE  | No                | false   | Whether to force path-style URLs for S3 requests. Set to true for MinIO and other S3-compatible services. |

:::info
When using S3 storage, make sure the bucket exists and the provided credentials have the necessary permissions to read, write, and delete objects in the bucket.
:::

:::warning
Switching between storage backends after data has been stored will require manual migration of existing assets. Plan your storage backend choice carefully before deploying.
:::

## Authentication / Signup

By default, Karakeep uses the database to store users, but it is possible to also use OAuth.
The flags need to be provided to the `web` container.

:::info
Only OIDC compliant OAuth providers are supported! For information on how to set it up, consult the documentation of your provider.
:::

:::info
When setting up OAuth, the allowed redirect URLs configured at the provider should be set to `<KARAKEEP_ADDRESS>/api/auth/callback/custom` where `<KARAKEEP_ADDRESS>` is the address you configured in `NEXTAUTH_URL` (for example: `https://try.karakeep.app/api/auth/callback/custom`).
:::

| Name                                        | Required | Default                | Description                                                                                                                                                                                           |
| ------------------------------------------- | -------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DISABLE_SIGNUPS                             | No       | false                  | If enabled, no new signups will be allowed and the signup button will be disabled in the UI                                                                                                           |
| DISABLE_PASSWORD_AUTH                       | No       | false                  | If enabled, only signups and logins using OAuth are allowed and the signup button and login form for local accounts will be disabled in the UI                                                        |
| EMAIL_VERIFICATION_REQUIRED                 | No       | false                  | Whether email verification is required during user signup. If enabled, users must verify their email address before they can use their account. If you enable this, you must configure SMTP settings. |
| OAUTH_WELLKNOWN_URL                         | No       | Not set                | The "wellknown Url" for openid-configuration as provided by the OAuth provider                                                                                                                        |
| OAUTH_CLIENT_SECRET                         | No       | Not set                | The "Client Secret" as provided by the OAuth provider                                                                                                                                                 |
| OAUTH_CLIENT_ID                             | No       | Not set                | The "Client ID" as provided by the OAuth provider                                                                                                                                                     |
| OAUTH_SCOPE                                 | No       | "openid email profile" | "Full list of scopes to request (space delimited)"                                                                                                                                                    |
| OAUTH_PROVIDER_NAME                         | No       | "Custom Provider"      | The name of your provider. Will be shown on the signup page as "Sign in with `<name>`"                                                                                                                |
| OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING | No       | false                  | Whether existing accounts in karakeep stored in the database should automatically be linked with your OAuth account. Only enable it if you trust the OAuth provider!                                  |
| OAUTH_TIMEOUT                               | No       | 3500                   | The wait time in milliseconds for the OAuth provider response. Increase this if you are having `outgoing request timed out` errors                                                                    |

For more information on `OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING`, check the [next-auth.js documentation](https://next-auth.js.org/configuration/providers/oauth#allowdangerousemailaccountlinking-option).

## Inference Configs (For automatic tagging)

Either `OPENAI_API_KEY` or `OLLAMA_BASE_URL` need to be set for automatic tagging to be enabled. Otherwise, automatic tagging will be skipped.

:::warning

- The quality of the tags you'll get will depend on the quality of the model you choose.
- You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be (money-wise on OpenAI and resource-wise on ollama).
  :::

| Name                                 | Required | Default                | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAI_API_KEY                       | No       | Not set                | The OpenAI key used for automatic tagging. More on that in [here](/openai).                                                                                                                                                                                                                                                                                                           |
| OPENAI_BASE_URL                      | No       | Not set                | If you just want to use OpenAI you don't need to pass this variable. If, however, you want to use some other openai compatible API (e.g. azure openai service), set this to the url of the API.                                                                                                                                                                                       |
| OLLAMA_BASE_URL                      | No       | Not set                | If you want to use ollama for local inference, set the address of ollama API here.                                                                                                                                                                                                                                                                                                    |
| OLLAMA_KEEP_ALIVE                    | No       | Not set                | Controls how long the model will stay loaded into memory following the request (example value: "5m").                                                                                                                                                                                                                                                                                 |
| INFERENCE_TEXT_MODEL                 | No       | gpt-4.1-mini           | The model to use for text inference. You'll need to change this to some other model if you're using ollama.                                                                                                                                                                                                                                                                           |
| INFERENCE_IMAGE_MODEL                | No       | gpt-4o-mini            | The model to use for image inference. You'll need to change this to some other model if you're using ollama and that model needs to support vision APIs (e.g. llava).                                                                                                                                                                                                                 |
| EMBEDDING_TEXT_MODEL                 | No       | text-embedding-3-small | The model to be used for generating embeddings for the text.                                                                                                                                                                                                                                                                                                                          |
| INFERENCE_CONTEXT_LENGTH             | No       | 2048                   | The max number of tokens that we'll pass to the inference model. If your content is larger than this size, it'll be truncated to fit. The larger this value, the more of the content will be used in tag inference, but the more expensive the inference will be (money-wise on openAI and resource-wise on ollama). Check the model you're using for its max supported content size. |
| INFERENCE_MAX_OUTPUT_TOKENS          | No       | 2048                   | The maximum number of tokens that the inference model is allowed to generate in its response. This controls the length of AI-generated content like tags and summaries. Increase this if you need longer responses, but be aware that higher values will increase costs (for OpenAI) and processing time.                                                                             |
| INFERENCE_USE_MAX_COMPLETION_TOKENS  | No       | false                  | \[OpenAI Only\] Whether to use the newer `max_completion_tokens` parameter instead of the deprecated `max_tokens` parameter. Set to `true` if using GPT-5 or o-series models which require this. Will become the default in a future release.                                                                                                                                         |
| INFERENCE_LANG                       | No       | english                | The language in which the tags will be generated.                                                                                                                                                                                                                                                                                                                                     |
| INFERENCE_NUM_WORKERS                | No       | 1                      | Number of concurrent workers for AI inference tasks (tagging and summarization). Increase this if you have multiple AI inference requests and want to process them in parallel.                                                                                                                                                                                                       |
| INFERENCE_ENABLE_AUTO_TAGGING        | No       | true                   | Whether automatic AI tagging is enabled or disabled.                                                                                                                                                                                                                                                                                                                                  |
| INFERENCE_ENABLE_AUTO_SUMMARIZATION  | No       | false                  | Whether automatic AI summarization is enabled or disabled.                                                                                                                                                                                                                                                                                                                            |
| INFERENCE_JOB_TIMEOUT_SEC            | No       | 30                     | How long to wait for the inference job to finish before timing out. If you're running ollama without powerful GPUs, you might want to increase the timeout a bit.                                                                                                                                                                                                                     |
| INFERENCE_FETCH_TIMEOUT_SEC          | No       | 300                    | \[Ollama Only\] The timeout of the fetch request to the ollama server. If your inference requests take longer than the default 5mins, you might want to increase this timeout.                                                                                                                                                                                                        |
| INFERENCE_SUPPORTS_STRUCTURED_OUTPUT | No       | Not set                | \[DEPRECATED\] Whether the inference model supports structured output or not. Use INFERENCE_OUTPUT_SCHEMA instead. Setting this to true translates to INFERENCE_OUTPUT_SCHEMA=structured, and to false translates to INFERENCE_OUTPUT_SCHEMA=plain.                                                                                                                                   |
| INFERENCE_OUTPUT_SCHEMA              | No       | structured             | Possible values are "structured", "json", "plain". Structured is the preferred option, but if your model doesn't support it, you can use "json" if your model supports JSON mode, otherwise "plain" which should be supported by all the models but the model might not output the data in the correct format.                                                                        |

:::info

- You can append additional instructions to the prompt used for automatic tagging, in the `AI Settings` (in the `User Settings` screen)
- You can use the placeholders `$tags`, `$aiTags`, `$userTags` in the prompt. These placeholders will be replaced with all tags, ai generated tags or human created tags when automatic tagging is performed (e.g. `[karakeep, computer, ai]`)
  :::

## Crawler Configs

| Name                                     | Required | Default   | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_NUM_WORKERS                      | No       | 1         | Number of allowed concurrent crawling jobs. By default, we're only doing one crawling request at a time to avoid consuming a lot of resources.                                                                                                                                                                                                                                |
| BROWSER_WEB_URL                          | No       | Not set   | The browser's http debugging address. The worker will talk to this endpoint to resolve the debugging console's websocket address. If you already have the websocket address, use `BROWSER_WEBSOCKET_URL` instead. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution. |
| BROWSER_WEBSOCKET_URL                    | No       | Not set   | The websocket address of browser's debugging console. If you want to use [browserless](https://browserless.io), use their websocket address here. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution.                                                                 |
| BROWSER_CONNECT_ONDEMAND                 | No       | false     | If set to false, the crawler will proactively connect to the browser instance and always maintain an active connection. If set to true, the browser will be launched on demand only whenever a crawling is requested. Set to true if you're using a service that provides you with browser instances on demand.                                                               |
| CRAWLER_DOWNLOAD_BANNER_IMAGE            | No       | true      | Whether to cache the banner image used in the cards locally or fetch it each time directly from the website. Caching it consumes more storage space, but is more resilient against link rot and rate limits from websites.                                                                                                                                                    |
| CRAWLER_STORE_SCREENSHOT                 | No       | true      | Whether to store a screenshot from the crawled website or not. Screenshots act as a fallback for when we fail to extract an image from a website. You can also view the stored screenshots for any link.                                                                                                                                                                      |
| CRAWLER_FULL_PAGE_SCREENSHOT             | No       | false     | Whether to store a screenshot of the full page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, the screenshot will only include the visible part of the page                                                                                                                                                                              |
| CRAWLER_SCREENSHOT_TIMEOUT_SEC           | No       | 5         | How long to wait for the screenshot finish before timing out. If you are capturing full-page screenshots of long webpages, consider increasing this value.                                                                                                                                                                                                                    |
| CRAWLER_FULL_PAGE_ARCHIVE                | No       | false     | Whether to store a full local copy of the page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, only the readable text of the page is archived.                                                                                                                                                                                            |
| CRAWLER_JOB_TIMEOUT_SEC                  | No       | 60        | How long to wait for the crawler job to finish before timing out. If you have a slow internet connection or a low powered device, you might want to bump this up a bit                                                                                                                                                                                                        |
| CRAWLER_NAVIGATE_TIMEOUT_SEC             | No       | 30        | How long to spend navigating to the page (along with its redirects). Increase this if you have a slow internet connection                                                                                                                                                                                                                                                     |
| CRAWLER_VIDEO_DOWNLOAD                   | No       | false     | Whether to download videos from the page or not (using yt-dlp)                                                                                                                                                                                                                                                                                                                |
| CRAWLER_VIDEO_DOWNLOAD_MAX_SIZE          | No       | 50        | The maximum file size for the downloaded video. The quality will be chosen accordingly. Use -1 to disable the limit.                                                                                                                                                                                                                                                          |
| CRAWLER_VIDEO_DOWNLOAD_TIMEOUT_SEC       | No       | 600       | How long to wait for the video download to finish                                                                                                                                                                                                                                                                                                                             |
| CRAWLER_ENABLE_ADBLOCKER                 | No       | true      | Whether to enable an adblocker in the crawler or not. If you're facing troubles downloading the adblocking lists on worker startup, you can disable this.                                                                                                                                                                                                                     |
| CRAWLER_YTDLP_ARGS                       | No       | []        | Include additional yt-dlp arguments to be passed at crawl time separated by %%: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#general-options                                                                                                                                                                                                                           |
| BROWSER_COOKIE_PATH                      | No       | Not set   | Path to a JSON file containing cookies to be loaded into the browser context. The file should be an array of cookie objects, each with name and value (required), and optional fields like domain, path, expires, httpOnly, secure, and sameSite (e.g., `[{"name": "session", "value": "xxx", "domain": ".example.com"}`]).                                                   |
| HTML_CONTENT_SIZE_INLINE_THRESHOLD_BYTES | No       | 5 \* 1024 | The thresholds in bytes after which larger assets will be stored in the assetdb (folder/s3) instead of inline in the database.                                                                                                                                                                                                                                                |

<details>

  <summary>More info on BROWSER_COOKIE_PATH</summary>

BROWSER_COOKIE_PATH specifies the path to a JSON file containing cookies to be loaded into the browser context for crawling.

The JSON file must be an array of cookie objects, each with:

- name: The cookie name (required).
- value: The cookie value (required).
- Optional fields: domain, path, expires, httpOnly, secure, sameSite (values: "Strict", "Lax", or "None").

Example JSON file:

```json
[
  {
    "name": "session",
    "value": "xxx",
    "domain": ".example.com",
    "path": "/",
    "expires": 1735689600,
    "httpOnly": true,
    "secure": true,
    "sameSite": "Lax"
  }
]
```

</details>

## OCR Configs

Karakeep uses [tesseract.js](https://github.com/naptha/tesseract.js) to extract text from images.

| Name                     | Required | Default   | Description                                                                                                                                                                                                                               |
| ------------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OCR_CACHE_DIR            | No       | $TEMP_DIR | The dir where tesseract will download its models. By default, those models are not persisted and stored in the OS' temp dir.                                                                                                              |
| OCR_LANGS                | No       | eng       | Comma separated list of the language codes that you want tesseract to support. You can find the language codes [here](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html). Set to empty string to disable OCR. |
| OCR_CONFIDENCE_THRESHOLD | No       | 50        | A number between 0 and 100 indicating the minimum acceptable confidence from tessaract. If tessaract's confidence is lower than this value, extracted text won't be stored.                                                               |

## Webhook Configs

You can use webhooks to trigger actions when bookmarks are created, changed or crawled.

| Name                | Required | Default | Description                                       |
| ------------------- | -------- | ------- | ------------------------------------------------- |
| WEBHOOK_TIMEOUT_SEC | No       | 5       | The timeout for the webhook request in seconds.   |
| WEBHOOK_RETRY_TIMES | No       | 3       | The number of times to retry the webhook request. |

:::info

- The WEBHOOK_TOKEN is used for authentication. It will appear in the Authorization header as Bearer token.
  ```
  Authorization: Bearer <WEBHOOK_TOKEN>
  ```
- The webhook will be triggered with the job id (used for idempotence), bookmark id, bookmark type, the user id, the url and the operation in JSON format in the body.

  ```json
  {
    "jobId": "123",
    "type": "link",
    "bookmarkId": "exampleBookmarkId",
    "userId": "exampleUserId",
    "url": "https://example.com",
    "operation": "crawled"
  }
  ```

  :::

## SMTP Configuration

Karakeep can send emails for various purposes such as email verification during signup. Configure these settings to enable email functionality.

| Name          | Required | Default | Description                                                                                     |
| ------------- | -------- | ------- | ----------------------------------------------------------------------------------------------- |
| SMTP_HOST     | No       | Not set | The SMTP server hostname or IP address. Required if you want to enable email functionality.     |
| SMTP_PORT     | No       | 587     | The SMTP server port. Common values are 587 (STARTTLS), 465 (SSL/TLS), or 25 (unencrypted).     |
| SMTP_SECURE   | No       | false   | Whether to use SSL/TLS encryption. Set to true for port 465, false for port 587 with STARTTLS.  |
| SMTP_USER     | No       | Not set | The username for SMTP authentication. Usually your email address.                               |
| SMTP_PASSWORD | No       | Not set | The password for SMTP authentication. For services like Gmail, use an app-specific password.    |
| SMTP_FROM     | No       | Not set | The "from" email address that will appear in sent emails. This should be a valid email address. |

## Proxy Configuration

If your Karakeep instance needs to connect through a proxy server, you can configure the following settings:

| Name                               | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_HTTP_PROXY                 | No       | Not set | HTTP proxy server URL for outgoing HTTP requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                       |
| CRAWLER_HTTPS_PROXY                | No       | Not set | HTTPS proxy server URL for outgoing HTTPS requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                     |
| CRAWLER_NO_PROXY                   | No       | Not set | Comma-separated list of hostnames/IPs that should bypass the proxy (e.g., `localhost,127.0.0.1,.local`)                                                                                                                                                                                                                                                                                                                                                                                 |
| CRAWLER_ALLOWED_INTERNAL_HOSTNAMES | No       | Not set | By default, Karakeep blocks worker-initiated requests whose DNS resolves to private, loopback, or link-local IP addresses. Use this to allowlist specific hostnames for internal access (e.g., `internal.company.com,.local`). Supports domain wildcards by prefixing with a dot (e.g., `.internal.company.com`). Note: Internal IP validation is bypassed when a proxy is configured for the URL as the local DNS resolver won't necessarily be the same as the one used by the proxy. |

:::info
These proxy settings will be used by the crawler and other components that make outgoing HTTP requests.
:::


==================================================
File: docs/versioned_docs/version-v0.28.0/04-screenshots.md
==================================================
# Screenshots

## Homepage

![Homepage](/img/screenshots/homepage.png)

## Homepage (Dark Mode)

![Homepage](/img/screenshots/homepage-dark.png)

## Tags

![All Tags](/img/screenshots/all-tags.png)

## Lists

![All Lists](/img/screenshots/all-lists.png)

## Bookmark Preview

![Bookmark Preview](/img/screenshots/bookmark-preview.png)

## Settings

![Settings](/img/screenshots/settings.png)

## Admin Panel

![Ammin](/img/screenshots/admin.png)


## iOS Sharing

<img src="/img/screenshots/share-sheet.png" width="400px"  />


==================================================
File: docs/versioned_docs/version-v0.28.0/05-quick-sharing.md
==================================================
# Quick Sharing Extensions

The whole point of Karakeep is making it easy to hoard the content. That's why there are a couple of 

## Mobile Apps

<img src="/img/quick-sharing/mobile.png" alt="mobile screenshot" width="300"/>


- **iOS app**: [App Store Link](https://apps.apple.com/us/app/karakeep-app/id6479258022).
- **Android App**: [Play Store link](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).

## Browser Extensions

<img src="/img/quick-sharing/extension.png" alt="mobile screenshot" width="300"/>

- **Chrome extension**: [here](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje).
- **Firefox addon**: [here](https://addons.mozilla.org/en-US/firefox/addon/karakeep/).

- ## Community Extensions
- **Safari extension**: [App Store Link](https://apps.apple.com/us/app/karakeeper-bookmarker/id6746722790).  For macOS and iOS to allow a simple way to add your bookmarks to your self hosted karakeep instance.


==================================================
File: docs/versioned_docs/version-v0.28.0/06-openai.md
==================================================
# OpenAI Costs

This service uses OpenAI for automatic tagging. This means that you'll incur some costs if automatic tagging is enabled. There are two type of inferences that we do:

## Text Tagging

For text tagging, we use the `gpt-4.1-mini` model. This model is [extremely cheap](https://openai.com/api/pricing). Cost per inference varies depending on the content size per article. Though, roughly, You'll be able to generate tags for almost 3000+ bookmarks for less than $1.

## Image Tagging

For image uploads, we use the `gpt-4o-mini` model for extracting tags from the image. You can learn more about the costs of using this model [here](https://platform.openai.com/docs/guides/images?api-mode=chat#calculating-costs). To lower the costs, we're using the low resolution mode (fixed number of tokens regardless of image size). You'll be able to run inference for 1000+ images for less than a $1.


==================================================
File: docs/versioned_docs/version-v0.28.0/07-development/01-setup.md
==================================================
# Setup

## Quick Start

For the fastest way to get started with development, use the one-command setup script:

```bash
./start-dev.sh
```

This script will automatically:
- Start Meilisearch in Docker (on port 7700)
- Start headless Chrome in Docker (on port 9222) 
- Install dependencies with `pnpm install` if needed
- Start both the web app and workers in parallel
- Provide cleanup when you stop with Ctrl+C

**Prerequisites:**
- Docker installed and running
- pnpm installed (see manual setup below for installation instructions)

The script will output the running services:
- Web app: http://localhost:3000
- Meilisearch: http://localhost:7700  
- Chrome debugger: http://localhost:9222

Press Ctrl+C to stop all services and clean up Docker containers.

## Manual Setup

Karakeep uses `node` version 22. To install it, you can use `nvm` [^1]

```
$ nvm install  22
```

Verify node version using this command:
```
$ node --version
v22.14.0
```

Karakeep also makes use of `corepack`[^2]. If you have `node` installed, then `corepack` should already be
installed on your machine, and you don't need to do anything. To verify the `corepack` is installed run:

```
$ command -v corepack
/home/<user>/.nvm/versions/node/v22.14.0/bin/corepack
```

To enable `corepack` run the following command:

```
$ corepack enable
```

Then, from the root of the repository, install the packages and dependencies using:

```
$ pnpm install
```

Output of a successful `pnpm install` run should look something like:

```
Scope: all 20 workspace projects
Lockfile is up to date, resolution step is skipped
Packages: +3129
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 0, reused 2699, downloaded 0, added 3129, done

devDependencies:
+ @karakeep/prettier-config 0.1.0 <- tooling/prettier

. prepare$ husky
└─ Done in 45ms
Done in 5.5s
```

You can now continue with the rest of this documentation.

### First Setup

- You'll need to prepare the environment variables for the dev env.
- Easiest would be to set it up once in the root of the repo and then symlink it in each app directory (e.g. `/apps/web`, `/apps/workers`) and also `/packages/db`.
- Start by copying the template by `cp .env.sample .env`.
- The most important env variables to set are:
  - `DATA_DIR`: Where the database and assets will be stored. This is the only required env variable. You can use an absolute path so that all apps point to the same dir.
  - `NEXTAUTH_SECRET`: Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`. Logging in will not work if this is missing!
  - `MEILI_ADDR`: If not set, search will be disabled. You can set it to `http://127.0.0.1:7700` if you run meilisearch using the command below.
  - `OPENAI_API_KEY`: If you want to enable auto tag inference in the dev env.
- run `pnpm run db:migrate` in the root of the repo to set up the database.

### Dependencies

#### Meilisearch

Meilisearch is the provider for the full text search (and at some point embeddings search too). You can get it running with `docker run -p 7700:7700 getmeili/meilisearch:v1.13.3`.

Mount persistent volume if you want to keep index data across restarts. You can trigger a re-index for the entire items collection in the admin panel in the web app.

#### Chrome

The worker app will automatically start headless chrome on startup for crawling pages. You don't need to do anything there.

### Web App

- Run `pnpm web` in the root of the repo.
- Go to `http://localhost:3000`.

> NOTE: The web app kinda works without any dependencies. However, search won't work unless meilisearch is running. Also, new items added won't get crawled/indexed unless workers are running.

### Workers

- Run `pnpm workers` in the root of the repo.

### Mobile App (iOS & Android)

#### Prerequisites

To build and run the mobile app locally, you'll need:

- **For iOS development**: 
  - macOS computer
  - Xcode installed from the App Store
  - iOS Simulator (comes with Xcode)

- **For Android development**:
  - Android Studio installed
  - Android SDK configured
  - Android Emulator or physical device

For detailed setup instructions, refer to the [Expo documentation](https://docs.expo.dev/guides/local-app-development/).

#### Running the app

- `cd apps/mobile`
- `pnpm exec expo prebuild --no-install` to build the app.

**For iOS:**
- `pnpm exec expo run:ios`
- The app will be installed and started in the simulator.

**Troubleshooting iOS Setup:**
If you encounter an error like `xcrun: error: SDK "iphoneos" cannot be located`, you may need to set the correct Xcode developer directory:
```bash
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

**For Android:**
- Start the Android emulator or connect a physical device.
- `pnpm exec expo run:android`
- The app will be installed and started on the emulator/device.

Changing the code will hot reload the app. However, installing new packages requires restarting the expo server.

### Browser Extension

- `cd apps/browser-extension`
- `pnpm dev`
- This will generate a `dist` package
- Go to extension settings in chrome and enable developer mode.
- Press `Load unpacked` and point it to the `dist` directory.
- The plugin will pop up in the plugin list.

In dev mode, opening and closing the plugin menu should reload the code.


## Docker Dev Env

If the manual setup is too much hassle for you. You can use a docker based dev environment by running `docker compose -f docker/docker-compose.dev.yml up` in the root of the repo. This setup wasn't super reliable for me though.


[^1]: [nvm](https://github.com/nvm-sh/nvm) is a node version manager. You can install it following [these
instructions](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

[^2]: [corepack](https://nodejs.org/api/corepack.html) is an experimental tool to help with managing versions of your
package managers.


==================================================
File: docs/versioned_docs/version-v0.28.0/07-development/02-directories.md
==================================================
# Directory Structure

## Apps

| Directory                | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| `apps/web`               | The main web app                                       |
| `apps/workers`           | The background workers logic                           |
| `apps/mobile`            | The react native based mobile app                      |
| `apps/browser-extension` | The browser extension                                  |
| `apps/landing`           | The landing page of [karakeep.app](https://karakeep.app) |

## Shared Packages

| Directory         | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `packages/db`     | The database schema and migrations                                           |
| `packages/trpc`   | Where most of the business logic lies built as TRPC routes                   |
| `packages/shared` | Some shared code between the different apps (e.g. loggers, configs, assetdb) |

## Toolings

| Directory            | Description             |
| -------------------- | ----------------------- |
| `tooling/typescript` | The shared tsconfigs    |
| `tooling/eslint`     | ESlint configs          |
| `tooling/prettier`   | Prettier configs        |
| `tooling/tailwind`   | Shared tailwind configs |


==================================================
File: docs/versioned_docs/version-v0.28.0/07-development/03-database.md
==================================================
# Database Migrations

- The database schema lives in `packages/db/schema.ts`.
- Changing the schema, requires a migration.
- You can generate the migration by running `pnpm run db:generate --name description_of_schema_change` in the root dir.
- You can then apply the migration by running `pnpm run db:migrate`.

## Drizzle Studio

You can start the drizzle studio by running `pnpm run db:studio` in the root of the repo.


==================================================
File: docs/versioned_docs/version-v0.28.0/07-development/04-architecture.md
==================================================
# Architecture

![Architecture Diagram](/img/architecture/arch.png)

- Webapp: NextJS based using sqlite for data storage.
- Workers: Consume the jobs from sqlite based job queue and executes them, there are three job types:
  1. Crawling: Fetches the content of links using a headless chrome browser running in the workers container.
  2. OpenAI: Uses OpenAI APIs to infer the tags of the content.
  3. Indexing: Indexes the content in meilisearch for faster retrieval during search.


==================================================
File: docs/versioned_docs/version-v0.28.0/08-security-considerations.md
==================================================
# Security Considerations

If you're going to give app access to untrusted users, there's some security considerations that you'll need to be aware of given how the crawler works. The crawler is basically running a browser to fetch the content of the bookmarks. Any untrusted user can submit bookmarks to be crawled from your server and they'll be able to see the crawling result. This can be abused in multiple ways:

1. Untrusted users can submit crawl requests to websites that you don't want to be coming out of your IPs.
2. Crawling user controlled websites can expose your origin IP (and location) even if your service is hosted behind cloudflare for example.
3. The crawling requests will be coming out from your own network, which untrusted users can leverage to crawl internal non-internet exposed endpoints.

To mitigate those risks, you can do one of the following:

1. Limit access to trusted users
2. Let the browser traffic go through some VPN with restricted network policies.
3. Host the browser container outside of your network.
4. Use a hosted browser as a service (e.g. [browserless](https://browserless.io)). Note: I've never used them before.


==================================================
File: docs/versioned_docs/version-v0.28.0/09-command-line.md
==================================================
# Command Line Tool (CLI)

Karakeep comes with a simple CLI for those users who want to do more advanced manipulation.

## Features

- Manipulate bookmarks, lists and tags
- Mass import/export of bookmarks

## Installation (NPM)

```
npm install -g @karakeep/cli
```


## Installation (Docker)

```
docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help
```

## Usage

```
karakeep
```

```
Usage: karakeep [options] [command]

A CLI interface to interact with the karakeep api

Options:
  --api-key <key>       the API key to interact with the API (env: KARAKEEP_API_KEY)
  --server-addr <addr>  the address of the server to connect to (env: KARAKEEP_SERVER_ADDR)
  -V, --version         output the version number
  -h, --help            display help for command

Commands:
  bookmarks             manipulating bookmarks
  lists                 manipulating lists
  tags                  manipulating tags
  whoami                returns info about the owner of this API key
  help [command]        display help for command
```

And some of the subcommands:

```
karakeep bookmarks
```

```
Usage: karakeep bookmarks [options] [command]

Manipulating bookmarks

Options:
  -h, --help             display help for command

Commands:
  add [options]          creates a new bookmark
  get <id>               fetch information about a bookmark
  update [options] <id>  updates bookmark
  list [options]         list all bookmarks
  delete <id>            delete a bookmark
  help [command]         display help for command

```

```
karakeep lists
```

```
Usage: karakeep lists [options] [command]

Manipulating lists

Options:
  -h, --help                 display help for command

Commands:
  list                       lists all lists
  delete <id>                deletes a list
  add-bookmark [options]     add a bookmark to list
  remove-bookmark [options]  remove a bookmark from list
  help [command]             display help for command
```

## Obtaining an API Key

To use the CLI, you'll need to get an API key from your karakeep settings. You can validate that it's working by running:

```
karakeep --api-key <key> --server-addr <addr> whoami
```

For example:

```
karakeep --api-key mysupersecretkey --server-addr https://try.karakeep.app whoami
{
  id: 'j29gnbzxxd01q74j2lu88tnb',
  name: 'Test User',
  email: 'test@gmail.com'
}
```


## Other clients

There also exists a **non-official**, community-maintained, python package called [karakeep-python-api](https://github.com/thiswillbeyourgithub/karakeep_python_api) that can be accessed from the CLI, but is **not** official.


==================================================
File: docs/versioned_docs/version-v0.28.0/09-mcp.md
==================================================
# Model Context Protocol Server (MCP)

Karakeep comes with a Model Context Protocol server that can be used to interact with it through LLMs.

## Supported Tools

- Searching bookmarks
- Adding and removing bookmarks from lists
- Attaching and detaching tags to bookmarks
- Creating new lists
- Creating text and URL bookmarks


## Usage with Claude Desktop

From NPM:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "npx",
      "args": [
        "@karakeep/mcp"
      ],
      "env": {
        "KARAKEEP_API_ADDR": "https://<YOUR_SERVER_ADDR>",
        "KARAKEEP_API_KEY": "<YOUR_TOKEN>"
      }
    }
  }
}
```

From Docker:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "docker",
      "args": [
        "run",
        "-e",
        "KARAKEEP_API_ADDR=https://<YOUR_SERVER_ADDR>",
        "-e",
        "KARAKEEP_API_KEY=<YOUR_TOKEN>",
        "ghcr.io/karakeep-app/karakeep-mcp:latest"
      ]
    }
  }
}
```


### Demo

#### Search
![mcp-1](/img/mcp-1.gif)

#### Adding Text Bookmarks
![mcp-2](/img/mcp-2.gif)

#### Adding URL Bookmarks
![mcp-2](/img/mcp-3.gif)


==================================================
File: docs/versioned_docs/version-v0.28.0/10-import.md
==================================================
# Importing Bookmarks


Karakeep supports importing bookmarks using the Netscape HTML Format, Pocket's new CSV format & Omnivore's JSONs. Titles, tags and addition date will be preserved during the import. An automatically created list will contain all the imported bookmarks.

:::info
All the URLs in the bookmarks file will be added automatically, you will not be able to pick and choose which bookmarks to import!
:::

## Import from Chrome

- Open Chrome and go to `chrome://bookmarks`
- Click on the three dots on the top right corner and choose `Export bookmarks`
- This will download an html file with all of your bookmarks.
- To import the bookmark file, go to the settings and click "Import Bookmarks from HTML file".

## Import from Firefox
- Open Firefox and click on the menu button (☰) in the top right corner.
- Navigate to Bookmarks > Manage bookmarks (or press Ctrl + Shift + O / Cmd + Shift + O to open the Bookmarks Library).
- In the Bookmarks Library, click the Import and Backup button at the top. Select Export Bookmarks to HTML... to save your bookmarks as an HTML file.
- To import a bookmark file, go back to the Import and Backup menu, then select Import Bookmarks from HTML... and choose your saved HTML file.

## Import from Pocket

- Go to the [Pocket export page](https://getpocket.com/export) and follow the instructions to export your bookmarks.
- Pocket after a couple of minutes will mail you a zip file with all the bookmarks.
- Unzip the file and you'll get a CSV file.
- To import the bookmark file, go to the settings and click "Import Bookmarks from Pocket export".

## Import from Omnivore

- Follow Omnivore's [documentation](https://docs.omnivore.app/using/exporting.html) to export your bookmarks.
- This will give you a zip file with all your data.
- The zip file contains a lot of JSONs in the format `metadata_*.json`. You can either import every JSON file manually, or merge the JSONs into a single JSON file and import that.
- To  merge the JSONs into a single JSON file, you can use the following command in the unzipped directory: `jq -r '.[]' metadata_*.json | jq -s > omnivore.json` and then import the `omnivore.json` file. You'll need to have the [jq](https://github.com/jqlang/jq) tool installed.

## Import using the CLI

:::warning
Importing bookmarks using the CLI requires some technical knowledge and might not be very straightforward for non-technical users. Don't hesitate to ask questions in github discussions or discord though.
:::

If you can get your bookmarks in a text file with one link per line, you can use the following command to import them using the [karakeep cli](https://docs.karakeep.app/command-line):

```
while IFS= read -r url; do
    karakeep --api-key "<KEY>" --server-addr "<SERVER_ADDR>" bookmarks add --link "$url"
done < all_links.txt
```


==================================================
File: docs/versioned_docs/version-v0.28.0/11-FAQ.md
==================================================
# Frequently Asked Questions (FAQ)

## User Management

### Lost password

#### If you are not an administrator

Administrators can reset the password of any user. Contact an administrator to reset the password for you.

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to reset the password
- Enter a new password and press `Reset`
- The new password is now set
- If required, you can change your password again (so the admin does not know your password) in the `User Settings`

#### If you are an administrator

If you are an administrator and lost your password, you have to reset the password in the database.

To reset the password:

- Acquire some kind of tools that helps you to connect to the database:
  - `sqlite3` on Linux: run `apt-get install sqlite3` (depending on your package manager)
  - e.g. `dbeaver` on Windows
- Shut down Karakeep
- Connect to the `db.db` database, which is located in the `data` directory you have mounted to your docker container:
  - by e.g. running `sqlite3 db.db` (in your `data` directory)
  - or going through e.g. the `dbeaver` UI to locate the file in the data directory and connecting to it
- Update the password in the database by running:
  - `update user set password='$2a$10$5u40XUq/cD/TmLdCOyZ82ePENE6hpkbodJhsp7.e/BgZssUO5DDTa', salt='' where email='<YOUR_EMAIL_HERE>';`
  - (don't forget to put your email address into the command)
- The new password for your user is now `adminadmin`.
- Start Karakeep again
- Log in with your email address and the password `adminadmin` and change the password to whatever you want in the `User Settings`

### Adding another administrator

By default, the first user to sign up gets promoted to administrator automatically.

In case you want to grant those permissions to another user:

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to change the Role
- Change the Role to `Admin`
- Press `Change`
- The new administrator has to log out and log in again to get the new role assigned

### Adding new users, when signups are disabled

Administrators can create new accounts any time:

- Navigate to the `Admin Settings` page
- Go to the `Users List`
- Press the `Create User` Button.
- Enter the information for the user
- Press `create`
- The new user can now log in


==================================================
File: docs/versioned_docs/version-v0.28.0/12-troubleshooting.md
==================================================
# Troubleshooting

## SqliteError: no such table: user

This usually means that there's something wrong with the database setup (more concretely, it means that the database is not initialized). This can be caused by multiple problems:
1. **Wiped DATA_DIR:** Your `DATA_DIR` got wiped (or the backing storage dir changed). If you did this intentionally, restart the container so that it can re-initalize the database.
2. **Missing DATA_DIR**: You're not using the default docker compose file, and you forgot to configure the `DATA_DIR` env var. This will result into the database getting set up in a different directory than the one used by the service.

## Chrome Failed to Read DnsConfig

If you see this error in the logs of the chrome container, it's a benign error and you can safely ignore it. Whatever problems you're having, is unrelated to this error.

## AI Tagging not working (when using OpenAI)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OPENAI_API_KEY` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring open ai.
3. OpenAI requires pre-charging the account with credits before using it, otherwise you'll get an error like "insufficient funds".

## AI Tagging not working (when using Ollama)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OLLAMA_BASE_URL` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring ollama.
3. You didn't change the `INFERENCE_TEXT_MODEL` env variable, resulting into karakeep attempting to use gpt models with ollama which won't work.
4. Ollama server is not reachable by the karakeep container. This can be caused by:
    1. Ollama server being in a different docker network than the karakeep container.
    2. You're using `localhost` as the `OLLAMA_BASE_URL` instead of the actual address of the ollama server. `localhost` points to the container itself, not the docker host. Check this [stackoverflow answer](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) to find how to correctly point to the docker host address instead.

## Crawling not working

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. You changed the name of the chrome container but didn't change the `BROWSER_WEB_URL` env variable.

## Upgrading Meilisearch - Migrating the Meilisearch db version

[Meilisearch](https://www.meilisearch.com/) is the database used by karakeep for searching in your bookmarks. The version used by karakeep is `1.13.3` and it is advised not to upgrade it without good reasons. If you do, you might see errors like `Your database version (1.11.1) is incompatible with your current engine version (1.13.3). To migrate data between Meilisearch versions, please follow our guide on https://www.meilisearch.com/docs/learn/update_and_migration/updating.`.

Luckily we can easily workaround this:
1. Stop the Meilisearch container.
2. Inside the Meilisearch volume bound to `/meili_data`, erase/rename the folder called `data.ms`.
3. Launch Meilisearch again.
4. Login to karakeep as administrator and go to (as of v0.24.1) `Admin Settings > Background Jobs` then click on `Reindex All Bookmarks`.
5. When the reindexing has finished, Meilisearch should be working as usual.

If you run into issues, the official documentation can be found [there](https://www.meilisearch.com/docs/learn/update_and_migration/updating).


==================================================
File: docs/versioned_docs/version-v0.28.0/13-community-projects.md
==================================================
# Community Projects

This page lists community projects that are built around Karakeep, but not officially supported by the development team.

:::warning
This list comes with no guarantees about security, performance, reliability, or accuracy. Use at your own risk.
:::

### Raycast Extension

_By [@luolei](https://github.com/foru17)._

A user-friendly Raycast extension that seamlessly integrates with Karakeep, bringing powerful bookmark management to your fingertips. Quickly save, search, and organize your bookmarks, texts, and images—all through Raycast's intuitive interface.

Get it [here](https://www.raycast.com/luolei/karakeep).

### Alfred Workflow

_By [@yinan-c](https://github.com/yinan-c)_

An Alfred workflow to quickly hoard stuff or access your hoarded bookmarks!

Get it [here](https://www.alfredforum.com/topic/22528-hoarder-workflow-for-self-hosted-bookmark-management/).

### Obsidian Plugin

_By [@jhofker](https://github.com/jhofker)_

An Obsidian plugin that syncs your Karakeep bookmarks with Obsidian, creating markdown notes for each bookmark in a designated folder.

Get it [here](https://github.com/jhofker/obsidian-hoarder/), or install it directly from Obsidian's community plugin store ([link](https://obsidian.md/plugins?id=hoarder-sync)).

### Telegram Bot

_By [@Madh93](https://github.com/Madh93)_

A Telegram Bot for saving bookmarks to Karakeep directly through Telegram.

Get it [here](https://github.com/Madh93/karakeepbot).

### Hoarder's Pipette

_By [@DanSnow](https://github.com/DanSnow)_

A chrome extension that injects karakeep's bookmarks into your search results.

Get it [here](https://dansnow.github.io/hoarder-pipette/guides/installation/).

### Karakeep-Python-API

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python package to simplify access to the karakeep API. Can be used as a library or from the CLI. Aims for feature completeness and high test coverage but do check its feature matrix before relying too much on it.

Its repository also hosts the [Community Script](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts), for example:

| Community Script | Description | Documentation |
|----------------|-------------|---------------|
| **Karakeep-Time-Tagger** | Automatically adds time-to-read tags (`0-5m`, `5-10m`, etc.) to bookmarks based on content length analysis. Includes systemd service and timer files for automated periodic execution. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-time-tagger) |
| **Karakeep-List-To-Tag** | Converts a Karakeep list into tags by adding a specified tag to all bookmarks within that list. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-list-to-tag) |
| **Omnivore2Karakeep-Highlights** | Imports highlights from Omnivore export data to Karakeep, with intelligent position detection and bookmark matching. Supports dry-run mode for testing. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/omnivore2karakeep-highlights) |


Get it [here](https://github.com/thiswillbeyourgithub/karakeep_python_api).

### FreshRSS_to_Karakeep

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python script to automatically create Karakeep bookmarks from your [FreshRSS](https://github.com/FreshRSS/FreshRSS) *favourites/saved* RSS item. Made to be called periodically. Based on the community project `Karakeep-Python-API` above, by the same author.

Get it [here](https://github.com/thiswillbeyourgithub/freshrss_to_karakeep).

### karakeep-sync
_By [@sidoshi](https://github.com/sidoshi/)_

Sync links from Hacker News upvotes, Reddit Saves to Karakeep for centralized bookmark management.

Get it [here](https://github.com/sidoshi/karakeep-sync)


==================================================
File: docs/versioned_docs/version-v0.28.0/14-guides/01-legacy-container-upgrade.md
==================================================
# Legacy Container Upgrade

Karakeep's 0.16 release consolidated the web and worker containers into a single container and also dropped the need for the redis container. The legacy containers will stop being supported soon, to upgrade to the new container do the following:

1. Remove the redis container and its volume if it had one.
2. Move the environment variables that you've set exclusively to the `workers` container to the `web` container.
3. Delete the `workers` container.
4. Rename the web container image from `hoarder-app/hoarder-web` to `hoarder-app/hoarder`.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder-web:${KARAKEEP_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${KARAKEEP_VERSION:-release}
     restart: unless-stopped
     volumes:
       - data:/data
@@ -10,14 +10,10 @@ services:
     env_file:
       - .env
     environment:
-      REDIS_HOST: redis
       MEILI_ADDR: http://meilisearch:7700
+      BROWSER_WEB_URL: http://chrome:9222
+      # OPENAI_API_KEY: ...
       DATA_DIR: /data
-  redis:
-    image: redis:7.2-alpine
-    restart: unless-stopped
-    volumes:
-      - redis:/data
   chrome:
     image: gcr.io/zenika-hub/alpine-chrome:123
     restart: unless-stopped
@@ -37,24 +33,7 @@ services:
       MEILI_NO_ANALYTICS: "true"
     volumes:
       - meilisearch:/meili_data
-  workers:
-    image: ghcr.io/hoarder-app/hoarder-workers:${KARAKEEP_VERSION:-release}
-    restart: unless-stopped
-    volumes:
-      - data:/data
-    env_file:
-      - .env
-    environment:
-      REDIS_HOST: redis
-      MEILI_ADDR: http://meilisearch:7700
-      BROWSER_WEB_URL: http://chrome:9222
-      DATA_DIR: /data
-      # OPENAI_API_KEY: ...
-    depends_on:
-      web:
-        condition: service_started

 volumes:
-  redis:
   meilisearch:
   data:
```


==================================================
File: docs/versioned_docs/version-v0.28.0/14-guides/02-search-query-language.md
==================================================
# Search Query Language

Karakeep provides a search query language to filter and find bookmarks. Here are all the supported qualifiers and how to use them:

## Basic Syntax

- Use spaces to separate multiple conditions (implicit AND)
- Use `and`/`or` keywords for explicit boolean logic
- Prefix qualifiers with `-` to negate them
- Use parentheses `()` for grouping conditions (note that groups can't be negated)

## Qualifiers

Here's a comprehensive table of all supported qualifiers:

| Qualifier                        | Description                                                                                                                                                                                               | Example Usage                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `is:fav`                         | Favorited bookmarks                                                                                                                                                                                       | `is:fav`                                     |
| `is:archived`                    | Archived bookmarks                                                                                                                                                                                        | `-is:archived`                               |
| `is:tagged`                      | Bookmarks that has one or more tags                                                                                                                                                                       | `is:tagged`                                  |
| `is:inlist`                      | Bookmarks that are in one or more lists                                                                                                                                                                   | `is:inlist`                                  |
| `is:link`, `is:text`, `is:media` | Bookmarks that are of type link, text or media                                                                                                                                                            | `is:link`                                    |
| `url:<value>`                    | Match bookmarks with URL substring                                                                                                                                                                        | `url:example.com`                            |
| `title:<value>`                  | Match bookmarks with title substring                                                                                                               | `title:example`                              |
|                                  | Supports quoted strings for titles with spaces                                                                                                   | `title:"my title"`                           |
| `#<tag>`                         | Match bookmarks with specific tag                                                                                                                                                                         | `#important`                                 |
|                                  | Supports quoted strings for tags with spaces                                                                                                                                                              | `#"work in progress"`                        |
| `list:<name>`                    | Match bookmarks in specific list                                                                                                                                                                          | `list:reading`                               |
|                                  | Supports quoted strings for list names with spaces                                                                                                                                                        | `list:"to review"`                           |
| `after:<date>`                   | Bookmarks created on or after date (YYYY-MM-DD)                                                                                                                                                           | `after:2023-01-01`                           |
| `before:<date>`                  | Bookmarks created on or before date (YYYY-MM-DD)                                                                                                                                                          | `before:2023-12-31`                          |
| `feed:<name>`                    | Bookmarks imported from a particular rss feed                                                                                                                                                             | `feed:Hackernews`                            |
| `age:<time-range>`               | Match bookmarks based on how long ago they were created. Use `<` or `>` to indicate the maximum / minimum age of the bookmarks. Supported units: `d` (days), `w` (weeks), `m` (months), `y` (years). | `age:<1d` `age:>2w` `age:<6m` `age:>3y` |

### Examples

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not tagged or not in any list
-is:tagged or -is:inlist
# Find bookmarks with "React" in the title
title:React
```

## Combining Conditions

You can combine multiple conditions using boolean logic:

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not favorited and not archived
-is:fav -is:archived
```

## Text Search

Any text not part of a qualifier will be treated as a full-text search:

```plaintext
# Search for "machine learning" in bookmark content
machine learning

# Combine text search with qualifiers
machine learning is:fav
```


==================================================
File: docs/versioned_docs/version-v0.28.0/14-guides/03-singlefile.md
==================================================
# Using Karakeep with SingleFile Extension

Karakeep supports being a destination for the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile). This has the benefit of allowing you to use the singlefile extension to hoard links as you're seeing them in the browser. This is perfect for websites that don't like to get crawled, has annoying cookie banner or require authentication.

## Setup

1. Install the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile).
2. In the extension settings, select `Destinations`.
3. Select `upload to a REST Form API`.
4. In the URL, insert the address: `https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile`.
5. In the `authorization token` field, paste an API key that you can get from your karakeep settings.
6. Set `data field name` to `file`.
7. Set `URL field name` to `url`.
8. (Optional) Add `&ifexists=MODE` to the URL where MODE is one of `skip`, `overwrite`, `overwrite-recrawl`, `append`, or `append-recrawl`. See "Handling Existing Bookmarks" section below for details.

Now, go to any page and click the singlefile extension icon. Once it's done with the upload, the bookmark should show up in your karakeep instance. Note that the singlefile extension doesn't show any progress on the upload. Given that archives are typically large, it might take 30+ seconds until the upload is done and starts showing up in Karakeep.

## Handling Existing Bookmarks

When uploading a page that already exists in your archive (same URL), you can control the behavior by setting the `ifexists` query parameter in the upload URL. The available modes are:

- `skip` (default): If the bookmark already exists, skip creating a new one
- `overwrite`: Replace existing precrawled archive (only the most recent archive is kept)
- `overwrite-recrawl`: Replace existing archive and queue a recrawl to update content
- `append`: Add new archive version alongside existing ones
- `append-recrawl`: Add new archive and queue a recrawl

To use these modes, append `?ifexists=MODE` to your upload URL, replacing `MODE` with your desired behavior.

For example:  
`https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile?ifexists=overwrite`


## Recommended settings

In the singlefile extension, you probably will want to change the following settings for better experience:
* Stylesheets > compress CSS content: on
* Stylesheets > group duplicate stylesheets together: on
* HTML content > remove frames: on

Also, you most likely will want to change the default `MAX_ASSET_SIZE_MB` in karakeep to something higher, for example `100`.

:::info
Currently, we don't support screenshots for singlefile uploads, but this will change in the future.
:::



==================================================
File: docs/versioned_docs/version-v0.28.0/14-guides/04-hoarder-to-karakeep-migration.md
==================================================
# Hoarder to Karakeep Migration

Hoarder is rebranding to Karakeep. Due to github limitations, the old docker image might not be getting new updates after the rebranding. You might need to update your docker image to point to the new karakeep image instead by applying the following change in the docker compose file.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder:${HOARDER_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${HOARDER_VERSION:-release}
```

You can also change the `HOARDER_VERSION` environment variable but if you do so remember to change it in the `.env` file as well.

## Migrating a Baremetal Installation

If you previously used the [Debian/Ubuntu install script](https://docs.karakeep.app/Installation/debuntu) to install Hoarder, there is an option to migrate your installation to Karakeep.

```bash
bash karakeep-linux.sh migrate
```

This will migrate your installation with no user input required. After the migration, the script will also check for an update.


==================================================
File: docs/versioned_docs/version-v0.28.0/14-guides/05-different-ai-providers.md
==================================================
# Configuring different AI Providers

Karakeep uses LLM providers for AI tagging and summarization. We support OpenAI-compatible providers and ollama. This guide will show you how to configure different providers.

## OpenAI

If you want to use OpenAI itself, you just need to pass in the OPENAI_API_KEY environment variable.

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# You can change the default models by uncommenting the following lines, and choosing your model.
# INFERENCE_TEXT_MODEL=gpt-4.1-mini
# INFERENCE_IMAGE_MODEL=gpt-4o-mini
```

## Ollama

Ollama is a local LLM provider that you can use to run your own LLM server. You'll need to pass ollama's address to karakeep and you need to ensure that it's accessible from within the karakeep container (e.g. no localhost addresses).

```
# MAKE SURE YOU DON'T HAVE OPENAI_API_KEY set, otherwise it takes precedence.

OLLAMA_BASE_URL=http://ollama.mylab.com:11434

# Make sure to pull the models in ollama first. Example models:
INFERENCE_TEXT_MODEL=gemma3
INFERENCE_IMAGE_MODEL=llava

# If the model you're using doesn't support structured output, you also need:
# INFERENCE_OUTPUT_SCHEMA=plain
```

## Gemini

Gemini has an OpenAI-compatible API. You need to get an api key from Google AI Studio.

```

OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=gemini-2.0-flash
INFERENCE_IMAGE_MODEL=gemini-2.0-flash
```

## OpenRouter

```
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=meta-llama/llama-4-scout
INFERENCE_IMAGE_MODEL=meta-llama/llama-4-scout
```

## Perplexity

```
OPENAI_BASE_URL: https://api.perplexity.ai
OPENAI_API_KEY: Your Perplexity API Key
INFERENCE_TEXT_MODEL: sonar-pro
INFERENCE_IMAGE_MODEL: sonar-pro
```

## Azure

Azure has an OpenAI-compatible API.

You can get your API key from the Overview page of the Azure AI Foundry Portal or via "Keys + Endpoints" on the resource in the Azure Portal.

:::warning
The [model name is the deployment name](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/switching-endpoints#keyword-argument-for-model) you specified when deploying the model, which may differ from the base model name.
:::

```
# Deployed via Azure AI Foundry:
OPENAI_BASE_URL=https://{your-azure-ai-foundry-resource-name}.cognitiveservices.azure.com/openai/v1/

# Deployed via Azure OpenAI Service:
OPENAI_BASE_URL=https://{your-azure-openai-resource-name}.openai.azure.com/openai/v1/

OPENAI_API_KEY=YOUR_API_KEY
INFERENCE_TEXT_MODEL=YOUR_DEPLOYMENT_NAME
INFERENCE_IMAGE_MODEL=YOUR_DEPLOYMENT_NAME
```


==================================================
File: docs/versioned_docs/version-v0.28.0/14-guides/06-server-migration.md
==================================================
# Migrating Between Servers

This guide explains how to migrate all of your data from one Karakeep server to another using the official CLI.

## What the command does

The migration copies user-owned data from a source server to a destination server in this order:

- User settings
- Lists (preserving hierarchy and settings)
- RSS feeds
- AI prompts (custom prompts and their enabled state)
- Webhooks (URL and events)
- Tags (ensures tags by name exist)
- Rule engine rules (IDs remapped to destination equivalents)
- Bookmarks (links, text, and assets)
  - After creation, attaches the correct tags and adds to the correct lists

Notes:
- Webhook tokens cannot be read via the API, so tokens are not migrated. Re‑add them on the destination if needed.
- Asset bookmarks are migrated by downloading the original asset and re‑uploading it to the destination. Only images and PDFs are supported for asset bookmarks.
- Link bookmarks on the destination may be de‑duplicated if the same URL already exists.

## Prerequisites

- Install the CLI:
  - NPM: `npm install -g @karakeep/cli`
  - Docker: `docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help`
- Collect API keys and base URLs for both servers:
  - Source: `--server-addr`, `--api-key`
  - Destination: `--dest-server`, `--dest-api-key`

## Quick start

```
karakeep --server-addr https://src.example.com --api-key <SOURCE_API_KEY> migrate \
  --dest-server https://dest.example.com \
  --dest-api-key <DEST_API_KEY>
```

The command is long‑running and shows live progress for each phase. You will be prompted for confirmation; pass `--yes` to skip the prompt.

### Options

- `--server-addr <url>`: Source server base URL
- `--api-key <key>`: API key for the source server
- `--dest-server <url>`: Destination server base URL
- `--dest-api-key <key>`: API key for the destination server
- `--batch-size <n>`: Page size for bookmark migration (default 50, max 100)
- `-y`, `--yes`: Skip the confirmation prompt

## What to expect

- Lists are recreated parent‑first and retain their hierarchy.
- Feeds, prompts, webhooks, and tags are recreated by value.
- Rules are recreated after IDs (tags, lists, feeds) are remapped to their corresponding destination IDs.
- After each bookmark is created, the command attaches the correct tags and adds it to the correct lists.

## Caveats and tips

- Webhook auth tokens must be re‑entered on the destination after migration.
- If your destination already contains data, duplicate links may be de‑duplicated; tags and list membership are still applied to the existing bookmark.

## Troubleshooting

- If the command exits early, you can re‑run it, but note:
  - Tags and lists that already exist are reused.
  - Link de‑duplication avoids duplicate link bookmarks. Notes and assets will get re-created.
  - Rules, webhooks, rss feeds will get re-created and you'll have to manually clean them up afterwards.
  - The progress log indicates how far it got.
- Use a smaller `--batch-size` if your source or destination is under heavy load.


==================================================
File: docs/versioned_docs/version-v0.29.0/01-intro.md
==================================================
---
slug: /
---

# Introduction

Karakeep (previously Hoarder) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

![Screenshot](https://raw.githubusercontent.com/karakeep-app/karakeep/main/screenshots/homepage.png)


## Features

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 🔎 Full text search of all the content stored.
- ✨ AI-based (aka chatgpt) automatic tagging and summarization. With supports for local models using ollama!
- 🤖 Rule-based engine for customized management.
- 🎆 OCR for extracting text from images.
- 🔖 [Chrome plugin](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje) and [Firefox addon](https://addons.mozilla.org/en-US/firefox/addon/karakeep/) for quick bookmarking.
- 📱 An [iOS app](https://apps.apple.com/us/app/karakeep-app/id6479258022), and an [Android app](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).
- 📰 Auto hoarding from RSS feeds.
- 🔌 REST API and multiple clients.
- 🌐 Multi-language support.
- 🖍️ Mark and store highlights from your hoarded content.
- 🗄️ Full page archival (using [monolith](https://github.com/Y2Z/monolith)) to protect against link rot.
- ▶️ Auto video archiving using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- ☑️ Bulk actions support.
- 🔐 SSO support.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
- 🔄 Automatic sync with browser bookmarks via [floccus](https://floccus.org/).
- [Planned] Offline reading on mobile, semantic search across bookmarks, ...

**⚠️ This app is under heavy development.**


## Demo

You can access the demo at [https://try.karakeep.app](https://try.karakeep.app). Login with the following creds:

```
email: demo@karakeep.app
password: demodemo
```

The demo is seeded with some content, but it's in read-only mode to prevent abuse.

## About the name

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).


==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/01-docker.md
==================================================
# Docker Compose [Recommended]

### Requirements

- Docker
- Docker Compose

### 1. Create a new directory

Create a new directory to host the compose file and env variables.

This is where you’ll place the `docker-compose.yml` file from the next step and the environment variables.

For example you could make a new directory called "karakeep-app" with the following command:
```
mkdir karakeep-app
```


### 2. Download the compose file

Download the docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml) directly into your new directory.

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/docker/docker-compose.yml
```

### 3. Populate the environment variables

To configure the app, create a `.env` file in the directory and add this minimal env file:

```
KARAKEEP_VERSION=release
NEXTAUTH_SECRET=super_random_string
MEILI_MASTER_KEY=another_random_string
NEXTAUTH_URL=http://localhost:3000
```

You **should** change the random strings. You can use `openssl rand -base64 36` in a seperate terminal window to generate the random strings. You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

Persistent storage and the wiring between the different services is already taken care of in the docker compose file.

Keep in mind that every time you change the `.env` file, you'll need to re-run `docker compose up`.

If you want more config params, check the config documentation [here](/configuration).

### 4. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the env file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](/openai).

<details>
    <summary>If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose.

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `llama3.1`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.
    - You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be.

</details>

### 5. Start the service

Start the service by running:

```
docker compose up -d
```

Then visit `http://localhost:3000` and you should be greeted with the Sign In page.

### [Optional] 6. Enable optional features

Check the [configuration docs](/configuration) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.

### [Optional] 7. Setup quick sharing extensions

Go to the [quick sharing page](/quick-sharing) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Updating Karakeep will depend on what you used for the `KARAKEEP_VERSION` env variable.

- If you pinned the app to a specific version, bump the version and re-run `docker compose up -d`. This should pull the new version for you.
- If you used `KARAKEEP_VERSION=release`, you'll need to force docker to pull the latest version by running `docker compose up --pull always -d`.

Note that if you want to upgrade/migrate `Meilisearch` versions, refer to the [troubleshooting](/troubleshooting) page.


==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/02-unraid.md
==================================================
# Unraid

## Docker Compose Manager Plugin (Recommended)

You can use [Docker Compose Manager](https://forums.unraid.net/topic/114415-plugin-docker-compose-manager/) plugin to deploy Karakeep using the official docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml). After creating the stack, you'll need to setup some env variables similar to that from the docker compose installation docs [here](/installation/docker#3-populate-the-environment-variables).

## Community Apps

:::info
The community application template is maintained by the community.
:::

Karakeep can be installed on Unraid using the community application plugins. Karakeep is a multi-container service, and because unraid doesn't natively support that, you'll have to install the different pieces as separate applications and wire them manually together.

Here's a high level overview of the services you'll need:

- **Karakeep** ([Support post](https://forums.unraid.net/topic/165108-support-collectathon-karakeep/)): Karakeep's main web app.
- **Browserless** ([Support post](https://forums.unraid.net/topic/130163-support-template-masterwishxbrowserless/)): The chrome headless service used for fetching the content. Karakeep's official docker compose doesn't use browserless, but it's currently the only headless chrome service available on unraid, so you'll have to use it.
- **MeiliSearch** ([Support post](https://forums.unraid.net/topic/164847-support-collectathon-meilisearch/)): The search engine used by Karakeep. It's optional but highly recommended. If you don't have it set up, search will be disabled.


==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/03-archlinux.md
==================================================
# Arch Linux

## Installation

> [Karakeep on AUR](https://aur.archlinux.org/packages/karakeep) is not maintained by the karakeep official.

1. Install karakeep

    ```shell
    paru -S karakeep
    ```

2. (**Optional**) Install optional dependencies

    ```shell
    # karakeep-cli: karakeep cli tool
    paru -S karakeep-cli

    # ollama: for automatic tagging
    sudo pacman -S ollama

    # yt-dlp: for download video
    sudo pacman -S yt-dlp
    ```

    You can use Open-AI instead of `ollama`. If you use `ollama`, you need to download the ollama model. Please refer to: [https://ollama.com/library](https://ollama.com/library).

3. Set up

    Environment variables can be set in `/etc/karakeep/karakeep.env` according to [configuration page](/configuration). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

4. Enable service

    ```shell
    sudo systemctl enable --now karakeep.target
    ```

    Then visit `http://localhost:3000` and you should be greated with the sign in page.

## Services and Ports

`karakeep.target` include 3 services: `karakeep-web.service`, `karakeep-works.service`, `karakeep-browser.service`.

- `karakeep-web.service`: Provide karakeep webui service, uses `3000` port by default.

- `karakeep-workers.service`: Provide karakeep workers service, no port.

- `karakeep-browser.service`: Provide browser headless service, uses `9222` port by default.

Now `karakeep` depends on `meilisearch`, and `karakeep-workers.service` wants `meilisearch.service`, starting `karakeep.target` will start `meilisearch.service` at the same time.

## How to Migrate from Hoarder to Karakeep

The PKGBUILD has been fully updated to replace all references to `hoarder` with `karakeep`. If you want to preserve your existing `hoarder` data during the upgrade, please follow the steps below:

**1. Stop the old services**

```shell
sudo systemctl stop hoarder-web.service hoarder-worker.service hoarder-browser.service
sudo systemctl disable --now hoarder.target
```

**2. Uninstall Hoarder**  
After uninstalling, you can manually remove the old `hoarder` user and group if needed.
```shell
paru -R hoarder
```

**3. Rename the old data directory**
```shell
sudo mv /var/lib/hoarder /var/lib/karakeep
```

**4. Install Karakeep**
```shell
paru -S karakeep
```

**5. Fix ownership of the data directory**
```shell
sudo chown -R karakeep:karakeep /var/lib/karakeep
```

**6. Set Karakeep**  
Edit `/etc/karakeep/karakeep.env` according to [configuration page](/configuration). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

Or you can copy old hoarder env file to karakeep:
```shell
sudo cp -f /etc/hoarder/hoarder.env /etc/karakeep/karakeep.env
```

**7. Start Karakeep**
```shell
sudo systemctl enable --now karakeep.target
```


==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/04-kubernetes.md
==================================================
# Kubernetes

### Requirements

- A kubernetes cluster
- kubectl
- kustomize

### 1. Get the deployment manifests

You can clone the repository and copy the `/kubernetes` directory into another directory of your choice.

### 2. Populate the environment variables and secrets

To configure the app, copy the `.env_sample` to `.env` and change to your specific needs.

You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

To see all available configuration options check the [documentation](https://docs.karakeep.app/configuration).

To configure the neccessary secrets for the application copy the `.secrets_sample` file to `.secrets` and change the sample secrets to your generated secrets.

> Note: You **should** change the random strings. You can use `openssl rand -base64 36` to generate the random strings. 

### 3. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](/openai).

<details>
    <summary>[EXPERIMENTAL] If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose. Running local models is a recent addition and not as battle tested as using openai, so proceed with care (and potentially expect a bunch of inference failures).

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `mistral`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.


</details>

### 4. Deploy the service

Deploy the service by running:

```
make deploy
```

### 5. Access the service

#### via LoadBalancer IP

By default, these manifests expose the application as a LoadBalancer Service. You can run `kubectl get services` to identify the IP of the loadbalancer for your service.

Then visit `http://<loadbalancer-ip>:3000` and you should be greated with the Sign In page.

> Note: Depending on your setup you might want to expose the service via an Ingress, or have a different means to access it.

#### Via Ingress

If you want to use an ingress, you can customize the sample ingress in the kubernetes folder and change the host to the DNS name of your choice.

After that you have to configure the web service to the type ClusterIP so it is only reachable via the ingress.

If you have already deployed the service you can patch the web service to the type ClusterIP with the following command:

` kubectl -n karakeep patch service web -p '{"spec":{"type":"ClusterIP"}}' `

Afterwards you can apply the ingress and access the service via your chosen URL.

#### Setting up HTTPS access to the Service

To access karakeep securely you can configure the ingress to use a preconfigured TLS certificate. This requires that you already have the needed files, namely your .crt and .key file, on hand.

After you have deployed the karakeep manifests you can deploy your certificate for karakeep in the `karakeep` namespace with this example command. You can name the secret however you want. But be aware that the secret name in the ingress definition has to match the secret name.

` $ kubectl --namespace karakeep create secret tls karakeep-web-tls --cert=/path/to/crt --key=/path/to/key `

If the secret is successfully created you can now configure the Ingress to use TLS via this changes to the spec:

```` yaml
 spec:
  tls:
  - hosts:
      - karakeep.example.com
    secretName: karakeep-web-tls
````

> Note: Be aware that the hosts have to match between the tls spec and the HTTP spec.

### [Optional] 6. Setup quick sharing extensions

Go to the [quick sharing page](/quick-sharing) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Edit the `KARAKEEP_VERSION` variable in the `kustomization.yaml` file and run `make clean deploy`.

If you have chosen `release` as the image tag you can also destroy the web pod, since the deployment has an ImagePullPolicy set to always the pod always pulls the image from the registry, this way we can ensure that the newest release image is pulled.


==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/05-pikapods.md
==================================================
# PikaPods [Paid Hosting]

:::info
Note: PikaPods shares some of its revenue from hosting Karakeep with the maintainer of this project.
:::

[PikaPods](https://www.pikapods.com/) offers managed paid hosting for many open source apps, including Karakeep.
Server administration, updates, migrations and backups are all taken care of, which makes it well suited
for less technical users. As of Nov 2024, running Karakeep there will cost you ~$3 per month.

### Requirements

- A _PikaPods_ account. Can be created for free [here](https://www.pikapods.com/register). You get an initial welcome credit of $5.

### 1. Choose app

Choose _Karakeep_ from their [list of apps](https://www.pikapods.com/apps) or use this [direct link](https://www.pikapods.com/pods?run=hoarder). This will either
open a new dialog to add a new _Karakeep_ pod or ask you to log in.

### 2. Add settings

There are a few settings to configure in the dialog:

- **Basics**: Give the pod a name and choose a region that's near you.
- **Env Vars**: Here you can disable signups or set an OpenAI API key. All settings are optional.
- **Resources**: The resources your _Karakeep_ pod can use. The defaults are fine, unless you have a very large collection.

### 3. Start pod and add user

After hitting _Add pod_ it will take about a minute for the app to fully start. After this you can visit
the pod's URL and add an initial user under _Sign Up_. After this you may want to disable further sign-ups
by setting the pod's `DISABLE_SIGNUPS` _Env Var_ to `true`.


==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/06-debuntu.md
==================================================
# Debian 12/Ubuntu 24.04

:::warning
This script is a stripped-down version of those found in the [Proxmox Community Scripts](https://github.com/community-scripts/ProxmoxVE) repo. It has been adapted to work on baremetal Debian 12 or Ubuntu 24.04 installs **only**. Any other use is not supported and you use this script at your own risk.
:::

### Requirements

- **Debian 12** (Buster) or
- **Ubuntu 24.04** (Noble Numbat)

The script will download and install all dependencies (except for Ollama), install Karakeep, do a basic configuration of Karakeep and Meilisearch (the search app used by Karakeep), and create and enable the systemd service files needed to run Karakeep on startup. Karakeep and Meilisearch are run in the context of their low-privilege user environments for more security.

The script functions as an update script in addition to an installer. See **[Updating](#updating)**.

### 1. Download the script from the [Karakeep repository](https://github.com/karakeep-app/karakeep/blob/main/karakeep-linux.sh)

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/karakeep-linux.sh
```

### 2. Run the script

> This script must be run as `root`, or as a user with `sudo` privileges.

    If this is a fresh install, then run the installer by using the following command:

    ```shell
    bash karakeep-linux.sh install
    ```

### 3. Create an account/sign in

    Then visit `http://localhost:3000` and you should be greated with the Sign In page.

## Updating

> This script must be run as `root`, or as a user with `sudo` privileges.

    If Karakeep has previously been installed using this script, then run the updater like so:

    ```shell
     bash karakeep-linux.sh update
    ```

## Services and Ports

`karakeep.target` includes 4 services: `meilisearch.service`, `karakeep-web.service`, `karakeep-workers.service`, `karakeep-browser.service`.

- `meilisearch.service`: Provides full-text search, Karakeep Workers service connects to it, uses port `7700` by default.

- `karakeep-web.service`: Provides the karakeep web service, uses `3000` port by default.

- `karakeep-workers.service`: Provides the karakeep workers service, no port.

- `karakeep-browser.service`: Provides the headless browser service, uses `9222` port by default.

## Configuration, ENV file, database locations

During installation, the script created a configuration file for `meilisearch`, an `ENV` file for Karakeep, and located config paths and database paths separate from the installation path of Karakeep, so as to allow for easier updating. Their names/locations are as follows:

- `/etc/meilisearch.toml` - a basic configuration for meilisearch, that contains configs for the database location, disabling analytics, and using a master key, which prevents unauthorized connections.
- `/var/lib/meilisearch` - Meilisearch DB location.
- `/etc/karakeep/karakeep.env` - The Karakeep `ENV` file. Edit this file to configure Karakeep beyond the default. The web service and the workers service need to be restarted after editing this file:

    ```shell
    sudo systemctl restart karakeep-workers karakeep-web
    ```

- `/var/lib/karakeep` - The Karakeep database location. If you delete the contents of this folder you will lose all your data.

## Still Running Hoarder?

There is a way to upgrade. Please see [Guides > Hoarder to Karakeep Migration](https://docs.karakeep.app/Guides/hoarder-to-karakeep-migration)


==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/07-minimal-install.md
==================================================
# Minimal Installation

:::warning
Unless necessary, prefer the [full installation](/installation/docker) to leverage all the features of Karakeep. You'll be sacrificing a lot of functionality if you go with the minimal installation route.
:::

Karakeep's default installation has a dependency on Meilisearch for the full text search, Chrome for crawling and OpenAI/Ollama for AI tagging. You can however run Karakeep without those dependencies if you're willing to sacrifice those features.

- If you run without meilisearch, the search functionality will be completely disabled.
- If you run without chrome, crawling will still work, but you'll lose ability to take screenshots of websites and websites with javascript content won't get crawled correctly.
- If you don't setup OpenAI/Ollama, AI tagging will be disabled.

Those features are important for leveraging Karakeep's full potential, but if you're running in constrained environments, you can use the following minimal docker compose to skip all those dependencies:

```yaml
services:
  web:
    image: ghcr.io/karakeep-app/karakeep:release
    restart: unless-stopped
    volumes:
      - data:/data
    ports:
      - 3000:3000
    environment:
      DATA_DIR: /data
      NEXTAUTH_SECRET: super_random_string
volumes:
  data:
```

Or just with the following docker command:

```base
docker run -d \
  --restart unless-stopped \
  -v data:/data \
  -p 3000:3000 \
  -e DATA_DIR=/data \
  -e NEXTAUTH_SECRET=super_random_string \
  ghcr.io/karakeep-app/karakeep:release
```

:::warning
You **MUST** change the `super_random_string` to a true random string which you can generate with `openssl rand -hex 32`.
:::

Check the [configuration docs](/configuration) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.




==================================================
File: docs/versioned_docs/version-v0.29.0/02-installation/08-truenas.md
==================================================
# TrueNAS

Karakeep is available directly from TrueNAS's app catalog ([link](https://apps.truenas.com/catalog/karakeep/)).


==================================================
File: docs/versioned_docs/version-v0.29.0/03-configuration.md
==================================================
# Configuration

The app is mainly configured by environment variables. All the used environment variables are listed in [packages/shared/config.ts](https://github.com/karakeep-app/karakeep/blob/main/packages/shared/config.ts). The most important ones are:

| Name                                   | Required                              | Default         | Description                                                                                                                                                                                                                                                                                                             |
| -------------------------------------- | ------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PORT                                   | No                                    | 3000            | The port on which the web server will listen. DON'T CHANGE THIS IF YOU'RE USING DOCKER, instead changed the docker bound external port.                                                                                                                                                                                 |
| WORKERS_PORT                           | No                                    | 0 (Random Port) | The port on which the worker will export its prometheus metrics on `/metrics`. By default it's a random unused port. If you want to utilize those metrics, fix the port to a value (and export it in docker if you're using docker).                                                                                    |
| WORKERS_HOST                           | No                                    | 127.0.0.1       | Host to listen to for requests to WORKERS_PORT. You will need to set this if running in a container, since localhost will not be reachable from outside                                                                                                                                                                 |
| WORKERS_ENABLED_WORKERS                | No                                    | Not set         | Comma separated list of worker names to enable. If set, only these workers will run. Valid values: crawler,inference,search,adminMaintenance,video,feed,assetPreprocessing,webhook,ruleEngine.                                                                                                                          |
| WORKERS_DISABLED_WORKERS               | No                                    | Not set         | Comma separated list of worker names to disable. Takes precedence over `WORKERS_ENABLED_WORKERS`.                                                                                                                                                                                                                       |
| LOG_LEVEL                              | No                                    | debug            | The application log level as defined in the [winston documentation](https://github.com/winstonjs/winston?tab=readme-ov-file#logging-levels). You may want to set this to `notice` or `warning` when running Karakeep in a production environment.                                                            |
| DATA_DIR                               | Yes                                   | Not set         | The path for the persistent data directory. This is where the db lives. Assets are stored here by default unless `ASSETS_DIR` is set.                                                                                                                                                                                   |
| ASSETS_DIR                             | No                                    | Not set         | The path where crawled assets will be stored. If not set, defaults to `${DATA_DIR}/assets`.                                                                                                                                                                                                                             |
| NEXTAUTH_URL                           | Yes                                   | Not set         | Should point to the address of your server. The app will function without it, but will redirect you to wrong addresses on signout for example.                                                                                                                                                                          |
| NEXTAUTH_SECRET                        | Yes                                   | Not set         | Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`.                                                                                                                                                                                                                                 |
| MEILI_ADDR                             | No                                    | Not set         | The address of meilisearch. If not set, Search will be disabled. E.g. (`http://meilisearch:7700`)                                                                                                                                                                                                                       |
| MEILI_MASTER_KEY                       | Only in Prod and if search is enabled | Not set         | The master key configured for meilisearch. Not needed in development environment. Generate one with `openssl rand -base64 36 \| tr -dc 'A-Za-z0-9'`                                                                                                                                                                     |
| MAX_ASSET_SIZE_MB                      | No                                    | 50              | Sets the maximum allowed asset size (in MB) to be uploaded                                                                                                                                                                                                                                                              |
| DISABLE_NEW_RELEASE_CHECK              | No                                    | false           | If set to true, latest release check will be disabled in the admin panel.                                                                                                                                                                                                                                               |
| PROMETHEUS_AUTH_TOKEN                  | No                                    | Random          | Enable a prometheus metrics endpoint at `/api/metrics`. This endpoint will require this token being passed in the Authorization header as a Bearer token. If not set, a new random token is generated everytime at startup. This cannot contain any special characters or you may encounter a 400 Bad Request response. |
| RATE_LIMITING_ENABLED                  | No                                    | false           | If set to true, API rate limiting will be enabled.                                                                                                                                                                                                                                                                      |
| CRAWLER_DOMAIN_RATE_LIMIT_WINDOW_MS    | No                                    | Not set         | Time window in milliseconds for per-domain crawler rate limiting.                                                                                                                                                                                                                                                       |
| CRAWLER_DOMAIN_RATE_LIMIT_MAX_REQUESTS | No                                    | Not set         | Maximum crawler requests allowed per domain inside the configured window.                                                                                                                                                                                                                                               |
| DB_WAL_MODE                            | No                                    | false           | Enables WAL mode for the sqlite database. This should improve the performance of the database. There's no reason why you shouldn't set this to true unless you're running the db on a network attached drive. This will become the default at some time in the future.                                                  |
| SEARCH_NUM_WORKERS                     | No                                    | 1               | Number of concurrent workers for search indexing tasks. Increase this if you have a high volume of content being indexed for search.                                                                                                                                                                                    |
| SEARCH_JOB_TIMEOUT_SEC                 | No                                    | 30              | How long to wait for a search indexing job to finish before timing out. Increase this if you have large bookmarks with extensive content that takes longer to index.                                                                                                                                                    |
| WEBHOOK_NUM_WORKERS                    | No                                    | 1               | Number of concurrent workers for webhook delivery. Increase this if you have multiple webhook endpoints or high webhook traffic.                                                                                                                                                                                        |
| ASSET_PREPROCESSING_NUM_WORKERS        | No                                    | 1               | Number of concurrent workers for asset preprocessing tasks (image processing, OCR, etc.). Increase this if you have many images or documents that need processing.                                                                                                                                                      |
| RULE_ENGINE_NUM_WORKERS                | No                                    | 1               | Number of concurrent workers for rule engine processing. Increase this if you have complex automation rules that need to be processed quickly.                                                                                                                                                                          |

## Asset Storage

Karakeep supports two storage backends for assets: local filesystem (default) and S3-compatible object storage. S3 storage is automatically detected when an S3 endpoint is passed.

| Name                             | Required          | Default | Description                                                                                               |
| -------------------------------- | ----------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| ASSET_STORE_S3_ENDPOINT          | No                | Not set | The S3 endpoint URL. Required for S3-compatible services like MinIO. **Setting this enables S3 storage**. |
| ASSET_STORE_S3_REGION            | No                | Not set | The S3 region to use.                                                                                     |
| ASSET_STORE_S3_BUCKET            | Yes when using S3 | Not set | The S3 bucket name where assets will be stored.                                                           |
| ASSET_STORE_S3_ACCESS_KEY_ID     | Yes when using S3 | Not set | The S3 access key ID for authentication.                                                                  |
| ASSET_STORE_S3_SECRET_ACCESS_KEY | Yes when using S3 | Not set | The S3 secret access key for authentication.                                                              |
| ASSET_STORE_S3_FORCE_PATH_STYLE  | No                | false   | Whether to force path-style URLs for S3 requests. Set to true for MinIO and other S3-compatible services. |

:::info
When using S3 storage, make sure the bucket exists and the provided credentials have the necessary permissions to read, write, and delete objects in the bucket.
:::

:::warning
Switching between storage backends after data has been stored will require manual migration of existing assets. Plan your storage backend choice carefully before deploying.
:::

## Authentication / Signup

By default, Karakeep uses the database to store users, but it is possible to also use OAuth.
The flags need to be provided to the `web` container.

:::info
Only OIDC compliant OAuth providers are supported! For information on how to set it up, consult the documentation of your provider.
:::

:::info
When setting up OAuth, the allowed redirect URLs configured at the provider should be set to `<KARAKEEP_ADDRESS>/api/auth/callback/custom` where `<KARAKEEP_ADDRESS>` is the address you configured in `NEXTAUTH_URL` (for example: `https://try.karakeep.app/api/auth/callback/custom`).
:::

| Name                                        | Required | Default                | Description                                                                                                                                                                                           |
| ------------------------------------------- | -------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DISABLE_SIGNUPS                             | No       | false                  | If enabled, no new signups will be allowed and the signup button will be disabled in the UI                                                                                                           |
| DISABLE_PASSWORD_AUTH                       | No       | false                  | If enabled, only signups and logins using OAuth are allowed and the signup button and login form for local accounts will be disabled in the UI                                                        |
| EMAIL_VERIFICATION_REQUIRED                 | No       | false                  | Whether email verification is required during user signup. If enabled, users must verify their email address before they can use their account. If you enable this, you must configure SMTP settings. |
| OAUTH_WELLKNOWN_URL                         | No       | Not set                | The "wellknown Url" for openid-configuration as provided by the OAuth provider                                                                                                                        |
| OAUTH_CLIENT_SECRET                         | No       | Not set                | The "Client Secret" as provided by the OAuth provider                                                                                                                                                 |
| OAUTH_CLIENT_ID                             | No       | Not set                | The "Client ID" as provided by the OAuth provider                                                                                                                                                     |
| OAUTH_SCOPE                                 | No       | "openid email profile" | "Full list of scopes to request (space delimited)"                                                                                                                                                    |
| OAUTH_PROVIDER_NAME                         | No       | "Custom Provider"      | The name of your provider. Will be shown on the signup page as "Sign in with `<name>`"                                                                                                                |
| OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING | No       | false                  | Whether existing accounts in karakeep stored in the database should automatically be linked with your OAuth account. Only enable it if you trust the OAuth provider!                                  |
| OAUTH_TIMEOUT                               | No       | 3500                   | The wait time in milliseconds for the OAuth provider response. Increase this if you are having `outgoing request timed out` errors                                                                    |

For more information on `OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING`, check the [next-auth.js documentation](https://next-auth.js.org/configuration/providers/oauth#allowdangerousemailaccountlinking-option).

## Inference Configs (For automatic tagging)

Either `OPENAI_API_KEY` or `OLLAMA_BASE_URL` need to be set for automatic tagging to be enabled. Otherwise, automatic tagging will be skipped.

:::warning

- The quality of the tags you'll get will depend on the quality of the model you choose.
- You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be (money-wise on OpenAI and resource-wise on ollama).
  :::

| Name                                 | Required | Default                | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAI_API_KEY                       | No       | Not set                | The OpenAI key used for automatic tagging. More on that in [here](/openai).                                                                                                                                                                                                                                                                                                           |
| OPENAI_BASE_URL                      | No       | Not set                | If you just want to use OpenAI you don't need to pass this variable. If, however, you want to use some other openai compatible API (e.g. azure openai service), set this to the url of the API.                                                                                                                                                                                       |
| OLLAMA_BASE_URL                      | No       | Not set                | If you want to use ollama for local inference, set the address of ollama API here.                                                                                                                                                                                                                                                                                                    |
| OLLAMA_KEEP_ALIVE                    | No       | Not set                | Controls how long the model will stay loaded into memory following the request (example value: "5m").                                                                                                                                                                                                                                                                                 |
| INFERENCE_TEXT_MODEL                 | No       | gpt-4.1-mini           | The model to use for text inference. You'll need to change this to some other model if you're using ollama.                                                                                                                                                                                                                                                                           |
| INFERENCE_IMAGE_MODEL                | No       | gpt-4o-mini            | The model to use for image inference. You'll need to change this to some other model if you're using ollama and that model needs to support vision APIs (e.g. llava).                                                                                                                                                                                                                 |
| EMBEDDING_TEXT_MODEL                 | No       | text-embedding-3-small | The model to be used for generating embeddings for the text.                                                                                                                                                                                                                                                                                                                          |
| INFERENCE_CONTEXT_LENGTH             | No       | 2048                   | The max number of tokens that we'll pass to the inference model. If your content is larger than this size, it'll be truncated to fit. The larger this value, the more of the content will be used in tag inference, but the more expensive the inference will be (money-wise on openAI and resource-wise on ollama). Check the model you're using for its max supported content size. |
| INFERENCE_MAX_OUTPUT_TOKENS          | No       | 2048                   | The maximum number of tokens that the inference model is allowed to generate in its response. This controls the length of AI-generated content like tags and summaries. Increase this if you need longer responses, but be aware that higher values will increase costs (for OpenAI) and processing time.                                                                             |
| INFERENCE_USE_MAX_COMPLETION_TOKENS  | No       | false                  | \[OpenAI Only\] Whether to use the newer `max_completion_tokens` parameter instead of the deprecated `max_tokens` parameter. Set to `true` if using GPT-5 or o-series models which require this. Will become the default in a future release.                                                                                                                                         |
| INFERENCE_LANG                       | No       | english                | The language in which the tags will be generated.                                                                                                                                                                                                                                                                                                                                     |
| INFERENCE_NUM_WORKERS                | No       | 1                      | Number of concurrent workers for AI inference tasks (tagging and summarization). Increase this if you have multiple AI inference requests and want to process them in parallel.                                                                                                                                                                                                       |
| INFERENCE_ENABLE_AUTO_TAGGING        | No       | true                   | Whether automatic AI tagging is enabled or disabled.                                                                                                                                                                                                                                                                                                                                  |
| INFERENCE_ENABLE_AUTO_SUMMARIZATION  | No       | false                  | Whether automatic AI summarization is enabled or disabled.                                                                                                                                                                                                                                                                                                                            |
| INFERENCE_JOB_TIMEOUT_SEC            | No       | 30                     | How long to wait for the inference job to finish before timing out. If you're running ollama without powerful GPUs, you might want to increase the timeout a bit.                                                                                                                                                                                                                     |
| INFERENCE_FETCH_TIMEOUT_SEC          | No       | 300                    | \[Ollama Only\] The timeout of the fetch request to the ollama server. If your inference requests take longer than the default 5mins, you might want to increase this timeout.                                                                                                                                                                                                        |
| INFERENCE_SUPPORTS_STRUCTURED_OUTPUT | No       | Not set                | \[DEPRECATED\] Whether the inference model supports structured output or not. Use INFERENCE_OUTPUT_SCHEMA instead. Setting this to true translates to INFERENCE_OUTPUT_SCHEMA=structured, and to false translates to INFERENCE_OUTPUT_SCHEMA=plain.                                                                                                                                   |
| INFERENCE_OUTPUT_SCHEMA              | No       | structured             | Possible values are "structured", "json", "plain". Structured is the preferred option, but if your model doesn't support it, you can use "json" if your model supports JSON mode, otherwise "plain" which should be supported by all the models but the model might not output the data in the correct format.                                                                        |

:::info

- You can append additional instructions to the prompt used for automatic tagging, in the `AI Settings` (in the `User Settings` screen)
- You can use the placeholders `$tags`, `$aiTags`, `$userTags` in the prompt. These placeholders will be replaced with all tags, ai generated tags or human created tags when automatic tagging is performed (e.g. `[karakeep, computer, ai]`)
  :::

## Crawler Configs

| Name                                     | Required | Default   | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_NUM_WORKERS                      | No       | 1         | Number of allowed concurrent crawling jobs. By default, we're only doing one crawling request at a time to avoid consuming a lot of resources.                                                                                                                                                                                                                                |
| BROWSER_WEB_URL                          | No       | Not set   | The browser's http debugging address. The worker will talk to this endpoint to resolve the debugging console's websocket address. If you already have the websocket address, use `BROWSER_WEBSOCKET_URL` instead. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution. |
| BROWSER_WEBSOCKET_URL                    | No       | Not set   | The websocket address of browser's debugging console. If you want to use [browserless](https://browserless.io), use their websocket address here. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution.                                                                 |
| BROWSER_CONNECT_ONDEMAND                 | No       | false     | If set to false, the crawler will proactively connect to the browser instance and always maintain an active connection. If set to true, the browser will be launched on demand only whenever a crawling is requested. Set to true if you're using a service that provides you with browser instances on demand.                                                               |
| CRAWLER_DOWNLOAD_BANNER_IMAGE            | No       | true      | Whether to cache the banner image used in the cards locally or fetch it each time directly from the website. Caching it consumes more storage space, but is more resilient against link rot and rate limits from websites.                                                                                                                                                    |
| CRAWLER_STORE_SCREENSHOT                 | No       | true      | Whether to store a screenshot from the crawled website or not. Screenshots act as a fallback for when we fail to extract an image from a website. You can also view the stored screenshots for any link.                                                                                                                                                                      |
| CRAWLER_FULL_PAGE_SCREENSHOT             | No       | false     | Whether to store a screenshot of the full page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, the screenshot will only include the visible part of the page                                                                                                                                                                              |
| CRAWLER_SCREENSHOT_TIMEOUT_SEC           | No       | 5         | How long to wait for the screenshot finish before timing out. If you are capturing full-page screenshots of long webpages, consider increasing this value.                                                                                                                                                                                                                    |
| CRAWLER_FULL_PAGE_ARCHIVE                | No       | false     | Whether to store a full local copy of the page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, only the readable text of the page is archived.                                                                                                                                                                                            |
| CRAWLER_JOB_TIMEOUT_SEC                  | No       | 60        | How long to wait for the crawler job to finish before timing out. If you have a slow internet connection or a low powered device, you might want to bump this up a bit                                                                                                                                                                                                        |
| CRAWLER_NAVIGATE_TIMEOUT_SEC             | No       | 30        | How long to spend navigating to the page (along with its redirects). Increase this if you have a slow internet connection                                                                                                                                                                                                                                                     |
| CRAWLER_VIDEO_DOWNLOAD                   | No       | false     | Whether to download videos from the page or not (using yt-dlp)                                                                                                                                                                                                                                                                                                                |
| CRAWLER_VIDEO_DOWNLOAD_MAX_SIZE          | No       | 50        | The maximum file size for the downloaded video. The quality will be chosen accordingly. Use -1 to disable the limit.                                                                                                                                                                                                                                                          |
| CRAWLER_VIDEO_DOWNLOAD_TIMEOUT_SEC       | No       | 600       | How long to wait for the video download to finish                                                                                                                                                                                                                                                                                                                             |
| CRAWLER_ENABLE_ADBLOCKER                 | No       | true      | Whether to enable an adblocker in the crawler or not. If you're facing troubles downloading the adblocking lists on worker startup, you can disable this.                                                                                                                                                                                                                     |
| CRAWLER_YTDLP_ARGS                       | No       | []        | Include additional yt-dlp arguments to be passed at crawl time separated by %%: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#general-options                                                                                                                                                                                                                           |
| BROWSER_COOKIE_PATH                      | No       | Not set   | Path to a JSON file containing cookies to be loaded into the browser context. The file should be an array of cookie objects, each with name and value (required), and optional fields like domain, path, expires, httpOnly, secure, and sameSite (e.g., `[{"name": "session", "value": "xxx", "domain": ".example.com"}`]).                                                   |
| HTML_CONTENT_SIZE_INLINE_THRESHOLD_BYTES | No       | 5 \* 1024 | The thresholds in bytes after which larger assets will be stored in the assetdb (folder/s3) instead of inline in the database.                                                                                                                                                                                                                                                |

<details>

  <summary>More info on BROWSER_COOKIE_PATH</summary>

BROWSER_COOKIE_PATH specifies the path to a JSON file containing cookies to be loaded into the browser context for crawling.

The JSON file must be an array of cookie objects, each with:

- name: The cookie name (required).
- value: The cookie value (required).
- Optional fields: domain, path, expires, httpOnly, secure, sameSite (values: "Strict", "Lax", or "None").

Example JSON file:

```json
[
  {
    "name": "session",
    "value": "xxx",
    "domain": ".example.com",
    "path": "/",
    "expires": 1735689600,
    "httpOnly": true,
    "secure": true,
    "sameSite": "Lax"
  }
]
```

</details>

## OCR Configs

Karakeep uses [tesseract.js](https://github.com/naptha/tesseract.js) to extract text from images.

| Name                     | Required | Default   | Description                                                                                                                                                                                                                               |
| ------------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OCR_CACHE_DIR            | No       | $TEMP_DIR | The dir where tesseract will download its models. By default, those models are not persisted and stored in the OS' temp dir.                                                                                                              |
| OCR_LANGS                | No       | eng       | Comma separated list of the language codes that you want tesseract to support. You can find the language codes [here](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html). Set to empty string to disable OCR. |
| OCR_CONFIDENCE_THRESHOLD | No       | 50        | A number between 0 and 100 indicating the minimum acceptable confidence from tessaract. If tessaract's confidence is lower than this value, extracted text won't be stored.                                                               |

## Webhook Configs

You can use webhooks to trigger actions when bookmarks are created, changed or crawled.

| Name                | Required | Default | Description                                       |
| ------------------- | -------- | ------- | ------------------------------------------------- |
| WEBHOOK_TIMEOUT_SEC | No       | 5       | The timeout for the webhook request in seconds.   |
| WEBHOOK_RETRY_TIMES | No       | 3       | The number of times to retry the webhook request. |

:::info

- The WEBHOOK_TOKEN is used for authentication. It will appear in the Authorization header as Bearer token.
  ```
  Authorization: Bearer <WEBHOOK_TOKEN>
  ```
- The webhook will be triggered with the job id (used for idempotence), bookmark id, bookmark type, the user id, the url and the operation in JSON format in the body.

  ```json
  {
    "jobId": "123",
    "type": "link",
    "bookmarkId": "exampleBookmarkId",
    "userId": "exampleUserId",
    "url": "https://example.com",
    "operation": "crawled"
  }
  ```

  :::

## SMTP Configuration

Karakeep can send emails for various purposes such as email verification during signup. Configure these settings to enable email functionality.

| Name          | Required | Default | Description                                                                                     |
| ------------- | -------- | ------- | ----------------------------------------------------------------------------------------------- |
| SMTP_HOST     | No       | Not set | The SMTP server hostname or IP address. Required if you want to enable email functionality.     |
| SMTP_PORT     | No       | 587     | The SMTP server port. Common values are 587 (STARTTLS), 465 (SSL/TLS), or 25 (unencrypted).     |
| SMTP_SECURE   | No       | false   | Whether to use SSL/TLS encryption. Set to true for port 465, false for port 587 with STARTTLS.  |
| SMTP_USER     | No       | Not set | The username for SMTP authentication. Usually your email address.                               |
| SMTP_PASSWORD | No       | Not set | The password for SMTP authentication. For services like Gmail, use an app-specific password.    |
| SMTP_FROM     | No       | Not set | The "from" email address that will appear in sent emails. This should be a valid email address. |

## Proxy Configuration

If your Karakeep instance needs to connect through a proxy server, you can configure the following settings:

| Name                               | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_HTTP_PROXY                 | No       | Not set | HTTP proxy server URL for outgoing HTTP requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                                                           |
| CRAWLER_HTTPS_PROXY                | No       | Not set | HTTPS proxy server URL for outgoing HTTPS requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                                                         |
| CRAWLER_NO_PROXY                   | No       | Not set | Comma-separated list of hostnames/IPs that should bypass the proxy (e.g., `localhost,127.0.0.1,.local`)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CRAWLER_ALLOWED_INTERNAL_HOSTNAMES | No       | Not set | By default, Karakeep blocks worker-initiated requests whose DNS resolves to private, loopback, or link-local IP addresses. Use this to allowlist specific hostnames for internal access (e.g., `internal.company.com,.local`). Supports domain wildcards by prefixing with a dot (e.g., `.internal.company.com`). Passing `.` allowlists all domains. Note: Internal IP validation is bypassed when a proxy is configured for the URL as the local DNS resolver won't necessarily be the same as the one used by the proxy. |

:::info
These proxy settings will be used by the crawler and other components that make outgoing HTTP requests.
:::


==================================================
File: docs/versioned_docs/version-v0.29.0/04-screenshots.md
==================================================
# Screenshots

## Homepage

![Homepage](/img/screenshots/homepage.png)

## Homepage (Dark Mode)

![Homepage](/img/screenshots/homepage-dark.png)

## Tags

![All Tags](/img/screenshots/all-tags.png)

## Lists

![All Lists](/img/screenshots/all-lists.png)

## Bookmark Preview

![Bookmark Preview](/img/screenshots/bookmark-preview.png)

## Settings

![Settings](/img/screenshots/settings.png)

## Admin Panel

![Ammin](/img/screenshots/admin.png)


## iOS Sharing

<img src="/img/screenshots/share-sheet.png" width="400px"  />


==================================================
File: docs/versioned_docs/version-v0.29.0/05-quick-sharing.md
==================================================
# Quick Sharing Extensions

The whole point of Karakeep is making it easy to hoard the content. That's why there are a couple of 

## Mobile Apps

<img src="/img/quick-sharing/mobile.png" alt="mobile screenshot" width="300"/>


- **iOS app**: [App Store Link](https://apps.apple.com/us/app/karakeep-app/id6479258022).
- **Android App**: [Play Store link](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).

## Browser Extensions

<img src="/img/quick-sharing/extension.png" alt="mobile screenshot" width="300"/>

- **Chrome extension**: [here](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje).
- **Firefox addon**: [here](https://addons.mozilla.org/en-US/firefox/addon/karakeep/).

- ## Community Extensions
- **Safari extension**: [App Store Link](https://apps.apple.com/us/app/karakeeper-bookmarker/id6746722790).  For macOS and iOS to allow a simple way to add your bookmarks to your self hosted karakeep instance.


==================================================
File: docs/versioned_docs/version-v0.29.0/06-openai.md
==================================================
# OpenAI Costs

This service uses OpenAI for automatic tagging. This means that you'll incur some costs if automatic tagging is enabled. There are two type of inferences that we do:

## Text Tagging

For text tagging, we use the `gpt-4.1-mini` model. This model is [extremely cheap](https://openai.com/api/pricing). Cost per inference varies depending on the content size per article. Though, roughly, You'll be able to generate tags for almost 3000+ bookmarks for less than $1.

## Image Tagging

For image uploads, we use the `gpt-4o-mini` model for extracting tags from the image. You can learn more about the costs of using this model [here](https://platform.openai.com/docs/guides/images?api-mode=chat#calculating-costs). To lower the costs, we're using the low resolution mode (fixed number of tokens regardless of image size). You'll be able to run inference for 1000+ images for less than a $1.


==================================================
File: docs/versioned_docs/version-v0.29.0/07-development/01-setup.md
==================================================
# Setup

## Quick Start

For the fastest way to get started with development, use the one-command setup script:

```bash
./start-dev.sh
```

This script will automatically:
- Start Meilisearch in Docker (on port 7700)
- Start headless Chrome in Docker (on port 9222) 
- Install dependencies with `pnpm install` if needed
- Start both the web app and workers in parallel
- Provide cleanup when you stop with Ctrl+C

**Prerequisites:**
- Docker installed and running
- pnpm installed (see manual setup below for installation instructions)

The script will output the running services:
- Web app: http://localhost:3000
- Meilisearch: http://localhost:7700  
- Chrome debugger: http://localhost:9222

Press Ctrl+C to stop all services and clean up Docker containers.

## Manual Setup

Karakeep uses `node` version 22. To install it, you can use `nvm` [^1]

```
$ nvm install  22
```

Verify node version using this command:
```
$ node --version
v22.14.0
```

Karakeep also makes use of `corepack`[^2]. If you have `node` installed, then `corepack` should already be
installed on your machine, and you don't need to do anything. To verify the `corepack` is installed run:

```
$ command -v corepack
/home/<user>/.nvm/versions/node/v22.14.0/bin/corepack
```

To enable `corepack` run the following command:

```
$ corepack enable
```

Then, from the root of the repository, install the packages and dependencies using:

```
$ pnpm install
```

Output of a successful `pnpm install` run should look something like:

```
Scope: all 20 workspace projects
Lockfile is up to date, resolution step is skipped
Packages: +3129
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 0, reused 2699, downloaded 0, added 3129, done

devDependencies:
+ @karakeep/prettier-config 0.1.0 <- tooling/prettier

. prepare$ husky
└─ Done in 45ms
Done in 5.5s
```

You can now continue with the rest of this documentation.

### First Setup

- You'll need to prepare the environment variables for the dev env.
- Easiest would be to set it up once in the root of the repo and then symlink it in each app directory (e.g. `/apps/web`, `/apps/workers`) and also `/packages/db`.
- Start by copying the template by `cp .env.sample .env`.
- The most important env variables to set are:
  - `DATA_DIR`: Where the database and assets will be stored. This is the only required env variable. You can use an absolute path so that all apps point to the same dir.
  - `NEXTAUTH_SECRET`: Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`. Logging in will not work if this is missing!
  - `MEILI_ADDR`: If not set, search will be disabled. You can set it to `http://127.0.0.1:7700` if you run meilisearch using the command below.
  - `OPENAI_API_KEY`: If you want to enable auto tag inference in the dev env.
- run `pnpm run db:migrate` in the root of the repo to set up the database.

### Dependencies

#### Meilisearch

Meilisearch is the provider for the full text search (and at some point embeddings search too). You can get it running with `docker run -p 7700:7700 getmeili/meilisearch:v1.13.3`.

Mount persistent volume if you want to keep index data across restarts. You can trigger a re-index for the entire items collection in the admin panel in the web app.

#### Chrome

The worker app will automatically start headless chrome on startup for crawling pages. You don't need to do anything there.

### Web App

- Run `pnpm web` in the root of the repo.
- Go to `http://localhost:3000`.

> NOTE: The web app kinda works without any dependencies. However, search won't work unless meilisearch is running. Also, new items added won't get crawled/indexed unless workers are running.

### Workers

- Run `pnpm workers` in the root of the repo.

### Mobile App (iOS & Android)

#### Prerequisites

To build and run the mobile app locally, you'll need:

- **For iOS development**: 
  - macOS computer
  - Xcode installed from the App Store
  - iOS Simulator (comes with Xcode)

- **For Android development**:
  - Android Studio installed
  - Android SDK configured
  - Android Emulator or physical device

For detailed setup instructions, refer to the [Expo documentation](https://docs.expo.dev/guides/local-app-development/).

#### Running the app

- `cd apps/mobile`
- `pnpm exec expo prebuild --no-install` to build the app.

**For iOS:**
- `pnpm exec expo run:ios`
- The app will be installed and started in the simulator.

**Troubleshooting iOS Setup:**
If you encounter an error like `xcrun: error: SDK "iphoneos" cannot be located`, you may need to set the correct Xcode developer directory:
```bash
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

**For Android:**
- Start the Android emulator or connect a physical device.
- `pnpm exec expo run:android`
- The app will be installed and started on the emulator/device.

Changing the code will hot reload the app. However, installing new packages requires restarting the expo server.

### Browser Extension

- `cd apps/browser-extension`
- `pnpm dev`
- This will generate a `dist` package
- Go to extension settings in chrome and enable developer mode.
- Press `Load unpacked` and point it to the `dist` directory.
- The plugin will pop up in the plugin list.

In dev mode, opening and closing the plugin menu should reload the code.


## Docker Dev Env

If the manual setup is too much hassle for you. You can use a docker based dev environment by running `docker compose -f docker/docker-compose.dev.yml up` in the root of the repo. This setup wasn't super reliable for me though.


[^1]: [nvm](https://github.com/nvm-sh/nvm) is a node version manager. You can install it following [these
instructions](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

[^2]: [corepack](https://nodejs.org/api/corepack.html) is an experimental tool to help with managing versions of your
package managers.


==================================================
File: docs/versioned_docs/version-v0.29.0/07-development/02-directories.md
==================================================
# Directory Structure

## Apps

| Directory                | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| `apps/web`               | The main web app                                       |
| `apps/workers`           | The background workers logic                           |
| `apps/mobile`            | The react native based mobile app                      |
| `apps/browser-extension` | The browser extension                                  |
| `apps/landing`           | The landing page of [karakeep.app](https://karakeep.app) |

## Shared Packages

| Directory         | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `packages/db`     | The database schema and migrations                                           |
| `packages/trpc`   | Where most of the business logic lies built as TRPC routes                   |
| `packages/shared` | Some shared code between the different apps (e.g. loggers, configs, assetdb) |

## Toolings

| Directory            | Description             |
| -------------------- | ----------------------- |
| `tooling/typescript` | The shared tsconfigs    |
| `tooling/eslint`     | ESlint configs          |
| `tooling/prettier`   | Prettier configs        |
| `tooling/tailwind`   | Shared tailwind configs |


==================================================
File: docs/versioned_docs/version-v0.29.0/07-development/03-database.md
==================================================
# Database Migrations

- The database schema lives in `packages/db/schema.ts`.
- Changing the schema, requires a migration.
- You can generate the migration by running `pnpm run db:generate --name description_of_schema_change` in the root dir.
- You can then apply the migration by running `pnpm run db:migrate`.

## Drizzle Studio

You can start the drizzle studio by running `pnpm run db:studio` in the root of the repo.


==================================================
File: docs/versioned_docs/version-v0.29.0/07-development/04-architecture.md
==================================================
# Architecture

![Architecture Diagram](/img/architecture/arch.png)

- Webapp: NextJS based using sqlite for data storage.
- Workers: Consume the jobs from sqlite based job queue and executes them, there are three job types:
  1. Crawling: Fetches the content of links using a headless chrome browser running in the workers container.
  2. OpenAI: Uses OpenAI APIs to infer the tags of the content.
  3. Indexing: Indexes the content in meilisearch for faster retrieval during search.


==================================================
File: docs/versioned_docs/version-v0.29.0/08-security-considerations.md
==================================================
# Security Considerations

If you're going to give app access to untrusted users, there's some security considerations that you'll need to be aware of given how the crawler works. The crawler is basically running a browser to fetch the content of the bookmarks. Any untrusted user can submit bookmarks to be crawled from your server and they'll be able to see the crawling result. This can be abused in multiple ways:

1. Untrusted users can submit crawl requests to websites that you don't want to be coming out of your IPs.
2. Crawling user controlled websites can expose your origin IP (and location) even if your service is hosted behind cloudflare for example.
3. The crawling requests will be coming out from your own network, which untrusted users can leverage to crawl internal non-internet exposed endpoints.

To mitigate those risks, you can do one of the following:

1. Limit access to trusted users
2. Let the browser traffic go through some VPN with restricted network policies.
3. Host the browser container outside of your network.
4. Use a hosted browser as a service (e.g. [browserless](https://browserless.io)). Note: I've never used them before.


==================================================
File: docs/versioned_docs/version-v0.29.0/09-command-line.md
==================================================
# Command Line Tool (CLI)

Karakeep comes with a simple CLI for those users who want to do more advanced manipulation.

## Features

- Manipulate bookmarks, lists and tags
- Mass import/export of bookmarks

## Installation (NPM)

```
npm install -g @karakeep/cli
```


## Installation (Docker)

```
docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help
```

## Usage

```
karakeep
```

```
Usage: karakeep [options] [command]

A CLI interface to interact with the karakeep api

Options:
  --api-key <key>       the API key to interact with the API (env: KARAKEEP_API_KEY)
  --server-addr <addr>  the address of the server to connect to (env: KARAKEEP_SERVER_ADDR)
  -V, --version         output the version number
  -h, --help            display help for command

Commands:
  bookmarks             manipulating bookmarks
  lists                 manipulating lists
  tags                  manipulating tags
  whoami                returns info about the owner of this API key
  help [command]        display help for command
```

And some of the subcommands:

```
karakeep bookmarks
```

```
Usage: karakeep bookmarks [options] [command]

Manipulating bookmarks

Options:
  -h, --help             display help for command

Commands:
  add [options]          creates a new bookmark
  get <id>               fetch information about a bookmark
  update [options] <id>  updates bookmark
  list [options]         list all bookmarks
  delete <id>            delete a bookmark
  help [command]         display help for command

```

```
karakeep lists
```

```
Usage: karakeep lists [options] [command]

Manipulating lists

Options:
  -h, --help                 display help for command

Commands:
  list                       lists all lists
  delete <id>                deletes a list
  add-bookmark [options]     add a bookmark to list
  remove-bookmark [options]  remove a bookmark from list
  help [command]             display help for command
```

## Obtaining an API Key

To use the CLI, you'll need to get an API key from your karakeep settings. You can validate that it's working by running:

```
karakeep --api-key <key> --server-addr <addr> whoami
```

For example:

```
karakeep --api-key mysupersecretkey --server-addr https://try.karakeep.app whoami
{
  id: 'j29gnbzxxd01q74j2lu88tnb',
  name: 'Test User',
  email: 'test@gmail.com'
}
```


## Other clients

There also exists a **non-official**, community-maintained, python package called [karakeep-python-api](https://github.com/thiswillbeyourgithub/karakeep_python_api) that can be accessed from the CLI, but is **not** official.


==================================================
File: docs/versioned_docs/version-v0.29.0/09-mcp.md
==================================================
# Model Context Protocol Server (MCP)

Karakeep comes with a Model Context Protocol server that can be used to interact with it through LLMs.

## Supported Tools

- Searching bookmarks
- Adding and removing bookmarks from lists
- Attaching and detaching tags to bookmarks
- Creating new lists
- Creating text and URL bookmarks


## Usage with Claude Desktop

From NPM:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "npx",
      "args": [
        "@karakeep/mcp"
      ],
      "env": {
        "KARAKEEP_API_ADDR": "https://<YOUR_SERVER_ADDR>",
        "KARAKEEP_API_KEY": "<YOUR_TOKEN>"
      }
    }
  }
}
```

From Docker:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "docker",
      "args": [
        "run",
        "-e",
        "KARAKEEP_API_ADDR=https://<YOUR_SERVER_ADDR>",
        "-e",
        "KARAKEEP_API_KEY=<YOUR_TOKEN>",
        "ghcr.io/karakeep-app/karakeep-mcp:latest"
      ]
    }
  }
}
```


### Demo

#### Search
![mcp-1](/img/mcp-1.gif)

#### Adding Text Bookmarks
![mcp-2](/img/mcp-2.gif)

#### Adding URL Bookmarks
![mcp-2](/img/mcp-3.gif)


==================================================
File: docs/versioned_docs/version-v0.29.0/10-import.md
==================================================
# Importing Bookmarks


Karakeep supports importing bookmarks using the Netscape HTML Format, Pocket's new CSV format & Omnivore's JSONs. Titles, tags and addition date will be preserved during the import. An automatically created list will contain all the imported bookmarks.

:::info
All the URLs in the bookmarks file will be added automatically, you will not be able to pick and choose which bookmarks to import!
:::

## Import from Chrome

- Open Chrome and go to `chrome://bookmarks`
- Click on the three dots on the top right corner and choose `Export bookmarks`
- This will download an html file with all of your bookmarks.
- To import the bookmark file, go to the settings and click "Import Bookmarks from HTML file".

## Import from Firefox
- Open Firefox and click on the menu button (☰) in the top right corner.
- Navigate to Bookmarks > Manage bookmarks (or press Ctrl + Shift + O / Cmd + Shift + O to open the Bookmarks Library).
- In the Bookmarks Library, click the Import and Backup button at the top. Select Export Bookmarks to HTML... to save your bookmarks as an HTML file.
- To import a bookmark file, go back to the Import and Backup menu, then select Import Bookmarks from HTML... and choose your saved HTML file.

## Import from Pocket

- Go to the [Pocket export page](https://getpocket.com/export) and follow the instructions to export your bookmarks.
- Pocket after a couple of minutes will mail you a zip file with all the bookmarks.
- Unzip the file and you'll get a CSV file.
- To import the bookmark file, go to the settings and click "Import Bookmarks from Pocket export".

## Import from Omnivore

- Follow Omnivore's [documentation](https://docs.omnivore.app/using/exporting.html) to export your bookmarks.
- This will give you a zip file with all your data.
- The zip file contains a lot of JSONs in the format `metadata_*.json`. You can either import every JSON file manually, or merge the JSONs into a single JSON file and import that.
- To  merge the JSONs into a single JSON file, you can use the following command in the unzipped directory: `jq -r '.[]' metadata_*.json | jq -s > omnivore.json` and then import the `omnivore.json` file. You'll need to have the [jq](https://github.com/jqlang/jq) tool installed.

## Import using the CLI

:::warning
Importing bookmarks using the CLI requires some technical knowledge and might not be very straightforward for non-technical users. Don't hesitate to ask questions in github discussions or discord though.
:::

If you can get your bookmarks in a text file with one link per line, you can use the following command to import them using the [karakeep cli](https://docs.karakeep.app/command-line):

```
while IFS= read -r url; do
    karakeep --api-key "<KEY>" --server-addr "<SERVER_ADDR>" bookmarks add --link "$url"
done < all_links.txt
```


==================================================
File: docs/versioned_docs/version-v0.29.0/11-FAQ.md
==================================================
# Frequently Asked Questions (FAQ)

## User Management

### Lost password

#### If you are not an administrator

Administrators can reset the password of any user. Contact an administrator to reset the password for you.

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to reset the password
- Enter a new password and press `Reset`
- The new password is now set
- If required, you can change your password again (so the admin does not know your password) in the `User Settings`

#### If you are an administrator

If you are an administrator and lost your password, you have to reset the password in the database.

To reset the password:

- Acquire some kind of tools that helps you to connect to the database:
  - `sqlite3` on Linux: run `apt-get install sqlite3` (depending on your package manager)
  - e.g. `dbeaver` on Windows
- Shut down Karakeep
- Connect to the `db.db` database, which is located in the `data` directory you have mounted to your docker container:
  - by e.g. running `sqlite3 db.db` (in your `data` directory)
  - or going through e.g. the `dbeaver` UI to locate the file in the data directory and connecting to it
- Update the password in the database by running:
  - `update user set password='$2a$10$5u40XUq/cD/TmLdCOyZ82ePENE6hpkbodJhsp7.e/BgZssUO5DDTa', salt='' where email='<YOUR_EMAIL_HERE>';`
  - (don't forget to put your email address into the command)
- The new password for your user is now `adminadmin`.
- Start Karakeep again
- Log in with your email address and the password `adminadmin` and change the password to whatever you want in the `User Settings`

### Adding another administrator

By default, the first user to sign up gets promoted to administrator automatically.

In case you want to grant those permissions to another user:

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to change the Role
- Change the Role to `Admin`
- Press `Change`
- The new administrator has to log out and log in again to get the new role assigned

### Adding new users, when signups are disabled

Administrators can create new accounts any time:

- Navigate to the `Admin Settings` page
- Go to the `Users List`
- Press the `Create User` Button.
- Enter the information for the user
- Press `create`
- The new user can now log in


==================================================
File: docs/versioned_docs/version-v0.29.0/12-troubleshooting.md
==================================================
# Troubleshooting

## SqliteError: no such table: user

This usually means that there's something wrong with the database setup (more concretely, it means that the database is not initialized). This can be caused by multiple problems:
1. **Wiped DATA_DIR:** Your `DATA_DIR` got wiped (or the backing storage dir changed). If you did this intentionally, restart the container so that it can re-initalize the database.
2. **Missing DATA_DIR**: You're not using the default docker compose file, and you forgot to configure the `DATA_DIR` env var. This will result into the database getting set up in a different directory than the one used by the service.

## Chrome Failed to Read DnsConfig

If you see this error in the logs of the chrome container, it's a benign error and you can safely ignore it. Whatever problems you're having, is unrelated to this error.

## AI Tagging not working (when using OpenAI)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OPENAI_API_KEY` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring open ai.
3. OpenAI requires pre-charging the account with credits before using it, otherwise you'll get an error like "insufficient funds".

## AI Tagging not working (when using Ollama)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OLLAMA_BASE_URL` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring ollama.
3. You didn't change the `INFERENCE_TEXT_MODEL` env variable, resulting into karakeep attempting to use gpt models with ollama which won't work.
4. Ollama server is not reachable by the karakeep container. This can be caused by:
    1. Ollama server being in a different docker network than the karakeep container.
    2. You're using `localhost` as the `OLLAMA_BASE_URL` instead of the actual address of the ollama server. `localhost` points to the container itself, not the docker host. Check this [stackoverflow answer](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) to find how to correctly point to the docker host address instead.

## Crawling not working

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. You changed the name of the chrome container but didn't change the `BROWSER_WEB_URL` env variable.

## Upgrading Meilisearch - Migrating the Meilisearch db version

[Meilisearch](https://www.meilisearch.com/) is the database used by karakeep for searching in your bookmarks. The version used by karakeep is `1.13.3` and it is advised not to upgrade it without good reasons. If you do, you might see errors like `Your database version (1.11.1) is incompatible with your current engine version (1.13.3). To migrate data between Meilisearch versions, please follow our guide on https://www.meilisearch.com/docs/learn/update_and_migration/updating.`.

Luckily we can easily workaround this:
1. Stop the Meilisearch container.
2. Inside the Meilisearch volume bound to `/meili_data`, erase/rename the folder called `data.ms`.
3. Launch Meilisearch again.
4. Login to karakeep as administrator and go to (as of v0.24.1) `Admin Settings > Background Jobs` then click on `Reindex All Bookmarks`.
5. When the reindexing has finished, Meilisearch should be working as usual.

If you run into issues, the official documentation can be found [there](https://www.meilisearch.com/docs/learn/update_and_migration/updating).


==================================================
File: docs/versioned_docs/version-v0.29.0/13-community-projects.md
==================================================
# Community Projects

This page lists community projects that are built around Karakeep, but not officially supported by the development team.

:::warning
This list comes with no guarantees about security, performance, reliability, or accuracy. Use at your own risk.
:::

### Raycast Extension

_By [@luolei](https://github.com/foru17)._

A user-friendly Raycast extension that seamlessly integrates with Karakeep, bringing powerful bookmark management to your fingertips. Quickly save, search, and organize your bookmarks, texts, and images—all through Raycast's intuitive interface.

Get it [here](https://www.raycast.com/luolei/karakeep).

### Alfred Workflow

_By [@yinan-c](https://github.com/yinan-c)_

An Alfred workflow to quickly hoard stuff or access your hoarded bookmarks!

Get it [here](https://www.alfredforum.com/topic/22528-hoarder-workflow-for-self-hosted-bookmark-management/).

### Obsidian Plugin

_By [@jhofker](https://github.com/jhofker)_

An Obsidian plugin that syncs your Karakeep bookmarks with Obsidian, creating markdown notes for each bookmark in a designated folder.

Get it [here](https://github.com/jhofker/obsidian-hoarder/), or install it directly from Obsidian's community plugin store ([link](https://obsidian.md/plugins?id=hoarder-sync)).

### Telegram Bot

_By [@Madh93](https://github.com/Madh93)_

A Telegram Bot for saving bookmarks to Karakeep directly through Telegram.

Get it [here](https://github.com/Madh93/karakeepbot).

### Hoarder's Pipette

_By [@DanSnow](https://github.com/DanSnow)_

A chrome extension that injects karakeep's bookmarks into your search results.

Get it [here](https://dansnow.github.io/hoarder-pipette/guides/installation/).

### Karakeep-Python-API

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python package to simplify access to the karakeep API. Can be used as a library or from the CLI. Aims for feature completeness and high test coverage but do check its feature matrix before relying too much on it.

Its repository also hosts the [Community Script](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts), for example:

| Community Script | Description | Documentation |
|----------------|-------------|---------------|
| **Karakeep-Time-Tagger** | Automatically adds time-to-read tags (`0-5m`, `5-10m`, etc.) to bookmarks based on content length analysis. Includes systemd service and timer files for automated periodic execution. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-time-tagger) |
| **Karakeep-List-To-Tag** | Converts a Karakeep list into tags by adding a specified tag to all bookmarks within that list. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-list-to-tag) |
| **Omnivore2Karakeep-Highlights** | Imports highlights from Omnivore export data to Karakeep, with intelligent position detection and bookmark matching. Supports dry-run mode for testing. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/omnivore2karakeep-highlights) |


Get it [here](https://github.com/thiswillbeyourgithub/karakeep_python_api).

### FreshRSS_to_Karakeep

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python script to automatically create Karakeep bookmarks from your [FreshRSS](https://github.com/FreshRSS/FreshRSS) *favourites/saved* RSS item. Made to be called periodically. Based on the community project `Karakeep-Python-API` above, by the same author.

Get it [here](https://github.com/thiswillbeyourgithub/freshrss_to_karakeep).

### karakeep-sync
_By [@sidoshi](https://github.com/sidoshi/)_

Sync links from Hacker News upvotes, Reddit Saves to Karakeep for centralized bookmark management.

Get it [here](https://github.com/sidoshi/karakeep-sync)


==================================================
File: docs/versioned_docs/version-v0.29.0/14-guides/01-legacy-container-upgrade.md
==================================================
# Legacy Container Upgrade

Karakeep's 0.16 release consolidated the web and worker containers into a single container and also dropped the need for the redis container. The legacy containers will stop being supported soon, to upgrade to the new container do the following:

1. Remove the redis container and its volume if it had one.
2. Move the environment variables that you've set exclusively to the `workers` container to the `web` container.
3. Delete the `workers` container.
4. Rename the web container image from `hoarder-app/hoarder-web` to `hoarder-app/hoarder`.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder-web:${KARAKEEP_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${KARAKEEP_VERSION:-release}
     restart: unless-stopped
     volumes:
       - data:/data
@@ -10,14 +10,10 @@ services:
     env_file:
       - .env
     environment:
-      REDIS_HOST: redis
       MEILI_ADDR: http://meilisearch:7700
+      BROWSER_WEB_URL: http://chrome:9222
+      # OPENAI_API_KEY: ...
       DATA_DIR: /data
-  redis:
-    image: redis:7.2-alpine
-    restart: unless-stopped
-    volumes:
-      - redis:/data
   chrome:
     image: gcr.io/zenika-hub/alpine-chrome:123
     restart: unless-stopped
@@ -37,24 +33,7 @@ services:
       MEILI_NO_ANALYTICS: "true"
     volumes:
       - meilisearch:/meili_data
-  workers:
-    image: ghcr.io/hoarder-app/hoarder-workers:${KARAKEEP_VERSION:-release}
-    restart: unless-stopped
-    volumes:
-      - data:/data
-    env_file:
-      - .env
-    environment:
-      REDIS_HOST: redis
-      MEILI_ADDR: http://meilisearch:7700
-      BROWSER_WEB_URL: http://chrome:9222
-      DATA_DIR: /data
-      # OPENAI_API_KEY: ...
-    depends_on:
-      web:
-        condition: service_started

 volumes:
-  redis:
   meilisearch:
   data:
```


==================================================
File: docs/versioned_docs/version-v0.29.0/14-guides/02-search-query-language.md
==================================================
# Search Query Language

Karakeep provides a search query language to filter and find bookmarks. Here are all the supported qualifiers and how to use them:

## Basic Syntax

- Use spaces to separate multiple conditions (implicit AND)
- Use `and`/`or` keywords for explicit boolean logic
- Prefix qualifiers with `-` to negate them
- Use parentheses `()` for grouping conditions (note that groups can't be negated)

## Qualifiers

Here's a comprehensive table of all supported qualifiers:

| Qualifier                        | Description                                                                                                                                                                                               | Example Usage                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `is:fav`                         | Favorited bookmarks                                                                                                                                                                                       | `is:fav`                                     |
| `is:archived`                    | Archived bookmarks                                                                                                                                                                                        | `-is:archived`                               |
| `is:tagged`                      | Bookmarks that has one or more tags                                                                                                                                                                       | `is:tagged`                                  |
| `is:inlist`                      | Bookmarks that are in one or more lists                                                                                                                                                                   | `is:inlist`                                  |
| `is:link`, `is:text`, `is:media` | Bookmarks that are of type link, text or media                                                                                                                                                            | `is:link`                                    |
| `url:<value>`                    | Match bookmarks with URL substring                                                                                                                                                                        | `url:example.com`                            |
| `title:<value>`                  | Match bookmarks with title substring                                                                                                               | `title:example`                              |
|                                  | Supports quoted strings for titles with spaces                                                                                                   | `title:"my title"`                           |
| `#<tag>`                         | Match bookmarks with specific tag                                                                                                                                                                         | `#important`                                 |
|                                  | Supports quoted strings for tags with spaces                                                                                                                                                              | `#"work in progress"`                        |
| `list:<name>`                    | Match bookmarks in specific list                                                                                                                                                                          | `list:reading`                               |
|                                  | Supports quoted strings for list names with spaces                                                                                                                                                        | `list:"to review"`                           |
| `after:<date>`                   | Bookmarks created on or after date (YYYY-MM-DD)                                                                                                                                                           | `after:2023-01-01`                           |
| `before:<date>`                  | Bookmarks created on or before date (YYYY-MM-DD)                                                                                                                                                          | `before:2023-12-31`                          |
| `feed:<name>`                    | Bookmarks imported from a particular rss feed                                                                                                                                                             | `feed:Hackernews`                            |
| `age:<time-range>`               | Match bookmarks based on how long ago they were created. Use `<` or `>` to indicate the maximum / minimum age of the bookmarks. Supported units: `d` (days), `w` (weeks), `m` (months), `y` (years). | `age:<1d` `age:>2w` `age:<6m` `age:>3y` |

### Examples

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not tagged or not in any list
-is:tagged or -is:inlist
# Find bookmarks with "React" in the title
title:React
```

## Combining Conditions

You can combine multiple conditions using boolean logic:

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not favorited and not archived
-is:fav -is:archived
```

## Text Search

Any text not part of a qualifier will be treated as a full-text search:

```plaintext
# Search for "machine learning" in bookmark content
machine learning

# Combine text search with qualifiers
machine learning is:fav
```


==================================================
File: docs/versioned_docs/version-v0.29.0/14-guides/03-singlefile.md
==================================================
# Using Karakeep with SingleFile Extension

Karakeep supports being a destination for the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile). This has the benefit of allowing you to use the singlefile extension to hoard links as you're seeing them in the browser. This is perfect for websites that don't like to get crawled, has annoying cookie banner or require authentication.

## Setup

1. Install the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile).
2. In the extension settings, select `Destinations`.
3. Select `upload to a REST Form API`.
4. In the URL, insert the address: `https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile`.
5. In the `authorization token` field, paste an API key that you can get from your karakeep settings.
6. Set `data field name` to `file`.
7. Set `URL field name` to `url`.
8. (Optional) Add `&ifexists=MODE` to the URL where MODE is one of `skip`, `overwrite`, `overwrite-recrawl`, `append`, or `append-recrawl`. See "Handling Existing Bookmarks" section below for details.

Now, go to any page and click the singlefile extension icon. Once it's done with the upload, the bookmark should show up in your karakeep instance. Note that the singlefile extension doesn't show any progress on the upload. Given that archives are typically large, it might take 30+ seconds until the upload is done and starts showing up in Karakeep.

## Handling Existing Bookmarks

When uploading a page that already exists in your archive (same URL), you can control the behavior by setting the `ifexists` query parameter in the upload URL. The available modes are:

- `skip` (default): If the bookmark already exists, skip creating a new one
- `overwrite`: Replace existing precrawled archive (only the most recent archive is kept)
- `overwrite-recrawl`: Replace existing archive and queue a recrawl to update content
- `append`: Add new archive version alongside existing ones
- `append-recrawl`: Add new archive and queue a recrawl

To use these modes, append `?ifexists=MODE` to your upload URL, replacing `MODE` with your desired behavior.

For example:  
`https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile?ifexists=overwrite`


## Recommended settings

In the singlefile extension, you probably will want to change the following settings for better experience:
* Stylesheets > compress CSS content: on
* Stylesheets > group duplicate stylesheets together: on
* HTML content > remove frames: on

Also, you most likely will want to change the default `MAX_ASSET_SIZE_MB` in karakeep to something higher, for example `100`.

:::info
Currently, we don't support screenshots for singlefile uploads, but this will change in the future.
:::



==================================================
File: docs/versioned_docs/version-v0.29.0/14-guides/04-hoarder-to-karakeep-migration.md
==================================================
# Hoarder to Karakeep Migration

Hoarder is rebranding to Karakeep. Due to github limitations, the old docker image might not be getting new updates after the rebranding. You might need to update your docker image to point to the new karakeep image instead by applying the following change in the docker compose file.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder:${HOARDER_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${HOARDER_VERSION:-release}
```

You can also change the `HOARDER_VERSION` environment variable but if you do so remember to change it in the `.env` file as well.

## Migrating a Baremetal Installation

If you previously used the [Debian/Ubuntu install script](https://docs.karakeep.app/Installation/debuntu) to install Hoarder, there is an option to migrate your installation to Karakeep.

```bash
bash karakeep-linux.sh migrate
```

This will migrate your installation with no user input required. After the migration, the script will also check for an update.


==================================================
File: docs/versioned_docs/version-v0.29.0/14-guides/05-different-ai-providers.md
==================================================
# Configuring different AI Providers

Karakeep uses LLM providers for AI tagging and summarization. We support OpenAI-compatible providers and ollama. This guide will show you how to configure different providers.

## OpenAI

If you want to use OpenAI itself, you just need to pass in the OPENAI_API_KEY environment variable.

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# You can change the default models by uncommenting the following lines, and choosing your model.
# INFERENCE_TEXT_MODEL=gpt-4.1-mini
# INFERENCE_IMAGE_MODEL=gpt-4o-mini
```

## Ollama

Ollama is a local LLM provider that you can use to run your own LLM server. You'll need to pass ollama's address to karakeep and you need to ensure that it's accessible from within the karakeep container (e.g. no localhost addresses).

```
# MAKE SURE YOU DON'T HAVE OPENAI_API_KEY set, otherwise it takes precedence.

OLLAMA_BASE_URL=http://ollama.mylab.com:11434

# Make sure to pull the models in ollama first. Example models:
INFERENCE_TEXT_MODEL=gemma3
INFERENCE_IMAGE_MODEL=llava

# If the model you're using doesn't support structured output, you also need:
# INFERENCE_OUTPUT_SCHEMA=plain
```

## Gemini

Gemini has an OpenAI-compatible API. You need to get an api key from Google AI Studio.

```

OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=gemini-2.0-flash
INFERENCE_IMAGE_MODEL=gemini-2.0-flash
```

## OpenRouter

```
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=meta-llama/llama-4-scout
INFERENCE_IMAGE_MODEL=meta-llama/llama-4-scout
```

## Perplexity

```
OPENAI_BASE_URL: https://api.perplexity.ai
OPENAI_API_KEY: Your Perplexity API Key
INFERENCE_TEXT_MODEL: sonar-pro
INFERENCE_IMAGE_MODEL: sonar-pro
```

## Azure

Azure has an OpenAI-compatible API.

You can get your API key from the Overview page of the Azure AI Foundry Portal or via "Keys + Endpoints" on the resource in the Azure Portal.

:::warning
The [model name is the deployment name](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/switching-endpoints#keyword-argument-for-model) you specified when deploying the model, which may differ from the base model name.
:::

```
# Deployed via Azure AI Foundry:
OPENAI_BASE_URL=https://{your-azure-ai-foundry-resource-name}.cognitiveservices.azure.com/openai/v1/

# Deployed via Azure OpenAI Service:
OPENAI_BASE_URL=https://{your-azure-openai-resource-name}.openai.azure.com/openai/v1/

OPENAI_API_KEY=YOUR_API_KEY
INFERENCE_TEXT_MODEL=YOUR_DEPLOYMENT_NAME
INFERENCE_IMAGE_MODEL=YOUR_DEPLOYMENT_NAME
```


==================================================
File: docs/versioned_docs/version-v0.29.0/14-guides/06-server-migration.md
==================================================
# Migrating Between Servers

This guide explains how to migrate all of your data from one Karakeep server to another using the official CLI.

## What the command does

The migration copies user-owned data from a source server to a destination server in this order:

- User settings
- Lists (preserving hierarchy and settings)
- RSS feeds
- AI prompts (custom prompts and their enabled state)
- Webhooks (URL and events)
- Tags (ensures tags by name exist)
- Rule engine rules (IDs remapped to destination equivalents)
- Bookmarks (links, text, and assets)
  - After creation, attaches the correct tags and adds to the correct lists

Notes:
- Webhook tokens cannot be read via the API, so tokens are not migrated. Re‑add them on the destination if needed.
- Asset bookmarks are migrated by downloading the original asset and re‑uploading it to the destination. Only images and PDFs are supported for asset bookmarks.
- Link bookmarks on the destination may be de‑duplicated if the same URL already exists.

## Prerequisites

- Install the CLI:
  - NPM: `npm install -g @karakeep/cli`
  - Docker: `docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help`
- Collect API keys and base URLs for both servers:
  - Source: `--server-addr`, `--api-key`
  - Destination: `--dest-server`, `--dest-api-key`

## Quick start

```
karakeep --server-addr https://src.example.com --api-key <SOURCE_API_KEY> migrate \
  --dest-server https://dest.example.com \
  --dest-api-key <DEST_API_KEY>
```

The command is long‑running and shows live progress for each phase. You will be prompted for confirmation; pass `--yes` to skip the prompt.

### Options

- `--server-addr <url>`: Source server base URL
- `--api-key <key>`: API key for the source server
- `--dest-server <url>`: Destination server base URL
- `--dest-api-key <key>`: API key for the destination server
- `--batch-size <n>`: Page size for bookmark migration (default 50, max 100)
- `-y`, `--yes`: Skip the confirmation prompt

## What to expect

- Lists are recreated parent‑first and retain their hierarchy.
- Feeds, prompts, webhooks, and tags are recreated by value.
- Rules are recreated after IDs (tags, lists, feeds) are remapped to their corresponding destination IDs.
- After each bookmark is created, the command attaches the correct tags and adds it to the correct lists.

## Caveats and tips

- Webhook auth tokens must be re‑entered on the destination after migration.
- If your destination already contains data, duplicate links may be de‑duplicated; tags and list membership are still applied to the existing bookmark.

## Troubleshooting

- If the command exits early, you can re‑run it, but note:
  - Tags and lists that already exist are reused.
  - Link de‑duplication avoids duplicate link bookmarks. Notes and assets will get re-created.
  - Rules, webhooks, rss feeds will get re-created and you'll have to manually clean them up afterwards.
  - The progress log indicates how far it got.
- Use a smaller `--batch-size` if your source or destination is under heavy load.


==================================================
File: docs/versioned_docs/version-v0.30.0/01-getting-started/01-intro.md
==================================================
---
slug: /
---

# Introduction

Karakeep (previously Hoarder) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

![Screenshot](https://raw.githubusercontent.com/karakeep-app/karakeep/main/screenshots/homepage.png)


## Features

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 👥 Collaborate with others on the same list.
- 🔎 Full text search of all the content stored.
- ✨ AI-based (aka chatgpt) automatic tagging and summarization. With supports for local models using ollama!
- 🤖 Rule-based engine for customized management.
- 🎆 OCR for extracting text from images.
- 🔖 [Chrome plugin](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje) and [Firefox addon](https://addons.mozilla.org/en-US/firefox/addon/karakeep/) for quick bookmarking.
- 📱 An [iOS app](https://apps.apple.com/us/app/karakeep-app/id6479258022), and an [Android app](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).
- 📰 Auto hoarding from RSS feeds.
- 🔌 REST API and multiple clients.
- 🌐 Multi-language support.
- 🖍️ Mark and store highlights from your hoarded content.
- 🗄️ Full page archival (using [monolith](https://github.com/Y2Z/monolith)) to protect against link rot.
- ▶️ Auto video archiving using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- ☑️ Bulk actions support.
- 🔐 SSO support.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
- 🔄 Automatic sync with browser bookmarks via [floccus](https://floccus.org/).
- [Planned] Offline reading on mobile, semantic search across bookmarks, ...

**⚠️ This app is under heavy development.**


## Demo

You can access the demo at [https://try.karakeep.app](https://try.karakeep.app). Login with the following creds:

```
email: demo@karakeep.app
password: demodemo
```

The demo is seeded with some content, but it's in read-only mode to prevent abuse.

## About the name

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).


==================================================
File: docs/versioned_docs/version-v0.30.0/01-getting-started/02-screenshots.md
==================================================
# Screenshots

## Homepage

![Homepage](/img/screenshots/homepage.png)

## Homepage (Dark Mode)

![Homepage](/img/screenshots/homepage-dark.png)

## Tags

![All Tags](/img/screenshots/all-tags.png)

## Lists

![All Lists](/img/screenshots/all-lists.png)

## Bookmark Preview

![Bookmark Preview](/img/screenshots/bookmark-preview.png)

## Settings

![Settings](/img/screenshots/settings.png)


## Sharing

<img src="/img/screenshots/share-sheet.png" width="400px"  />


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/01-docker.md
==================================================
# Docker

### Requirements

- Docker
- Docker Compose

### 1. Create a new directory

Create a new directory to host the compose file and env variables.

This is where you’ll place the `docker-compose.yml` file from the next step and the environment variables.

For example you could make a new directory called "karakeep-app" with the following command:
```
mkdir karakeep-app
```


### 2. Download the compose file

Download the docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml) directly into your new directory.

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/docker/docker-compose.yml
```

### 3. Populate the environment variables

To configure the app, create a `.env` file in the directory and add this minimal env file:

```
KARAKEEP_VERSION=release
NEXTAUTH_SECRET=super_random_string
MEILI_MASTER_KEY=another_random_string
NEXTAUTH_URL=http://localhost:3000
```

You **should** change the random strings. You can use `openssl rand -base64 36` in a seperate terminal window to generate the random strings. You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

Persistent storage and the wiring between the different services is already taken care of in the docker compose file.

Keep in mind that every time you change the `.env` file, you'll need to re-run `docker compose up`.

If you want more config params, check the config documentation [here](../03-configuration/01-environment-variables.md).

### 4. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the env file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](../06-administration/03-openai.md).

<details>
    <summary>If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose.

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `llama3.1`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.
    - You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be.

</details>

### 5. Start the service

Start the service by running:

```
docker compose up -d
```

Then visit `http://localhost:3000` and you should be greeted with the Sign In page.

### [Optional] 6. Enable optional features

Check the [configuration docs](../03-configuration/01-environment-variables.md) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.

### [Optional] 7. Setup quick sharing extensions

Go to the [quick sharing page](../04-using-karakeep/quick-sharing.md) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Updating Karakeep will depend on what you used for the `KARAKEEP_VERSION` env variable.

- If you pinned the app to a specific version, bump the version and re-run `docker compose up -d`. This should pull the new version for you.
- If you used `KARAKEEP_VERSION=release`, you'll need to force docker to pull the latest version by running `docker compose up --pull always -d`.

Note that if you want to upgrade/migrate `Meilisearch` versions, refer to the [troubleshooting](../06-administration/05-troubleshooting.md) page.


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/02-unraid.md
==================================================
# Unraid

## Docker Compose Manager Plugin (Recommended)

You can use [Docker Compose Manager](https://forums.unraid.net/topic/114415-plugin-docker-compose-manager/) plugin to deploy Karakeep using the official docker compose file provided [here](https://github.com/karakeep-app/karakeep/blob/main/docker/docker-compose.yml). After creating the stack, you'll need to setup some env variables similar to that from the docker compose installation docs [here](/installation/docker#3-populate-the-environment-variables).

## Community Apps

:::info
The community application template is maintained by the community.
:::

Karakeep can be installed on Unraid using the community application plugins. Karakeep is a multi-container service, and because unraid doesn't natively support that, you'll have to install the different pieces as separate applications and wire them manually together.

Here's a high level overview of the services you'll need:

- **Karakeep** ([Support post](https://forums.unraid.net/topic/165108-support-collectathon-karakeep/)): Karakeep's main web app.
- **Browserless** ([Support post](https://forums.unraid.net/topic/130163-support-template-masterwishxbrowserless/)): The chrome headless service used for fetching the content. Karakeep's official docker compose doesn't use browserless, but it's currently the only headless chrome service available on unraid, so you'll have to use it.
- **MeiliSearch** ([Support post](https://forums.unraid.net/topic/164847-support-collectathon-meilisearch/)): The search engine used by Karakeep. It's optional but highly recommended. If you don't have it set up, search will be disabled.


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/03-archlinux.md
==================================================
# Arch Linux

## Installation

> [Karakeep on AUR](https://aur.archlinux.org/packages/karakeep) is not maintained by the karakeep official.

1. Install karakeep

    ```shell
    paru -S karakeep
    ```

2. (**Optional**) Install optional dependencies

    ```shell
    # karakeep-cli: karakeep cli tool
    paru -S karakeep-cli

    # ollama: for automatic tagging
    sudo pacman -S ollama

    # yt-dlp: for download video
    sudo pacman -S yt-dlp
    ```

    You can use Open-AI instead of `ollama`. If you use `ollama`, you need to download the ollama model. Please refer to: [https://ollama.com/library](https://ollama.com/library).

3. Set up

    Environment variables can be set in `/etc/karakeep/karakeep.env` according to [configuration page](../03-configuration/01-environment-variables.md). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

4. Enable service

    ```shell
    sudo systemctl enable --now karakeep.target
    ```

    Then visit `http://localhost:3000` and you should be greated with the sign in page.

## Services and Ports

`karakeep.target` include 3 services: `karakeep-web.service`, `karakeep-works.service`, `karakeep-browser.service`.

- `karakeep-web.service`: Provide karakeep webui service, uses `3000` port by default.

- `karakeep-workers.service`: Provide karakeep workers service, no port.

- `karakeep-browser.service`: Provide browser headless service, uses `9222` port by default.

Now `karakeep` depends on `meilisearch`, and `karakeep-workers.service` wants `meilisearch.service`, starting `karakeep.target` will start `meilisearch.service` at the same time.

## How to Migrate from Hoarder to Karakeep

The PKGBUILD has been fully updated to replace all references to `hoarder` with `karakeep`. If you want to preserve your existing `hoarder` data during the upgrade, please follow the steps below:

**1. Stop the old services**

```shell
sudo systemctl stop hoarder-web.service hoarder-worker.service hoarder-browser.service
sudo systemctl disable --now hoarder.target
```

**2. Uninstall Hoarder**  
After uninstalling, you can manually remove the old `hoarder` user and group if needed.
```shell
paru -R hoarder
```

**3. Rename the old data directory**
```shell
sudo mv /var/lib/hoarder /var/lib/karakeep
```

**4. Install Karakeep**
```shell
paru -S karakeep
```

**5. Fix ownership of the data directory**
```shell
sudo chown -R karakeep:karakeep /var/lib/karakeep
```

**6. Set Karakeep**  
Edit `/etc/karakeep/karakeep.env` according to [configuration page](../03-configuration/01-environment-variables.md). **The environment variables that are not specified in `/etc/karakeep/karakeep.env` need to be added by yourself.**

Or you can copy old hoarder env file to karakeep:
```shell
sudo cp -f /etc/hoarder/hoarder.env /etc/karakeep/karakeep.env
```

**7. Start Karakeep**
```shell
sudo systemctl enable --now karakeep.target
```


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/04-kubernetes.md
==================================================
# Kubernetes

### Requirements

- A kubernetes cluster
- kubectl
- kustomize

### 1. Get the deployment manifests

You can clone the repository and copy the `/kubernetes` directory into another directory of your choice.

### 2. Populate the environment variables and secrets

To configure the app, copy the `.env_sample` to `.env` and change to your specific needs.

You should also change the `NEXTAUTH_URL` variable to point to your server address.

Using `KARAKEEP_VERSION=release` will pull the latest stable version. You might want to pin the version instead to control the upgrades (e.g. `KARAKEEP_VERSION=0.10.0`). Check the latest versions [here](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep).

To see all available configuration options check the [documentation](../03-configuration/01-environment-variables.md).

To configure the neccessary secrets for the application copy the `.secrets_sample` file to `.secrets` and change the sample secrets to your generated secrets.

> Note: You **should** change the random strings. You can use `openssl rand -base64 36` to generate the random strings. 

### 3. Setup OpenAI

To enable automatic tagging, you'll need to configure OpenAI. This is optional though but highly recommended.

- Follow [OpenAI's help](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to get an API key.
- Add the OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=<key>
```

Learn more about the costs of using openai [here](../06-administration/03-openai.md).

<details>
    <summary>[EXPERIMENTAL] If you want to use Ollama (https://ollama.com/) instead for local inference.</summary>

    **Note:** The quality of the tags you'll get will depend on the quality of the model you choose. Running local models is a recent addition and not as battle tested as using openai, so proceed with care (and potentially expect a bunch of inference failures).

    - Make sure ollama is running.
    - Set the `OLLAMA_BASE_URL` env variable to the address of the ollama API.
    - Set `INFERENCE_TEXT_MODEL` to the model you want to use for text inference in ollama (for example: `mistral`)
    - Set `INFERENCE_IMAGE_MODEL` to the model you want to use for image inference in ollama (for example: `llava`)
    - Make sure that you `ollama pull`-ed the models that you want to use.


</details>

### 4. Deploy the service

Deploy the service by running:

```
make deploy
```

### 5. Access the service

#### via LoadBalancer IP

By default, these manifests expose the application as a LoadBalancer Service. You can run `kubectl get services` to identify the IP of the loadbalancer for your service.

Then visit `http://<loadbalancer-ip>:3000` and you should be greated with the Sign In page.

> Note: Depending on your setup you might want to expose the service via an Ingress, or have a different means to access it.

#### Via Ingress

If you want to use an ingress, you can customize the sample ingress in the kubernetes folder and change the host to the DNS name of your choice.

After that you have to configure the web service to the type ClusterIP so it is only reachable via the ingress.

If you have already deployed the service you can patch the web service to the type ClusterIP with the following command:

` kubectl -n karakeep patch service web -p '{"spec":{"type":"ClusterIP"}}' `

Afterwards you can apply the ingress and access the service via your chosen URL.

#### Setting up HTTPS access to the Service

To access karakeep securely you can configure the ingress to use a preconfigured TLS certificate. This requires that you already have the needed files, namely your .crt and .key file, on hand.

After you have deployed the karakeep manifests you can deploy your certificate for karakeep in the `karakeep` namespace with this example command. You can name the secret however you want. But be aware that the secret name in the ingress definition has to match the secret name.

` $ kubectl --namespace karakeep create secret tls karakeep-web-tls --cert=/path/to/crt --key=/path/to/key `

If the secret is successfully created you can now configure the Ingress to use TLS via this changes to the spec:

```` yaml
 spec:
  tls:
  - hosts:
      - karakeep.example.com
    secretName: karakeep-web-tls
````

> Note: Be aware that the hosts have to match between the tls spec and the HTTP spec.

### [Optional] 6. Setup quick sharing extensions

Go to the [quick sharing page](../04-using-karakeep/quick-sharing.md) to install the mobile apps and the browser extensions. Those will help you hoard things faster!

## Updating

Edit the `KARAKEEP_VERSION` variable in the `kustomization.yaml` file and run `make clean deploy`.

If you have chosen `release` as the image tag you can also destroy the web pod, since the deployment has an ImagePullPolicy set to always the pod always pulls the image from the registry, this way we can ensure that the newest release image is pulled.


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/06-debuntu.md
==================================================
# Debian 12/Ubuntu 24.04

:::warning
This script is a stripped-down version of those found in the [Proxmox Community Scripts](https://github.com/community-scripts/ProxmoxVE) repo. It has been adapted to work on baremetal Debian 12 or Ubuntu 24.04 installs **only**. Any other use is not supported and you use this script at your own risk.
:::

### Requirements

- **Debian 12** (Buster) or
- **Ubuntu 24.04** (Noble Numbat)

The script will download and install all dependencies (except for Ollama), install Karakeep, do a basic configuration of Karakeep and Meilisearch (the search app used by Karakeep), and create and enable the systemd service files needed to run Karakeep on startup. Karakeep and Meilisearch are run in the context of their low-privilege user environments for more security.

The script functions as an update script in addition to an installer. See **[Updating](#updating)**.

### 1. Download the script from the [Karakeep repository](https://github.com/karakeep-app/karakeep/blob/main/karakeep-linux.sh)

```
wget https://raw.githubusercontent.com/karakeep-app/karakeep/main/karakeep-linux.sh
```

### 2. Run the script

> This script must be run as `root`, or as a user with `sudo` privileges.

    If this is a fresh install, then run the installer by using the following command:

    ```shell
    bash karakeep-linux.sh install
    ```

### 3. Create an account/sign in

    Then visit `http://localhost:3000` and you should be greated with the Sign In page.

## Updating

> This script must be run as `root`, or as a user with `sudo` privileges.

    If Karakeep has previously been installed using this script, then run the updater like so:

    ```shell
     bash karakeep-linux.sh update
    ```

## Services and Ports

`karakeep.target` includes 4 services: `meilisearch.service`, `karakeep-web.service`, `karakeep-workers.service`, `karakeep-browser.service`.

- `meilisearch.service`: Provides full-text search, Karakeep Workers service connects to it, uses port `7700` by default.

- `karakeep-web.service`: Provides the karakeep web service, uses `3000` port by default.

- `karakeep-workers.service`: Provides the karakeep workers service, no port.

- `karakeep-browser.service`: Provides the headless browser service, uses `9222` port by default.

## Configuration, ENV file, database locations

During installation, the script created a configuration file for `meilisearch`, an `ENV` file for Karakeep, and located config paths and database paths separate from the installation path of Karakeep, so as to allow for easier updating. Their names/locations are as follows:

- `/etc/meilisearch.toml` - a basic configuration for meilisearch, that contains configs for the database location, disabling analytics, and using a master key, which prevents unauthorized connections.
- `/var/lib/meilisearch` - Meilisearch DB location.
- `/etc/karakeep/karakeep.env` - The Karakeep `ENV` file. Edit this file to configure Karakeep beyond the default. The web service and the workers service need to be restarted after editing this file:

    ```shell
    sudo systemctl restart karakeep-workers karakeep-web
    ```

- `/var/lib/karakeep` - The Karakeep database location. If you delete the contents of this folder you will lose all your data.

## Still Running Hoarder?

There is a way to upgrade. Please see [Hoarder to Karakeep Migration](../06-administration/08-hoarder-to-karakeep-migration.md)


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/07-minimal-install.md
==================================================
# Minimal Installation

:::warning
Unless necessary, prefer the [full installation](/installation/docker) to leverage all the features of Karakeep. You'll be sacrificing a lot of functionality if you go with the minimal installation route.
:::

Karakeep's default installation has a dependency on Meilisearch for the full text search, Chrome for crawling and OpenAI/Ollama for AI tagging. You can however run Karakeep without those dependencies if you're willing to sacrifice those features.

- If you run without meilisearch, the search functionality will be completely disabled.
- If you run without chrome, crawling will still work, but you'll lose ability to take screenshots of websites and websites with javascript content won't get crawled correctly.
- If you don't setup OpenAI/Ollama, AI tagging will be disabled.

Those features are important for leveraging Karakeep's full potential, but if you're running in constrained environments, you can use the following minimal docker compose to skip all those dependencies:

```yaml
services:
  web:
    image: ghcr.io/karakeep-app/karakeep:release
    restart: unless-stopped
    volumes:
      - data:/data
    ports:
      - 3000:3000
    environment:
      DATA_DIR: /data
      NEXTAUTH_SECRET: super_random_string
volumes:
  data:
```

Or just with the following docker command:

```base
docker run -d \
  --restart unless-stopped \
  -v data:/data \
  -p 3000:3000 \
  -e DATA_DIR=/data \
  -e NEXTAUTH_SECRET=super_random_string \
  ghcr.io/karakeep-app/karakeep:release
```

:::warning
You **MUST** change the `super_random_string` to a true random string which you can generate with `openssl rand -hex 32`.
:::

Check the [configuration docs](../03-configuration/01-environment-variables.md) for extra features to enable such as full page archival, full page screenshots, inference languages, etc.


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/08-truenas.md
==================================================
# TrueNAS

Karakeep is available directly from TrueNAS's app catalog ([link](https://apps.truenas.com/catalog/karakeep/)).


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/09-cloud-hosting.md
==================================================
# Karakeep Cloud

:::tip
If you want to use Karakeep without running your own servers, the hosted cloud option is the fastest way to start.
:::

[Karakeep Cloud](https://cloud.karakeep.app) is the fully managed version of Karakeep operated by the core team. It handles hosting, updates, monitoring, and backups for you, so you can focus on saving content instead of maintaining infrastructure.

### Get started

1. Visit [cloud.karakeep.app](https://cloud.karakeep.app) and create an account.
2. Follow the onboarding flow to create your workspace.
3. Install the browser extension or mobile apps from the [quick sharing page](../04-using-karakeep/quick-sharing.md) and start saving links immediately.


==================================================
File: docs/versioned_docs/version-v0.30.0/02-installation/10-pikapods.md
==================================================
# PikaPods

:::info
Note: PikaPods shares some of its revenue from hosting Karakeep with the maintainer of this project.
:::

[PikaPods](https://www.pikapods.com/) offers managed paid hosting for many open source apps, including Karakeep.
Server administration, updates, migrations and backups are all taken care of, which makes it well suited
for less technical users. As of Nov 2024, running Karakeep there will cost you ~$3 per month.

### Requirements

- A _PikaPods_ account. Can be created for free [here](https://www.pikapods.com/register). You get an initial welcome credit of $5.

### 1. Choose app

Choose _Karakeep_ from their [list of apps](https://www.pikapods.com/apps) or use this [direct link](https://www.pikapods.com/pods?run=hoarder). This will either
open a new dialog to add a new _Karakeep_ pod or ask you to log in.

### 2. Add settings

There are a few settings to configure in the dialog:

- **Basics**: Give the pod a name and choose a region that's near you.
- **Env Vars**: Here you can disable signups or set an OpenAI API key. All settings are optional.
- **Resources**: The resources your _Karakeep_ pod can use. The defaults are fine, unless you have a very large collection.

### 3. Start pod and add user

After hitting _Add pod_ it will take about a minute for the app to fully start. After this you can visit
the pod's URL and add an initial user under _Sign Up_. After this you may want to disable further sign-ups
by setting the pod's `DISABLE_SIGNUPS` _Env Var_ to `true`.


==================================================
File: docs/versioned_docs/version-v0.30.0/03-configuration/01-environment-variables.md
==================================================
# Configuration

The app is mainly configured by environment variables. All the used environment variables are listed in [packages/shared/config.ts](https://github.com/karakeep-app/karakeep/blob/main/packages/shared/config.ts). The most important ones are:

| Name                                   | Required                              | Default         | Description                                                                                                                                                                                                                                                            |
| -------------------------------------- | ------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PORT                                   | No                                    | 3000            | The port on which the web server will listen. DON'T CHANGE THIS IF YOU'RE USING DOCKER, instead changed the docker bound external port.                                                                                                                                |
| WORKERS_PORT                           | No                                    | 0 (Random Port) | The port on which the worker will export its prometheus metrics on `/metrics`. By default it's a random unused port. If you want to utilize those metrics, fix the port to a value (and export it in docker if you're using docker).                                   |
| WORKERS_HOST                           | No                                    | 127.0.0.1       | Host to listen to for requests to WORKERS_PORT. You will need to set this if running in a container, since localhost will not be reachable from outside                                                                                                                |
| WORKERS_ENABLED_WORKERS                | No                                    | Not set         | Comma separated list of worker names to enable. If set, only these workers will run. Valid values: crawler,inference,search,adminMaintenance,video,feed,assetPreprocessing,webhook,ruleEngine.                                                                         |
| WORKERS_DISABLED_WORKERS               | No                                    | Not set         | Comma separated list of worker names to disable. Takes precedence over `WORKERS_ENABLED_WORKERS`.                                                                                                                                                                      |
| LOG_LEVEL                              | No                                    | debug           | The application log level as defined in the [winston documentation](https://github.com/winstonjs/winston?tab=readme-ov-file#logging-levels). You may want to set this to `notice` or `warning` when running Karakeep in a production environment.                      |
| DATA_DIR                               | Yes                                   | Not set         | The path for the persistent data directory. This is where the db lives. Assets are stored here by default unless `ASSETS_DIR` is set.                                                                                                                                  |
| ASSETS_DIR                             | No                                    | Not set         | The path where crawled assets will be stored. If not set, defaults to `${DATA_DIR}/assets`.                                                                                                                                                                            |
| NEXTAUTH_URL                           | Yes                                   | Not set         | Should point to the address of your server. The app will function without it, but will redirect you to wrong addresses on signout for example.                                                                                                                         |
| NEXTAUTH_SECRET                        | Yes                                   | Not set         | Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`.                                                                                                                                                                                |
| MEILI_ADDR                             | No                                    | Not set         | The address of meilisearch. If not set, Search will be disabled. E.g. (`http://meilisearch:7700`)                                                                                                                                                                      |
| MEILI_MASTER_KEY                       | Only in Prod and if search is enabled | Not set         | The master key configured for meilisearch. Not needed in development environment. Generate one with `openssl rand -base64 36 \| tr -dc 'A-Za-z0-9'`                                                                                                                    |
| MAX_ASSET_SIZE_MB                      | No                                    | 50              | Sets the maximum allowed asset size (in MB) to be uploaded                                                                                                                                                                                                             |
| DISABLE_NEW_RELEASE_CHECK              | No                                    | false           | If set to true, latest release check will be disabled in the admin panel.                                                                                                                                                                                              |
| RATE_LIMITING_ENABLED                  | No                                    | false           | If set to true, API rate limiting will be enabled.                                                                                                                                                                                                                     |
| CRAWLER_DOMAIN_RATE_LIMIT_WINDOW_MS    | No                                    | Not set         | Time window in milliseconds for per-domain crawler rate limiting.                                                                                                                                                                                                      |
| CRAWLER_DOMAIN_RATE_LIMIT_MAX_REQUESTS | No                                    | Not set         | Maximum crawler requests allowed per domain inside the configured window.                                                                                                                                                                                              |
| DB_WAL_MODE                            | No                                    | false           | Enables WAL mode for the sqlite database. This should improve the performance of the database. There's no reason why you shouldn't set this to true unless you're running the db on a network attached drive. This will become the default at some time in the future. |
| SEARCH_NUM_WORKERS                     | No                                    | 1               | Number of concurrent workers for search indexing tasks. Increase this if you have a high volume of content being indexed for search.                                                                                                                                   |
| SEARCH_JOB_TIMEOUT_SEC                 | No                                    | 30              | How long to wait for a search indexing job to finish before timing out. Increase this if you have large bookmarks with extensive content that takes longer to index.                                                                                                   |
| WEBHOOK_NUM_WORKERS                    | No                                    | 1               | Number of concurrent workers for webhook delivery. Increase this if you have multiple webhook endpoints or high webhook traffic.                                                                                                                                       |
| ASSET_PREPROCESSING_NUM_WORKERS        | No                                    | 1               | Number of concurrent workers for asset preprocessing tasks (image processing, OCR, etc.). Increase this if you have many images or documents that need processing.                                                                                                     |
| ASSET_PREPROCESSING_JOB_TIMEOUT_SEC    | No                                    | 60              | How long to wait for an asset preprocessing job to finish before timing out. Increase this if you have large images or PDFs that take longer to process.                                                                                                               |
| RULE_ENGINE_NUM_WORKERS                | No                                    | 1               | Number of concurrent workers for rule engine processing. Increase this if you have complex automation rules that need to be processed quickly.                                                                                                                         |
| MAX_RSS_FEEDS_PER_USER                 | No                                    | 1000            | The maximum number of RSS feeds a user can create.                                                                                                                                                                                                                     |
| MAX_WEBHOOKS_PER_USER                  | No                                    | 100             | The maximum number of webhooks a user can create.                                                                                                                                                                                                                      |

## Asset Storage

Karakeep supports two storage backends for assets: local filesystem (default) and S3-compatible object storage. S3 storage is automatically detected when an S3 endpoint is passed.

| Name                             | Required          | Default | Description                                                                                               |
| -------------------------------- | ----------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| ASSET_STORE_S3_ENDPOINT          | No                | Not set | The S3 endpoint URL. Required for S3-compatible services like MinIO. **Setting this enables S3 storage**. |
| ASSET_STORE_S3_REGION            | No                | Not set | The S3 region to use.                                                                                     |
| ASSET_STORE_S3_BUCKET            | Yes when using S3 | Not set | The S3 bucket name where assets will be stored.                                                           |
| ASSET_STORE_S3_ACCESS_KEY_ID     | Yes when using S3 | Not set | The S3 access key ID for authentication.                                                                  |
| ASSET_STORE_S3_SECRET_ACCESS_KEY | Yes when using S3 | Not set | The S3 secret access key for authentication.                                                              |
| ASSET_STORE_S3_FORCE_PATH_STYLE  | No                | false   | Whether to force path-style URLs for S3 requests. Set to true for MinIO and other S3-compatible services. |

:::info
When using S3 storage, make sure the bucket exists and the provided credentials have the necessary permissions to read, write, and delete objects in the bucket.
:::

:::warning
Switching between storage backends after data has been stored will require manual migration of existing assets. Plan your storage backend choice carefully before deploying.
:::

## Authentication / Signup

By default, Karakeep uses the database to store users, but it is possible to also use OAuth.
The flags need to be provided to the `web` container.

:::info
Only OIDC compliant OAuth providers are supported! For information on how to set it up, consult the documentation of your provider.
:::

:::info
When setting up OAuth, the allowed redirect URLs configured at the provider should be set to `<KARAKEEP_ADDRESS>/api/auth/callback/custom` where `<KARAKEEP_ADDRESS>` is the address you configured in `NEXTAUTH_URL` (for example: `https://try.karakeep.app/api/auth/callback/custom`).
:::

| Name                                        | Required | Default                | Description                                                                                                                                                                                           |
| ------------------------------------------- | -------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DISABLE_SIGNUPS                             | No       | false                  | If enabled, no new signups will be allowed and the signup button will be disabled in the UI                                                                                                           |
| DISABLE_PASSWORD_AUTH                       | No       | false                  | If enabled, only signups and logins using OAuth are allowed and the signup button and login form for local accounts will be disabled in the UI                                                        |
| EMAIL_VERIFICATION_REQUIRED                 | No       | false                  | Whether email verification is required during user signup. If enabled, users must verify their email address before they can use their account. If you enable this, you must configure SMTP settings. |
| OAUTH_WELLKNOWN_URL                         | No       | Not set                | The "wellknown Url" for openid-configuration as provided by the OAuth provider                                                                                                                        |
| OAUTH_CLIENT_SECRET                         | No       | Not set                | The "Client Secret" as provided by the OAuth provider                                                                                                                                                 |
| OAUTH_CLIENT_ID                             | No       | Not set                | The "Client ID" as provided by the OAuth provider                                                                                                                                                     |
| OAUTH_SCOPE                                 | No       | "openid email profile" | "Full list of scopes to request (space delimited)"                                                                                                                                                    |
| OAUTH_PROVIDER_NAME                         | No       | "Custom Provider"      | The name of your provider. Will be shown on the signup page as "Sign in with `<name>`"                                                                                                                |
| OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING | No       | false                  | Whether existing accounts in karakeep stored in the database should automatically be linked with your OAuth account. Only enable it if you trust the OAuth provider!                                  |
| OAUTH_TIMEOUT                               | No       | 3500                   | The wait time in milliseconds for the OAuth provider response. Increase this if you are having `outgoing request timed out` errors                                                                    |

For more information on `OAUTH_ALLOW_DANGEROUS_EMAIL_ACCOUNT_LINKING`, check the [next-auth.js documentation](https://next-auth.js.org/configuration/providers/oauth#allowdangerousemailaccountlinking-option).

## Inference Configs (For automatic tagging)

Either `OPENAI_API_KEY` or `OLLAMA_BASE_URL` need to be set for automatic tagging to be enabled. Otherwise, automatic tagging will be skipped.

:::warning

- The quality of the tags you'll get will depend on the quality of the model you choose.
- You might want to tune the `INFERENCE_CONTEXT_LENGTH` as the default is quite small. The larger the value, the better the quality of the tags, but the more expensive the inference will be (money-wise on OpenAI and resource-wise on ollama).
  :::

| Name                                 | Required | Default                | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAI_API_KEY                       | No       | Not set                | The OpenAI key used for automatic tagging. More on that in [here](../06-administration/03-openai.md).                                                                                                                                                                                                                                                                                            |
| OPENAI_BASE_URL                      | No       | Not set                | If you just want to use OpenAI you don't need to pass this variable. If, however, you want to use some other openai compatible API (e.g. azure openai service), set this to the url of the API.                                                                                                                                                                                       |
| OPENAI_PROXY_URL                     | No       | Not set                | HTTP proxy server URL for OpenAI API requests (e.g., `http://proxy.example.com:8080`).                                                                                                                                                                                                                                                                                                |
| OLLAMA_BASE_URL                      | No       | Not set                | If you want to use ollama for local inference, set the address of ollama API here.                                                                                                                                                                                                                                                                                                    |
| OLLAMA_KEEP_ALIVE                    | No       | Not set                | Controls how long the model will stay loaded into memory following the request (examples: "5m" for 5 minutes, "-1m" to keep the model loaded indefinitely, "0" to unload the model instantly after processing is complete).                                                                                                                                                                                                                                                                                 |
| INFERENCE_TEXT_MODEL                 | No       | gpt-4.1-mini           | The model to use for text inference. You'll need to change this to some other model if you're using ollama.                                                                                                                                                                                                                                                                           |
| INFERENCE_IMAGE_MODEL                | No       | gpt-4o-mini            | The model to use for image inference. You'll need to change this to some other model if you're using ollama and that model needs to support vision APIs (e.g. llava).                                                                                                                                                                                                                 |
| EMBEDDING_TEXT_MODEL                 | No       | text-embedding-3-small | The model to be used for generating embeddings for the text.                                                                                                                                                                                                                                                                                                                          |
| INFERENCE_CONTEXT_LENGTH             | No       | 2048                   | The max number of tokens that we'll pass to the inference model. If your content is larger than this size, it'll be truncated to fit. The larger this value, the more of the content will be used in tag inference, but the more expensive the inference will be (money-wise on openAI and resource-wise on ollama). Check the model you're using for its max supported content size. |
| INFERENCE_MAX_OUTPUT_TOKENS          | No       | 2048                   | The maximum number of tokens that the inference model is allowed to generate in its response. This controls the length of AI-generated content like tags and summaries. Increase this if you need longer responses, but be aware that higher values will increase costs (for OpenAI) and processing time.                                                                             |
| INFERENCE_USE_MAX_COMPLETION_TOKENS  | No       | false                  | \[OpenAI Only\] Whether to use the newer `max_completion_tokens` parameter instead of the deprecated `max_tokens` parameter. Set to `true` if using GPT-5 or o-series models which require this. Will become the default in a future release.                                                                                                                                         |
| INFERENCE_LANG                       | No       | english                | The language in which the tags will be generated.                                                                                                                                                                                                                                                                                                                                     |
| INFERENCE_NUM_WORKERS                | No       | 1                      | Number of concurrent workers for AI inference tasks (tagging and summarization). Increase this if you have multiple AI inference requests and want to process them in parallel.                                                                                                                                                                                                       |
| INFERENCE_ENABLE_AUTO_TAGGING        | No       | true                   | Whether automatic AI tagging is enabled or disabled.                                                                                                                                                                                                                                                                                                                                  |
| INFERENCE_ENABLE_AUTO_SUMMARIZATION  | No       | false                  | Whether automatic AI summarization is enabled or disabled.                                                                                                                                                                                                                                                                                                                            |
| INFERENCE_JOB_TIMEOUT_SEC            | No       | 30                     | How long to wait for the inference job to finish before timing out. If you're running ollama without powerful GPUs, you might want to increase the timeout a bit.                                                                                                                                                                                                                     |
| INFERENCE_FETCH_TIMEOUT_SEC          | No       | 300                    | \[Ollama Only\] The timeout of the fetch request to the ollama server. If your inference requests take longer than the default 5mins, you might want to increase this timeout.                                                                                                                                                                                                        |
| INFERENCE_SUPPORTS_STRUCTURED_OUTPUT | No       | Not set                | \[DEPRECATED\] Whether the inference model supports structured output or not. Use INFERENCE_OUTPUT_SCHEMA instead. Setting this to true translates to INFERENCE_OUTPUT_SCHEMA=structured, and to false translates to INFERENCE_OUTPUT_SCHEMA=plain.                                                                                                                                   |
| INFERENCE_OUTPUT_SCHEMA              | No       | structured             | Possible values are "structured", "json", "plain". Structured is the preferred option, but if your model doesn't support it, you can use "json" if your model supports JSON mode, otherwise "plain" which should be supported by all the models but the model might not output the data in the correct format.                                                                        |

:::info

- You can append additional instructions to the prompt used for automatic tagging, in the `AI Settings` (in the `User Settings` screen)
- You can use the placeholders `$tags`, `$aiTags`, `$userTags` in the prompt. These placeholders will be replaced with all tags, ai generated tags or human created tags when automatic tagging is performed (e.g. `[karakeep, computer, ai]`)
  :::

## Crawler Configs

| Name                                     | Required | Default   | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_NUM_WORKERS                      | No       | 1         | Number of allowed concurrent crawling jobs. By default, we're only doing one crawling request at a time to avoid consuming a lot of resources.                                                                                                                                                                                                                                |
| BROWSER_WEB_URL                          | No       | Not set   | The browser's http debugging address. The worker will talk to this endpoint to resolve the debugging console's websocket address. If you already have the websocket address, use `BROWSER_WEBSOCKET_URL` instead. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution. |
| BROWSER_WEBSOCKET_URL                    | No       | Not set   | The websocket address of browser's debugging console. If you want to use [browserless](https://browserless.io), use their websocket address here. If neither `BROWSER_WEB_URL` nor `BROWSER_WEBSOCKET_URL` are set, the worker will use plain http requests skipping screenshotting and javascript execution.                                                                 |
| BROWSER_CONNECT_ONDEMAND                 | No       | false     | If set to false, the crawler will proactively connect to the browser instance and always maintain an active connection. If set to true, the browser will be launched on demand only whenever a crawling is requested. Set to true if you're using a service that provides you with browser instances on demand.                                                               |
| CRAWLER_DOWNLOAD_BANNER_IMAGE            | No       | true      | Whether to cache the banner image used in the cards locally or fetch it each time directly from the website. Caching it consumes more storage space, but is more resilient against link rot and rate limits from websites.                                                                                                                                                    |
| CRAWLER_STORE_SCREENSHOT                 | No       | true      | Whether to store a screenshot from the crawled website or not. Screenshots act as a fallback for when we fail to extract an image from a website. You can also view the stored screenshots for any link.                                                                                                                                                                      |
| CRAWLER_FULL_PAGE_SCREENSHOT             | No       | false     | Whether to store a screenshot of the full page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, the screenshot will only include the visible part of the page                                                                                                                                                                              |
| CRAWLER_SCREENSHOT_TIMEOUT_SEC           | No       | 5         | How long to wait for the screenshot finish before timing out. If you are capturing full-page screenshots of long webpages, consider increasing this value.                                                                                                                                                                                                                    |
| CRAWLER_STORE_PDF                        | No       | false     | Whether to store a PDF snapshot of the crawled page. Disabled by default, as it can lead to much higher disk usage. When enabled, a PDF version of each crawled page will be captured and stored as an asset, which can be viewed in the bookmark preview.                                                                                                                    |
| CRAWLER_FULL_PAGE_ARCHIVE                | No       | false     | Whether to store a full local copy of the page or not. Disabled by default, as it can lead to much higher disk usage. If disabled, only the readable text of the page is archived.                                                                                                                                                                                            |
| CRAWLER_JOB_TIMEOUT_SEC                  | No       | 60        | How long to wait for the crawler job to finish before timing out. If you have a slow internet connection or a low powered device, you might want to bump this up a bit                                                                                                                                                                                                        |
| CRAWLER_NAVIGATE_TIMEOUT_SEC             | No       | 30        | How long to spend navigating to the page (along with its redirects). Increase this if you have a slow internet connection                                                                                                                                                                                                                                                     |
| CRAWLER_VIDEO_DOWNLOAD                   | No       | false     | Whether to download videos from the page or not (using yt-dlp)                                                                                                                                                                                                                                                                                                                |
| CRAWLER_VIDEO_DOWNLOAD_MAX_SIZE          | No       | 50        | The maximum file size for the downloaded video. The quality will be chosen accordingly. Use -1 to disable the limit.                                                                                                                                                                                                                                                          |
| CRAWLER_VIDEO_DOWNLOAD_TIMEOUT_SEC       | No       | 600       | How long to wait for the video download to finish                                                                                                                                                                                                                                                                                                                             |
| CRAWLER_ENABLE_ADBLOCKER                 | No       | true      | Whether to enable an adblocker in the crawler or not. If you're facing troubles downloading the adblocking lists on worker startup, you can disable this.                                                                                                                                                                                                                     |
| CRAWLER_YTDLP_ARGS                       | No       | []        | Include additional yt-dlp arguments to be passed at crawl time separated by %%: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#general-options                                                                                                                                                                                                                           |
| BROWSER_COOKIE_PATH                      | No       | Not set   | Path to a JSON file containing cookies to be loaded into the browser context. The file should be an array of cookie objects, each with name and value (required), and optional fields like domain, path, expires, httpOnly, secure, and sameSite (e.g., `[{"name": "session", "value": "xxx", "domain": ".example.com"}`]).                                                   |
| HTML_CONTENT_SIZE_INLINE_THRESHOLD_BYTES | No       | 5 \* 1024 | The thresholds in bytes after which larger assets will be stored in the assetdb (folder/s3) instead of inline in the database.                                                                                                                                                                                                                                                |

<details>

  <summary>More info on BROWSER_COOKIE_PATH</summary>

BROWSER_COOKIE_PATH specifies the path to a JSON file containing cookies to be loaded into the browser context for crawling.

The JSON file must be an array of cookie objects, each with:

- name: The cookie name (required).
- value: The cookie value (required).
- Optional fields: domain, path, expires, httpOnly, secure, sameSite (values: "Strict", "Lax", or "None").

Example JSON file:

```json
[
  {
    "name": "session",
    "value": "xxx",
    "domain": ".example.com",
    "path": "/",
    "expires": 1735689600,
    "httpOnly": true,
    "secure": true,
    "sameSite": "Lax"
  }
]
```

</details>

## OCR Configs

Karakeep uses [tesseract.js](https://github.com/naptha/tesseract.js) to extract text from images.

| Name                     | Required | Default   | Description                                                                                                                                                                                                                               |
| ------------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OCR_CACHE_DIR            | No       | $TEMP_DIR | The dir where tesseract will download its models. By default, those models are not persisted and stored in the OS' temp dir.                                                                                                              |
| OCR_LANGS                | No       | eng       | Comma separated list of the language codes that you want tesseract to support. You can find the language codes [here](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html). Set to empty string to disable OCR. |
| OCR_CONFIDENCE_THRESHOLD | No       | 50        | A number between 0 and 100 indicating the minimum acceptable confidence from tessaract. If tessaract's confidence is lower than this value, extracted text won't be stored.                                                               |

## Webhook Configs

You can use webhooks to trigger actions when bookmarks are created, changed or crawled.

| Name                | Required | Default | Description                                       |
| ------------------- | -------- | ------- | ------------------------------------------------- |
| WEBHOOK_TIMEOUT_SEC | No       | 5       | The timeout for the webhook request in seconds.   |
| WEBHOOK_RETRY_TIMES | No       | 3       | The number of times to retry the webhook request. |

:::info

- The WEBHOOK_TOKEN is used for authentication. It will appear in the Authorization header as Bearer token.
  ```
  Authorization: Bearer <WEBHOOK_TOKEN>
  ```
- The webhook will be triggered with the job id (used for idempotence), bookmark id, bookmark type, the user id, the url and the operation in JSON format in the body.

  ```json
  {
    "jobId": "123",
    "type": "link",
    "bookmarkId": "exampleBookmarkId",
    "userId": "exampleUserId",
    "url": "https://example.com",
    "operation": "crawled"
  }
  ```

  :::

## SMTP Configuration

Karakeep can send emails for various purposes such as email verification during signup. Configure these settings to enable email functionality.

| Name          | Required | Default | Description                                                                                     |
| ------------- | -------- | ------- | ----------------------------------------------------------------------------------------------- |
| SMTP_HOST     | No       | Not set | The SMTP server hostname or IP address. Required if you want to enable email functionality.     |
| SMTP_PORT     | No       | 587     | The SMTP server port. Common values are 587 (STARTTLS), 465 (SSL/TLS), or 25 (unencrypted).     |
| SMTP_SECURE   | No       | false   | Whether to use SSL/TLS encryption. Set to true for port 465, false for port 587 with STARTTLS.  |
| SMTP_USER     | No       | Not set | The username for SMTP authentication. Usually your email address.                               |
| SMTP_PASSWORD | No       | Not set | The password for SMTP authentication. For services like Gmail, use an app-specific password.    |
| SMTP_FROM     | No       | Not set | The "from" email address that will appear in sent emails. This should be a valid email address. |

## Proxy Configuration

If your Karakeep instance needs to connect through a proxy server, you can configure the following settings:

| Name                               | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRAWLER_HTTP_PROXY                 | No       | Not set | HTTP proxy server URL for outgoing HTTP requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                                                           |
| CRAWLER_HTTPS_PROXY                | No       | Not set | HTTPS proxy server URL for outgoing HTTPS requests (e.g., `http://proxy.example.com:8080`). You can pass multiple comma separated proxies and the used one will be chosen at random. The proxy is used for crawling, RSS feed fetches and webhooks.                                                                                                                                                                                                                                                                         |
| CRAWLER_NO_PROXY                   | No       | Not set | Comma-separated list of hostnames/IPs that should bypass the proxy (e.g., `localhost,127.0.0.1,.local`)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CRAWLER_ALLOWED_INTERNAL_HOSTNAMES | No       | Not set | By default, Karakeep blocks worker-initiated requests whose DNS resolves to private, loopback, link-local, or Tailscale CGNAT IP addresses. Use this to allowlist specific hostnames for internal access (e.g., `internal.company.com`, `app-name.local`). Supports domain wildcards by prefixing with a dot (e.g., `.internal.company.com`, `.<tailnet-name>.ts.net`). Passing `.` allowlists all domains. Note: Internal IP validation is bypassed when a proxy is configured for the URL as the local DNS resolver won't necessarily be the same as the one used by the proxy. |

:::info
These proxy settings will be used by the crawler and other components that make outgoing HTTP requests.
:::

## Monitoring

Karakeep supports distributed tracing via OpenTelemetry. When enabled, traces are collected for tRPC API calls, background worker operations, and other key workflows. Karakeep also exports prometheus-based metrics.

| Name                        | Required | Default  | Description                                                                                                                                                                                                                                                                                                             |
| --------------------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OTEL_TRACING_ENABLED        | No       | false    | Set to `true` to enable OpenTelemetry tracing. When disabled, all tracing operations are no-ops.                                                                                                                                                                                                                        |
| OTEL_EXPORTER_OTLP_ENDPOINT | No       | Not set  | The OTLP HTTP endpoint to send traces to (e.g., `http://jaeger:4318/v1/traces` or `http://otel-collector:4318/v1/traces`). If not set, traces are logged to the console.                                                                                                                                                |
| OTEL_SERVICE_NAME           | No       | karakeep | The service name that will appear in your tracing backend. The actual service name will include a suffix (e.g., `karakeep-api`, `karakeep-workers`).                                                                                                                                                                    |
| OTEL_SAMPLE_RATE            | No       | 1.0      | The sampling rate for traces, between 0.0 and 1.0. A value of 1.0 means all traces are sampled, while 0.1 means only 10% of traces are sampled. Lower values reduce overhead and storage costs in production.                                                                                                           |
| PROMETHEUS_AUTH_TOKEN       | No       | Random   | Enable a prometheus metrics endpoint at `/api/metrics`. This endpoint will require this token being passed in the Authorization header as a Bearer token. If not set, a new random token is generated everytime at startup. This cannot contain any special characters or you may encounter a 400 Bad Request response. |


==================================================
File: docs/versioned_docs/version-v0.30.0/03-configuration/02-different-ai-providers.md
==================================================
# Configuring different AI Providers

Karakeep uses LLM providers for AI tagging and summarization. We support OpenAI-compatible providers and ollama. This guide will show you how to configure different providers.

## OpenAI

If you want to use OpenAI itself, you just need to pass in the OPENAI_API_KEY environment variable.

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# You can change the default models by uncommenting the following lines, and choosing your model.
# INFERENCE_TEXT_MODEL=gpt-4.1-mini
# INFERENCE_IMAGE_MODEL=gpt-4o-mini
```

## Ollama

Ollama is a local LLM provider that you can use to run your own LLM server. You'll need to pass ollama's address to karakeep and you need to ensure that it's accessible from within the karakeep container (e.g. no localhost addresses).

```
# MAKE SURE YOU DON'T HAVE OPENAI_API_KEY set, otherwise it takes precedence.

OLLAMA_BASE_URL=http://ollama.mylab.com:11434

# Make sure to pull the models in ollama first. Example models:
INFERENCE_TEXT_MODEL=gemma3
INFERENCE_IMAGE_MODEL=llava

# If the model you're using doesn't support structured output, you also need:
# INFERENCE_OUTPUT_SCHEMA=plain
```

## Gemini

Gemini has an OpenAI-compatible API. You need to get an api key from Google AI Studio.

```

OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=gemini-2.0-flash
INFERENCE_IMAGE_MODEL=gemini-2.0-flash
```

## OpenRouter

```
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=YOUR_API_KEY

# Example models:
INFERENCE_TEXT_MODEL=meta-llama/llama-4-scout
INFERENCE_IMAGE_MODEL=meta-llama/llama-4-scout
```

## Perplexity

```
OPENAI_BASE_URL: https://api.perplexity.ai
OPENAI_API_KEY: Your Perplexity API Key
INFERENCE_TEXT_MODEL: sonar-pro
INFERENCE_IMAGE_MODEL: sonar-pro
```

## Azure

Azure has an OpenAI-compatible API.

You can get your API key from the Overview page of the Azure AI Foundry Portal or via "Keys + Endpoints" on the resource in the Azure Portal.

:::warning
The [model name is the deployment name](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/switching-endpoints#keyword-argument-for-model) you specified when deploying the model, which may differ from the base model name.
:::

```
# Deployed via Azure AI Foundry:
OPENAI_BASE_URL=https://{your-azure-ai-foundry-resource-name}.cognitiveservices.azure.com/openai/v1/

# Deployed via Azure OpenAI Service:
OPENAI_BASE_URL=https://{your-azure-openai-resource-name}.openai.azure.com/openai/v1/

OPENAI_API_KEY=YOUR_API_KEY
INFERENCE_TEXT_MODEL=YOUR_DEPLOYMENT_NAME
INFERENCE_IMAGE_MODEL=YOUR_DEPLOYMENT_NAME
```


==================================================
File: docs/versioned_docs/version-v0.30.0/04-using-karakeep/advanced-workflows.md
==================================================
---
sidebar_position: 10
slug: advanced-workflows
---

# Advanced workflows

Push Karakeep further with automation and integrations.

## Rule engine

- Create if-this-then-that style rules to auto-tag, favourite, or route bookmarks into lists based on metadata or content.
- Useful for keeping inboxes tidy (e.g. auto-archive newsletters, auto-tag domains, or flag videos).

## API

- Use the API to script imports, syncs, or custom tools. Same surface area the apps use.
- Great for integrating with personal scripts, cron jobs, or other services.

## Webhooks

- Subscribe to bookmark events and trigger your own systems when something is added, updated, or archived.
- Pair with the API to build end-to-end automations (e.g. push new saves into a writing queue or a team chat).


==================================================
File: docs/versioned_docs/version-v0.30.0/04-using-karakeep/bookmarking.md
==================================================
---
sidebar_position: 1
slug: bookmarking
---

# Bookmarking

Everything in Karakeep starts as a bookmark. Here’s how the different types work and how to keep your home view tidy with favourites and archive.

## Favourites

- Star bookmarks you like so they sit in their own dedicated favourites view for quick return visits.
- Handy for saved gems you want to re-open often like articles you enjoyed, references you come back to, or things worth sharing.

## Archiving

- Archive hides a bookmark from the homepage without deleting it.
- Archived items stay searchable and keep all tags, highlights, and attachments.
- Ideal for achieving inbox-zero style for your homepage.

## Bookmark types

- **Links**: URLs saved from the web or extension. Karakeep grabs metadata, previews, screenshots, and archives when configured.
- **Text**: Quick notes or snippets you paste in. Great for ideas, quotes, or saving context alongside links.
- **Media**: Images or PDFs you want to save for later. Karakeep automatically extracts content out of those files and makes them searchable.

## Notes

- Attach personal notes to any bookmark to capture context, reminders, or next steps.
- Notes live with the bookmark and are searchable, so you can recall why something mattered.

## Highlights

- Save quotes, summaries, or TODOs while reading.
- Highlights show up in the bookmark detail view/reader and are searchable, so you can jump straight to the key ideas.

## Attachments

- Store extra context alongside a bookmark: screenshots, page captures, videos, and files you upload.
- **Screenshots & archives**: fallback when the original page changes or disappear.
- **Uploaded files**: keep PDFs, notes, or supporting assets right with the link.
- Manage attachments from the bookmark detail view: upload, download, or detach as needed.


==================================================
File: docs/versioned_docs/version-v0.30.0/04-using-karakeep/import.md
==================================================
---
sidebar_position: 8
slug: import
---

# Import your library


Karakeep supports importing bookmarks using the Netscape HTML Format, Pocket's new CSV format & Omnivore's JSONs. Titles, tags and addition date will be preserved during the import. An automatically created list will contain all the imported bookmarks.

:::info
All the URLs in the bookmarks file will be added automatically, you will not be able to pick and choose which bookmarks to import!
:::

## Import from Chrome

- Open Chrome and go to `chrome://bookmarks`
- Click on the three dots on the top right corner and choose `Export bookmarks`
- This will download an html file with all of your bookmarks.
- To import the bookmark file, go to the settings and click "Import Bookmarks from HTML file".

## Import from Firefox
- Open Firefox and click on the menu button (☰) in the top right corner.
- Navigate to Bookmarks > Manage bookmarks (or press Ctrl + Shift + O / Cmd + Shift + O to open the Bookmarks Library).
- In the Bookmarks Library, click the Import and Backup button at the top. Select Export Bookmarks to HTML... to save your bookmarks as an HTML file.
- To import a bookmark file, go back to the Import and Backup menu, then select Import Bookmarks from HTML... and choose your saved HTML file.

## Import from Pocket

- Go to the [Pocket export page](https://getpocket.com/export) and follow the instructions to export your bookmarks.
- Pocket after a couple of minutes will mail you a zip file with all the bookmarks.
- Unzip the file and you'll get a CSV file.
- To import the bookmark file, go to the settings and click "Import Bookmarks from Pocket export".

## Import from Omnivore

- Follow Omnivore's [documentation](https://docs.omnivore.app/using/exporting.html) to export your bookmarks.
- This will give you a zip file with all your data.
- The zip file contains a lot of JSONs in the format `metadata_*.json`. You can either import every JSON file manually, or merge the JSONs into a single JSON file and import that.
- To  merge the JSONs into a single JSON file, you can use the following command in the unzipped directory: `jq -r '.[]' metadata_*.json | jq -s > omnivore.json` and then import the `omnivore.json` file. You'll need to have the [jq](https://github.com/jqlang/jq) tool installed.

## Import using the CLI

:::warning
Importing bookmarks using the CLI requires some technical knowledge and might not be very straightforward for non-technical users. Don't hesitate to ask questions in github discussions or discord though.
:::

If you can get your bookmarks in a text file with one link per line, you can use the following command to import them using the [karakeep cli](../05-integrations/02-command-line.md):

```
while IFS= read -r url; do
    karakeep --api-key "<KEY>" --server-addr "<SERVER_ADDR>" bookmarks add --link "$url"
done < all_links.txt
```


==================================================
File: docs/versioned_docs/version-v0.30.0/04-using-karakeep/lists.md
==================================================
---
sidebar_position: 2
---

# Lists

Lists are the core organizational layer in Karakeep. Every saved item can sit in multiple lists so you can group links by project, topic, or audience without duplicating them.

## Manual lists

- Curated sets you add bookmarks to by hand. Great for projects, reading queues, or hand-picked collections.
- Can be **private** (visible only to you) or **public** (share a read-only link).
- Can be **collaborative**: invite people by email as viewers or editors. Editors can add their own bookmarks; viewers can browse. Your personal states (favourite/archive) stay yours even inside a shared list.

## Smart lists

- Auto-updating lists powered by a saved search query (e.g. `#ai -archived`).
- Best for dynamic views like `Youtube links added last week` or `All reddit links from r/selfhosted`.


==================================================
File: docs/versioned_docs/version-v0.30.0/04-using-karakeep/quick-sharing.md
==================================================
---
sidebar_position: 7
slug: quick-sharing
---

# Quick capture and sharing

The whole point of Karakeep is making it easy to hoard the content. That's why there are a couple of 

## Mobile Apps

<img src="/img/quick-sharing/mobile.png" alt="mobile screenshot" width="300"/>


- **iOS app**: [App Store Link](https://apps.apple.com/us/app/karakeep-app/id6479258022).
- **Android App**: [Play Store link](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share).

## Browser Extensions

<img src="/img/quick-sharing/extension.png" alt="mobile screenshot" width="300"/>

- **Chrome extension**: [here](https://chromewebstore.google.com/detail/karakeep/kgcjekpmcjjogibpjebkhaanilehneje).
- **Firefox addon**: [here](https://addons.mozilla.org/en-US/firefox/addon/karakeep/).

- ## Community Extensions
- **Safari extension**: [App Store Link](https://apps.apple.com/us/app/karakeeper-bookmarker/id6746722790).  For macOS and iOS to allow a simple way to add your bookmarks to your self hosted karakeep instance.


==================================================
File: docs/versioned_docs/version-v0.30.0/04-using-karakeep/search-query-language.md
==================================================
---
sidebar_position: 9
slug: search-query-language
---

# Search Query Language

Karakeep provides a search query language to filter and find bookmarks. Here are all the supported qualifiers and how to use them:

## Basic Syntax

- Use spaces to separate multiple conditions (implicit AND)
- Use `and`/`or` keywords for explicit boolean logic
- Prefix qualifiers with `-` to negate them
- Use parentheses `()` for grouping conditions (note that groups can't be negated)

## Qualifiers

Here's a comprehensive table of all supported qualifiers:

| Qualifier                        | Description                                                                                                                                                                                               | Example Usage                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `is:fav`                         | Favorited bookmarks                                                                                                                                                                                       | `is:fav`                                     |
| `is:archived`                    | Archived bookmarks                                                                                                                                                                                        | `-is:archived`                               |
| `is:tagged`                      | Bookmarks that has one or more tags                                                                                                                                                                       | `is:tagged`                                  |
| `is:inlist`                      | Bookmarks that are in one or more lists                                                                                                                                                                   | `is:inlist`                                  |
| `is:link`, `is:text`, `is:media` | Bookmarks that are of type link, text or media                                                                                                                                                            | `is:link`                                    |
| `is:broken`                      | Bookmarks with broken/failed links (crawl failures or non-2xx status codes)                                                                                                                               | `is:broken`                                  |
| `url:<value>`                    | Match bookmarks with URL substring                                                                                                                                                                        | `url:example.com`                            |
| `title:<value>`                  | Match bookmarks with title substring                                                                                                               | `title:example`                              |
|                                  | Supports quoted strings for titles with spaces                                                                                                   | `title:"my title"`                           |
| `#<tag>`                         | Match bookmarks with specific tag                                                                                                                                                                         | `#important`                                 |
|                                  | Supports quoted strings for tags with spaces                                                                                                                                                              | `#"work in progress"`                        |
| `list:<name>`                    | Match bookmarks in specific list                                                                                                                                                                          | `list:reading`                               |
|                                  | Supports quoted strings for list names with spaces                                                                                                                                                        | `list:"to review"`                           |
| `after:<date>`                   | Bookmarks created on or after date (YYYY-MM-DD)                                                                                                                                                           | `after:2023-01-01`                           |
| `before:<date>`                  | Bookmarks created on or before date (YYYY-MM-DD)                                                                                                                                                          | `before:2023-12-31`                          |
| `feed:<name>`                    | Bookmarks imported from a particular rss feed                                                                                                                                                             | `feed:Hackernews`                            |
| `age:<time-range>`               | Match bookmarks based on how long ago they were created. Use `<` or `>` to indicate the maximum / minimum age of the bookmarks. Supported units: `d` (days), `w` (weeks), `m` (months), `y` (years). | `age:<1d` `age:>2w` `age:<6m` `age:>3y` |

### Examples

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not tagged or not in any list
-is:tagged or -is:inlist
# Find bookmarks with "React" in the title
title:React
```

## Combining Conditions

You can combine multiple conditions using boolean logic:

```plaintext
# Find favorited bookmarks from 2023 that are tagged "important"
is:fav after:2023-01-01 before:2023-12-31 #important

# Find archived bookmarks that are either in "reading" list or tagged "work"
is:archived and (list:reading or #work)

# Find bookmarks that are not favorited and not archived
-is:fav -is:archived
```

## Text Search

Any text not part of a qualifier will be treated as a full-text search:

```plaintext
# Search for "machine learning" in bookmark content
machine learning

# Combine text search with qualifiers
machine learning is:fav
```


==================================================
File: docs/versioned_docs/version-v0.30.0/04-using-karakeep/tags.md
==================================================
---
sidebar_position: 3
---

# Tags

Tags are lightweight labels you can attach to any bookmark to add meaning without rigid folders.

- Use tags to capture topics, sources, people, or workflow states (e.g. `ai`, `design`, `to-read`).
- Combine multiple tags to filter or build smart lists; tags travel with a bookmark wherever it appears.
- AI tags might look a little messy, but the extra labels make finding things easier. Use tags for broad discovery and lists when you want a clean, hand-picked setup.


==================================================
File: docs/versioned_docs/version-v0.30.0/05-integrations/02-command-line.md
==================================================
# Command Line Tool (CLI)

Karakeep comes with a simple CLI for those users who want to do more advanced manipulation.

## Features

- Manipulate bookmarks, lists and tags
- Mass import/export of bookmarks

## Installation (NPM)

```
npm install -g @karakeep/cli
```


## Installation (Docker)

```
docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help
```

## Usage

```
karakeep
```

```
Usage: karakeep [options] [command]

A CLI interface to interact with the karakeep api

Options:
  --api-key <key>       the API key to interact with the API (env: KARAKEEP_API_KEY)
  --server-addr <addr>  the address of the server to connect to (env: KARAKEEP_SERVER_ADDR)
  -V, --version         output the version number
  -h, --help            display help for command

Commands:
  bookmarks             manipulating bookmarks
  lists                 manipulating lists
  tags                  manipulating tags
  whoami                returns info about the owner of this API key
  help [command]        display help for command
```

And some of the subcommands:

```
karakeep bookmarks
```

```
Usage: karakeep bookmarks [options] [command]

Manipulating bookmarks

Options:
  -h, --help             display help for command

Commands:
  add [options]          creates a new bookmark
  get <id>               fetch information about a bookmark
  update [options] <id>  updates bookmark
  list [options]         list all bookmarks
  delete <id>            delete a bookmark
  help [command]         display help for command

```

```
karakeep lists
```

```
Usage: karakeep lists [options] [command]

Manipulating lists

Options:
  -h, --help                 display help for command

Commands:
  list                       lists all lists
  delete <id>                deletes a list
  add-bookmark [options]     add a bookmark to list
  remove-bookmark [options]  remove a bookmark from list
  help [command]             display help for command
```

## Obtaining an API Key

To use the CLI, you'll need to get an API key from your karakeep settings. You can validate that it's working by running:

```
karakeep --api-key <key> --server-addr <addr> whoami
```

For example:

```
karakeep --api-key mysupersecretkey --server-addr https://try.karakeep.app whoami
{
  id: 'j29gnbzxxd01q74j2lu88tnb',
  name: 'Test User',
  email: 'test@gmail.com'
}
```


## Other clients

There also exists a **non-official**, community-maintained, python package called [karakeep-python-api](https://github.com/thiswillbeyourgithub/karakeep_python_api) that can be accessed from the CLI, but is **not** official.


==================================================
File: docs/versioned_docs/version-v0.30.0/05-integrations/03-mcp.md
==================================================
# Model Context Protocol Server (MCP)

Karakeep comes with a Model Context Protocol server that can be used to interact with it through LLMs.

## Supported Tools

- Searching bookmarks
- Adding and removing bookmarks from lists
- Attaching and detaching tags to bookmarks
- Creating new lists
- Creating text and URL bookmarks


## Usage with Claude Desktop

From NPM:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "npx",
      "args": [
        "@karakeep/mcp"
      ],
      "env": {
        "KARAKEEP_API_ADDR": "https://<YOUR_SERVER_ADDR>",
        "KARAKEEP_API_KEY": "<YOUR_TOKEN>"
      }
    }
  }
}
```

From Docker:

```json
{
  "mcpServers": {
    "karakeep": {
      "command": "docker",
      "args": [
        "run",
        "-e",
        "KARAKEEP_API_ADDR=https://<YOUR_SERVER_ADDR>",
        "-e",
        "KARAKEEP_API_KEY=<YOUR_TOKEN>",
        "ghcr.io/karakeep-app/karakeep-mcp:latest"
      ]
    }
  }
}
```


### Demo

#### Search
![mcp-1](/img/mcp-1.gif)

#### Adding Text Bookmarks
![mcp-2](/img/mcp-2.gif)

#### Adding URL Bookmarks
![mcp-2](/img/mcp-3.gif)


==================================================
File: docs/versioned_docs/version-v0.30.0/05-integrations/05-singlefile.md
==================================================
# Using Karakeep with SingleFile Extension

Karakeep supports being a destination for the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile). This has the benefit of allowing you to use the singlefile extension to hoard links as you're seeing them in the browser. This is perfect for websites that don't like to get crawled, has annoying cookie banner or require authentication.

## Setup

1. Install the [SingleFile extension](https://github.com/gildas-lormeau/SingleFile).
2. In the extension settings, select `Destinations`.
3. Select `upload to a REST Form API`.
4. In the URL, insert the address: `https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile`.
5. In the `authorization token` field, paste an API key that you can get from your karakeep settings.
6. Set `data field name` to `file`.
7. Set `URL field name` to `url`.
8. (Optional) Add `&ifexists=MODE` to the URL where MODE is one of `skip`, `overwrite`, `overwrite-recrawl`, `append`, or `append-recrawl`. See "Handling Existing Bookmarks" section below for details.

Now, go to any page and click the singlefile extension icon. Once it's done with the upload, the bookmark should show up in your karakeep instance. Note that the singlefile extension doesn't show any progress on the upload. Given that archives are typically large, it might take 30+ seconds until the upload is done and starts showing up in Karakeep.

## Handling Existing Bookmarks

When uploading a page that already exists in your archive (same URL), you can control the behavior by setting the `ifexists` query parameter in the upload URL. The available modes are:

- `skip` (default): If the bookmark already exists, skip creating a new one
- `overwrite`: Replace existing precrawled archive (only the most recent archive is kept)
- `overwrite-recrawl`: Replace existing archive and queue a recrawl to update content
- `append`: Add new archive version alongside existing ones
- `append-recrawl`: Add new archive and queue a recrawl

To use these modes, append `?ifexists=MODE` to your upload URL, replacing `MODE` with your desired behavior.

For example:  
`https://YOUR_SERVER_ADDRESS/api/v1/bookmarks/singlefile?ifexists=overwrite`


## Recommended settings

In the singlefile extension, you probably will want to change the following settings for better experience:
* Stylesheets > compress CSS content: on
* Stylesheets > group duplicate stylesheets together: on
* HTML content > remove frames: on

Also, you most likely will want to change the default `MAX_ASSET_SIZE_MB` in karakeep to something higher, for example `100`.

:::info
Currently, we don't support screenshots for singlefile uploads, but this will change in the future.
:::



==================================================
File: docs/versioned_docs/version-v0.30.0/05-integrations/06-rss-feeds.md
==================================================
# RSS Feeds

Karakeep offers RSS feed integration, allowing you to both consume RSS feeds from external sources and publish your lists as RSS feeds for others to subscribe to.

## Publishing RSS Feeds

You can publish any of your lists as an RSS feed, making it easy to share your bookmarks with others or integrate them into RSS readers.

### Enabling RSS for a List

1. Navigate to one of your lists
2. Click on the list settings (three dots menu)
3. Toggle the "RSS Feed" switch to enable it
4. Copy the generated RSS feed URL

### What Gets Published

RSS feeds include:
- **Links**: Bookmarks of type "link" with their URL, title, description, and author
- **Assets**: Uploaded files (PDFs, images) are included with a link to view them
- **Tags**: Bookmark tags are exported as RSS categories
- **Dates**: The bookmark creation date is used as the publication date

Note: Text notes are not included in RSS feeds as they don't have an associated URL.

### Security Considerations

- Each RSS feed requires a unique token for access
- Tokens can be regenerated at any time, which will invalidate the old URL
- Disabling RSS for a list immediately revokes access

## Consuming RSS Feeds

Karakeep can automatically monitor RSS feeds and create bookmarks from new entries, making it perfect for staying up to date with blogs, news sites, and other content sources.

### Adding an RSS Feed

1. Go to **Settings** → **RSS Feeds**
2. Click **Add Feed**
3. Enter the feed details:
   - **Name**: A friendly name for the feed
   - **URL**: The RSS/Atom feed URL
   - **Enabled**: Toggle to enable/disable the feed
   - **Import Tags**: Enable to import RSS categories as bookmark tags

### How It Works

- Karakeep checks enabled RSS feeds **every hour**
- New entries are automatically created as bookmarks
- Duplicate entries are automatically detected and skipped


==================================================
File: docs/versioned_docs/version-v0.30.0/06-administration/01-security-considerations.md
==================================================
# Security Considerations

If you're going to give app access to untrusted users, there's some security considerations that you'll need to be aware of given how the crawler works. The crawler is basically running a browser to fetch the content of the bookmarks. Any untrusted user can submit bookmarks to be crawled from your server and they'll be able to see the crawling result. This can be abused in multiple ways:

1. Untrusted users can submit crawl requests to websites that you don't want to be coming out of your IPs.
2. Crawling user controlled websites can expose your origin IP (and location) even if your service is hosted behind cloudflare for example.
3. The crawling requests will be coming out from your own network, which untrusted users can leverage to crawl internal non-internet exposed endpoints.

To mitigate those risks, you can do one of the following:

1. Limit access to trusted users
2. Let the browser traffic go through some VPN with restricted network policies.
3. Host the browser container outside of your network.
4. Use a hosted browser as a service (e.g. [browserless](https://browserless.io)). Note: I've never used them before.


==================================================
File: docs/versioned_docs/version-v0.30.0/06-administration/02-FAQ.md
==================================================
# Frequently Asked Questions (FAQ)

## User Management

### Lost password

#### If you are not an administrator

Administrators can reset the password of any user. Contact an administrator to reset the password for you.

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to reset the password
- Enter a new password and press `Reset`
- The new password is now set
- If required, you can change your password again (so the admin does not know your password) in the `User Settings`

#### If you are an administrator

If you are an administrator and lost your password, you have to reset the password in the database.

To reset the password:

- Acquire some kind of tools that helps you to connect to the database:
  - `sqlite3` on Linux: run `apt-get install sqlite3` (depending on your package manager)
  - e.g. `dbeaver` on Windows
- Shut down Karakeep
- Connect to the `db.db` database, which is located in the `data` directory you have mounted to your docker container:
  - by e.g. running `sqlite3 db.db` (in your `data` directory)
  - or going through e.g. the `dbeaver` UI to locate the file in the data directory and connecting to it
- Update the password in the database by running:
  - `update user set password='$2a$10$5u40XUq/cD/TmLdCOyZ82ePENE6hpkbodJhsp7.e/BgZssUO5DDTa', salt='' where email='<YOUR_EMAIL_HERE>';`
  - (don't forget to put your email address into the command)
- The new password for your user is now `adminadmin`.
- Start Karakeep again
- Log in with your email address and the password `adminadmin` and change the password to whatever you want in the `User Settings`

### Adding another administrator

By default, the first user to sign up gets promoted to administrator automatically.

In case you want to grant those permissions to another user:

- Navigate to the `Admin Settings` page
- Find the user in the `Users List`
- In the `Actions` column, there is a button to change the Role
- Change the Role to `Admin`
- Press `Change`
- The new administrator has to log out and log in again to get the new role assigned

### Adding new users, when signups are disabled

Administrators can create new accounts any time:

- Navigate to the `Admin Settings` page
- Go to the `Users List`
- Press the `Create User` Button.
- Enter the information for the user
- Press `create`
- The new user can now log in


==================================================
File: docs/versioned_docs/version-v0.30.0/06-administration/03-openai.md
==================================================
# Tagging Costs

This service uses OpenAI for automatic tagging. This means that you'll incur some costs if automatic tagging is enabled. There are two type of inferences that we do:

## Text Tagging

For text tagging, we use the `gpt-4.1-mini` model. This model is [extremely cheap](https://openai.com/api/pricing). Cost per inference varies depending on the content size per article. Though, roughly, You'll be able to generate tags for almost 3000+ bookmarks for less than $1.

## Image Tagging

For image uploads, we use the `gpt-4o-mini` model for extracting tags from the image. You can learn more about the costs of using this model [here](https://platform.openai.com/docs/guides/images?api-mode=chat#calculating-costs). To lower the costs, we're using the low resolution mode (fixed number of tokens regardless of image size). You'll be able to run inference for 1000+ images for less than a $1.


==================================================
File: docs/versioned_docs/version-v0.30.0/06-administration/05-troubleshooting.md
==================================================
# Troubleshooting

## SqliteError: no such table: user

This usually means that there's something wrong with the database setup (more concretely, it means that the database is not initialized). This can be caused by multiple problems:
1. **Wiped DATA_DIR:** Your `DATA_DIR` got wiped (or the backing storage dir changed). If you did this intentionally, restart the container so that it can re-initalize the database.
2. **Missing DATA_DIR**: You're not using the default docker compose file, and you forgot to configure the `DATA_DIR` env var. This will result into the database getting set up in a different directory than the one used by the service.

## Chrome Failed to Read DnsConfig

If you see this error in the logs of the chrome container, it's a benign error and you can safely ignore it. Whatever problems you're having, is unrelated to this error.

## AI Tagging not working (when using OpenAI)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OPENAI_API_KEY` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring open ai.
3. OpenAI requires pre-charging the account with credits before using it, otherwise you'll get an error like "insufficient funds".

## AI Tagging not working (when using Ollama)

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. Typo in the env variable `OLLAMA_BASE_URL` name resulting into logs saying something like "skipping inference as it's not configured".
2. You forgot to call `docker compose up` after configuring ollama.
3. You didn't change the `INFERENCE_TEXT_MODEL` env variable, resulting into karakeep attempting to use gpt models with ollama which won't work.
4. Ollama server is not reachable by the karakeep container. This can be caused by:
    1. Ollama server being in a different docker network than the karakeep container.
    2. You're using `localhost` as the `OLLAMA_BASE_URL` instead of the actual address of the ollama server. `localhost` points to the container itself, not the docker host. Check this [stackoverflow answer](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) to find how to correctly point to the docker host address instead.

## Crawling not working

Check the logs of the container and this will usually tell you what's wrong. Common problems are:
1. You changed the name of the chrome container but didn't change the `BROWSER_WEB_URL` env variable.

## Upgrading Meilisearch - Migrating the Meilisearch db version

[Meilisearch](https://www.meilisearch.com/) is the database used by karakeep for searching in your bookmarks. The version used by karakeep is `1.13.3` and it is advised not to upgrade it without good reasons. If you do, you might see errors like `Your database version (1.11.1) is incompatible with your current engine version (1.13.3). To migrate data between Meilisearch versions, please follow our guide on https://www.meilisearch.com/docs/learn/update_and_migration/updating.`.

Luckily we can easily workaround this:
1. Stop the Meilisearch container.
2. Inside the Meilisearch volume bound to `/meili_data`, erase/rename the folder called `data.ms`.
3. Launch Meilisearch again.
4. Login to karakeep as administrator and go to (as of v0.24.1) `Admin Settings > Background Jobs` then click on `Reindex All Bookmarks`.
5. When the reindexing has finished, Meilisearch should be working as usual.

If you run into issues, the official documentation can be found [there](https://www.meilisearch.com/docs/learn/update_and_migration/updating).


==================================================
File: docs/versioned_docs/version-v0.30.0/06-administration/06-server-migration.md
==================================================
# Migrating Between Servers

This guide explains how to migrate all of your data from one Karakeep server to another using the official CLI.

## What the command does

The migration copies user-owned data from a source server to a destination server in this order:

- User settings
- Lists (preserving hierarchy and settings)
- RSS feeds
- AI prompts (custom prompts and their enabled state)
- Webhooks (URL and events)
- Tags (ensures tags by name exist)
- Rule engine rules (IDs remapped to destination equivalents)
- Bookmarks (links, text, and assets)
  - After creation, attaches the correct tags and adds to the correct lists

Notes:
- Webhook tokens cannot be read via the API, so tokens are not migrated. Re‑add them on the destination if needed.
- Asset bookmarks are migrated by downloading the original asset and re‑uploading it to the destination. Only images and PDFs are supported for asset bookmarks.
- Link bookmarks on the destination may be de‑duplicated if the same URL already exists.

## Prerequisites

- Install the CLI:
  - NPM: `npm install -g @karakeep/cli`
  - Docker: `docker run --rm ghcr.io/karakeep-app/karakeep-cli:release --help`
- Collect API keys and base URLs for both servers:
  - Source: `--server-addr`, `--api-key`
  - Destination: `--dest-server`, `--dest-api-key`

## Quick start

```
karakeep --server-addr https://src.example.com --api-key <SOURCE_API_KEY> migrate \
  --dest-server https://dest.example.com \
  --dest-api-key <DEST_API_KEY>
```

The command is long‑running and shows live progress for each phase. You will be prompted for confirmation; pass `--yes` to skip the prompt.

### Options

- `--server-addr <url>`: Source server base URL
- `--api-key <key>`: API key for the source server
- `--dest-server <url>`: Destination server base URL
- `--dest-api-key <key>`: API key for the destination server
- `--batch-size <n>`: Page size for bookmark migration (default 50, max 100)
- `-y`, `--yes`: Skip the confirmation prompt

## What to expect

- Lists are recreated parent‑first and retain their hierarchy.
- Feeds, prompts, webhooks, and tags are recreated by value.
- Rules are recreated after IDs (tags, lists, feeds) are remapped to their corresponding destination IDs.
- After each bookmark is created, the command attaches the correct tags and adds it to the correct lists.

## Caveats and tips

- Webhook auth tokens must be re‑entered on the destination after migration.
- If your destination already contains data, duplicate links may be de‑duplicated; tags and list membership are still applied to the existing bookmark.

## Troubleshooting

- If the command exits early, you can re‑run it, but note:
  - Tags and lists that already exist are reused.
  - Link de‑duplication avoids duplicate link bookmarks. Notes and assets will get re-created.
  - Rules, webhooks, rss feeds will get re-created and you'll have to manually clean them up afterwards.
  - The progress log indicates how far it got.
- Use a smaller `--batch-size` if your source or destination is under heavy load.


==================================================
File: docs/versioned_docs/version-v0.30.0/06-administration/07-legacy-container-upgrade.md
==================================================
# Legacy Container Upgrade

Karakeep's 0.16 release consolidated the web and worker containers into a single container and also dropped the need for the redis container. The legacy containers will stop being supported soon, to upgrade to the new container do the following:

1. Remove the redis container and its volume if it had one.
2. Move the environment variables that you've set exclusively to the `workers` container to the `web` container.
3. Delete the `workers` container.
4. Rename the web container image from `hoarder-app/hoarder-web` to `hoarder-app/hoarder`.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder-web:${KARAKEEP_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${KARAKEEP_VERSION:-release}
     restart: unless-stopped
     volumes:
       - data:/data
@@ -10,14 +10,10 @@ services:
     env_file:
       - .env
     environment:
-      REDIS_HOST: redis
       MEILI_ADDR: http://meilisearch:7700
+      BROWSER_WEB_URL: http://chrome:9222
+      # OPENAI_API_KEY: ...
       DATA_DIR: /data
-  redis:
-    image: redis:7.2-alpine
-    restart: unless-stopped
-    volumes:
-      - redis:/data
   chrome:
     image: gcr.io/zenika-hub/alpine-chrome:123
     restart: unless-stopped
@@ -37,24 +33,7 @@ services:
       MEILI_NO_ANALYTICS: "true"
     volumes:
       - meilisearch:/meili_data
-  workers:
-    image: ghcr.io/hoarder-app/hoarder-workers:${KARAKEEP_VERSION:-release}
-    restart: unless-stopped
-    volumes:
-      - data:/data
-    env_file:
-      - .env
-    environment:
-      REDIS_HOST: redis
-      MEILI_ADDR: http://meilisearch:7700
-      BROWSER_WEB_URL: http://chrome:9222
-      DATA_DIR: /data
-      # OPENAI_API_KEY: ...
-    depends_on:
-      web:
-        condition: service_started

 volumes:
-  redis:
   meilisearch:
   data:
```


==================================================
File: docs/versioned_docs/version-v0.30.0/06-administration/08-hoarder-to-karakeep-migration.md
==================================================
# Hoarder to Karakeep Migration

Hoarder is rebranding to Karakeep. Due to github limitations, the old docker image might not be getting new updates after the rebranding. You might need to update your docker image to point to the new karakeep image instead by applying the following change in the docker compose file.

```diff
diff --git a/docker/docker-compose.yml b/docker/docker-compose.yml
index cdfc908..6297563 100644
--- a/docker/docker-compose.yml
+++ b/docker/docker-compose.yml
@@ -1,7 +1,7 @@
 version: "3.8"
 services:
   web:
-    image: ghcr.io/hoarder-app/hoarder:${HOARDER_VERSION:-release}
+    image: ghcr.io/karakeep-app/karakeep:${HOARDER_VERSION:-release}
```

You can also change the `HOARDER_VERSION` environment variable but if you do so remember to change it in the `.env` file as well.

## Migrating a Baremetal Installation

If you previously used the [Debian/Ubuntu install script](../02-installation/06-debuntu.md) to install Hoarder, there is an option to migrate your installation to Karakeep.

```bash
bash karakeep-linux.sh migrate
```

This will migrate your installation with no user input required. After the migration, the script will also check for an update.


==================================================
File: docs/versioned_docs/version-v0.30.0/07-community/01-community-projects.md
==================================================
# Community Projects

This page lists community projects that are built around Karakeep, but not officially supported by the development team.

:::warning
This list comes with no guarantees about security, performance, reliability, or accuracy. Use at your own risk.
:::

### Raycast Extension

_By [@luolei](https://github.com/foru17)._

A user-friendly Raycast extension that seamlessly integrates with Karakeep, bringing powerful bookmark management to your fingertips. Quickly save, search, and organize your bookmarks, texts, and images—all through Raycast's intuitive interface.

Get it [here](https://www.raycast.com/luolei/karakeep).

### Alfred Workflow

_By [@yinan-c](https://github.com/yinan-c)_

An Alfred workflow to quickly hoard stuff or access your hoarded bookmarks!

Get it [here](https://www.alfredforum.com/topic/22528-hoarder-workflow-for-self-hosted-bookmark-management/).

### Obsidian Plugin

_By [@jhofker](https://github.com/jhofker)_

An Obsidian plugin that syncs your Karakeep bookmarks with Obsidian, creating markdown notes for each bookmark in a designated folder.

Get it [here](https://github.com/jhofker/obsidian-hoarder/), or install it directly from Obsidian's community plugin store ([link](https://obsidian.md/plugins?id=hoarder-sync)).

### Telegram Bot

_By [@Madh93](https://github.com/Madh93)_

A Telegram Bot for saving bookmarks to Karakeep directly through Telegram.

Get it [here](https://github.com/Madh93/karakeepbot).

### Hoarder's Pipette

_By [@DanSnow](https://github.com/DanSnow)_

A chrome extension that injects karakeep's bookmarks into your search results.

Get it [here](https://dansnow.github.io/hoarder-pipette/guides/installation/).

### Karakeep-Python-API

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python package to simplify access to the karakeep API. Can be used as a library or from the CLI. Aims for feature completeness and high test coverage but do check its feature matrix before relying too much on it.

Its repository also hosts the [Community Script](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts), for example:

| Community Script | Description | Documentation |
|----------------|-------------|---------------|
| **Karakeep-Time-Tagger** | Automatically adds time-to-read tags (`0-5m`, `5-10m`, etc.) to bookmarks based on content length analysis. Includes systemd service and timer files for automated periodic execution. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-time-tagger) |
| **Karakeep-List-To-Tag** | Converts a Karakeep list into tags by adding a specified tag to all bookmarks within that list. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/karakeep-list-to-tag) |
| **Omnivore2Karakeep-Highlights** | Imports highlights from Omnivore export data to Karakeep, with intelligent position detection and bookmark matching. Supports dry-run mode for testing. | [`Link`](https://github.com/thiswillbeyourgithub/karakeep_python_api/tree/main/community_scripts/omnivore2karakeep-highlights) |


Get it [here](https://github.com/thiswillbeyourgithub/karakeep_python_api).

### FreshRSS_to_Karakeep

_By [@thiswillbeyourgithub](https://github.com/thiswillbeyourgithub/)_

A python script to automatically create Karakeep bookmarks from your [FreshRSS](https://github.com/FreshRSS/FreshRSS) *favourites/saved* RSS item. Made to be called periodically. Based on the community project `Karakeep-Python-API` above, by the same author.

Get it [here](https://github.com/thiswillbeyourgithub/freshrss_to_karakeep).

### karakeep-sync
_By [@sidoshi](https://github.com/sidoshi/)_

Sync links from Hacker News upvotes, Reddit Saves to Karakeep for centralized bookmark management.

Get it [here](https://github.com/sidoshi/karakeep-sync)

### Home Assistant Integration

_By [@sli-cka](https://github.com/sli-cka)_

A custom integration that brings Karakeep data into Home Assistant. It exposes your Karakeep statistics data (like lists, bookmarks, tag, etc.) as Home Assistant entities, enabling dashboards, automations, and notifications based on your Karakeep data.

Get it [here](https://github.com/sli-cka/karakeep-homeassistant)


==================================================
File: docs/versioned_docs/version-v0.30.0/07-community/02-community-channels.md
==================================================
# Community Channels

Stay connected with the Karakeep team and community for updates, support, and feature discussions.

## Discord

- Join the official server: [discord.gg/NrgeYywsFh](https://discord.gg/NrgeYywsFh)
- Great for getting help, sharing setups, and chatting with the team and other users.

## Twitter / X

- Follow [@karakeep_app](https://twitter.com/karakeep_app) for release announcements, tips, and product news.
- DM or tag us with feedback or things you'd like to see next.


==================================================
File: docs/versioned_docs/version-v0.30.0/08-development/01-setup.md
==================================================
# Setup

## Quick Start

For the fastest way to get started with development, use the one-command setup script:

```bash
./start-dev.sh
```

This script will automatically:
- Start Meilisearch in Docker (on port 7700)
- Start headless Chrome in Docker (on port 9222) 
- Install dependencies with `pnpm install` if needed
- Start both the web app and workers in parallel
- Provide cleanup when you stop with Ctrl+C

**Prerequisites:**
- Docker installed and running
- pnpm installed (see manual setup below for installation instructions)

The script will output the running services:
- Web app: http://localhost:3000
- Meilisearch: http://localhost:7700  
- Chrome debugger: http://localhost:9222

Press Ctrl+C to stop all services and clean up Docker containers.

## Manual Setup

Karakeep uses `node` version 24. To install it, you can use `nvm` [^1]

```
$ nvm install  24
```

Verify node version using this command:
```
$ node --version
v24.14.0
```

Karakeep also makes use of `corepack`[^2]. If you have `node` installed, then `corepack` should already be
installed on your machine, and you don't need to do anything. To verify the `corepack` is installed run:

```
$ command -v corepack
/home/<user>/.nvm/versions/node/v24.14.0/bin/corepack
```

To enable `corepack` run the following command:

```
$ corepack enable
```

Then, from the root of the repository, install the packages and dependencies using:

```
$ pnpm install
```

Output of a successful `pnpm install` run should look something like:

```
Scope: all 20 workspace projects
Lockfile is up to date, resolution step is skipped
Packages: +3129
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 0, reused 2699, downloaded 0, added 3129, done

devDependencies:
+ @karakeep/prettier-config 0.1.0 <- tooling/prettier

. prepare$ husky
└─ Done in 45ms
Done in 5.5s
```

You can now continue with the rest of this documentation.

### First Setup

- You'll need to prepare the environment variables for the dev env.
- Easiest would be to set it up once in the root of the repo and then symlink it in each app directory (e.g. `/apps/web`, `/apps/workers`) and also `/packages/db`.
- Start by copying the template by `cp .env.sample .env`.
- The most important env variables to set are:
  - `DATA_DIR`: Where the database and assets will be stored. This is the only required env variable. You can use an absolute path so that all apps point to the same dir.
  - `NEXTAUTH_SECRET`: Random string used to sign the JWT tokens. Generate one with `openssl rand -base64 36`. Logging in will not work if this is missing!
  - `MEILI_ADDR`: If not set, search will be disabled. You can set it to `http://127.0.0.1:7700` if you run meilisearch using the command below.
  - `OPENAI_API_KEY`: If you want to enable auto tag inference in the dev env.
- run `pnpm run db:migrate` in the root of the repo to set up the database.

### Dependencies

#### Meilisearch

Meilisearch is the provider for the full text search (and at some point embeddings search too). You can get it running with `docker run -p 7700:7700 getmeili/meilisearch:v1.13.3`.

Mount persistent volume if you want to keep index data across restarts. You can trigger a re-index for the entire items collection in the admin panel in the web app.

#### Chrome

The worker app will automatically start headless chrome on startup for crawling pages. You don't need to do anything there.

### Web App

- Run `pnpm web` in the root of the repo.
- Go to `http://localhost:3000`.

> NOTE: The web app kinda works without any dependencies. However, search won't work unless meilisearch is running. Also, new items added won't get crawled/indexed unless workers are running.

### Workers

- Run `pnpm workers` in the root of the repo.

### Mobile App (iOS & Android)

#### Prerequisites

To build and run the mobile app locally, you'll need:

- **For iOS development**: 
  - macOS computer
  - Xcode installed from the App Store
  - iOS Simulator (comes with Xcode)

- **For Android development**:
  - Android Studio installed
  - Android SDK configured
  - Android Emulator or physical device

For detailed setup instructions, refer to the [Expo documentation](https://docs.expo.dev/guides/local-app-development/).

#### Running the app

- `cd apps/mobile`
- `pnpm exec expo prebuild --no-install` to build the app.

**For iOS:**
- `pnpm exec expo run:ios`
- The app will be installed and started in the simulator.

**Troubleshooting iOS Setup:**
If you encounter an error like `xcrun: error: SDK "iphoneos" cannot be located`, you may need to set the correct Xcode developer directory:
```bash
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

**For Android:**
- Start the Android emulator or connect a physical device.
- `pnpm exec expo run:android`
- The app will be installed and started on the emulator/device.

Changing the code will hot reload the app. However, installing new packages requires restarting the expo server.

### Browser Extension

- `cd apps/browser-extension`
- `pnpm dev`
- This will generate a `dist` package
- Go to extension settings in chrome and enable developer mode.
- Press `Load unpacked` and point it to the `dist` directory.
- The plugin will pop up in the plugin list.

In dev mode, opening and closing the plugin menu should reload the code.


## Docker Dev Env

If the manual setup is too much hassle for you. You can use a docker based dev environment by running `docker compose -f docker/docker-compose.dev.yml up` in the root of the repo. This setup wasn't super reliable for me though.


[^1]: [nvm](https://github.com/nvm-sh/nvm) is a node version manager. You can install it following [these
instructions](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

[^2]: [corepack](https://nodejs.org/api/corepack.html) is an experimental tool to help with managing versions of your
package managers.


==================================================
File: docs/versioned_docs/version-v0.30.0/08-development/02-directories.md
==================================================
# Directory Structure

## Apps

| Directory                | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| `apps/web`               | The main web app                                       |
| `apps/workers`           | The background workers logic                           |
| `apps/mobile`            | The react native based mobile app                      |
| `apps/browser-extension` | The browser extension                                  |
| `apps/landing`           | The landing page of [karakeep.app](https://karakeep.app) |

## Shared Packages

| Directory         | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `packages/db`     | The database schema and migrations                                           |
| `packages/trpc`   | Where most of the business logic lies built as TRPC routes                   |
| `packages/shared` | Some shared code between the different apps (e.g. loggers, configs, assetdb) |

## Toolings

| Directory            | Description             |
| -------------------- | ----------------------- |
| `tooling/typescript` | The shared tsconfigs    |
| `tooling/eslint`     | ESlint configs          |
| `tooling/prettier`   | Prettier configs        |
| `tooling/tailwind`   | Shared tailwind configs |


==================================================
File: docs/versioned_docs/version-v0.30.0/08-development/03-database.md
==================================================
# Database Migrations

- The database schema lives in `packages/db/schema.ts`.
- Changing the schema, requires a migration.
- You can generate the migration by running `pnpm run db:generate --name description_of_schema_change` in the root dir.
- You can then apply the migration by running `pnpm run db:migrate`.

## Drizzle Studio

You can start the drizzle studio by running `pnpm run db:studio` in the root of the repo.


==================================================
File: docs/versioned_docs/version-v0.30.0/08-development/04-architecture.md
==================================================
# Architecture

![Architecture Diagram](/img/architecture/arch.png)

- Webapp: NextJS based using sqlite for data storage.
- Workers: Consume the jobs from sqlite based job queue and executes them, there are three job types:
  1. Crawling: Fetches the content of links using a headless chrome browser running in the workers container.
  2. OpenAI: Uses OpenAI APIs to infer the tags of the content.
  3. Indexing: Indexes the content in meilisearch for faster retrieval during search.


==================================================
File: kubernetes/README.md
==================================================
# Kubernetes installation with Kustomize

You can:

- edit the configuration in `.env`.

Then run `make deploy`.


==================================================
File: packages/benchmarks/README.md
==================================================
# Karakeep Benchmarks

This package spins up a production-like Karakeep stack in Docker, seeds it with a sizeable dataset, then benchmarks a handful of high-signal APIs.

## Usage

```bash
pnpm --filter @karakeep/benchmarks bench
```

The command will:

- Start the docker-compose stack on a random free port
- Create a dedicated benchmark user, tags, lists, and hundreds of bookmarks
- Run a suite of benchmarks (create, list, search, and list metadata calls)
- Print a table with ops/sec and latency percentiles
- Tear down the containers and capture logs (unless you opt out)

## Configuration

Control the run via environment variables:

- `BENCH_BOOKMARKS` (default `400`): number of bookmarks to seed
- `BENCH_TAGS` (default `25`): number of tags to seed
- `BENCH_LISTS` (default `6`): number of lists to seed
- `BENCH_SEED_CONCURRENCY` (default `12`): concurrent seeding operations
- `BENCH_TIME_MS` (default `1000`): time per benchmark case
- `BENCH_WARMUP_MS` (default `300`): warmup time per case
- `BENCH_NO_BUILD=1`: reuse existing docker images instead of rebuilding
- `BENCH_KEEP_CONTAINERS=1`: leave the stack running after the run

The stack uses the package-local `docker-compose.yml` and serves a tiny HTML fixture from `setup/html`.


==================================================
File: packages/sdk/README.md
==================================================
# Karakeep SDK

This package contains the official typescript SDK for the karakeep API.

## Installation

```
npm install @karakeep/sdk
```

## Usage

```typescript
import { createKarakeepClient } from "@karakeep/sdk";

// Create a client
const apiKey = "my-super-secret-key";
const addr = `https://karakeep.mydomain.com`;
const client = createKarakeepClient({
  baseUrl: `${addr}/api/v1/`,
  headers: {
    "Content-Type": "application/json",
    authorization: `Bearer ${apiKey}`,
  },
});

// Create a bookmark
const {
  data: createdBookmark,
  response: createResponse,
  error: createError,
} = await client.POST("/bookmarks", {
  body: {
    type: "text",
    title: "Search Test 1",
    text: "This is a test bookmark for search",
  },
});

console.log(createResponse.status, createdBookmark, createError);

// Search for bookmarks
const {
  data: searchResults,
  response: searchResponse,
  error: searchError,
} = await client.GET("/bookmarks/search", {
  params: {
    query: {
      q: "test bookmark",
    },
  },
});
console.log(searchResponse.status, searchResults, searchError);
```

## Docs

API docs can be found [here](https://docs.karakeep.app/api).

## Versioning

- This package follows the minor version of the karakeep server. So new APIs introduced in Karakeep version `0.21.0` will be available in this package starting from version `0.21.0`.
- Karakeep strives to maintain backward compatibility in its APIs, so older versions of this package should continue working with newer karakeep server versions.


==================================================
File: tools/compare-models/README.md
==================================================
# Model Comparison Tool

A standalone CLI tool to compare the tagging performance of AI models using your existing Karakeep bookmarks.

## Features

- **Two comparison modes:**
  - **Model vs Model**: Compare two AI models against each other
  - **Model vs Existing**: Compare a new model against existing AI-generated tags on your bookmarks
- Fetches existing bookmarks from your Karakeep instance
- Runs tagging inference with AI models
- **Random shuffling**: Models/tags are randomly assigned to "Model A" or "Model B" for each bookmark to eliminate bias
- Blind comparison: Model names are hidden during voting (only shown as "Model A" and "Model B")
- Interactive voting interface
- Shows final results with winner

## Setup

### Environment Variables

Required environment variables:

```bash
# Karakeep API configuration
KARAKEEP_API_KEY=your_api_key_here
KARAKEEP_SERVER_ADDR=https://your-karakeep-instance.com

# Comparison mode (default: model-vs-model)
# - "model-vs-model": Compare two models against each other
# - "model-vs-existing": Compare a model against existing AI tags
COMPARISON_MODE=model-vs-model

# Models to compare
# MODEL1_NAME: The new model to test (always required)
# MODEL2_NAME: The second model to compare against (required only for model-vs-model mode)
MODEL1_NAME=gpt-4o-mini
MODEL2_NAME=claude-3-5-sonnet

# OpenAI/OpenRouter API configuration (for running inference)
OPENAI_API_KEY=your_openai_or_openrouter_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1  # Optional, defaults to OpenAI

# Optional: Number of bookmarks to test (default: 10)
COMPARE_LIMIT=10
```

### Using OpenRouter

For OpenRouter, set:
```bash
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=your_openrouter_key
```

### Using OpenAI Directly

For OpenAI directly:
```bash
OPENAI_API_KEY=your_openai_key
# OPENAI_BASE_URL can be omitted for direct OpenAI
```

## Usage

### Run with pnpm (Recommended)

```bash
cd tools/compare-models
pnpm install
pnpm run
```

### Run with environment file

Create a `.env` file:

```env
KARAKEEP_API_KEY=your_api_key
KARAKEEP_SERVER_ADDR=https://your-karakeep-instance.com
MODEL1_NAME=gpt-4o-mini
MODEL2_NAME=claude-3-5-sonnet
OPENAI_API_KEY=your_openai_key
COMPARE_LIMIT=10
```

Then run:
```bash
pnpm run
```

### Using directly with node

If you prefer to run the compiled JavaScript directly:

```bash
pnpm build
export KARAKEEP_API_KEY=your_api_key
export KARAKEEP_SERVER_ADDR=https://your-karakeep-instance.com
export MODEL1_NAME=gpt-4o-mini
export MODEL2_NAME=claude-3-5-sonnet
export OPENAI_API_KEY=your_openai_key
node dist/index.js
```

## Comparison Modes

### Model vs Model Mode

Compare two different AI models against each other:

```bash
COMPARISON_MODE=model-vs-model
MODEL1_NAME=gpt-4o-mini
MODEL2_NAME=claude-3-5-sonnet
```

This mode runs inference with both models on each bookmark and lets you choose which tags are better.

### Model vs Existing Mode

Compare a new model against existing AI-generated tags on your bookmarks:

```bash
COMPARISON_MODE=model-vs-existing
MODEL1_NAME=gpt-4o-mini
# MODEL2_NAME is not required in this mode
```

This mode is useful for:
- Testing if a new model produces better tags than your current model
- Evaluating whether to switch from one model to another
- Quality assurance on existing AI tags

**Note:** This mode only compares bookmarks that already have AI-generated tags (tags with `attachedBy: "ai"`). Bookmarks without AI tags are automatically filtered out.

## Usage Flow

1. The tool fetches your latest link bookmarks from Karakeep
   - In **model-vs-existing** mode, only bookmarks with existing AI tags are included
2. For each bookmark, it randomly assigns the options to "Model A" or "Model B" and runs tagging
3. You'll see a side-by-side comparison (randomly shuffled each time):
   ```
   === Bookmark 1/10 ===
   How to Build Better AI Systems
   https://example.com/article
   This article explores modern approaches to...

   ─────────────────────────────────────

   Model A (blind):
     • ai
     • machine-learning
     • engineering

   Model B (blind):
     • artificial-intelligence
     • ML
     • software-development

   ─────────────────────────────────────

   Which tags do you prefer? [1=Model A, 2=Model B, s=skip, q=quit] >
   ```

4. Choose your preference:
   - `1` - Vote for Model A
   - `2` - Vote for Model B
   - `s` or `skip` - Skip this comparison
   - `q` or `quit` - Exit early and show current results

5. After completing all comparisons (or quitting early), results are displayed:
   ```
   ───────────────────────────────────────
   === FINAL RESULTS ===
   ───────────────────────────────────────
   gpt-4o-mini: 6 votes
   claude-3-5-sonnet: 3 votes
   Skipped: 1
   Errors: 0
   ───────────────────────────────────────
   Total bookmarks tested: 10

   🏆 WINNER: gpt-4o-mini
   ───────────────────────────────────────
   ```

6. The actual model names are only shown in the final results - during voting you see only "Model A" and "Model B"

## Bookmark Filtering

The tool currently tests only:
- **Link-type bookmarks** (not text notes or assets)
- **Non-archived** bookmarks
- **Latest N bookmarks** (where N is COMPARE_LIMIT)
- **In model-vs-existing mode**: Only bookmarks with existing AI tags (tags with `attachedBy: "ai"`)

## Architecture

This tool leverages Karakeep's shared infrastructure:
- **API Client**: Uses `@karakeep/sdk` for type-safe API interactions with proper authentication
- **Inference**: Reuses `@karakeep/shared/inference` for OpenAI client with structured output support
- **Prompts**: Uses `@karakeep/shared/prompts` for consistent tagging prompt generation with token management
- No code duplication - all core functionality is shared with the main Karakeep application


## Error Handling

- If a model fails to generate tags for a bookmark, an error is shown and comparison continues
- Errors are counted separately in final results
- Missing required environment variables will cause the tool to exit with a clear error message

## Build

To build a standalone binary:

```bash
pnpm build
```

The built binary will be in `dist/index.js`.

## Notes

- The tool is designed for manual, human-in-the-loop evaluation
- No results are persisted - they're only displayed in console
- Content is fetched with `includeContent=true` from Karakeep API
- Uses Karakeep SDK (`@karakeep/sdk`) for type-safe API interactions
- Inference runs sequentially to keep state management simple
- Recommended to use `pnpm run` for the best experience (uses tsx for development)
- **Random shuffling**: For each bookmark, models are randomly assigned to "Model A" or "Model B" to eliminate position bias. The actual model names are only revealed in the final results.


