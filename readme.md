#IS601002 -Web Systems Development 
#User Management System

         Project Link - https://github.com/Tushar140498/user_management

Course Learnings & Project Insights:
Throughout this project, I gained valuable experience in real-world software development, particularly in user management systems. I learned how to effectively collaborate in a team environment, contributing to feature implementation, bug fixing, and ensuring code quality. By implementing a new feature, I followed industry best practices for coding, testing, and documentation. I also enhanced the system's test coverage, identifying gaps and writing additional tests to handle edge cases and error scenarios.
This project provided hands-on experience with tools and practices commonly used in the software industry, such as version control with Git, Docker for deployment, and continuous integration for automated testing. I also developed problem-solving skills by debugging and addressing issues, ensuring the system remained functional and reliable. Overall, this project has equipped me with practical skills and a deeper understanding of the development process, preparing me for future professional challenges.

Project Accomplishments:
Profile Picture Upload with MinIO: Integrated MinIO for object storage, allowing users to upload and manage profile pictures securely.
JWT-based Authentication & Role Management: Implemented role-based access control with JWT tokens to protect routes and ensure proper user authorization.
User CRUD Operations: Fully functional Create, Read, Update, and Delete operations for managing user profiles and related data.
Pagination and HATEOAS Links: Incorporated pagination and HATEOAS (Hypermedia As The Engine of Application State) links to facilitate scalable and flexible API responses.


Closed Issues (Bug Fixes):
I resolved several critical bugs during the project. These fixes directly contributed to the stability and security of the application. Below are the close issues:

 Email Verification :
 The email verification process was not being executed properly due to the issue of connecting it properly with Mailtrap.By resolving the issue the email verification link was sent to the registered user's email address and only after verification the user was checked as verified.
Link - https://github.com/Tushar140498/user_management/Issue1


Admin Verification handling 
The admin was getting verified automatically without being verified via mailtrap. The first user will be admin but the verification for the admin has been implemented. 
Link - https://github.com/Tushar140498/user_management/Issue2


 Password Logic implementation
The user should enter at least one digit, one special character, one uppercase alphabet, one lowercase alphabet and at least 10 characters
 Link - https://github.com/Tushar140498/user_management/Issue3


Skip and limit values validation  
The issue was while getting the list of the user, when we enter the negative value for skip and limit then instead of error it returns 200(Ok).
Link - https://github.com/Tushar140498/user_management/Issue4


Showing is_professional false 
The issue is fixed. Now when we mark the is_professional as true then while getting the user we will get true instead of false.
Link - https://github.com/Tushar140498/user_management/Issue5



New Feature – User Profile Management :
This feature allows users to manage their profile information. It enables managers and admins to upgrade users to professional status.

Link to new feature : https://github.com/Tushar140498/user_management/new_feature


Docker Hub Repo:
The project has been successfully containerized using Docker. The image is available on DockerHub, and can be found here:
https://hub.docker.com/r/tushar140498/user_management/tags



Reflection:
This project was both challenging and rewarding. It provided me with the opportunity to apply everything I have learned throughout the course to build a production-grade backend system. From handling user data securely to implementing a robust testing suite and setting up automated deployment, the project encompassed many aspects of modern backend development.

The integration of MinIO for profile picture uploads was a valuable learning experience. It demonstrated how object storage can be efficiently utilized in modern applications, especially when dealing with large media files. Additionally, working with JWT tokens and ensuring secure password validation helped me better understand authentication mechanisms and best practices for user security.

Furthermore, this project reinforced the importance of testing. Writing unit tests, handling edge cases, and ensuring high test coverage were essential in building a reliable system. The CI/CD pipeline using GitHub Actions was also an eye-opener, as it allowed me to automate testing, building, and deployment processes, ensuring that my code was always ready for production.

Overall, the project helped me improve my problem-solving skills and learn how to implement real-world features that are secure, scalable, and maintainable. I am confident that the skills I have gained through this course and this project will serve me well in my future software engineering endeavors.







