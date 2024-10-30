Title: Wednesday News
Date: 2024-10-30 13:17

Nothing much happened today, but we imported some changes from home
that allow us to open the browser as soon as python is serving content when invoking
`python build.py --server`.

As a reminder, a fully stand-alone copy of the site is built by running `python build.py`.

After running, `./content/output/*` contains an `index.html` and the rest of the webpage.
Searches happen on clients, so the server only needs to be able to serve out `*.wasm` files.






