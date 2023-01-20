# Copyright (C) 2023 Tobias Specht
# This file is part of ldaf-example <https://github.com/peckto/ldaf-example>.
#
# ldaf-example is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldaf-example is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ldaf-example.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import matplotlib.style
matplotlib.style.use('ggplot')


import typing
if typing.TYPE_CHECKING:
    from ldaf.App import App


settings = {}
"Work in process"
actions = {}
"Work in process"

name = 'Module 1'
"Display name of module"
table = 'example1'
"is mapped to app.active_table, WIP"


def example_1(app: 'App', fig=None):
    """Example taken from:
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py

    """
    # Get data set from data_source
    df = app.data_source.get_table('sin')

    # create Axis from provided fig object
    axs = fig.add_subplot(111)

    # Plot as usual
    axs.plot(df.t, df.s1, df.t, df.s2)
    axs.set_xlim(0, 2)
    axs.set_xlabel('Time')
    axs.set_ylabel('s1 and s2')
    axs.grid(True)

    return 'matplotlib'


def example_2(app: 'App', fig=None):
    """Example taken from:
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py

    """
    def onpick(event):
        """matplotlib event handler for pick event

        :param event: pick event
        """
        data = df.iloc[event.ind]
        for idx, row in data.iterrows():
            app.log('Selected Date: %s' % (row['date'].to_numpy(),))

    # Get data set from data_source
    df = app.data_source.get_table('goog')

    price_data = df[-250:]  # get the most recent 250 trading days

    delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

    # Marker size in units of points^2
    volume = (15 * price_data.volume.iloc[:-2] / price_data.volume.iloc[0]) ** 2
    close = 0.003 * price_data.close.iloc[:-2] / 0.003 * price_data.open.iloc[:-2]

    # create Axis from provided fig object
    ax = fig.add_subplot(111)

    # Plot as usual
    ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5, picker=5)

    ax.set_xlabel(r'$\Delta_i$', fontsize=15)
    ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
    ax.set_title('Volume and percent change')

    ax.grid(True)

    # install onpick event handler
    app.current_module.handler_f = onpick

    # Indicate that we created a figure with matplotlib
    return 'matplotlib'


def randrange(n, vmin, vmax):
    """source: https://matplotlib.org/3.1.1/gallery/mplot3d/scatter3d.html
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin


def example_3(app: 'App', fig=None):
    """Example taken from:
    https://matplotlib.org/3.1.1/gallery/mplot3d/scatter3d.html

    """
    # Create 3D figure
    ax = fig.add_subplot(111, projection='3d')
    n = 100

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, marker=m)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # Indicate that we created a figure with matplotlib
    return 'matplotlib'


functions = {
    'Example 1 line': example_1,
    'Example 2 scatter': example_2,
    'Example 3 3D': example_3,
}