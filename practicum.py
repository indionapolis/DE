"""
Programming Assignment 1
Made by Pavel Nikulin
"""
from math import pow, e, pi, sqrt, erf

import plotly.offline as py
import numpy as np


# 16 variant
# 2yx + 5 - x^2


def exact(x_values):
    """
    Function returns values of exact solution of initial equation
    :param x_values: set of x values on [x0, X] region
    :return: set of y values mapped from x_values by function f
    """
    y_values = []

    f = lambda x: 1 / 4 * (9 * sqrt(pi) * pow(e, pow(x, 2)) * erf(x) + 4 * pow(e, pow(x, 2)) + 2 * x)

    for x in x_values:
        y_values.append(f(x))

    return y_values


def euler(y0, x_values, h, F):
    """
    Function implements Euler numeric algorithm
    :param y0: initial y value
    :param x_values: set of x values on [x0, X] region
    :param h: grid step
    :param F: initial function
    :return: approximate y values
    """
    y_values = [y0]

    for i in range(len(x_values)-1):
        value = y_values[i] + h * F(x_values[i], y_values[i])
        y_values.append(value)

    return y_values


def improved_euler(y0, x_values, h, F):
    """
    Function implements improved Euler numeric algorithm
    :param y0: initial y value
    :param x_values: set of x values on [x0, X] region
    :param h: grid step
    :param F: initial function
    :return: approximate y values
    """
    y_values = [y0]

    for i in range(len(x_values) - 1):
        k1 = F(x_values[i], y_values[i])
        k2 = F(x_values[i] + h, y_values[i] + h * k1)
        value = y_values[i] + (h / 2) * (k1 + k2)
        y_values.append(value)

    return y_values


def runge_kutta(y0, x_values, h, F):
    """
    Function implements Runge Kutta numeric algorithm
    :param y0: initial y value
    :param x_values: set of x values on [x0, X] region
    :param h: grid step
    :param F: initial function
    :return: approximate y values
    """
    y_values = [y0]

    for i in range(len(x_values) - 1):
        k1 = F(x_values[i], y_values[i])
        k2 = F(x_values[i] + h / 2, y_values[i] + h * k1 / 2)
        k3 = F(x_values[i] + h / 2, y_values[i] + h * k2 / 2)
        k4 = F(x_values[i] + h, y_values[i] + h * k3)
        value = y_values[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y_values.append(value)

    return y_values


if __name__ == '__main__':
    """initial values"""
    x0 = 0
    y0 = 1
    X = 3

    """initial function"""
    f = lambda x, y: 2 * y * x + 5 - pow(x, 2)

    grid_steps = np.array([1] + [0.1 / (2 ** i) for i in range(8)])

    """one graph for one value set is one trace object (dict)"""
    exact_trace = []
    euler_trace = []
    improved_euler_trace = []
    runge_kutta_trace = []

    for step in grid_steps:
        """for each grid step calculate value set and corresponding errors"""

        x_values = np.array(np.arange(x0, X + step, step))

        y_ex_values = np.array(exact(x_values))

        y_e_values = np.array(euler(y0, x_values, step, f))

        y_ie_values = np.array(improved_euler(y0, x_values, step, f))

        y_rk_values = np.array(runge_kutta(y0, x_values, step, f))

        exact_trace.append(dict(
            visible=False,
            line=dict(color='#FF0948', width=3),
            name='Exact solution',
            x=x_values,
            y=y_ex_values, ))

        euler_trace.append(dict(
            visible=False,
            line=dict(color='#00CED1', width=3),
            name='Euler method',
            text=['Error: {}'.format(round(abs(y_ex_values[i] - y_e_values[i]), 5)) for i in range(len(y_ex_values))],
            x=x_values,
            y=y_e_values,))

        improved_euler_trace.append(dict(
            visible=False,
            line=dict(color='#BB33FF', width=3),
            name='Improved Euler method',
            text=['Error: {}'.format(round(abs(y_ex_values[i] - y_ie_values[i]), 5)) for i in range(len(y_ex_values))],
            x=x_values,
            y=y_ie_values, ))

        runge_kutta_trace.append(dict(
            visible=False,
            line=dict(color='#FC33FF', width=3),
            name='Runge Kutta method',
            text=['Error: {}'.format(round(abs(y_ex_values[i] - y_rk_values[i]), 5)) for i in range(len(y_ex_values))],
            x=x_values,
            y=y_rk_values, ))

    """initial graphs"""
    exact_trace[0]['visible'] = True
    euler_trace[0]['visible'] = True
    improved_euler_trace[0]['visible'] = True
    runge_kutta_trace[0]['visible'] = True

    """stiles and slider"""
    steps = []
    for i in range(len(grid_steps)):
        step = dict(
            method='restyle',
            args=['visible', [False] * len(grid_steps) * 4],
            label=grid_steps[i],
        )
        """make visible traces for corresponding grid step"""
        step['args'][1][i] = True  # Toggle i'th trace to "visible"
        step['args'][1][len(grid_steps) + i] = True  # Toggle i'th trace to "visible"
        step['args'][1][len(grid_steps) * 2 + i] = True  # Toggle i'th trace to "visible"
        step['args'][1][len(grid_steps) * 3 + i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    slider = [dict(
        active=0,
        currentvalue={"prefix": "grid step: "},
        steps=steps,
        bgcolor='#7f7f7f',
        font=dict(
            color='#7f7f7f',
        ),
        bordercolor='#A4A4A4',
        activebgcolor='#A4A4A4',

    )]

    data = euler_trace + improved_euler_trace + runge_kutta_trace + exact_trace

    layout = dict(sliders=slider,
                  title="<b>Practicum: y' = 2xy - 5 + x<sup>2</sup></b>",
                  titlefont=dict(
                      size=20,
                      color='#969696',
                  ),
                  plot_bgcolor='#424242',
                  paper_bgcolor='#2E2E2E',
                  xaxis=dict(
                      color='#7f7f7f',
                      gridwidth=1,
                      gridcolor='#7f7f7f',
                  ),
                  yaxis=dict(
                      color='#7f7f7f',
                      gridwidth=1,
                      gridcolor='#7f7f7f',
                  ),
                  legend=dict(
                      font=dict(
                          family='sans-serif',
                          size=12,
                          color='#7f7f7f',
                      ),
                  ),
                  )

    fig = dict(data=data, layout=layout)

    py.plot(fig, filename='practicum')