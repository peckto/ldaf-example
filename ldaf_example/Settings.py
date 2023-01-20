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

from ldaf.Settings import Settings as Settings_L


class Settings(Settings_L):
    def add_settings(self):
        self.cb_tables = self.settings_add_combo_box('Table', [])

    def update_tables_cb(self):
        self.cb_tables.clear()
        tables = self.app.data_source.get_loaded_tables()
        self.cb_tables.addItems(tables)
