One-hot multinomial logistic regression
========================

Quick Start
-----------

Installation
~~~~~~~~~~~~

- To install ``ohmlr`` on your computer using ``pip``, execute

  .. code-block:: sh

     pip install ohmlr

- Test out ``ohmlr`` in Python:

  .. code-block:: python

     import ohmlr
     import numpy as np

     # create model and generate data
     n_features = 16
     n_x_classes = np.random.randint(2, 10, size=n_features)
     n_y_classes = 8
     model = ohmlr.ohmlr().random(n_features, n_x_classes, n_y_classes)
     x, y = model.generate_data(n_samples=1000)

     # fit and score model
     model.fit(x, y)
     print(model.score(x, y))


Links
-----

Online documentation:
    http://joepatmckenna.github.io/ohmlr

Source code repository:
    https://github.com/joepatmckenna/ohmlr

Python package index:
    https://pypi.python.org/pypi/ohmlr
