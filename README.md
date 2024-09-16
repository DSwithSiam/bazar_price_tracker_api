### **Bazar (Market) Price Tracker API Documentation**

---

#### **API Base URL:**
`http://127.0.0.1:8000/api/`

---

### **Authentication**
**JWT Authentication** ব্যবহার করতে হবে।

- **Login and Get Token:**
  - **URL:** `/api/token/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Response:**
    ```json
    {
      "refresh": "your_refresh_token",
      "access": "your_access_token"
    }
    ```

- **Refresh Token:**
  - **URL:** `/api/token/refresh/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "refresh": "your_refresh_token"
    }
    ```
  - **Response:**
    ```json
    {
      "access": "new_access_token"
    }
    ```

---

### **Market API**

- **Get All Markets**
  - **URL:** `/api/markets/`
  - **Method:** `GET`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Kawran Bazar",
        "location": "Dhaka",
        "opening_hours": "9 AM - 9 PM"
      }
    ]
    ```

- **Get Single Market**
  - **URL:** `/api/markets/{id}/`
  - **Method:** `GET`
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Kawran Bazar",
      "location": "Dhaka",
      "opening_hours": "9 AM - 9 PM"
    }
    ```

- **Create New Market**
  - **URL:** `/api/markets/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "name": "New Market",
      "location": "Sylhet",
      "opening_hours": "10 AM - 8 PM"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 2,
      "name": "New Market",
      "location": "Sylhet",
      "opening_hours": "10 AM - 8 PM"
    }
    ```

- **Update Market**
  - **URL:** `/api/markets/{id}/`
  - **Method:** `PUT`
  - **Request Body:**
    ```json
    {
      "name": "Updated Market",
      "location": "Chittagong",
      "opening_hours": "8 AM - 6 PM"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Updated Market",
      "location": "Chittagong",
      "opening_hours": "8 AM - 6 PM"
    }
    ```

- **Delete Market**
  - **URL:** `/api/markets/{id}/`
  - **Method:** `DELETE`
  - **Response:** `204 No Content`

---

### **Item API**

- **Get All Items**
  - **URL:** `/api/items/`
  - **Method:** `GET`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Potato"
      },
      {
        "id": 2,
        "name": "Tomato"
      }
    ]
    ```

- **Create New Item**
  - **URL:** `/api/items/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "name": "Onion"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 3,
      "name": "Onion"
    }
    ```

---

### **Price API**

- **Get All Prices**
  - **URL:** `/api/prices/`
  - **Method:** `GET`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "market": {
          "id": 1,
          "name": "Kawran Bazar"
        },
        "item": {
          "id": 1,
          "name": "Potato"
        },
        "price_per_kg": "30.00",
        "last_updated": "2024-09-15"
      }
    ]
    ```

- **Create New Price**
  - **URL:** `/api/prices/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "market": 1,
      "item": 2,
      "price_per_kg": "40.00"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 2,
      "market": {
        "id": 1,
        "name": "Kawran Bazar"
      },
      "item": {
        "id": 2,
        "name": "Tomato"
      },
      "price_per_kg": "40.00",
      "last_updated": "2024-09-15"
    }
    ```

- **Update Price**
  - **URL:** `/api/prices/{id}/`
  - **Method:** `PUT`
  - **Request Body:**
    ```json
    {
      "market": 1,
      "item": 2,
      "price_per_kg": "45.00"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "market": {
        "id": 1,
        "name": "Kawran Bazar"
      },
      "item": {
        "id": 2,
        "name": "Tomato"
      },
      "price_per_kg": "45.00",
      "last_updated": "2024-09-15"
    }
    ```

---

### **Price Comparison API**

- **Compare Prices of an Item in Multiple Markets**
  - **URL:** `/api/compare/`
  - **Method:** `GET`
  - **Query Parameters:**
    - `item`: Item name
    - `markets`: List of market IDs (comma-separated)
  - **Example URL:**
    `/api/compare/?item=potato&markets=1,2`
  - **Response:**
    ```json
    {
      "prices": [
        {
          "market": {
            "id": 1,
            "name": "Kawran Bazar"
          },
          "item": {
            "id": 1,
            "name": "Potato"
          },
          "price_per_kg": "30.00",
          "last_updated": "2024-09-15"
        },
        {
          "market": {
            "id": 2,
            "name": "New Market"
          },
          "item": {
            "id": 1,
            "name": "Potato"
          },
          "price_per_kg": "28.00",
          "last_updated": "2024-09-15"
        }
      ]
    }
    ```

---

### **Price History API**

- **Get Price History of an Item**
  - **URL:** `/api/prices/{item_id}/history/`
  - **Method:** `GET`
  - **Response:**
    ```json
    {
      "history": [
        {
          "market": {
            "id": 1,
            "name": "Kawran Bazar"
          },
          "item": {
            "id": 1,
            "name": "Potato"
          },
          "price_per_kg": "30.00",
          "last_updated": "2024-09-15"
        },
        {
          "market": {
            "id": 1,
            "name": "Kawran Bazar"
          },
          "item": {
            "id": 1,
            "name": "Potato"
          },
          "price_per_kg": "35.00",
          "last_updated": "2024-09-14"
        }
      ]
    }
    ```

---

### **Errors and Responses**

- **404 Not Found**: 
  - Occurs if a resource (market, item, price) is not found.
  - **Response:**
    ```json
    {
      "detail": "Not found."
    }
    ```

- **401 Unauthorized**: 
  - Occurs if JWT token is missing or invalid.
  - **Response:**
    ```json
    {
      "detail": "Authentication credentials were not provided."
    }
    ```

---
