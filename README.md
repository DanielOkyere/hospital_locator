# HOSPITAL LOCATOR
## Motivation & Background

The hospital locator project is a final project for the ALX 2022/23 Program Cohort 6 members.

The inspiration for the project stems from our need to provide users with a convenient way
to locate specialist hospitals around them using the mapping system.

The project is focused on Ghana and is looking to be expanded to global community.

### Description of the Project:
The Hospital Locator is a web-based application that uses geolocation technology to provide users with the nearest hospital based on their current location. This project aims to provide users with a quick and easy way to locate the nearest hospital in case of emergencies.

The Hospital Locator is built using modern web development technologies, such as HTML, CSS, JavaScript, and APIs. The application uses the user's geolocation data to determine their current location and then use that data to search for hospitals within a certain radius.

The application will display the nearest hospital along with its address, phone number, and distance from the user's current location. Additionally, the application will provide directions to the hospital using Google Maps, making it easy for users to navigate to the hospital.

The Hospital Locator will be designed to be user-friendly and accessible to all users, regardless of their technical proficiency. The application will be optimized for use on desktop and mobile devices, allowing users to access the service from anywhere.

The main features of the Hospital Locator will include:

Geolocation-based hospital search
Display of nearest hospital with address, phone number, and distance from user
Directions to the hospital using Google Maps
User-friendly interface for easy navigation
Optimized for desktop and mobile devices
The Hospital Locator will be a valuable resource for people in need of emergency medical care, as well as for individuals who are traveling or in unfamiliar locations. The project aims to help save lives by providing quick and easy access to medical facilities when they are needed most.

## How to Run Application
- Setup Postgres With POSTGIS extension
- Create env file like 
```
DATABASE_URL=
SECRET_KEYS=
ALGORITHM=
EXPIRY_MINUTES=
MAPS_API_KEY=
```
- Run application by execting file ```start.sh```
## Team
- [Daniel Okyere]
- [Gabriel Ahiamata]
- [Tobex Iloabuchi]

## Requirements
- Python 3.7+
- FastAPI 
- PostGIS
- Google MAP API
- Unittest

