# Learnify

## Project Overview

This project is an online Learning Management System (LMS) designed to facilitate the creation and sharing of educational materials and courses. It allows users to register, log in using their email, and manage their profiles. The system supports the creation of courses, which can contain multiple lessons. Each course includes details such as a title, preview image, and description, while each lesson has its own title, description, preview image, and a link to video content. The backend is built using Django and Django Rest Framework (DRF) to provide a robust API that returns JSON structures to a Single Page Application (SPA) frontend. The project aims to support the growing trend of online learning by providing a platform for both instructors and learners.

### 1. Project Setup with Docker

- **Clone the Repository**
  - Clone the project repository using the command:
    ```bash
    git clone git@github.com:RomanPecheritsa/Learnify.git
    ```

- **Navigate to the Project Directory**
  - Change to the project directory:
    ```bash
    cd Learnify
    ```
### 2. Create Your .env File

- **Create a new .env**
  - Create a new .env file based on the provided .env.example:
    ```bash
    cp .env.example .env
    ```

### 3. Build and Run Docker Containers

- **Build the Docker Images**
  - Execute the following command to build the Docker images:
    ```bash
    docker-compose build
    ```

- **Start the Docker Containers**
  - Start the application and its dependencies using:
    ```bash
    docker-compose up
    ```
  
  - The application should be running at http://127.0.0.1:8000.

### 4. Testing the Application

To run the tests and check the test coverage, follow these steps:

**Run the tests with coverage**:
   This command runs the Django tests and collects coverage data.

   ```bash
   docker exec -it django coverage run --source='.' manage.py test
   docker exec -it django coverage report
   ```

### 5. Stopping and Cleaning Up

- **Stop Running Containers**
  - To stop the running containers, use:
    ```bash
    docker-compose down
    ```

- **Remove Unused Containers and Images**
  - If necessary, remove unused containers and images to free up space:
    ```bash
    docker system prune -a
    ```
    
## Documentation & Additional information
**The full API documentation is available at:**

[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

**После запуска контейнера будут созданы:**
- Два курса (Один привязан к пользователю), восемь уроков (шесть из которых привязаны к курсам, два привязаны к пользователю), 3 платежа
- Два пользователя:
```json
{
  "email": "test@test.com",
  "password": "12345678"
}
```
```json
{
  "email": "moderator@test.com",
  "password": "12345678"
}
```