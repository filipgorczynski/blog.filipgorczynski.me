Title: Developer in depression
Date: 2021-03-20 11:12
Modified: 2021-03-20 11:12
Category: Tech
Tags: #reactjs, #event, #input, #onchange
Slug: developer-in-depression
Author: filipgorczynski
Status: draft
Summary: 

Simply speaking, problem was with the `key` property I was passing to
component. I was building it with JavaScript template literal string this way:

```javascript
key={`${props.name}-${props.index}`}
```

As you can see with every input text change, the name props changed as well,
so because `key` props changed I ended up with new component every time it
changed.

Every day is a good day to learn something new. Even if it is just a really
stupid mistake.
