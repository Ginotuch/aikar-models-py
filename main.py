"""
Example code to:
- Print out list of plugins
- Print out list of timing snapshot IDs
"""

from aikarmodelspy.configmodels import Config
from aikarmodelspy.historymodels import History


def main():
    config = Config.parse_file("aikarconfig.json")
    for plugin in config.timings_master.plugins.keys():
        print(plugin)

    history = History.parse_file("history.json")
    for snapshot_id in history.history.keys():
        print(snapshot_id)


if __name__ == '__main__':
    main()
