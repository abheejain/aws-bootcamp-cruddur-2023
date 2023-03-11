# Week 3 — Decentralized Authentication

## Provision via ClickOps a Amazon Cognito User Pool
- This task was done manually to create a Cognito Pool in various steps. 

Proof of the AWS Cognito Pool Creation 
## Verificaton Image

![Cognito Pool Creation](assets/week-3/Week3-Cognito-create-user-pool.png)

Proof of the AWS Cognito Pool Details 
## Verificaton Image

![Cognito Pool Creation](assets/week-3/Week3-Cognito-user-pool-details-after-error.png)

<hr>

- Next was to Install and configure Amplify client-side library for Amazon Congito, tested with an error message

## Verificaton Image

![Setup Client-side lib](assets/week-3/Week3-Cognito-sign-in-page-test-error-debug.png)

<hr>

### Implement API calls to Amazon Coginto for custom login, signup, recovery and forgot password page

## Implement Custom Signin Page
- Started with Sign in Page

## Verificaton Image

![Signin Page](assets/week-3/Week3-Cognito-sign-in-page-test-error.png)

<hr>

- New User added to the User Pool
## Verificaton Image

![New User Added](assets/week-3/Week3-Cognito-added-new-user.png)

- Email Received at the User Email 
## Verificaton Image

![Email Received](assets/week-3/Week3-Cognito-user-received-email.png)


- User Confirmed using CLI

The user status was showing `Confirmation status` as `Force change password` which is not ble to login until it changes to `Confirmed` 
Ref: https://stackoverflow.com/questions/40287012/how-to-change-user-status-force-change-password 


## Verificaton Image

![Force change password](assets/week-3/week3-Cognito-user-confimed-using-cli.png)


- User was able to login after Status shown as `Confirmed`

## Verificaton Image

![Login After Confirmed](assets/week-3/week3-Cognito-after-status-confirmed-CLI.png)


- User Handle is still not updated, because we have not mentioned or selected to set the `attributes` while creating the User Pool, so I changed it manually in the `Edit User` on the Cognito Pool Console  

## Verificaton Image Before

![Handle Before ](assets/week-3/week3-Cognito-changed-handle.png)

- Added the `Prefered Username` attribute to the user

## Verificaton Image Before

![Handle Added ](assets/week-3/week3-Cognito-set-prefered-username-added.png)


## Verificaton Image After

![Handle After ](assets/week-3/week3-Cognito-set-prefered-username-after.png)

<hr>

NOTE: The verification is done for the `Signin Page`, and it is not good practice to add users manually, we will delete the Users from Cognito Pool and go ahead to proceed setting up for `Signup Page`

## Verificaton Image
![User Deleted ](assets/week-3/Week3-Cognito-user-deleted.png)

<hr>

## Implement Custom Signup Page

- Updated Signup page with Amplify

## Verificaton Image
![User Deleted ](assets/week-3/week3-Cognito-signup-page-success.png)


- Received Verifictoin email in the email

## Verificaton Image
![Email Received](assets/week-3/week3-Cognito-Your-verification-code-email1.png)


- Confirmed and went to next page after verification Code

## Verificaton Image
![Confirmed](assets/week-3/week3-Cognito-Your-verification-code-coonfirm.png)

- Cognito Pool Showing the User added to the pool

## Verificaton Image
![User added confirmed ](assets/week-3/week3-Cognito-signup-confirmed-User-added.png)

<hr>

## Implement Custom Confirmation Page

- Using `Forgot Password`

## Verificaton Image
![Forgot Password](assets/week-3/week3-Cognito-user-forgot-password.png)

- Received another code for Recover Account

## Verificaton Image
![Recover Password Code](assets/week-3/week3-Cognito-Recover-account-received-code.png)


<hr>

## Implement Custom Recovery Page

- Recover Account setup using Amplify

## Verificaton Image
![Recover Password Confirmed](assets/week-3/week3-Cognito-Recover-account-confirmed.png)


- Confirmed on the Recover Password worked with Username and Preferred Username 

## Verificaton Image
![Recover Password Verified](assets/week-3/week3-Cognito-Recover-account-confirmed-verify.png)

<hr>

## Watch about different approaches to verifying JWTs

- how-to-get-http-headers-in-flask
Ref: https://stackoverflow.com/questions/29386995/how-to-get-http-headers-in-flask


<hr>
