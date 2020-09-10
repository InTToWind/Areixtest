# Introduction

Areix test API is used for tracking expense records and presenting an analytical view based on them.

# Functions

This API provides a variety of functions where users are able to create, edit, delete and inquire their expense records. Users may also get filtered, sorted and summary results.

## Create Expense

  Create an expense record.

* **URL**

  /api/expense

* **Method:**

  `POST`
  
*  **URL Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| name | string | expense record name |
| amount | double | expense record amount |
| category | string | expense record category |
| created_at | string | expense record created date |

* **Success Response:**

```
{
    “data”: {
      'record_id': 1231343112,
      'name': xxx,
      'amount': 900.0,
      'category': 'Leisure',
      'created_at': '2020-02-02'
    },
    “error”: false,
    “success”: true,
    "msg": 'successfully created an expense'
    }
```
* **Error Response:**

  * **Reason:** Users have to make a request form.
    **Content:** `{'error': True, 'msg': '404 NOT FOUND'}`

  OR

  * **Reason:** Users input 'amount' or 'category' in the wrong form. 'amount' should be real positive numbers and 'category should be one of Leisure, Others, Financials and Homes'
    **Content:** `{'error': True, 'msg': 'Invalid Input'}`

## Get Expense record list

  Return Expense record List data

* **URL**

  /api/expenses/page={page}&per_page={per_page}

* **Method:**

  `GET`
  
*  **URL Params**

| Name | Type | Description |
| :---: | :---: | --- |
| page | int | page |
| per_page | int | number of items per page |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
|  |  | |

* **Success Response:**

    **Content:** 
```
{
  “data”: [
    {
      "record_id": "x11",
      "name": "xxx1",
      "created_at": '2020-04-23',
      "amount": 22133.23,
      "category":"Home",
    },
    ...
  ],
  “error”: false,
  “success”: true,
  “msg”: “'successfully got detailed expenses records'”
}
```
* **Error Response:**

  * **Reason:** Users have to input valid page number and records per page.
    **Content:** `{'error': True, 'msg': '404 NOT FOUND'}`

## Get Expense record detail

  Return Expense record detail data

* **URL**

  /api/expense/{record_id}

* **Method:**

  `GET`
  
*  **URL Params**

| Name | Type | Description |
| record_id | int | the record id to be inquired |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Success Response:**

    **Content:** 

```
{
  “data”: {
      "record_id": "x11",
      "name": "xxx1",
      "created_at": '2020-04-23',
      "amount": 22133.23,
      "category":"Home",
  },
  “error”: false,
  “success”: true,
  “msg”: 'successfully got detailed record'
}
```
* **Error Response:**

  * **Reason:** Users have to input a valid record id.
    **Content:** {'error': True, 'msg': '404 NOT FOUND'}

## Edit Expense record

  Edit Expense record

* **URL**

  /api/expense/{record_id}

* **Method:**

  `PUT`
  
*  **URL Params**

| Name | Type | Description |
| record_id | int | the record id to be updated |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| name | string | updated name of the record |
| amount | double | updated amount of the record |
| category | string | updated category of the record |
| created_at | string | updated created time of the record |

* **Success Response:**

    **Content:** 

```
{
  “data”: None,
  “error”: false,
  “success”: true,
  “msg”: 'successfully updated record'
}
```

* **Error Response:**

  * **Reason:** No record id was found.
    **Content:** `{'error': True, 'msg': '404 NOT FOUND'}`

  OR

  * **Reason:** Users input 'amount' or 'category' in the wrong form. 'amount' should be real positive numbers and 'category should be one of Leisure, Others, Financials and Homes'
    **Content:** `{'error': True, 'msg': 'Invalid Input'}`

## Delete Expense record

  Delete Expense record

* **URL**

  /api/expense/{record_id}

* **Method:**

  `DELETE`
  
*  **URL Params**

| Name | Type | Description |
| record_id | int | the record id to be deleted |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Success Response:**

    **Content:** 

```
{
  “data”: None,
  “error”: false,
  “success”: true,
  “msg”: 'successfully deleted record'
}
```

* **Error Response:**

  * **Reason:** No record id was found.
    **Content:** `{'error': True, 'msg': '404 NOT FOUND'}`

## Filter by category

  Filter by category

* **URL**

  /api/expense/category={category}

* **Method:**

  `GET`
  
*  **URL Params**

| Name | Type | Description |
| category | str | chosen category to be shown |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Success Response:**

    **Content:** 

```
{
  “data”: [
    {
      "record_id": "x11",
      "name": "xxx1",
      "created_at": '2020-04-23',
      "amount": 22133.23,
      "category":"Home",
    },
    ...
  ],
  'category': category,
  “error”: false,
  “success”: true,
  “msg”: 'successfully filtered by ...'
}
```

* **Error Response:**

  * **Reason:** 'category' should be one of Financials, Leisure, Others and Homes.
    **Content:** `{'error': True, 'msg': 'no such category'}`

## Filter by month

  Filter by month

* **URL**

  /api/expense/year={year}&month={month}

* **Method:**

  `GET`
  
*  **URL Params**

| Name | Type | Description |
| year | int | selected year |
| month | int | selected month |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Success Response:**

    **Content:** 

```
{
  “data”: [
    {
      "record_id": "x11",
      "name": "xxx1",
      "created_at": '2020-04-23',
      "amount": 22133.23,
      "category":"Home",
    },
    ...
  ],
  'category': category,
  “error”: false,
  “success”: true,
  “msg”: 'successfully filtered by ...'
}
```

  OR

```
{
	'error': False,
	'msg': 'no records found'
}
```

## Sort by created_at

  Sort by created_at

* **URL**

  /api/expense/sort_by_created_at

* **Method:**

  `GET`
  
*  **URL Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Success Response:**

    **Content:** 

```
{
  “data”: [
    {
      "record_id": "x11",
      "name": "xxx1",
      "created_at": '2020-04-23',
      "amount": 22133.23,
      "category":"Home",
    },
    ...
  ],
  “error”: false,
  “success”: true,
  “msg”: 'successfully sorted by created at'
}
```

  OR

```
{
	'error': False,
	'msg': 'no records found'
}
```

## Sort by amount

  Sort by amount

* **URL**

  /api/expense/sort_by_amount

* **Method:**

  `GET`
  
*  **URL Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Success Response:**

    **Content:** 

```
{
  “data”: [
    {
      "record_id": "x11",
      "name": "xxx1",
      "created_at": '2020-04-23',
      "amount": 22133.23,
      "category":"Home",
    },
    ...
  ],
  “error”: false,
  “success”: true,
  “msg”: 'successfully sorted by amount'
}
```

  OR

```
{
	'error': False,
	'msg': 'no records found'
}
```

## Analyze expenses

  Analyze expenses

* **URL**

  /api/expense/analysis

* **Method:**

  `GET`
  
*  **URL Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Data Params**

| Name | Type | Description |
| :---: | :---: | --- |
| | | |

* **Success Response:**

    **Content:** 

```
{
  “data”: [
    {
      'sum_amount': 100,
      'max_amount': 50,
      'mean_amount': 20
    },
    ...
  ],
  “error”: false,
  “success”: true,
  “msg”: 'successfully analyze the records'
}
```

  OR

```
{
	'error': False,
	'msg': 'no records found'
}
```








