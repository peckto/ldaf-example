# Copyright (C) 2020 Tobias Specht
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
from ggplot import meat

from ldaf.DataSource import DataSource as DataSource_L


class DataSource(DataSource_L):
    """Class to store all Data

    """

    def load_data(self):
        self.dfs['meat'] = meat

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
