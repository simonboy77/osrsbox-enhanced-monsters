"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Script to update JSON files.

Copyright (c) 2019, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""
import json
import collections
from pathlib import Path

import config
from osrsreboxed import monsters_api


def generate_monsters_complete():
    """Generate the `docs/monsters-complete.json` file."""
    # Read in the monster database content
    path_to_monsters_json = Path(config.DOCS_PATH / "monsters-json")
    all_db_monsters = monsters_api.all_monsters.AllMonsters(path_to_monsters_json)

    monsters = {}

    for monster in all_db_monsters:
        json_out = monster.construct_json()
        monsters[monster.id] = json_out

    # Save all monsters to docs/monsters-complete.json
    out_fi = Path(config.DOCS_PATH / "monsters-complete.json")
    with open(out_fi, "w") as f:
        json.dump(monsters, f)

    # Save all monsters to osrsbox/docs/monsters-complete.json
    out_fi = Path(config.PACKAGE_PATH / "docs" / "monsters-complete.json")
    with open(out_fi, "w") as f:
        json.dump(monsters, f)


def main():
    print("Generating monsters-complete.json file...")
    generate_monsters_complete()


if __name__ == '__main__':
    main()
