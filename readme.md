<h1>
	guidly_backend REST API.
</h1>


This project was generated using the ADVANCED template of the drf-cli


## Running the Project

- Run `pre-commit install` in your project's root directory to install git hooks 
in your `.git` directory

- To see your git hooks in action, make your first git commit. The first time your hooks run,
it will take a while to execute. It's normal. Subsequent executions won't take that long

- Run `docker-compose up --build` to build your docker image and start your docker container.

- Navigate to your project directory in a new terminal and run 
`docker-compose exec web python manage.py makemigrations users` to create migrations for the customUser model

- Run `docker-compose exec web python manage.py migrate`

- Point your browser to `http://localhost:8000/api/v1/docs`. You should see the auto-generated 
docs on that page