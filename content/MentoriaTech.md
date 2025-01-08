---
title: "MentoriaTech"
date: 2024-10-21T14:45:17-04:00
draft: true
---

# Sistema 1: E-commerce Microservices Platform

## Objetivos

Aprender conceitos de backend, frontend e DevOps desenvolvendo um sistema full-stack.

- Microservices, containerization, REST APIs, SQL/NoSQL databases, message queues, system design.
- Github Actions, Project Management

## Descrição técnica do projeto

![](mentor-architecture1.png)

**Overview:**
Build a small e-commerce platform with services such as:

- **Product Catalog:** Uses a NoSQL database (e.g., MongoDB) to store product information.
- **Order Management:** Uses SQL (e.g., PostgreSQL) to store orders and transactions.
- **User Service:** Handles authentication (JWT) and user profiles.
- **Notification Service:** Sends emails or SMS using message queues (e.g., RabbitMQ or Kafka).

**Tasks for the mentee:**

- Deploy microservices using **Docker**.
- Set up message queues to notify users of successful orders.
- Integrate SQL for order management and NoSQL for the product catalog.
- Introduce **API gateways** for communication between services.

## Semana 1

### Tarefa
- Implementar serviço de produtos (API em Django Rest Framework, CRUD, banco de dados NoSQL)

### Teoria

- [SQL vs NoSQL](https://medium.com/@abhirup.acharya009/sql-vs-nosql-choosing-the-right-database-model-for-your-business-needs-66aa39199c55)
- [API Gateway vs Load Balancer](https://www.moesif.com/blog/technical/api-development/API-Gateway-VS-Load-Balancer/)
- [A simple guide to configure Nginx as an API Gateway](https://medium.com/@nirmalkumar30/a-simple-guide-to-configure-nginx-as-an-api-gateway-684924cd51d0)
- [Docker curriculum](https://docker-curriculum.com/)
- [Microsserviços Prontos Para a Produção: Construindo Sistemas Padronizados em uma Organização de Engenharia de Software](https://www.amazon.com.br/Microsservi%C3%A7os-Prontos-Para-Produ%C3%A7%C3%A3o-Padronizados/dp/8575226215)

## Semana 2

### Tarefa

- Acessar o console do MongoDB localmente e brincar fazendo queries.
- Implementar frontend de produtos (projeto React, CRUD usando a api criada na primeira semana)
- Usar docker para toda a aplicação (container para o serviço de produtos, pro frontend, pro banco de dados)

### Teoria

![](cap_base_acid.png)

- [CAP Theorem Simplified](https://www.youtube.com/watch?v=BHqjEjzAicA)
- [ACID Databases](https://www.freecodecamp.org/news/acid-databases-explained/#:~:text=ACID%20stands%20for%20Atomicity%2C%20Consistency,guarantees%20out%20of%20the%20box.)
- [ACID vs BASE](https://aws.amazon.com/compare/the-difference-between-acid-and-base-database/)
- [Normalização em banco de dados](https://www.alura.com.br/artigos/normalizacao-banco-de-dados-estrutura?srsltid=AfmBOoomdREOxWZ15bFoRScZ-j8zrGJ-yJHuM51VjP-6gwqx9yJR2h0P)
- [Dockerfile vs. Docker Compose: What You Should Know](https://www.techopsexamples.com/p/dockerfile-vs-docker-compose-what-you-should-know)
- [10 Core Concepts You Need to Know About React](https://payalpaul2436.medium.com/10-main-core-concept-you-need-to-know-about-react-303e986e1763)
- [Microsserviços Prontos Para a Produção: Construindo Sistemas Padronizados em uma Organização de Engenharia de Software](https://www.amazon.com.br/Microsservi%C3%A7os-Prontos-Para-Produ%C3%A7%C3%A3o-Padronizados/dp/8575226215)

## Semana 3

### Tarefa

- Acessar o console do MongoDB localmente e brincar fazendo queries.
- Usar docker para toda a aplicação (container para o serviço de produtos, pro frontend, pro banco de dados)
- Criar (backend e frontend) order management service
	- Com docker, backend em FastAPI, PostgreSQL como banco de dados. 

### Teoria

- [Database Types](https://www.linkedin.com/posts/tauseeffayyaz_%F0%9D%90%83%F0%9D%90%9A%F0%9D%90%AD%F0%9D%90%9A%F0%9D%90%9B%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%9E-%F0%9D%90%93%F0%9D%90%B2%F0%9D%90%A9%F0%9D%90%9E%F0%9D%90%AC-key-value-activity-7261767413392699392-NRLK/?utm_source=share&utm_medium=member_desktop)
- [7 must-know strategies to scale your database](https://www.linkedin.com/feed/update/urn:li:activity:7261693073129115648/?utm_source=share&utm_medium=member_android)
- [Locust load testing](https://www.linode.com/docs/guides/load-testing-with-locust/)
- [Microsserviços Prontos Para a Produção: Construindo Sistemas Padronizados em uma Organização de Engenharia de Software](https://www.amazon.com.br/Microsservi%C3%A7os-Prontos-Para-Produ%C3%A7%C3%A3o-Padronizados/dp/8575226215)



## Semana 4

### Tarefa

- Fazer load-testing da aplicação localmente
- Usar docker para toda a aplicação (container para o serviço de produtos, pro frontend, pro banco de dados)

### Teoria

- [Selecting a React Component Library, the Strategic Way](https://www.superblocks.com/blog/selecting-a-react-component-library-the-strategic-way)
- [What I Wish Someone Told Me About Postgres](https://challahscript.com/what_i_wish_someone_told_me_about_postgres)
- [How Amazon Scaled E-commerce Shopping Cart Data Infrastructure](https://newsletter.systemdesign.one/p/amazon-dynamo-architecture)
- [Everything You NEED to KNOW About Web Applications](https://www.youtube.com/watch?v=_higfXfhjdo)


## Semana 5

![](microservices-architecture.gif)

###  Tarefa

- Consertar docker
- Montar layout do site (usando alguma component library do react e/ou tailwind)

### Teoria
- [From laid off to hired: A Software Engineer’s guide](https://newsletter.eng-leadership.com/p/from-laid-off-to-hired-a-software)
- [Good software development habits](https://zarar.dev/good-software-development-habits/)
- [7 Mindsets That Are Slowing Down Your Career Growth](https://www.thecaringtechie.com/p/7-mindsets-that-are-slowing-down)

# Sistema 2: AWS - Site estático

## Semana 6

### Tarefa

- Deployar um site estático na AWS

### Teoria

- [AWS - Host a Static Website](https://aws.amazon.com/getting-started/hands-on/host-static-website/)

# Sistema 3: Task Management Application

![](mentor-architecture2.png)

### High-Level Overview
This project is a task management application designed to allow users to manage their daily tasks with features like adding, updating, deleting, and categorizing tasks. Each task can have a title, description, priority, deadline, and tags (e.g., "work," "personal"). Users will also be able to mark tasks as completed and filter tasks by category, deadline, or priority.

The system should be implemented using Python for the backend, React for the frontend, and deployed to AWS. It will focus on SOLID principles, proper API design, NoSQL database usage, and design patterns for maintainable and scalable code.

### Core Functionalities
#### User Authentication
- Register, login, and logout features using AWS Cognito.
- Secure the API with authentication tokens (JWT).
#### Task Management
- Add new tasks with details (title, description, priority, deadline, tags).
- Update or delete existing tasks.
- Mark tasks as completed.
- List tasks with filtering and sorting options (e.g., by priority, deadline, or tags).
#### Tags Management
- Allow users to define and assign tags for better categorization.
#### Task Insights
- Provide a summary of task statistics, such as the number of completed tasks and pending tasks grouped by priority or deadline.
### High-Level Architecture
#### Frontend (React)

- UI Framework: Use Material-UI or Tailwind CSS for styling.
- State Management: Use Context API or Redux for state management.

##### Features:
- A dashboard for managing tasks.
- Forms for adding/updating tasks.
- Filtering and sorting options for tasks.
- Authentication pages (login/register).

#### Backend (Python)

- Framework: Use FastAPI for a clean and simple API.
- Database: Use MongoDB (hosted on AWS DocumentDB) for storing tasks, users, and tags.

##### Features:
- RESTful APIs for CRUD operations.
- Input validation and error handling.
- Modularized codebase adhering to SOLID principles.

#### AWS Deployment
- Backend: Deploy as a containerized service using AWS ECS.
- Frontend: Host the React app on AWS S3 and use CloudFront for CDN.
- Database: Use AWS DocumentDB (MongoDB).
- Authentication: Manage using AWS Cognito.

### Focus on SOLID Principles
- **Single Responsibility**: Separate concerns into services: authentication, task management, and tags.
- **Open/Closed Principle**: Design services and models to allow extensions without modifying the existing codebase.
- **Liskov Substitution**: Use interfaces or abstract classes where necessary (e.g., for repository pattern).
- ** Interface Segregation**: Keep APIs focused on single responsibilities (e.g., task endpoints don’t handle user-related operations).
- ** Dependency Inversion**: Use dependency injection for database access, allowing for easier testing and mocking.

### Design Patterns
- **Repository Pattern**: Abstract MongoDB operations into a repository to separate database logic from business logic.
- **Factory Pattern**: Use factories for creating tasks or tags with default values and validations.
- **Strategy Pattern**: Implement sorting and filtering using interchangeable strategies.

### AWS Services
- AWS ECS: Host the Python backend as a containerized service.
- AWS S3 + CloudFront: Serve the React frontend.
- AWS Cognito: Manage user authentication.
- AWS DocumentDB: Store tasks and tags in a MongoDB-compatible NoSQL database.
- AWS CloudWatch: Monitor logs and system performance.
- AWS IAM: Secure access to AWS resources.

## Semana 7

![](big-o.gif)

![](oop.gif)

### Teoria

- [Linux Commands Every DevOps Engineer Must Know](https://linux-series.hashnode.dev/linux-commands-every-devops-engineer-must-know)
- [Big O Notation](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)
- [SOLID: The First 5 Principles of Object Oriented Design](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
- [Design Patterns in Python](https://refactoring.guru/design-patterns/python)