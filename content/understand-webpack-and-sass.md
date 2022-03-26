Title: Understand Webpack & Sass
Date: 2022-03-25 07:24
Modified: 2022-03-25 07:24
Category: Tech
Tags: #tech, #webpack, #sass, #node-sass
Slug: understand-webpack-and-sass
Author: filipgorczynski
Status: draft
Cover: https://blog.filipgorczynski.me/images/post/2022/03/annie-spratt-M20ylqCzSZw.jpg
meta_url: https://blog.filipgorczynski.me/2022/03/understand-webpack-and-sass
Summary: 

webpack.config.js

```javascript
const path = require('path');

module.exports = {
    entry: './index.js',
    output: [
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist'),
    ]
}
```

- `entry` key may define multiple entry points.
- If entry is not provided, webpack will assume that `./src/index.js` will be used.
- filename is the name of the file webpack will produce.
- path is the directory name, where the `filename` will be saved - full system path is required in that case
- __dirname - global variable used/provided by `node`
- to run webpack directly from command line, full path `./node_modules/.bin/webpack` is required
- When run through `npm` scripts included in `package.json` only `webpack` is needed as bin path is added to it automatically.
- webpack --mode=production vs webpack --mode=development
- default mode can be set in webpack.config.js
- webpack core concepts
  - entry
  - output
  - loaders
  - plugins
- webpack ONLY understands plain JavaScript files
- webpack need to know how to process non JavaScript file through loaders.
- plugins extend the functionality of webpack, like starting server, deploying application, create/delete files, etc
- babel
  - babel takes javascript to the next level
  - allow to use latest JavaScript syntax
  - it's a transpiler
  - allow to support older browsers JavaScript engines
  - it's a modular library
    - Babel Core (heart of Babel)
    - Babel Preset
    - Babel Loader

style-loader
css-loader
sass-loader