#!/bin/bash
(sudo rm -rf ohmlr.egg-info/)
(rm -rf build/)
(rm -rf dist/)
(sudo pip install -e .)
(python increment_version_number.py)
(python setup.py sdist)
(twine upload dist/*)
(cd ./ohmlr && sphinx-apidoc -o ../doc -f .)
(cd ./doc && make html)
(git add -A . && cat version | xargs git commit -m  && git push -f origin master)
(git subtree push --prefix doc/build/html origin gh-pages)
