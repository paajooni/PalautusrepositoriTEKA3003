*** Settings ***
Resource  resource.robot
# Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User
    Validate User  jounas  jounas456
    # No assertion needed: test passes if no error is raised

Register With Already Taken Username And Valid Password
    Input New Command
    Create User  jounas  jounas456
    Run Keyword And Expect Error  User with username jounas already exists  Create User  jounas  joopajaapa456

Register With Too Short Username And Valid Password
    Input New Command
    Run Keyword And Expect Error  AuthenticationError: Username must be at least 3 characters long  Create User  jo  jounas456

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Run Keyword And Expect Error  AuthenticationError: Username must contain only lowercase letters  Create User  jou3nas  jounas456

Register With Valid Username And Too Short Password
    Input New Command
    Run Keyword And Expect Error  AuthenticationError: Password must be at least 8 characters long  Create User  jounas  jou456

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Run Keyword And Expect Error  AuthenticationError: Password must contain at least one non-letter character  Create User  jounas  jounaspassword

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  jounas  jounas456  
