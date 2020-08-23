# Dio handle Transfer-Encoding have some error



Make response data (The server must have Transfer-Encoding)

## Open Transfer-Encoding test server 

listen on 5433

```bash
cd server
python3 read_server.py 
```



and use MDN example to test 

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding

listen on 5432

```bash
cd server
python3 mozilla_example_server.py 
```



---

Other terminal

## 1. test request by Python requests

### test own data

```bash
python3 python_requests_client/main.py 5433
```

### result

```
200

<html>
<title></title>
<head>
<META HTTP-EQUIV="Pragma" content="no-cache">
<META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
...
```

> looks great



### test MDN example data

```bash
python3 python_requests_client/main.py 5432
```

### result

```
200
MozillaDeveloperNetwork
```

>  :)

## 2. test request by Curl

### test own data

```bash
curl http://127.0.0.1:5433
```

### result

```

<html>
<title></title>
<head>
<META HTTP-EQUIV="Pragma" content="no-cache">
<META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
...
```

> looks great



### test MDN example data

```bash
curl http://127.0.0.1:5432 
```

### result

```
MozillaDeveloperNetwork%  
```

> looks great too




## 3. test request by Dart dio

### test own data

```bash
cd Dio_chunked_issue
dart bin/dio_client_test.dart 5433 
```

### result

```
22f

<html>
<title></title>
<head>
<META HTTP-EQUIV="Pragma" content="no-cache">
<META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
<META HTTP-EQUIV="Content-Type" content="text/html;charset=UTF-8">
```

> some chunked length not removed





### test MDN example data

```bash
cd Dio_chunked_issue
dart bin/dio_client_test.dart 5432
```

### result

on MDN example  hmmm...

```
MozillaDeveloperNetwork
```

> Success to parse.





## Make own response data

Make response data (The server must have Transfer-Encoding)

```bash
curl xxx  -i --raw > server/raw_response.data
```

