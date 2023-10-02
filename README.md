** This is an out of date respository and should not be used, but will keep for historical reference **

# Django Elastic Beanstalk
Starter Template for a Django project that will be deployed to AWS Elastic Beanstalk.
This is a quick template to use if you know you'll be deploying to Amazon Web Services using the Elastic Beanstalk deployment service (combination of EC2, RDS, S3).

# Installation
`git clone https://github.com/awwester/django-elastic-beanstalk <project_name>`

`cd <project_name>`

`pip install -r requirements.txt`

# Deployment
This repository provides all the code you need, but you'll still need to create
and setup your account on AWS. There are some steps involved. I should have a video
out soon that will take you through this whole process.

- Create AWS account
- Setup an IAM user
- eb init
- eb create
- eb deploy
- success

# Options

### Postgres
If you would like to install Postgres with your Elastic Beanstalk deployment, you
can checkout the postgres branch (`git checkout postgres`) which will add the proper settings and server package. **Note: You'll still need to create a Postgres database in the AWS Console**

### Tips
To run manage.py commands on the Amazon Linux server you need to first acticate the environment and current environment
`cd /opt/python/current/app`
`/opt/python/run/venv/bin/python manage.py <command>`
