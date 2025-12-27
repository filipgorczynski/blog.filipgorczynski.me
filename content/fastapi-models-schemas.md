Title: FastAPI: Routes, Models, Schemas and Data Validation, Repotiories
Date: 2025-12-07 09:35:52
Modified: 2025-12-07 09:35:52
Category: Tech
Tags: #tech, #fastapi
Slug: fast-api-models-schemas-and-data-validation
Author: filipgorczynski
Status: draft
Cover: https://blog.filipgorczynski.me/images/post/2025/06/2025-06-24T122628.jpeg
meta_url: https://blog.filipgorczynski.me/2025/12/fast-api-models-schemas-and-data-validation
Summary: Due to popular demand of the FastAPI understanding I still struggle with separation of models and schemas. As I spent most of my development in Django, I tend to mix those two concepts. I will try to clarify the differences and best practices, at least as notes for my future self.

Due to popular demand of the FastAPI understanding I still struggle with separation of models and schemas. As I spent most of my development in Django, I tend to mix those two concepts. I will try to clarify the differences and best practices, at least as notes for my future self.

## Plan

-   Create FastAPI project
-   Set up database connection
-   Define Models using SQLAlchemy
-   Create Schemas using Pydantic
-   Validate data using Schemas
-   Repository pattern for data access
-   Implement CRUD operations: route handlers
-   What are Schemas?
-   What are Models?
-   What is orm_mode=True
-   Differences between Models and Schemas
-   Best Practices
