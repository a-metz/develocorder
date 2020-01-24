Develocorder
============

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


TODOs
-----
  - [ ] document how to extend
  - [ ] check ipython notebook compatability
  - [ ] add new plot types
  - [ ] persistent storage/loading of log(?)
