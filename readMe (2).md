Lauren DiGiovanni

My bookstore is focused specifically on celebrity biographies. I used sqlite to create the database and then used python to be able to 
interact with it through a command line interface.

Instructions to create the database
1. create the database bookstore.db -> sqlite3 bookstore.db
2. use the createTables.sql file to insert create the tables and add constraints to each column -> sqlite3 bookstore.db < createTables.sql
3. use the insertRows.sql file to populate the tables with data about the biographies -> sqlite3 bookstore.db < insertRows.sql
4. populate the database with the tables 
5. create the bookstore_cli.py file to connect to the database and allow users to interact with it

Running the program: python3 bookstore_cli.py
