### django aws eb base project code

### versions
- python 3.6.3
  - elastic beanstalk
- django 2.1.10

### 
- awscli
- awsebcli
- boto3
- django-cors-headers
- django-storages


* steps to Install

- create aws iam user
- activate venv and pip install -r requirements.txt
- eb init
- eb create
- update .gitlab-ci.yml
- update bin/development.sh and bin/production.sh
- update config in aws elastic beanastalk config as per production.py os.environ variable
- set AWS_ACCESS_KEY_ID, AWS_DEFAULT_REGION, AWS_SECRET_ACCESS_KEY in gitlab ci_cd Variables

