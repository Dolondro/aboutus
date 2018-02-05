# AboutUs

Analysing relationships over time via Python. I like doing this kind of number crunching, but this is primarily a
"learn best practices in python" style project. If anything looks sub-par, please point out what I could have done better. I likes the learning!

## Resources

Current resources that I've been reading to try and make this non-awful
- http://docs.python-guide.org/en/latest/writing/structure/


- http://pep8.org/#descriptive-naming-styles - this seems to be the definitive style guide

## Things of Note!

I've played with Python in the past, but never in proper depth. I come from a PHP/JS background so these are just the things that allow me to do things I'm used to doing in other ways

### ALWAYS REMEMBER
Python has weirdness when it comes to how (essentially) autoloading works. If something is throwing odd errors, make sure you don't have any files with the same name as one of your imports in the same directory.

I'm looking at you anything called test.py...

### Imports are done beautifully

`from foo import blah as foo_bar`. If I can remember how to write it, that's such a nice syntax. It's actually the right order! *sniffs*
### Folders are evil...

Well, not evil. But the namespace folder upon folder upon folder stuff of PHP/JS seems to not be in vogue.
Maybe. I don't really know. But having a folder seems to imply a new package. Some projects do seem to do this (TensorFlow, but then they're more problematic than most), but other popular ones don't
(flask and requests).

Todo: Work out best practices, if such a thing exists in how you're meant to deal with things

### Package Management
Pip is the package manager for Python (analogous to Composer/NPM/Bundler). The equivalent of composer.json/package.json is the requirements.txt file.

Apparently you're now meant to use `pipenv` to wrap everything is a more well thought out way. This just works by using `pipenv install x` instead of `pip install x`.

This should give us the more expected pipfiles. As such, I'd expect the first thing to do when starting a new project is `pip install pipenv`

Chain of URLs that got me to this conclusion:
- https://stackoverflow.com/questions/19135867/what-is-pips-equivalent-of-npm-install-package-save-dev
- https://www.kennethreitz.org/essays/a-better-pip-workflow
- https://docs.pipenv.org/install/

### VirtualEnv
By default you'll end up installing to the global namespace. This can be prevented through virtual environments, but as
PyCharm was nice enough to automatically set this up, I'm still unsure what was done to set it up and the best practices about it
@todo: set it up manually and work it out