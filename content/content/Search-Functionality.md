Title: Cool Search Functionality!
Date: 2024-10-28 13:55
Category: Neat-Stuff

Today saw the integration of [Stork](https://stork-search.net/), a WASM-based search engine
written in Rust!

If you don't know where an article is, the content and keywords may be queried using the search bar that
was addd to the UI with the following tags under the `.pull-right` `<div>`:

```html
<div>
    Search: <input data-stork="sitesearch" />
    <div data-stork="sitesearch-output"></div>
</div>
```

This test also measures how well our markdown plugin can handle HTML-in-HTML!
