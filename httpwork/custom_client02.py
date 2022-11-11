#!/usr/bin/env python3
import http.client
import argparse   # pull in arguments from CLI

def main():

    ## think of this as setting up the connection
    conn = http.client.HTTPConnection("localhost", 9021)

    if args.optionCon == 1:
     ## Send an HTTP request and store the HTTP response
     ##    from our webserver
     conn.request('HEAD', '/')

     ## Returns just the response that has been associated with
     ##    the **conn** object.
     res = conn.getresponse()
    
     ## response status and the reason to the screen.
     print(res.status, res.reason)

    elif args.optionCon == 2:
     ## this time we'll issue GET
     conn.request('GET', '/')
    
     ## res is equal to the response associated with conn
     res = conn.getresponse()
    
     ## print the response status code and reason
     print(res.status, res.reason)
    
     ## page_data is all of the data associated with res 
     page_data = res.read()

     ## this will point out all of the data associated with res
     print(page_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--optionCon', help='Provide 1 for HEAD or 2 for GET')
    args = parser.parse_args()
    main()

