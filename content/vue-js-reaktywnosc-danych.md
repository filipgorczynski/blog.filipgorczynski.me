Title: Vue.js reaktywność danych
Date: 2020-02-25 07:44
Author: filipgorczynski
Category: Programowanie
Slug: vue-js-reaktywnosc-danych
Status: draft

Object.defineProperty,

vue.js -\> reactiveSetter,

<div>

<div>

dep.notify()

</div>

<div>

let object = {};

</div>

<div>

let text = {}

</div>

<div>

let header = document.querySelector('\#header');

</div>

</div>

<div>

Object.defineProperty(obj, 'text', {

</div>

<div>

   get: function get() {

</div>

<div>

      return text;

</div>

<div>

   },

</div>

<div>

   set: function set(newValue) {

</div>

<div>

      text = newValue;

</div>

<div>

      header.innerHTML = text;

</div>

<div>

   }

</div>

<div>

});

</div>

<div>

</div>
