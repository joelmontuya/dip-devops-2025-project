# Diploma in Devops - Summer 2025
### Submitted by: Joel Albert Montuya


# Service: Books Catalog API

### Project Overview:
  <p> The project's goal is to create, implement, and deploy a backend service
for managing a book catalog. The service was built using the Django
framework, which ensures a structured and RESTful endpoints. In addition, the project implemented and follows DevOps-oriented development cycle
including creation of contrainers for the application and Posgres database, CI/CD using GitHub, and automated deployment of the service through
Kubernetes and Helm. </p>
  
### The project includes: <br />
<li> Building a Django REST API with endpoints for creating, reading, updating, and deleting book records. </li>
<li> Writing unit tests to validate API functionality. </li> 
<li> Containerizing the application using Docker and Docker Compose for local development. </li>
<li> Creating a CI/CD pipeline with GitHub Actions to automate builds, testing, image publishing, and Kubernetes deployment. </li>
<li> Deploying the app to a Kubernetes cluster using Helm charts, with support for Ingress, environment configs, and service exposure. </li>
<li> Maintaining source control with Git and GitHub, following Conventional Commits. </li>

## CRUD Endpoints: <br />
### 1. <b> GET </b> /api/books/ - The enpoint will return all books contained in the database. <br />
Sample response:<br />
<b> 200: Success <b/>
```json
[	
  {
    "book_id": 1,
    "title": "Dune",
    "description": "Let the spice flowing",
    "author": "The author of Dune",
    "isbn": "10-1223-12",
    "published_date": "2025-01-21",
    "created_at": "2025-07-29T08:33:40.205840Z"
  }
]
```


### 2. <b> POST </b> /api/books/ - Adds new book entry in the database. <br />
Request Body:
```curl
curl --location 'http://localhost:8081/api/books/' \
--header 'Content-Type: application/json' \
--data '    {
        "title":"Testing",
        "description": "Let the spice flowing and ing",
        "author": "The author of Dune",
        "isbn": "10-1223-12",
        "published_date": "2025-01-21"
    }'
```

Sample response: <br/>
200: Success - Record was successfully added to the database.
```json
{
  "book_id": 1,
  "title": "Dune",
  "description": "Let the spice flowing",
  "author": "The author of Dune",
  "isbn": "10-1223-12-10",
  "published_date": "2025-01-21",
  "created_at": "2025-07-29T12:34:56.866030Z"
}
```

400: Bad Request - Missing required field.
```json
{
  "title": [
    "This field is required."
]
```

### <b> 3. DELETE </b> /api/books/{book_id}/ - Deletes a record of a book in the database using primary key <b>'book_id'</b>.
Sample Response: <br />
204: No Content - Record was deleted successfully.
```json
{
  "status": 204,
  "status_message": "Book was deleted successfully."
}
```

404: Not Found - Record is not existing in the database.
```json
{
  "status": 404,
  "status_message": "Book with ID 1 does not exist."
}
```


### <b> 4. PUT </b> /api/books/{book_id}/ - Updates a record in the database with the use of primary key <b>'book_id'</b>.
Request:<br />
```curl
curl --location --request PUT 'http://localhost:8000/api/books/2/' \
--header 'Content-Type: application/json' \
--data '    {
        "description": "Let the spice flowing and ing updated and updated"
    }'
```

Response:<br />
200: Success - Record was updated successfully.
```json
{
    "book_id": 2,
    "title": "Dune",
    "description": "This line was updated.",
    "author": "The author of Dune",
    "isbn": null,
    "published_date": null,
    "created_at": "2025-07-28T07:23:47.491483Z"
}
```



<hr>

# Starting the Server Locally

## Create a virtual environment

First you need to create and activate a [Python Virtual Environment](https://docs.python.org/3/library/venv.html)

```bash
$ python -m venv ./.venv
$ source ./.venv/bin/activate
```

## Install the dependencies

There's a file in this project named `requirements.txt` this is a common file found in python project and it contains a list of all dependencies needed to run it

```bash
$ pip install -r requirements.txt
```

## Run the Server

You should now be able to start the server

```bash
$ python manage.py runserver
```
<hr />


# Running the Service in Docker

Make entrypoint.sh executable: <br />
```bash
  $ chmod +x entrypoint.sh 
```
Build and start the containers: <br />

```bash
  $  docker-compose up
```
Test the endpoints by running:
```curl
curl --location 'http://localhost:8000/api/books/'
```

<hr />

# Deploying using Kubernetes and Helm

1. Create a cluster by running: 
```bash
k3d cluster create <name of cluster>
--port "8081:80@loadbalancer"
--port "8443:443@loadbalancer"
--port "30000-30010:30000-30010@server:0
```

2. Initialize Postgres Database:
```bash
helm install books-database oci://registry-1.docker.io/bitnamicharts/postgresql -f ./deployment/postgres-helm/values.yaml
```

3.  Create a Kubernetes secret to store ghcr token:
```bash
kubectl create secret docker-registry ghcr-token \
  --docker-server=ghcr.io \
  --docker-username=<github_username>\
  --docker-password=<github_classic_token> \
```

5. Deploy the service using helm:
```bash
helm install books-catalog ./deployment/books-catalog-chart
```

7. Test the service:
```bash
curl --location 'http://localhost:8081/api/books/
```

<hr />


