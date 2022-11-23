# Utils bot backend

Its proxy service which routing tasks to service, which can do this tasks


# Communication API

- Proxy service take url of worker services from database. 
- After that its can show all connected service by request to ```/services_list``` route. 
- Client can get more information about particular service and state machine which
this service should use with this service by request to ```/service_info/{id}``` route.
- Client can add task by request to ```/add_task``` route.

# API specification

### /services_list

Its route return the array of the JSON objects, which described above

```json
{
  "service_id": 0,
  "service_name": "image_transform_service"
}
```

### /service_info/{id}

Its route return more information about service with particular {id}

```json
{
  "service_id": 0, // int
  "service_name": "image_transform_service", // str
  "service_description": "description" // str.  Some user friendly description of availability of service,
  "arguments": [
    {
      "argument_name": "argument_name",
      "argument_description": "description",
      "type": "image"
    },
    {
      "argument_name": "argument_name2",
      "argument_description": "description",
      "type": "int"
    }
  ] // array. List of arguments, which service is receive
}
```

### /add_task

Its route put task arguments in load balancer and awaiting response

```json
{
  "service_id": 0, // int. Target service id.
  "args": [...] // array. Task argument
}

```

# Include service minimal interface

Description of interface which service should implement for interaction with proxy service

### /me

Its route return all required information about service

```json
{
  "name": "service_name", // str. Name of the service
  "description": "some description", // str. Some service description
  "input": [
    {
      "argument_name": "argument_name",
      "argument_description": "description",
      "type": "image"
    },
    {
      "argument_name": "argument_name2",
      "argument_description": "description",
      "type": "int"
    }
  ]
}
```
