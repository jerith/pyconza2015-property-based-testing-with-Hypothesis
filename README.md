## Property-based Testing With Hypothesis

To make this run, do the following:

    cd reveal.js
    npm install
    npm install grunt-cli
    PATH=$PATH:node_modules/.bin grunt serve

Then hit `localhost:8080` in a browser. (You could `npm install -g grunt`
instead of manipulating `$PATH`, but I don't like installing any npm stuff
globally.)

If you want to run `py.test` (which the grunt task does whenever a `.py` file
changes), you also need to have a virtualenv active with the contents of
`code/requirements.txt` installed in it.

Assuming you're using virtualenvwrapper (and are in the `reveal.js` dir):

    mkvirtualenv myenv
    pip install -r ../code/requirements.txt
    PATH=$PATH:node_modules/.bin grunt serve
