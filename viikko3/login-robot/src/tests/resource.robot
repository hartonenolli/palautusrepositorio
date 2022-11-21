*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input New Command
    Input  new

#Input New Command And Create User
#    [Arguments]  ${username}  ${password}
#    Input  ${username}
#    Input  ${password}
#    Run Application