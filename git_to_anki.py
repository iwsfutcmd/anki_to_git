#!/usr/bin/env python3
import shutil
import sqlite3
from pathlib import Path
from sys import argv
import os

if __name__ == "__main__":
    directory = Path(argv[1])
    if not directory.is_dir():
        raise TypeError(f"{directory} is not a directory")
    tmp_dir = Path("tmp")
    shutil.rmtree(tmp_dir, ignore_errors=True)
    os.makedirs(tmp_dir)
    for filename in directory.glob("*"):
        shutil.copy(filename, tmp_dir)
    con = sqlite3.connect(tmp_dir / "collection.anki2")
    sql_file = tmp_dir / "collection.sql"
    with open(sql_file) as file:
        con.executescript(file.read())
    con.close()
    os.remove(sql_file)
    zipfile = Path(shutil.make_archive(directory, "zip", tmp_dir))
    shutil.move(zipfile, zipfile.with_suffix(".apkg"))
    shutil.rmtree(tmp_dir, ignore_errors=True)
