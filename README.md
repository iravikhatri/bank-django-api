# Bank Branch API

## API Features

1) Given a bank branch IFSC code, get branch details
2) Given a bank name and city, gets details of all branches of the bank in the city

## How to use API

### Call base url like

```
http://localhost/api or  http://127.0.0.1:8000/api
```

&nbsp;
### Getting a bank details by IFSC code

To call api use base url with endpoint complete url with endpoint:
```
http://localhost/api/banks
```

It also takes an argument 'ifsc' with endpoint
```
?ifsc=value
```

&nbsp;

Example: A bank IFSC code is ABHY0065020

The complete url will be like
```
http://localhost/api/banks?ifsc=ABHY0065020
```

Result:
```json
{
    "id": 1,
    "ifsc": "ABHY0065020",
    "bank_id": 60,
    "branch": "DHARAVI",
    "address": "WESTERN INDIA TANNERIES, SION DHARAVI ROAD, MUMBAI-400017",
    "city": "MUMBAI",
    "district": "GREATER MUMBAI",
    "state": "MAHARASHTRA",
    "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
}
```

&nbsp;
### Getting details of all branches of the bank in the city by bank name and city

To call api use base url with endpoint complete url with endpoint:
```
http://localhost/api/banks
```

It also takes 2 arguments 'city' and 'name' with endpoint
```
?bank_name=value&city=value
```

&nbsp;

Example: A bank name is ABHYUDAYA COOPERATIVE BANK LIMITED and city PUNE

The complete url will be like
```
http://localhost/api/banks?bank_name=ABHYUDAYA COOPERATIVE BANK LIMITED&city=PUNE
```

Result:

```json
[

    {
        "id": 7,
        "ifsc": "ABHY0065105",
        "bank_id": 60,
        "branch": "PIMPRI",
        "address": "SUNSHINE MARKS, CTS NO.4840, MUMBAI-PUNE RD, OPP B AMBEDKAR STATUE, PIMPRI, PUNE-411018",
        "city": "PUNE",
        "district": "PUNE",
        "state": "MAHARASHTRA",
        "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
    },
    {
        "id": 8,
        "ifsc": "ABHY0065106",
        "bank_id": 60,
        "branch": "PAUD PHATA",
        "address": "MANGALAM CHAMBERS, ERANDWANA, PAUD ROAD, PUNE-411038",
        "city": "PUNE",
        "district": "PUNE",
        "state": "MAHARASHTRA",
        "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
    }
]
```
