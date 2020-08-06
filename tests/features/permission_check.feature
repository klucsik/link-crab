Feature: Permission checks on links for given users

    As a tester, I would like to define user permission sets for links
    so I can check if there is a misconfigured permission set

    Rule: If permission set csv and login credentials are provided, the Crab should check the accessibility for provided links for given user

        Example: Parsing a csv
            Given I have the following csv as 'tc1.csv'
                """
            link,                   accessible
            example.com,            true
            example.com/logged-in,  true
            example.com/admin,      false
                """
            And I provide the config file as '.link-crab.yml'
                """
            login:
            url: example.com/login
            email: user@xmpl.tst
            password: Passw0rd
            permission-set: tc1.csv
                """
            When I run the Crab
            Then the Crab should log in to the webpage
            And expect access granted to 'example.com'
            And except access granted to 'example.com/logged-in'
            And except access denied to 'example.com/admin'

        Example: Except access granted to link
            Given the Crab need to check 'example.com' link
            When the Crab makes a GET requests to the link
            Then the response's status code is 200
            And the response's url should be 'example.com'

        Example: Except access denied to link
            Given the Crab need to check 'example.com/logged-in' link
            And  is not logged in
            When the Crab makes a GET requests to the link
            Then the response's status code is not 200 or the response's url is not 'example.com/logged-in'