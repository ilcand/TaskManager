# TaskManager

## How to Run the Application

1. Clone the repository
  - git clone https://github.com/ilcand/TaskManager.git
  - cd TaskManager

2. Setup required docker images configuration build 
  - docker-compose up -d --build 

3. Add dummy data into the database
  - docker-compose exec backend python seed.py

4.Install dependencies required for client including (frontend)
  - cd frontend
  - npm install
  - npm start

## Check presentation powerpoint for in depth information and a quick demo of the application

