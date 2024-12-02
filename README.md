```markdown
# Piggy Bank API Documentation

The **Piggy Bank** project is an application to track user expenses. It supports multiple users and allows managing categories, transactions, and currencies.

## Currencies

### List Currencies

- **GET** `http://127.0.0.1:8000/api/currencies/`
- **Authorization**: API Key
  - **Key**: `Authorization`
  - **Value**: `<value>`
```

## Categories

### List Categories

- **GET** `http://127.0.0.1:8000/api/categories/`
- **Authorization**: API Key
  - **Key**: `Authorization`
  - **Value**: `<value>`

### Create Category

- **POST** `http://127.0.0.1:8000/api/categories/`
- **Authorization**: API Key
  - **Key**: `Authorization`
  - **Value**: `<value>`
- **Body (raw JSON)**:
  ```json
  {
    "name": "Home s"
  }
  ```

```

```

### Retrieve Single Category

- **GET** `http://127.0.0.1:8000/api/categories/1/`
- **Authorization**: API Key
  - **Key**: `Authorization`
  - **Value**: `<value>`

### Update Category

- **PATCH** `http://127.0.0.1:8000/api/categories/1/`
- **Body (raw JSON)**:
  ```json
  {
    "name": "changepets"
  }
  ```

### Delete Category

- **DELETE** `http://127.0.0.1:8000/api/categories/1/`
-

## Transactions

### List Transactions

- **GET** `http://127.0.0.1:8000/api/transactions/`
- **Authorization**: API Key
  - **Key**: `Authorization`
  - **Value**: `<value>`
- **Query Parameters**:
  - `page`: Page number (e.g., `2`)
  - `search`: Search by descriptions (e.g., `tea`)
  - `currency__code`: Filter by currency code (e.g., `Rs`)

### Retrieve Single Transaction

- **GET** `http://127.0.0.1:8000/api/transactions/15/`
- **Authorization**: API Key
  - **Key**: `Authorization`
  - **Value**: `<value>`

### Create Transaction

- **POST** `http://127.0.0.1:8000/api/transactions/`
- **Body (raw JSON)**:
  ```json
  {
    "amount": "777",
    "currency": "Rs",
    "date": "2024-11-29",
    "description": "demo Descriptions",
    "category": 8
  }
  ```

### Update Transaction

- **PATCH** `http://127.0.0.1:8000/api/transactions/34/`
- **Body (raw JSON)**:
  ```json
  {
    "amount": "200.00",
    "currency": "EUR",
    "date": "2024-11-17",
    "description": "Test Transactions 3",
    "category": 2
  }
  ```

### Delete Transaction

- **DELETE** `http://127.0.0.1:8000/api/transactions/35/`
- **Authorization**: API Key
  - **Key**: `Authorization`
  - **Value**: `<value>`

## Authentication

### Login

- **POST** `http://127.0.0.1:8000/api/login/`
- **Body (raw JSON)**:
  ```json
  {
    "username": "username",
    "password": "password"
  }
  ```

This structure organizes the API documentation clearly, with each section describing the available endpoints for categories, transactions, authentication, and currencies. The markdown formatting ensures that it is readable and easy to follow in a GitHub repository.

```

```
