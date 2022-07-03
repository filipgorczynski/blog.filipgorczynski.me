Title: NodeJS internals
Date: 2022-07-03 07:26
Modified: 2022-07-03 07:26
Category: Tech
Tags: #tech, #node, #libuv
Slug: node-js-internals
Author: filipgorczynski
Status: draft
Cover: https://blog.filipgorczynski.me/images/feature/ghaith-alsirawan-mI2s7nh6fPg.jpg
meta_url: https://blog.filipgorczynski.me/2022/07/node-js-internals
Summary: 

![Photo by GHAITH ALSIRAWAN](https://blog.filipgorczynski.me/images/feature/ghaith-alsirawan-mI2s7nh6fPg.jpg)

- github.com/node/nodejs -> API (console, http, fs, process) -> lib -> bindings -> src | https://github.com/nodejs/node/blob/main/lib/fs.js#L559
- https://nodejs.org/dist/latest-v16.x/docs/api/fs.html
- https://nodejs.org/dist/latest-v16.x/docs/api/fs.html#fspromisesopenpath-flags-mode
- NodeJS bindings (JavaScript <-> C++)
- [libuv](https://github.com/libuv/libuv) -> https://github.com/libuv/libuv/blob/v1.x/src/unix/fs.c#L1983 and https://github.com/libuv/libuv/blob/v1.x/src/unix/fs.c#L381
- synchronous vs asynchronous
- asynchronous callbacks
- non-blocking Input & Output
- Multi-Threading, Processes and Threads
- The Event Loop
- Callback Queues
- Phases of the Event Loop
- Observer Design Pattern
- The Node Event Emitter
    

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@g_sirawan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">GHAITH ALSIRAWAN</a> on <a href="https://unsplash.com/s/photos/v8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</span>