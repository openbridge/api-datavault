

<h2>OVERVIEW</h2>

The API is a powerful data injest service using standard HTTPS POST/GET for fast and easy data colection. The Openbridge API acts as a trusted broker between a client and a third party service enpoint. Those service endpoints can be RESTful, SOAP or any other HTTP based connection. By routing requests through the broker the process of exposing data that may otherwise be resident in a downstream system that is diffuclt to access or completely unavailable. 

The basic process looks like this;

       +--------------+    +---------------+    +---------------+
       |              |    |               |    |               |
       |              |+-->|               |+-->|               |
       |              |    |               |    |               |
       |  client      |    |  broker       |    |  endpoint     |
       |              |<--+|               |<--+|               |
       |              |    |               |    |               |
       +--------------+    +---------------+    +---------------+
                                   +
                                   |
                           +------- -------+
                           |               |
                           |               |
                           |  storage      |
                           |               |
                           |               |
                           +---------------+

<ul>
<li><strong>Client:</strong></li>
<li><strong>Broker:</strong></li>
<li><strong>Storage:</strong> All requests from clients and responses from enpoints are captured and stored by the broker. The broker supports any HTTP client, in any programming language, that can perform a HTTPS POST/GET to interact with the broker API. Openbridge will setup a dedicated broker for your account and supply a private URL to be used by clients for making POST/GET calls to service endpoints.</li>
<li><strong>Service Enpoint:</strong></li>
</ul>



<h2>HOW IT WORKS</h2>
When you initiate a connection to Openbridge, there are some basic requirements that need to be met in order to successfully send data to a vault. The documentation outlined below assumes your are embedding the API URL into your client application. 

<h3>Base URL</h3>
All Broker API URLs referenced in this documentation have the following base
<pre>https://XXX</pre>

The Openbridge Broker API is served over HTTPS. Unencrypted HTTP is not allowed.

To make a call, send a HTTPS POST request to your account's Broker URL. It will look something like this

https://xxxxx/user/"product-id"/"account-sid"/"version"


<h2>RESPONSE CODES</h2>

The Openbridge Broker API will echo back to your client the response codes presented to us by the service endpoint. Those may be a combination of HTTP response codes as well as application specific codes resident in a response payload. Your application should take care to handle both situations. For example, is the Openbridge Broker API responds to your request with "Request Not Allowed: 403 Forbidden". This means the service enpoint has rejected the request, possibly due to an issue in how you are supplying your credentials. Please note, if the API Key was recently provisioned it may take between 5-10 minutes to have it propogate into our system. If you are still having an issue you can contact support for assistance.




<h2>Request Body</h2>

JSON

We do not require any complex data mapping or schemas. The request body sent to the vault reflects the structure of the underlying payload. The request body is often slow changing in terms of what is sent as a payload. However, in the event there are changes in a request body, such as a new attribute, it signals you have changed the underlying data structures. When we detect these changes we simply version the data in your vault. Think of a version as starting a new snapshot. These different snapshots allow you audit changes over time.

Position or order can change in the request as we look at the attributes in the rquest body to determine structure.

This provides a simple, yet effective mechnism to identify changes over time and provide the apporiate absraction between payloads.

AUTHENTICATION

API Key

Is a unique 32 bit key associated with URL that needs to be send as part of the payload.

"api_key" is a required field in JSON payload.

For example:

{"foo":"bar", "api_key":"Y20YVVNCESCVNL6S03H3HIPMT7NKTKV6"}

If API Key is not associated with URL, then the server will throw 403 error. For security purposes each key can authenticate the URL it was provisioned with. If you attempt to use a API Key associated with another URL the server will reject the request. Also, if the API key has been expired or invalidated the server will not allow further requests for that specific URL.

*********************************
ALOHA
*********************************

ALOHA BASE URL
	Pre Prod: https://memberlinkWS.alohaenterprise.com/insightws/MemberLinkWS?wsdl
	Prod:https://memberlink.alohaenterprise.com/insightws/MemberLinkWS?wsdl

ALOHA BASE REQUEST PAYLOADS
	name: companyID | data type:String – The five-character string that determines the Radiant customer
	name: userID | data type:String – The identifier used to authenticate the company for the Aloha
	name: password | data type:String – The password associated with the userID used to authenticate the company for the Aloha
	name: requestTime | data type:dateTime -The date/time stamp for the request.

ALOHA BASE RESPONSE PAYLOADS
	name: companyID | data type:String – Echoed back from the Request message.
	name: userID | data type:String – Echoed back from the Request message.
	name: executionStatus | data type:int – (see ExecutionStatus Types table below)
	name: executionStatusDescription | data type:String (see ExecutionStatus Descriptions table below) 
	name: requestTime | data type:dateTime - The date/time stamp for the request."
	
ALOHA METHODS	
	
Use Case = UC3 - Register for Starpass
Method = addMemberProfile()
			
			AddMemberProfileRequest	
			-----------------------
				name: memberAccountID | data type:int
				name: cardNumber | data type:String
				name: firstName | data type:String
				name: lastName | data type:String
				name: company | data type:String
				name: dateOfBirth | data type:VanityDate
				name: anniversaryDate | data type:VanityDate
				name: driversLicense | data type:String
				name: address1 | data type:String
				name: address2 | data type:String
				name: city | data type:String
				name: stateProvince | data type:String
				name: country | data type:String
				name: postalCode | data type:String
				name: emailAddress | data type:String
				name: phoneNumber | data type:String
				name: otherPhoneNumber | data type:String
				name: companyDefined1-30 | data type:String (30 available)
				name: profileExists | data type:boolean (1 exists, 0 does not exisit (?))

				VanityDate: The attributes of VanityDate include the following
					name: date | data type:tring
					name: locale | data type:String
						Locale is a 5 character string in the form xx_YY where xx is the language code as defined in ISO-639 and YY is country as defined in ISO-3166. Examples:
							en_GB for English - United Kingdom 
							de_DE for German - Germany 
							es_MX for Español - Mexico
							en_US for English - United States 
							tr_TR for Türkçe - Türkiye
							pt_BR for Português – Brasil

	
			AddMemberProfileResult
			-----------------------
				name: cardNumber | data type:String – Echoed back from AddMemberProfileRequest().
	

Use Case = UC10 - Viewing the Profile Page 
Method = getMemberProfile()

			GetMemberProfileRequest
			-----------------------
				cardNumber:String – The 14-digit member card input to get the member

			GetMemberProfileResult
			-----------------------
				cardNumber:String – Echoed back from GetMemberProfileRequest.
				profile:MemberProfile – See MemberProfile under the addMemberProfile() method

	
Use Case = UC10 - Update existing member profile
Method = updateMemberProfile()

			UpdateMemberProfileRequest
			-----------------------
				profile:MemberProfile – See MemberProfile under the addMemberProfile() method

			UpdateMemberProfileResult
			-----------------------
				cardNumber:String – Echoed back from UpdateMemberProfileRequest()
	

Use Case = UC11 - Viewing Rewards History	
Method = getBonusPlanHistory()

			GetBonusPlanHistoryRequest
			-----------------------
				X

			GetBonusPlanHistoryResult
			-----------------------
				X
	
######################	
EXECUTION STATUS CODES
######################

ExecutionStatus / ExecutionStatusDescription
0	Successful execution
1	Member not found
2	Account not active
3	Database error
	
ExecutionStatus	ExecutionStatusDescription
4	Internal error %message%
5	Invalid passcode
6	Data error. %message%
7	Invalid card number
8	Insufficient Access Privileges
9	Account locked, too many login failures
10	Invalid Login Credential
11	Adjustment amount invalid
12	Adjustment amount exceeded
	
ExecutionStatus	ExecutionStatusDescription
14	Bonus plan not found - failed to find Bonus Plan entry for this Bonus Plan ID"
15	Claim ID not found
16	Claim ID expired
17	Claim ID has already been processed
18	Child Card Number already associated to the requested Parent Card Number.
19	Child Card Number already associated to another Parent Card Number.
20	Requested Child Card Number is already a Parent Card Number.
21	Requested Parent Card Number is already a Child Card Number.
22	The child card number is not found
23	The parent card number is not found
24	Processing
25	Invalid Batch ID
26	Card Range in Use
27	Partial List
28	Create Card Failed
29	Invalid Sequence Type – cannot mix usage of sequential and random type in a series
30	Invalid Series
31	Card number not found
32	Company not found
	
ExecutionStatus	ExecutionStatusDescription
33	Card number already in use
34	Card series (first 5 numbers) do not match.
35	Card series would extend beyond maximum allowable number
36	Check not found
37	Amount exceeds the transaction limit allowed
38	Amount exceeds the max balance limit allowed
39	Activation reason not found
40	Requested amount would cause a negative balance
41	Open assignment already exists for this member
42	Series only allows a single POS activation
43	Amount cannot be negative or zero
44	Series is inactive
	
