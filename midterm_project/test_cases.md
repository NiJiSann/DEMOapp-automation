# List of test cases:
- ### API calls Section 
    - #### Test 1
            Name: Get Europe specific devices(EU-DC)  
            Description: In API calls section get commonly used devices in Europe
            Objective: Validate that API call is responding with list of devices
            Test data: No-data

    - #### Test 2
            Name: Get United States specific devices(US-DC)  
            Description: In API calls section get commonly used devices in United States
            Objective: Validate that API call is responding with list of devices
            Test data: No-data

    - #### Test 3
            Name: Handle Unauthorized API call  
            Description: In API calls section send Unauthorized API request (401)
            Objective: Validate that Unauthorized API call is handled and not responding with "Unauthorized"
            Test data: No-data
  
    - #### Test 4
            Name: Handle Getting non existing item with API call  
            Description: In API calls section send API request for not existing item (404)
            Objective: Validate that API request for existing item is handled and not responding with "Not Found"
            Test data: No-data


- ### Login Section 
    - #### Test 1
            Name: Log in with wrong credentials
            Description: Test logging into app with wrong username and password
            Objective: Log in must be aborted with "Provided credentials do not match any user in this service" text
            Test data: [username - qwerty@sync.xyz, password - 12345]

    - #### Test 2
            Name: Log in 
            Description: Test logging into app 
            Objective: Log in must redirect to address adding screen
            Test data: [username - bob@example.com, password - 10203040]

    - #### Test 3
            Name: Log in with locked account
            Description: Test logging into app with banned account 
            Objective: Log in must be aborted with "Sorry, this user has been locked out" text
            Test data: [username - alice@example.com, password - 10203040]

    - #### Test 4
            Name: Log out
            Description: Test logging out in app
            Objective: Log out must be alerted with "You are successfully logged out" text
            Test data: No-data

    - #### Test 5
            Name: Log in with fingerprint
            Description:Turn on Finger print in app.
                        Test logging out in app using finger print.
                        *Fingerprint(Finger 1) must be configured beforehand* 
            Objective: Log in must redirect to address adding screen
            Test data: No-data

- ### End 2 End scenario Section 
    - #### Test 1
            Name: Add item to cart
            Description: Add any item from catalog to cart. 
                         Choose color from item color spectrum and random amount 
            Objective: Items in cart must match to selected items(colors and amount)
            Test data: 

    - #### Test 2
            Name: Fill Checkout Address without data 
            Description: From Cart Proceed To Checkout. 
                         Left every field in Checkout page empty and press "To Payment"
            Objective: Under every text field labaled with '*' should apper 'Please provide..." text
            Test data: 

    - #### Test 3
            Name: Fill Checkout Address with random text
            Description: From Cart Proceed To Checkout. 
                         Left every field in Checkout page empty and press "To Payment"
            Objective: Page must redirect to Payement page
            Test data: 

    - #### Test 4
            Name: Fill Payment without data 
            Description: Left every field in Checkout page empty and press "Reveiw"
            Objective: Under every text field labaled with '*' should apper 'Value looks invalid." text
            Test data: 

    - #### Test 5
            Name: Fill Expiration Date with wrong values  
            Description: Insert invalid values to Expiration Date field
            Objective: Under Expiration Date field should apper 'Value looks invalid." text
            Test data: value_1 - qwert, value_2 - 1111, value_1 - 9999

    - #### Test 6
            Name: Fill Security Code with wrong values  
            Description: Insert invalid values to Security Code field
            Objective: Under Security Code field should apper 'Value looks invalid." text
            Test data: value_1 - qwert, value_2 - 1111, value_1 - 9999

    - #### Test 7
            Name: Fill Expiration Date 
            Description: Expiration Date field must contain only month from 1-12 and years from current year and until 2043
            Objective:  Under Expiration Date field should not apper 'Value looks invalid." text
            Test data: value_1 - 1124, value_2 - 0233, value_1 - 0643

    - #### Test 8
            Name: Fill Security Code 
            Description: Security Code field must contain only 3 numbers 
            Objective:  Under Expiration Date field should not apper 'Value looks invalid." text
            Test data: value_1 - 111, value_2 - 222, value_1 - 333

    - #### Test 9
            Name: Fill Name and Card 
            Description: Fill Name, Card fields and click 'Review Order' 
            Objective: 
            Test data: name - qwerty, card - 5555555555554444
    
    - #### Test 10
            Name: Check Delivery Address and Payment Method
            Description: Check Delivery Address and Payment Method and press 'Place Order'
            Objective: Delivery Address and Payment Method in order review page must be same as intended
            Test data:

    - #### Test 11
            Name: Check Order Completion 
            Description: After Placing order check if Checkout Completed
            Objective: Check if 'Checkout Completed' text present in page after Placing order
            Test data:

- ### Webview Section 
    - #### Test 1
           Name: Go to Google
           Description: In Webview page insert google's url and go to site
           Objective: Google page must open in app webview 
           Test data:

- ### Geo Location Section 
    - #### Test 1
            Name: Check Geo Location
            Description: Set couple locations to driver and check it in Geo Location Page  
            Objective: Values in app must be same as you set to driver
            Test data: [loc_1 -  20, 20], [loc_2 -  30, 50], [loc_3 -  60, 60]

- ### Drawing Section 
    - #### Test 1
            Name: Draw
            Description: In Drawing page draw a line
            Objective: In drawing view must appear red line
            Test data:

    - #### Test 2
            Name: Clear Draw
            Description: Clear drawing and check if all clear 
            Objective: Any drawing in drawing view must be cleared
            Test data:

- ### Reset App State Section 
    - #### Test 1
            Name: Reset app 
            Description: Add items to cart and then reset app
            Objective: Cart must be empty after reset
            Test data:

