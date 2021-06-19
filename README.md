# FastApiArchitecture
 FastApi Project Architecture with database and alembic tools

Create virtual environment then activate to install requirements libraries from requirements.txt

Project is set up in BaseApp folder. In this manager.py file have app configurations.

To run and configure with your local details only change in .env file.
For database migration we need to change same url of database in .env and also in alembic.ini file.

### Run FastApi Server
I am using uvicorn server to run app

`uvicorn BaseApp.manager:app --reload`

## Database migrations using alembic.

### Initialize alembic 
**db-migration** is folder name

`alembic init db-migration`

### Configure alembic for database and apps models
Edit env.py file and change according to this repo env.py file.
In this change Database url with environment variable and configure into mehod of run_migrations_offline and run_migrations_online.

Change database url in **alembic.ini** file also

### Auto generate migration script
import project app models all
and import project database **Base**
initialize it like this.

`target_metadata = Base.metadata`

Now we are connected with models for migrations.

### Now generate migration script with this
This will scan the models and generate upgrade & downgrade scripts.

`alembic revision --autogenerate -m “message”`

### Run migration into database
This upgrade your model columns into database.
### Run upgrade command to migrate models
`alembic upgrade head`

### Run downgrade command to drop models
`alembic downgrade`


