
# Table A NBP currency rates browser

This application generates currency rate charts using data from table 'A' of the NBP API. When you initially run the app on your local machine, it will fetch the currency rate data starting from 2005 until the current date. A scheduled task is also set up to fetch the latest data every day at 12:16. This timing aligns with the API's daily update, which occurs between 11:45 and 12:15.


## Run Locally

Clone the project

```bash
  git clone git@github.com:martynawitkowska/nbp_currency_browser.git
```

Go to the project directory

```bash
  cd nbp_currency_browser
```

[Instructions to fill Environment Variables](#environment-variables)
```bash
  cp ./envs/backend.default.env ./envs/backend.env
  cp ./envs/postgres.default.env ./envs/postgres.env
  # set variable values
```

Start the server

```bash
  docker compose up
```

**The migration for fetching the data might take some time since it is making requests for data since 2 january 2005, and there is a 93 days limit in the NBP API.**


# Environment Variables
To run this project, you will need to add the following environment variables to your ./envs/api.env file

```dotenv
DJ_SECRET_KEY= # Django Secret Key for CSRF link
DJ_DEBUG= # Production development mode
DJ_ALLOWED_HOSTS= # Allowed Hosts for Django

LOGGING_LVL= # Python logging package levels

DJ_SU_NAME= # Default superusername
DJ_SU_EMAIL= # Default superuser email
DJ_SU_PASSWORD= # Default superuser password
```

Postgres variables ./envs/postgres.env

```dotenv
POSTGRES_USER= # Postgres root user
POSTGRES_PASSWORD= # Postgres root password
POSTGRES_DB= # Database name
POSTGRES_HOST= # Database host: set to docker compose swervice name
POSTGRES_PORT= # Database port

DB_CONNECTION_STRING=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```
## Authors

- [GitHub](https://github.com/martynawitkowska)
- [LinkedIn](https://www.linkedin.com/in/martyna-witkowska-3b101684/)

