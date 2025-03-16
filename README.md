# Aggregation excercise

This is a Python script that uses **PostgreSQL** as its database, managed with **Docker Compose**.

### **Prerequisites**
Ensure you have the following installed:
- [Docker & Docker Compose](https://docs.docker.com/get-docker/)
---

### **Build & Start Containers**

To run this example:
```sh
`docker-compose up`
```
---

### Expected output:

```
RealDictRow([('dimension_1', 'a'), ('dimension_2', 'W'), ('measure_1', 8), ('measure_2', 7)])
RealDictRow([('dimension_1', 'b'), ('dimension_2', 'X'), ('measure_1', 2), ('measure_2', 10)])
RealDictRow([('dimension_1', 'c'), ('dimension_2', 'Y'), ('measure_1', 5), ('measure_2', 0)])
RealDictRow([('dimension_1', 'd'), ('dimension_2', 'Z'), ('measure_1', 0), ('measure_2', 4)])
```
