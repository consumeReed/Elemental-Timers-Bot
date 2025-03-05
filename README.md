# Elemental-Timers-Bot
## About The Project

The Elemental Timers Bot is a Discord Bot that keeps track of boss times and respawns from Celtic Heroes. 


### Built With and Using

* Python
* Discord Python
* MongoDB


### Getting Started and Requirements
Dependencies and Requirements
* Requires Python 3.8 or higher
* Requires a MongoDB connection
* Requires a unique Discord Bot Authentication Token

Creating database, downloading assets, and starting bot
* Run database creation scripts with a valid MongoDB database connection
* Change the .env file to a valid Discord Bot Authentication Token
* Start bot

### Usage
The Elemental Timers Bot commands all use ! before each command. Use help while running for list of all commands.

General usage
* find - Query the given list of bosses to see their respawn timers
* aliases - List of each boss and their usable alternative names
* down - Set a boss to be down at current time OR past time
* update - Set a boss's respawn and window period
* log - Retrieve a log of recently modified bosses


