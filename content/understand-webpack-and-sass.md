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
  - is a modular library
    - Babel Core (heart of Babel), read code and compiles it
    - Babel Loader - necessary if work with webpack (allows webpack to understand JavaScript language)
    - Babel Preset - various JS dialects es2015, es2016
      - commonly `@babel/preset-env`
- Babel and Webpack can be used independently
- how to configure Babel with Webpack (after installing required packages)
  - babel and webpack are not connected by default thus babel-loader is needed to integrate them
    - use module property in webpack.config.js
    - module property allows you to configure 3rd party modules
    - describes how modules work with webpack
    - it's a place to provide our loaders
    - provide rules for every module, if a file match a rule - this rule will be applied to that file
      - rule: `test: /\.js$/` - files ending with js extension
      - optionally provide `exclude: /node_modules/` but can be valid 
      - provide `use` property, with `babel-loader`
      - `.babelrc` can be provided; alternatively configure babel in webpack.config.js
      - define `presets` as a list of presets to use by babel
- Play with Sass - superset of CSS, a stylesheet language similar and just like CSS
  - add specific rule to webpack.config.js -> and test for `/\.s[ac]ss$/`
  - use `css-loader and sass-loader` as loaders
  - webpack will use `use` property list of loaders from bottom to top, which means first loader used will be the last one in the list
    - WHY: because css-loader does not understand SASS code
    - now, webpack should be able to understand SASS code - transpiles to regular CSS
    - and we can use `import` SCSS statement in our JavaScript files - which will be embedded in generated bundle.js file
    - during compilation process Webpack will scan our codebase looking for import statements, and that's why we can import scss files in out JavaScript files; webpack does not execute that javaScript code
    - 
  -  
    - 

style-loader
css-loader
sass-loader