# Building and Running with Docker

Follow these steps to build and run application using Docker and Docker Compose.

***
## Step-by-Step Guide
#### 1. Clone Your Repository
```bash
git clone https://github.com/subho-1011/fyle-interview-intern-backend.git
cd fyle-interview-intern-backend
```

#### 2. Create `.env` File
Create a `.env` file in the root directory with the environment variables 
```bash
FLASK_APP=core/server.py
FLASK_ENV=production
```

#### 3. Build and Start the Containers
Run the following command to build the Docker image and start the container:
```bash
docker-compose up --build
```

Flags Explanation:
- `--build`: Forces a rebuild of the Docker image.
- `-d (optional)`: Runs containers in the background (detached mode)

**Example:**
```bash
docker-compose up --build -d
```

#### 4. Verify the Application
*Web Application:* Access the Flask application by navigating to http://localhost:5000 in your browser.

#### 5. Stopping the Application
To stop the running container, use:
```bash
docker-compose down
```

#### 6. Viewing Logs
```bash
docker-compose logs -f
```

***
## Running Tests

You can run your tests inside the Docker container.

#### Ensure the Service Is Running
Make sure the `web` service is up and running.
```bash
docker-compose up --build -d
```

#### Access the Web Container

Execute a bash shell inside the web container to run tests.
```bash
docker-compose exec web bash
```

#### Run Tests
Inside the container, use pytest or another testing framework to execute the tests.
```bash
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```

#### Exit the Container
After running the tests, exit the container shell:
```bash
exit
```
