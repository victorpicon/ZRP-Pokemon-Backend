# PokeApi
ZRP PokeAPI is an application that uses Python and Flask to help trainers locate their Pokémon's abilities. In the app, you'll find the 151 initial Pokémon of Kanto sorted by their Pokédex numbers and, when you select the desired Pokémon, you'll see a list of its abilities in alphabetical order. 
The application was made for the technical challenge of ZRP Applications, a brazilian software and digital products consulting company founded in 2015 and committed to technological innovation to solve its clients’ real challenges.

## ✨ Features
    • Show all Pokémon's abilities in alphabetical order
    • Save requested data to the database to avoid PokeAPI's downtimes

## 🎉 Bonus
    • Code formatting using Black
    • API's Documentation on Swagger (/docs endpoint)
    • Unit tests with Pytest
    • Project Environment using Docker
    • Pokémon Caching on Database for faster resend data.

## 💪 Improvement Points
    • Deploy with an Serverless Solution
    • Implement Logs
    • Implement new features as: Fetching all Pokémons and all Abilities

## 📦 Resources
    • API’s Documentation at /docs

## 🚀 Technologies
This project was developed with the following technologies:

    • Python
    • Flask
    • Docker
    • Docker Compose
    • SQLAlchemy
    • Flask Smorest
    • SQLite

## 🔧 Requirements
To run this application, you only need to have docker on your computer.
You can verify its installation by running the command docker compose version or docker-compose --version in your terminal.

## 🏃 How to Run
    1. Make a clone;
    2. Open the project on your terminal;
    3. Run docker compose up to run the server;
        • By default the server will run at localhost:5000.
  
  Alternatively you can run the project by having an python virtual env and using `pip i -r requirements.txt` and then `flask run`

## 🤔 How to contribute
    • Make a fork;
    • Create a branch with your feature: git checkout -b my-feature;
    • Do commit with your changes: git commit -m 'feat: My new feature';
    • Do a push for your branch: git push origin my-feature.
After the merge of your pull request was made, you can delete your branch.