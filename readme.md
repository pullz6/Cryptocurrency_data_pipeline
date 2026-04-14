Following the steps included in https://elibenjamin.medium.com/data-engineering-automatically-update-postgresql-database-from-api-4f07da1df2a9

We are using the stocks API included here to create a local postgres server that then adds the data incrementally into the server as run. 

Pre-requisite 
1. Postgres server running on port 5432
2. Table names need to be created stocks 
3. Below columns and corresponding column types need to be there 
4. Need to have an API key for the website from the above tutorial and must be saved as .env

How to run: 
1. Build enironment with dockerfile 
2. Remember to create the .env file with your api key 
3. Run the docker-compose
