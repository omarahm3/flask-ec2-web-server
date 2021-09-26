# Simple Flask Web Server
This is a simple Flask web server that was created to test interacting with AWS EC2 instance by calling sending requests to endpoints, it exposes these endpoints:

- `/`: Home page, act like a status page to check whether the server is actually running
- `/tags`: Will return a list of instance tags
- `/shutdown`: Will shutdown the instance, and response will print the instance ID if stopping the instance was actually done

## Setup
Make sure you have this installed, versions here were the ones used to actually develop this server, other versions were not tested:

- Python: 3.8.10 (Required)
- Pip: 20.0.2 (Required)
- Docker: 20.10.8, build 3967b7d
- Docker Server: 20.10, build 75249d8

## Run
Server can be run locally using Flask, first you can have a virtual environment using `venv`

```
python3 -m venv venv
. venv/bin/activate # Or you can source venv/bin/activate.fish if you're using fish
```

Then just install the requirements 

```
pip3 install -r requirements.txt
```

Server is expecting some ENV variables to be exported and used by the script. You can also prefix the `flask run` command with the ENV variables it expects

- `AWS_ACCESS_KEY_ID` (Required)
- `AWS_SECRET_ACCESS_KEY` (Required)
- `EC2_INSTANCE_ID` (Required)
- `AWS_DEFAULT_REGION` (Required)
- `FLASK_APP` (Required)

For example:
```
EC2_INSTANCE_ID=i-hu423h482h8 FLASK_APP=server FLASK_DEBUG=1 AWS_DEFAULT_REGION=eu-central-1 AWS_ACCESS_KEY_ID=xxxxxxxxxxxxx AWS_SECRET_ACCESS_KEY=xxxxxxxxxx flask run
```

Then you can check the CLI output, normally server will be running locally on port `5000` and you can check it on http://localhost:5000

Or you can simply run it using docker, by:
```
docker build -t mrg/flask .
docker run -d --net=host --name flask-server -e EC2_INSTANCE_ID=i-hu423h482h8 -e AWS_ACCESS_KEY_ID=XXXXX -e AWS_SECRET_ACCESS_KEY=XXXXXXX -e AWS_DEFAULT_REGION=eu-central-1 mrg/flask
```

Then you can access the server by heading to http://localhost.

## Technical Description
This web server is built on top of [Flask framework](https://flask.palletsprojects.com/en/2.0.x/) and its heavily using [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to interact with AWS services, customization is done using ENV variables that are later obtained by python `os.environ`. Mainly this web server is interacting with AWS EC2 instance to retrieve a list of its current tags, and to shutdown this instance.






















































