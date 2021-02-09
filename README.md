# anki_to_git
Convert Anki .apkg files to a more version-control-friendly format, and vice-versa.

## Usage

* Unpacking:

     `./anki_to_git.py {anki_deck}.apkg`

    Unpacks an `.apkg` file into a directory named `{anki_deck}`.

* Repacking:

    `./git_to_anki.py {anki_deck_dir}`

    Repacks an unpacked Anki deck dir back into `{anki_deck_dir}.apkg`


Note: There is no special handling of any of the files within the `.apkg` archive other than converting the `.anki2` SQLite3 database file into an `.sql` database dump.

Pull requests welcome.