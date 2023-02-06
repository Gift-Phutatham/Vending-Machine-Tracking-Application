# Vending-Machine-Tracking-Application

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Gift-Phutatham_Vending-Machine-Tracking-Application&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Gift-Phutatham_Vending-Machine-Tracking-Application)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Gift-Phutatham_Vending-Machine-Tracking-Application&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Gift-Phutatham_Vending-Machine-Tracking-Application)

## How to Run the Project

```
docker compose up -d
python manage.py migrate
python manage.py runserver
```

## API Reference

### Vending Machine

#### Get all vending machines

```http
  GET /vending-machine/
```

#### Get a vending machine

```http
  GET /vending-machine/<id>/
```

| Parameter | Type  | Description                           |
|:----------|:------|:--------------------------------------|
| `id`      | `int` | **Required**. Id of a vending machine |

#### Create a vending machine

```http
  POST /vending-machine/
```

| Body        | Type      | Description                                                       |
|:------------|:----------|:------------------------------------------------------------------|
| `name`      | `string`  | **Required**. Unique name of a vending machine                    |
| `location`  | `string`  | **Required**. Location of the vending machine                     |
| `is_active` | `boolean` | **Optional**. Status whether the vending machine is active or not |

#### Update a vending machine

```http
  PUT /vending-machine/<id>/
```

| Parameter | Type  | Description                           |
|:----------|:------|:--------------------------------------|
| `id`      | `int` | **Required**. Id of a vending machine |

| Body        | Type      | Description                                                       |
|:------------|:----------|:------------------------------------------------------------------|
| `name`      | `string`  | **Required**. Unique name of a vending machine                    |
| `location`  | `string`  | **Required**. Location of the vending machine                     |
| `is_active` | `boolean` | **Optional**. Status whether the vending machine is active or not |

#### Delete a vending machine

```http
  DELETE /vending-machine/<id>/
```

| Parameter | Type  | Description                           |
|:----------|:------|:--------------------------------------|
| `id`      | `int` | **Required**. Id of a vending machine |

### Product

#### Get all products

```http
  GET /product/
```

#### Get a product

```http
  GET /product/<id>/
```

| Parameter | Type  | Description                   |
|:----------|:------|:------------------------------|
| `id`      | `int` | **Required**. Id of a product |

#### Create a product

```http
  POST /product/
```

| Body   | Type      | Description                            |
|:-------|:----------|:---------------------------------------|
| `name` | `string`  | **Required**. Unique name of a product |
| `cost` | `decimal` | **Required**. Cost of the product      |

#### Update a product

```http
  PUT /product/<id>/
```

| Parameter | Type  | Description                   |
|:----------|:------|:------------------------------|
| `id`      | `int` | **Required**. Id of a product |

| Body   | Type      | Description                            |
|:-------|:----------|:---------------------------------------|
| `name` | `string`  | **Required**. Unique name of a product |
| `cost` | `decimal` | **Required**. Cost of the product      |

#### Delete a product

```http
  DELETE /product/<id>/
```

| Parameter | Type  | Description                   |
|:----------|:------|:------------------------------|
| `id`      | `int` | **Required**. Id of a product |

### Stock

#### Get all stocks

```http
  GET /stock/
```

#### Get a stock

```http
  GET /stock/<id>/
```

| Parameter | Type  | Description                 |
|:----------|:------|:----------------------------|
| `id`      | `int` | **Required**. Id of a stock |

#### Create a stock

```http
  POST /stock/
```

| Body              | Type  | Description                                                  |
|:------------------|:------|:-------------------------------------------------------------|
| `vending_machine` | `int` | **Required**. Id of a vending machine                        |
| `product`         | `int` | **Required**. Id of a product                                |
| `quantity`        | `int` | **Required**. Quantity of the product in the vending machine |

#### Update a stock

```http
  PUT /stock/<id>/
```

| Parameter | Type  | Description                 |
|:----------|:------|:----------------------------|
| `id`      | `int` | **Required**. Id of a stock |

| Body              | Type  | Description                                                  |
|:------------------|:------|:-------------------------------------------------------------|
| `vending_machine` | `int` | **Required**. Id of a vending machine                        |
| `product`         | `int` | **Required**. Id of a product                                |
| `quantity`        | `int` | **Required**. Quantity of the product in the vending machine |

#### Delete a stock

```http
  DELETE /stock/<id>/
```

| Parameter | Type  | Description                 |
|:----------|:------|:----------------------------|
| `id`      | `int` | **Required**. Id of a stock |
