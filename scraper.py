import sys
from getopt import getopt

from utils import download_manga


if __name__ == "__main__":
    myopts, _ = getopt(sys.argv[1:], "n:i:f:l:s:")
    if not myopts:
        raise KeyError("There's no arguments!")

    manga_title = None
    params = {}

    params_dict = {
        "-n": {
            "variable": "manga_title",
            "type": str,
        },
        "-i": {
            "variable": "initial_chapter",
            "type": int,
        },
        "-f": {
            "variable": "final_chapter",
            "type": str,
        },
        "-l": {
            "variable": "download_last_chapter",
            "type": bool,
        },
        "-s": {
            "variable": "single_chapter",
            "type": int,
        },
    }

    for key, value in myopts:
        arg = params_dict.get(key)
        params[arg["variable"]] = arg["type"](value)

    download_manga(**params)

    print("Bye!")

