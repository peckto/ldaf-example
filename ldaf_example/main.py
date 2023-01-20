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

import sys
from PyQt5.QtWidgets import QApplication
import pandas as pd

from ldaf.App import App
from .Settings import Settings
from .DataSource import DataSource

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def main():
    app = QApplication(sys.argv)
    data_source = DataSource()
    settings = Settings()
    modules_dir = 'ldaf_example/Modules'
    window_title = 'LDAF - Examples'

    window = App(app, data_source, modules_dir, settings, window_title)
    window.show()

    sys.exit(app.exec_())

