*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  olli  olli666polli
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  joraa100
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ol  olli666polli
    Output Should Contain  Username was too short. Password ok!

Register With Valid Username And Too Short Password
    Input Credentials  mikko  m4lli
    Output Should Contain  Username ok! Password too short.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  simo  frangeen
    Output Should Contain  Password must contain numbers!

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
    
