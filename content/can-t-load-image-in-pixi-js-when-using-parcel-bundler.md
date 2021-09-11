Title: Can't load image in PIXI.js when using Parcel bundler
Date: 2021-09-11 10:11
Modified: 2021-09-11 10:11
Category: tech
Tags: #pixi.js, #parcel, #asset, #load, #image, #parcel-plugin-static-files-copy, #til, #public-learning
Slug: can-t-load-image-in-pixi-js-when-using-parcel-bundler
Author: filipgorczynski
Status: published
Summary: Today I've tried to play with PIXI.js with Parcel bundler. Even if it's a convenient way to build and serve HTML file with your application, it does not resolve assets paths correctly.

Today I've tried to play with PIXI.js with Parcel bundler. Even if it's a convenient way to build and serve HTML file with your application, it does not resolve assets paths correctly.

The problem I've encountered was missing references to assets after serving HTML with Parcel. Static files were not copied into `/dist` directory - thus served `index.html` wasn't aware of it.

The easiest solution I've found was to use Parcel plugin `parcel-plugin-static-files-copy` which copied all `/static` directory content into `/dist` and it was actually everything I needed (in that case) to resolve paths properly.

Source code for this article: [with a problem](https://github.com/filipgorczynski/pixijs-parcel-load-assets/releases/tag/problem) and [with a solution](https://github.com/filipgorczynski/pixijs-parcel-load-assets/releases/tag/solution)