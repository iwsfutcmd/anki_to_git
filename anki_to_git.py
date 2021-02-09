#!/usr/bin/env python3
import shutil
import sqlite3
from pathlib import Path
from sys import argv
from os import remove

if __name__ == "__main__":
    p = Path(argv[1])
    directory = Path(p.stem)
    shutil.unpack_archive(p, directory, "zip")
    anki2_file = directory / "collection.anki2"
    con = sqlite3.connect(anki2_file)
    with open(directory / "collection.sql", "w") as file:
        for line in con.iterdump():
            file.write(f"{line}\n")
    con.close()
    remove(anki2_file)

