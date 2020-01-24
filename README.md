Develocorder
============

![Pytest badge](https://github.com/wahtak/develocorder/workflows/Pytest/badge.svg)

Develocorder is a simple live value plotter for Python3 using Matplotlib. It is intended to give insights into the training of machine learning models / reinforcement learning agents with only minimal effort to add to existing code.

![Original Develocorder](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Viewing_of_Develocorder_Film.jpg/319px-Viewing_of_Develocorder_Film.jpg)

[(image source)](https://commons.wikimedia.org/wiki/File:Viewing_of_Develocorder_Film.jpg)


Installation
------------

```
$ pip install develocorder
```


Simple Example
--------------

``` python
# initialize once
set_recorder(my_value=LinePlot())

# add values to plot anywhere
for _ in range(10):
    record(my_value=random())
```

### Result
![Simple Example](doc/simple_example.png)


Fancy Example
--------------

See [examples/examples.py](examples/fancy.py)

![Fancy Example](doc/fancy_example.png)


Jupyter notebook
----------------

For use in a Jupyter notebook use the `%matplotlib notebook` backend. As of now you cannot rerun the cell which is showing the plot without restarting the notebook, otherwise the plot will disappear.

See [examples/simple.ipynb](examples/simple.ipynb)


TODOs
-----
  - [ ] document how to extend
  - [ ] better support for jupyter notebook
  - [ ] add new plot types(?)
  - [ ] persistent storage/loading of log(?)
