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

- **Check API Endpoints**
  - Use Postman or another API client to verify the functionality of the API endpoints.


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
    
## API Endpoints
- После запуска контейнера появятся два курса, восемь уроков (шесть из которых привязаны к курсам, а два — нет), три пользователя и четыре платежа, связанные с курсами и уроками

| **Маршрут**        | **Метод** | **Описание**                                           |  
|--------------------|-----------|--------------------------------------------------------|  
| /learning/courses/ | GET       | Получить список всех курсов                           |  
| /learning/courses/      | POST      | Создать новый курс                                     |  
| /learning/courses/{id}/ | GET       | Получить информацию о конкретном курсе                |  
| /learning/courses/{id}/ | PUT       | Обновить информацию о курсе                           |  
| /learning/courses/{id}/ | DELETE    | Удалить курс                                          |  
| /learning/lessons/      | GET       | Получить список всех уроков                           |  
| /learning/lessons/      | POST      | Создать новый урок                                     |  
| /learning/lessons/{id}/ | GET       | Получить информацию о конкретном уроке                |  
| /learning/lessons/{id}/ | PUT       | Обновить информацию об уроке                          |  
| /learning/lessons/{id}/ | DELETE    | Удалить урок                                          |  
| /users/            | GET       | Получить список всех пользователей                    |  
| /users/{id}/       | GET       | Получить профиль пользователя                         |  
| /users/{id}/       | PUT       | Обновить информацию о пользователе                    |  
| /users/{id}/       | DELETE    | Удалить пользователя                                  |  
| /users/payment/    | GET       | Получить список всех платежей                         |  
| /users/payment/    | POST      | Создать новый платеж                                  |  
