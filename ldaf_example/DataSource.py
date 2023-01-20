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

import pandas as pd
import numpy as np
import matplotlib.cbook as cbook

from ldaf.DataSource import DataSource as DataSource_L


class DataSource(DataSource_L):
    """Class to store all Data

    """

    def load_data(self):
        # https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py
        # Fixing random state for reproducibility
        np.random.seed(19680801)

        dt = 0.01
        t = np.arange(0, 30, dt)
        nse1 = np.random.randn(len(t))                 # white noise 1
        nse2 = np.random.randn(len(t))                 # white noise 2

        # Two signals with a coherent part at 10 Hz and a random part
        s1 = np.sin(2 * np.pi * 10 * t) + nse1
        s2 = np.sin(2 * np.pi * 10 * t) + nse2

        self.dfs['sin'] = pd.DataFrame({'t': t, 's1': s1, 's2': s2})

        # https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-py
        with cbook.get_sample_data('goog.npz') as datafile:
            goog = np.load(datafile)['price_data'].view(np.recarray)

        goog = pd.DataFrame(goog)
        self.dfs['goog'] = goog

        self.app.settings.update_tables_cb()

    def on_tab_change(self, i=0):
        pass

    def get_loaded_tables(self) -> list:
        return self.dfs.keys()

    def get_table_shape(self, table: str) -> tuple:
        return self.dfs[table].shape
