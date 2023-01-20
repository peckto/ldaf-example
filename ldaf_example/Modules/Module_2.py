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

import matplotlib.style
matplotlib.style.use('ggplot')

import typing
if typing.TYPE_CHECKING:
    from ldaf.App import App


settings = {}
"Work in process"
actions = {}
"Work in process"

name = 'Module 2'
"Display name of module"
table = 'example2'
"is mapped to app.active_table, WIP"


def example_1(app: 'App', fig=None):
    # Read setting Table from UI
    table = app.settings.get('Table')

    # Get data set from data_source
    df = app.data_source.get_table(table)

    # name attribute must be set and is displayed as title above the table
    df.name = '%s Data' % table

    return df


functions = {
    'Example 1 Table': example_1,
}