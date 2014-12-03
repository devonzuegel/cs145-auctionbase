## Running sqlite from the command line

1. `ssh` into corn (`ssh -Y SUNetID@corn.stanford.edu`), and `cd` into your project directory (`cd cgi-bin`).

2. Execute `$ sqlite3 auctions.db`

To get column names from a table, execute: `PRAGMA table_info(tablename);` in the sqlite3 shell.