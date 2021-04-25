# FSND-Capstone-Sprint-Attendence-Planning

## Capstone Project: Provides a management tool for Sprint Attendence in SCRUM teams

The tool shall provide SCRUM Development teams an easy option to calculate the basic Scrum values needed to plan a subsequent Sprint.

All Developers are allowed to access the tool to display the content of the Developers table which contains the names of the team members and a value which is indicating with how many percent the team members contribute to the SCRUM project.

In a second table the Sprints are defined. Each spritnt has a unique Name, the planned Story points, the story points which were completed (to be filled out after the sprint). The velocity factor which will show you the ratio between available FTE per Sprint and completed Story points. A sprint has a start and ending date and a predicition value how many story points the team can finish in the subsequent sprint.

### Attention: 
The application is work in progress. Currently the calculations and the table 'Vacation' is not yet implemented. I hope the current state is still matching with the project requirements.

In the Vacation Table every Developer can enter vacation dates to make the prediction more precisely. The vacation dates will be calculated with the proj_participation of the respective Developer and will end in the sprint_fte_sum where the man/woman power per sprint is stored.

The front end is not yet developed, but will follow soon...

## Roles

There are two different Roles defined to interact with the API:

- Developer: developers have the permission to 
    - get:developers
    - get:sprints
    - post:developers (which includes also patch developers)

- Scrum Master: has all rights including the Developer rights
    - get:developers
    - get:sprints
    - delete:sprints (not yet implemented)
    - delete:developers
    - post:developers
    - post:sprints

## Testing

Testing can be performed either with the app_unittest.py file localy on a "velocity_test" database. Or with the exported Postman collection online on the Heroku application.

## Authentification

- Auth0 Domain Name: fsnd-groscht.eu.auth0.com
- Auth0 Client ID: H0ZTM8O9Xg6fdTu1Wu9Opf29UzlL2Bfl
- JWT for Developer: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1wSjduRi0xQXZsT3JSbjctT2FRNCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3Jvc2NodC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2YzUwMjJjY2YwNDMwMDY5MjRlNzkwIiwiYXVkIjoic3ByaW50X3ZlbCIsImlhdCI6MTYxOTI0ODQ5NCwiZXhwIjoxNjE5MzM0ODk0LCJhenAiOiJIMFpUTThPOVhnNmZkVHUxV3U5T3BmMjlVemxMMkJmbCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRldmVsb3BlcnMiLCJnZXQ6c3ByaW50cyIsInBvc3Q6ZGV2ZWxvcGVycyJdfQ.VavaiLBHJQBkP4xWhJfakkTKEgi8on4F2KMwYvrN17Nw5yCOG0b3odIu_npsWDwx-y_Vy4pQSkTHKQj5P21EBswvgDSnfg7kgrGqQ67hsWwfGk1rFaRJPYy_t3RUhje5rBiNULoUJgUihEh1t6NitrlDUIZFO0yzL7XXjZ5QIZXol6-zfHib3_nkj80cqk2Z3iZbMmGDXEw6XkjDPvp3Yqaf0fRdwAYTpFpg1xBrH79tC5lrkp_gt0wa7VnOGhImXdy3M00JLb_jJnh0Q9CYVASFqcAHgaVDiUS1PsTt86jtOliXWt1CaK5EKlpg7q8e8Br7DFjRsM4ALqJV2IRgNA
- JWT for Scrum Master: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1wSjduRi0xQXZsT3JSbjctT2FRNCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3Jvc2NodC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2NmM1MDkxODNhMmUwMDY5NGU2ZTBjIiwiYXVkIjoic3ByaW50X3ZlbCIsImlhdCI6MTYxOTI0ODU5MSwiZXhwIjoxNjE5MzM0OTkxLCJhenAiOiJIMFpUTThPOVhnNmZkVHUxV3U5T3BmMjlVemxMMkJmbCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRldmVsb3BlcnMiLCJkZWxldGU6c3ByaW50cyIsImdldDpkZXZlbG9wZXJzIiwiZ2V0OnNwcmludHMiLCJwb3N0OmRldmVsb3BlcnMiLCJwb3N0OnNwcmludHMiXX0.BDCJtw729z9lUggunoa3iESr_FH3ssIldSHY90sLrqOqdV3AkORtiqM42JEaD2eUhPm29AyF4fFZsycD8KSyLoDYQwsrKazn6yl5n8ux76_S8RG2Ws__tMB8bTd3b1yxTFOzETRduMJZKZdhalMkDyfu2vNdEirmx8jzHvbouw2e6JTZZf6d0YqHzOVZs9BadlztlTkiqZt4yXmAz6rDN-DpI5GDX-9tzienjXGRNHfpN9rX2SJ60kAbdwEnBtAHjwFLneO2fg_mKuiJxfCQhzbAi7IEXA89N93KE-ZoE3pg5TZrEqGmjdfy-upMCZBx-dEc1-INWzz-aND2eGWrxA

## Application URL

https://fsnd-sprint-velocity-planning.herokuapp.com/

## Environment Variables

To run the app a 'SECRET_KEY' Env Variable has to be defined.

# API Documentation

Can be found here: https://documenter.getpostman.com/view/15193396/TzJyaaPE