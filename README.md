api-datavault
=============

Simple, schema-less and powerful data injest API using standard HTTPS POST and JSON payload for faster and easier data colection. http://www.openbridge.com

<h2>REST Web Service Interface</h2>

This REST API allows you to POST data into your account. The API is based on REST principles, which means we leverage standard HTTP concepts to simplify applications that need to consume it. You can use almost any HTTP client in any programming language that can perform a HTTPS POST to interact with the API. 

Don't do anything prohibited by the Rules and talk to us if you think we should make a change or give you an exception.

<h2>How It Works</h2>

You setup your account and have provisioned a private URL. This private URL allows you to connect to Openbridge to POST data. Since the API uses standards based HTTP mechanisms you can use almost any client to connect, including embedding your URL into third party tools like Twitter Lead Cards.

When you initiate a connection to Openbridge, there are some basic requirements that need to be met in order to successfully send data to a vault. The documentation outlined below assumes your are embedding the URL into your application.  We have added some sample code libraries that will help get your started.

<b>NOTE:</b> If your application will eventually need more than 10 million daily API calls, you will need to talk to us directly about your access to the Openbridge API as you may be subject to additional terms and costs. 

<h2>Base URL</h2>

<h4>Base</h4>
All Datavault URLs referenced in this documentation have the following base
```sh
https://api.openbridge.io/user
```
<h2>HTTP POST</h2>
The REST API is served over HTTPS via PORT 80. <b>Unencrypted HTTP is not allowed</b>.

To make a call, send a HTTPS POST request to your account's Datavault URL. It will look something like this

```sh
https://api.openbridge.io/user/"product-id"/"account-sid"/"version"
```
<h3>Response Codes</h3>
Standard HTTP 1.1 status codes denote the status of your request. The following are a few of the key response codes for a request

<h4>Successful Request: 202 Accepted</h4>
The request and data payload has been accepted by our system. However, there is additional processing that has not been completed downstream. For example, you may have setup various "in-flight" data transformation activities to occur on all request payloads for a given Datavault. 


<h4>Request Not Allowed: 403 Forbidden</h4>
We got the request, but will not fulfill it. The request SHOULD NOT be repeated unless there was an issue in how you are supplying your API Key. Please note, if the API Key was recently provisioned it may take between 5-10 minutes to have it propogate into our system. If you are still having an issue you can contact support for assistance.

<h4>System Availability: 503 Service Unavailable</h4>
Our systems is unable to handle your request. This is likely temporary and you should make sure you rety the request

More on HTTP 1.1 status codes can be found here: http://www.w3.org/Protocols/rfc2616/rfc2616.html

<h2>Request Body</h2>

<h3>JSON</h3>

<h3>No Schema</h3>
We do not require any complex data mapping or schemas. The request body sent to the vault reflects the structure of the underlying payload. The request body is often slow changing in terms of what is sent as a payload. However, in the event there are changes in a request body, such as a new attribute, it signals you have changed the underlying data structures. When we detect these changes we simply version the data in your vault. Think of a version as starting a new snapshot. These different snapshots allow you audit changes over time.

Position or order can change in the request as we look at the attributes in the rquest body to determine structure.

This provides a simple, yet effective mechnism to identify changes over time and provide the apporiate absraction between payloads.

<h2>Authentication</h2>

<h3>API Key</h3>

<h3>Keep it safe, keep it hidden</h3>

Please keep your API Key and your URL secure. Treat them like you would your username and password. 

<h2>Error Handling</h2>






