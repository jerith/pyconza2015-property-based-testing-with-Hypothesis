## Property-based testing with Hypothesis

This is the source for my
[PyConZA 2015 talk](https://2015.za.pycon.org/talks/8/) of the same name.

The generated slides can be found at
http://jerith.github.io/pyconza2015-property-based-testing-with-Hypothesis
(hit `s` to open a speaker-mode window and see notes and such).

There's a video at
http://www.pyvideo.org/video/3934/property-based-testing-with-hypothesis as
well.

### How to make it run

To make it run, do the following:

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

### Licenses

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

The code examples in `code/` are in the public domain. (I doubt they're useful
for anything other than this presentation, but feel free to do whatever you
like with them.)

[reveal.js][1] (which is almost everything in `reveal.js/`) is covered by its
own MIT license (`reveal.js/LICENSE`) as are the minor modifications I made to
it for this presentation.

The [tomorrow-night syntax highlighting theme][2]
(`reveal.js/css/highlight_tomorrow.css`) doesn't have a listed license, but
[the theme upon which it is based][3] is covered by the MIT license.

[1]: https://github.com/hakimel/reveal.js
[2]: http://jmblog.github.io/color-themes-for-highlightjs/tomorrow-night/
[3]: https://github.com/chriskempson/tomorrow-theme
