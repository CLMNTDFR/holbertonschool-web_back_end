# **Basic authentication** :computer:

## **Description:** :speech_balloon:

* Basic authentication is a straightforward authentication scheme integrated into the HTTP protocol, allowing an HTTP user agent, like a web browser, to provide a username and password with a request. In this method, the username and password are joined with a colon, base64-encoded, and sent in the Authorization header of the HTTP request. However, since base64 encoding is easily reversible, Basic Authentication is considered insecure over unencrypted connections, making it essential to use it over HTTPS to protect credentials from interception. Although simple and widely supported, Basic Authentication's lack of features such as token expiration and revocation makes it less suitable for complex or security-sensitive applications, with more robust methods like OAuth or JWT (JSON Web Tokens) being recommended for these cases.

## **What we should learn from this project:** :bookmark_tabs:


* What authentication means
* What Base64 is
* How to encode a string in Base64
* What Basic authentication means
* How to send the Authorization header

## **Tasks** :books:

#### **0. Simple-basic-API**

#### **1. Error handler: Unauthorized**

#### **2. Error handler: Forbidden**

#### **3. Auth class**

#### **4. Define which routes don't need authentication**

#### **5. Request validation!**

#### **6. Basic auth**

#### **7. Basic - Base64 part**

#### **8. Basic - Base64 decode**

#### **9. Basic - User credentials**

#### **10. Basic - User object**

#### **11. Basic - Overload current_user - and BOOM!**


## **Author**

* **Clément DEFER**


## License :page_with_curl:
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
