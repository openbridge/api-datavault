## Usage
Send POST  request to a given URL

####What it does:

  1. checks if payload satisfies serialization format
  2. checks if url is in right format
  3. sends a payload to the url
  4. gets and returns response from the server

####Install:

    git clone https://github.com/openbridge/api-datavault
    cd api-datavault/openbridge
    python setup.py install

####Examples:
    
    from openbridge.post import poster
    response = poster.send_json_post_request({'fooo':'bar', 'api_key':'Y20YVVMCESCVNL6S03H3HIPMT7NKTKV6'}, 'https://api.openbridge.io/user/foo/bar/1')
    print response.status_code     # 202
    print response.ok              # ok
    print response.url             # u'https://api.openbridge.io/user/foo/bar/1' 
