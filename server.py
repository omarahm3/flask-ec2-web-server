from flask import Flask
from os import environ
import boto3

ec2 = boto3.resource('ec2')
app = Flask(__name__)
app.config['ec2_instance_id'] = environ.get('EC2_INSTANCE_ID')

print('------------- SERVER INFO --------------')
print('Printing needed ENV variables')
print('PORT\t\t', environ.get('PORT'))
print('EC2_INSTANCE_ID\t\t', environ.get('EC2_INSTANCE_ID'))
print('FLASK_APP\t\t', environ.get('FLASK_APP'))
print('AWS_ACCESS_KEY_ID\t', environ.get('AWS_ACCESS_KEY_ID'))
print('AWS_SECRET_ACCESS_KEY\t', environ.get('AWS_SECRET_ACCESS_KEY'))
print('------------- SERVER INFO --------------')

def getInstance():
    return ec2.Instance(app.config['ec2_instance_id'])

def getInstanceTags():
    tags = getInstance().tags
    print('MRG:: Instance tags', tags)
    return tags

@app.route('/')
def home():
    return "<p>Server is up & running... </p>"

@app.route("/tags")
def tags():
    print('MRG:: User requesting tags..')
    tags = getInstanceTags()
    html = ''
    for tag in tags:
        html += f"<p><b>{tag['Key']}:</b> <small>{tag['Value']}</small></p>"
    return html

@app.route('/shutdown')
def shutdownInstance():
    print('MRG:: User is shutting down the instance..')
    result = getInstance().stop()
    print('MRG:: Shutdown result', result)

    return f"<p><b>Server [{app.config['ec2_instance_id']}] was shutdown</b></p>"

if __name__ == '__main__':
    port = int(environ.get('PORT', 80))
    app.run(host="0.0.0.0", port=port, debug=True)
