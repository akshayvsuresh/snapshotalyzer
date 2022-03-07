from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from google.cloud import storage
from twilio.rest import Client
import pymsteams
import sendgrid
import base64
import json
import os
import re
import time
import requests
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
"""Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
        
"""
def terraformbuild(event, context):
    myTeamsMessage = pymsteams.connectorcard("https://deloitte.webhook.office.com/webhookb2/aa700184-cdec-464d-b903-8b5624983c0f@36da45f1-dd2c-4d1f-af13-5abe46b99921/IncomingWebhook/8562c87b5af4473294546a1520c145b8/c8a4981b-7615-47e4-b3e0-a53625cb9a0f")
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    # Pub/Sub message
    final = json.loads(pubsub_message)

    def mail(subject,context):
        if str(os.environ['EMAIL']) == 'ENABLE':
            sg = sendgrid.SendGridClient("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")
            message = sendgrid.Mail()
            message.add_to("lishadang308@gmail.com")
            message.set_from("akshayvsuresh27@gmail.com")
            message.set_subject(str(subject))
            message.set_html(str(context))
            sg.send(message)

    # mail(subject="blah",context="benjamin");
    def teams(message,title,color):
        if str(os.environ['TEAMS']) == 'ENABLE':
            HOOK_URL="https://deloitte.webhook.office.com/webhookb2/aa700184-cdec-464d-b903-8b5624983c0f@36da45f1-dd2c-4d1f-af13-5abe46b99921/IncomingWebhook/8562c87b5af4473294546a1520c145b8/c8a4981b-7615-47e4-b3e0-a53625cb9a0f"    
            message = message
            title=title
            base_data = {
            "color": color,
            "title": title,
            "text": message
            }

            message = {
            "@context": "https://schema.org/extensions",
            "@type": "MessageCard",
            "themeColor": base_data["color"],
            "title": base_data["title"],
            "text": base_data["text"]
            }
            req = Request(HOOK_URL, json.dumps(message).encode('utf-8'))
            response = urlopen(req)
            response.read()
    def caller(message):
        if str(os.environ['CALLS']) == 'ENABLE':

            account_sid = "AC99d0792d1b153d03391d642272e9c900"

            auth_token = "59ef3f9560d6cbeb029faa2cea56dbba"

            client = Client(account_sid, auth_token)

            mesg='<Response><Say>'+message+'</Say></Response>'

            call = client.calls.create(

            twiml=mesg,

            to='+917012528320',

            from_='+17065103202'

            )
    
    def slack(message):
        if str(os.environ['SLACK']) == 'ENABLE':
            payload='{"text":"%s"}' %message
            response=requests.post('https://hooks.slack.com/services/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',data=payload)
            print(response.text)


    """ Resource Type[compute instance, buckets, 
        cloudsql, firewall] for this request.
    """
    resourcetype = final['resource']['type']

    # Compute Engine Vulnerabilities
    if resourcetype == 'gce_instance':
    
        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('compute', 'v1', credentials=credentials)
        # Instance ID for this request.
        instanceid = final['resource']['labels']['instance_id']

        # Implement labels using function.
        def labels():
            credentials = GoogleCredentials.get_application_default()
            service = discovery.build('compute', 'v1', credentials=credentials)

            # Name of the instance scoping this request.    
            resource_name = final['protoPayload']['request']['name']
            # Project ID for this request.
            project_id = final['resource']['labels']['project_id']
            # The name of the zone for this request.
            zone = final['resource']['labels']['zone']

            email = final['protoPayload']['authenticationInfo']['principalEmail']
            first_name = email.partition('@')
            owner = first_name[0]

            
            try: 
                instances_set_labels_request_body = {
                # TODO: Add desired entries to the request body.
                    "labels": { "user": project_id , 
                        "owner": owner },

                    "labelFingerprint": "42WmSpB8rSM="
                }

                request = service.instances().setLabels(project=project_id, zone=zone, instance=resource_name, body=instances_set_labels_request_body)
                response = request.execute()
                string = "Labels are implemented by-default on instance created by "+ str(email)
                teams(message= string,title="INFO!!",color="64a837");


            except Exception as e:
                myTeamsMessage.text(str(e))
                myTeamsMessage.send()

        
        # Checking service account usage with regular expression..
        def servicaccount():
            service = final['protoPayload']['request']['serviceAccounts']
            zone = final['resource']['labels']['zone']
            service1 = service[0]
            serviceaccount=service1['email']
            pattern = re.compile(r'^[\d*]+\-+[a-z]+@developer.gserviceaccount.com')
            try: 
                if re.search(pattern, serviceaccount):

                    string = "Service account created in "+ str(zone) + "is using default service account"
                    teams(message= string,title="WARNING!!",color="cd5c5c");
                else: 
                    
                    string = "Service account created in "+ str(zone) + "is not using default service account"
                    teams(message= string,title="INFO!!",color="64a837"); 
            
            except Exception as e:
                myTeamsMessage.text(str(e))
                myTeamsMessage.send()

        """ Checking deletion Protection enabled or not.. [ if its enabled 
        at the time of deleting instance it will show as restriction]"""
        def delprotection():
            deleprotect = final['protoPayload']['request']['deletionProtection']
            
            if deleprotect == False:
                
                string = "Instance id "+ str(instanceid) + " has not enabled deletionProtection."
                teams(message= string,title="ALERT!",color="E4D00A");
        
        # Checking network account usage with slicing..
        def default():
            network = final['protoPayload']['request']['networkInterfaces']
            interface = network[0]
            networkinterf = interface['subnetwork']
            interest = networkinterf[-8:]
            if interest == '/default':

                string = "Instance id "+ str(instanceid) + " is using default network.. Please change it"
                teams(message= string,title="ALERT!",color="E4D00A");


        labels();
        servicaccount();
        delprotection();
        default();
        
    # Cloud Storage Vulnerabilities
    elif resourcetype == 'gcs_bucket':
        bucket_name = final['resource']['labels']['bucket_name']
        
        try:
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)
            
        except Exception as e:
            myTeamsMessage.text(str(e))
            myTeamsMessage.send()

        # Location may be in region or multi-region..
        def location():
            if bucket.location_type[0:2] != 'mu':
                string = "Please enable bucket "+ str(bucket_name) + " to multi-region for high avaliblilty.."
                teams(message= string,title="INFO!!",color="64a837");
                mail(subject="Bucket location",context=str(string));

        # Configure retention policy is enabled or not. [i.e. time period take to prevent bucket deletion]
        def retention():
            if bucket.retention_period == None:
                string = "Bucket retention period is not enabled for bucket "+ str(bucket_name) 
                teams(message= string,title="WARNING !!",color="cd5c5c");
                mail(subject="Bucket retention",context=str(string));

        """Configuring public access prevention is enforced or inherited[enforced 
        will make it as private and inherited will make it as public]"""
        def publicaccess():
            if bucket.iam_configuration.public_access_prevention == 'enforced':
                string = "Public access is enabled for bucket "+ str(bucket_name) 
                teams(message= string,title="ALERT !!",color="E4D00A");
                mail(subject="Bucket public",context=str(string));
            else:
                
                string = "Public access is not enabled for bucket "+ str(bucket_name) 
                teams(message= string,title="ALERT !!",color="E4D00A");
                mail(subject="Bucket not public",context=str(string));
        # Check whether object versioning is enabled or not.
        def version():
            if bucket.versioning_enabled == False:
                string = "Object versioning is not enabled for Bucket"+ str(bucket_name) 
                teams(message= string,title="ALERT !!",color="E4D00A");
                mail(subject="Bucket version",context=str(string));
                

        
        location();
        retention();
        publicaccess();
        version();

    # Firewall Vulnerabilities
    elif resourcetype == 'gce_firewall_rule':
        firewalname = final['resource']['labels']['firewall_rule_id']
        owner = final['protoPayload']['authenticationInfo']['principalEmail']
        
        # Configure logs are enabled or not..
        def logs():
            if final['protoPayload']['request']['logConfig']['enable'] == False:
                try:
                    string = "Please enable Logconfig for firewall created with email-id "+ str(owner)
                    teams(message= string,title="INFO!!",color="64a837");
                    caller(message=str(string));
                except Exception as e:
                    myTeamsMessage.text(str(e))
                    myTeamsMessage.send()
                # string = "Please enable Logconfig for firewall created with email-id "+ str(owner) 
                # teams(message= string,title="INFO!!",color="64a837");
                

        """ Source Range in firewall is using vpn or open-to-internet..
        We can change source range to Deloitte VPN or any source-range required"""
        def sourcerange():
            source = final['protoPayload']['request']['sourceRanges']
            sourcerange = source[0]
            if sourcerange == '0.0.0.0/0':

                string = "Firewall created by email-id "+ str(owner) + " is open to internet." 
                teams(message= string,title="ALERT!!",color="E4D00A");
                time.sleep(30)
                caller(message=str(string));

        logs();
        sourcerange();

    # SQL Vulnerabilities
    elif resourcetype == 'cloudsql_database':
        resourcename = final['resource']['type']
        owner = final['protoPayload']['authenticationInfo']['principalEmail']
        
        # Configure availability type can be zonal or regional..
        def availabilityType():
            if final['protoPayload']['request']['body']['settings']['availabilityType'] == 'ZONAL':

                string = "Availability Type of "+ str(resourcename) + " is zonal. You can change it to regional for high availability.." 
                teams(message= string,title="INFO!!",color="64a837");
                try:
                    slack(message=str(string));
                except Exception as e:
                    myTeamsMessage.text(str(e))
                    myTeamsMessage.send()

        # Configuring backup is enabled or not..
        def logs():
            if final['protoPayload']['request']['body']['settings']['backupConfiguration']['enabled'] == True:
                string = str(resourcename) + " is enabled. "
                teams(message= string,title="WARNING!!",color="cd5c5c");
                try:
                    slack(message=str(string));
                except Exception as e:
                    myTeamsMessage.text(str(e))
                    myTeamsMessage.send()
                
            else:
                string = "Please enable logconfig for "+ str(resourcename) 
                teams(message= string,title="WARNING!!",color="cd5c5c");
                try:
                    slack(message=str(string));
                except Exception as e:
                    myTeamsMessage.text(str(e))
                    myTeamsMessage.send()

        availabilityType();
        logs();
        