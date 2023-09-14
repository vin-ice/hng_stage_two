# HNGx Internship - Stage Two
You are to build a simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. 
Your API should dynamically handle parameters, such as adding or retrieving a person by name. Accompany the development with UML diagrams to represent your system's design and database structure.  
Host your entire project on GitHub, and provide a well-structured documentation in the repository that outlines request/response formats, setup instructions, and sample API usage.

## Table of Content
* [Environment](#environment)
* [Setup](#setup)
* [API](#API)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Setup
run:
*   [git clone](https://www.github.com/vin-ice/hng_stage_two.git)
*   `cd 0x02-stage_two`
*   `python -m venv venv && source venv/bin/activate`
*   `source ./.env
*   `pip installl -r requirements.txt`
*   `cat db_dev.sql | mysql -u <user> -p <password>`

## API
End Point    | Method | Path parameter | Body Parameter  (json)  | Return Type (json)
------------ | ------ | -------------- | ----------------------- | --------------
/api         | POST   |  -             | {name: str, value: str} | {name: str, value: str, user_id: str(uuid4)}
/api/user_id | GET    | user_id: str   |             -           | {name: str, value: str, user_id: str(uuid4)}
/api/user_id | PUT    | user_id: str   | {name: str, value: str} | {name: str, value: str, user_id: str(uuid4)}
/api/user_id | DELETE | user_id: str   | -                       | {name: str, value: str, user_id: str(uuid4)}

