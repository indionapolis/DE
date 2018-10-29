## Practicum
### Variant 16

initial problem: <br/><a href="https://www.codecogs.com/eqnedit.php?latex=y'=2xy&space;&plus;&space;5-x^2,&space;x_0&space;=&space;0,&space;y_0&space;=&space;1,&space;X&space;=&space;3." target="_blank"><img src="https://latex.codecogs.com/gif.latex?y'=2xy&space;&plus;&space;5-x^2,&space;x_0&space;=&space;0,&space;y_0&space;=&space;1,&space;X&space;=&space;3." title="y'=2xy + 5-x^2, x_0 = 0, y_0 = 1, X = 3." /></a>

exact solution: <br/><a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;\frac{1}{4}\left&space;(&space;9\sqrt{\pi&space;}e^{x^{2}}\text{erf}(x)&plus;&space;4e^{x^{2}}&plus;2x\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;\frac{1}{4}\left&space;(&space;9\sqrt{\pi&space;}e^{x^{2}}\text{erf}(x)&plus;&space;4e^{x^{2}}&plus;2x\right&space;)" title="y = \frac{1}{4}\left ( 9\sqrt{\pi }e^{x^{2}}\text{erf}(x)+ 4e^{x^{2}}+2x\right )" /></a>

try [link](https://indionapolis.github.io/DE/) to see interactive chart.

try [link](https://indionapolis.github.io/DE/pydoc) to see python documentation

## Report

### Technology stack:

* ```python```
* ```html```
* ```javascript```

### In this repository:

* ```index.html``` - chart representation [check out here](https://indionapolis.github.io/DE/).
* ```practicum.py``` - python implementation of numeric methods and chart construction using ```plotly```.
* ```pydoc.html``` - documentation for ```practicum.py``` [check out here](https://indionapolis.github.io/DE/pydoc).

## Research

### Aims:

1. Implement various numerical methods to solve first order O.D.E
2. Realize the exact solution of the initial value problem
3. Compare approximation errors of numerical methods and exact solution

### Observation:

The implementation of all numerical methods and their comparison with the exact solution shows the accuracy of each method. Was identified that the less grid step the less average error. Runge Kutta method showed the best result among others.


### Result:

The result of the study is following chart:

[![none](https://github.com/indionapolis/DE/blob/master/src/sample.png "clik me!")](https://indionapolis.github.io/DE/)
