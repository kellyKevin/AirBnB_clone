Partner 1 is here (KellyKevin) www.github.com/KellyKevin
Partner 2 is here (RichesUR7) www.github.com/RichesUR7



AirBnB Clone


This project is an implementation of a command-line interface (CLI) for an AirBnB clone. It provides functionalities for managing objects in a persistent storage system, including creation, updating, deletion, and querying of various types of objects such as User, Place, Review, and Amenity.

Command Interpreter


How to Start It
To start the command interpreter, follow these steps:

Clone the repository from GitHub:


bash
Copy code
git clone https://github.com/your_username/AirBnB_clone.git
Navigate to the project directory:
bash
Copy code
cd AirBnB_clone
Run the command interpreter:
bash
Copy code
./console.py

How to Use It


Once the command interpreter is running, you can use various commands to interact with the system. Some of the available commands include:

create: Create a new instance of a specified class.
show: Display information about a specific instance.
update: Update attributes of a specific instance.
destroy: Delete a specific instance.
all: Display information about all instances or all instances of a specific class.
count: Count the number of instances of a specified class.
quit or EOF: Exit the command interpreter.
For a complete list of available commands and their usage, refer to the documentation or use the help command within the interpreter.

Examples


Here are some examples of how to use the command interpreter:

Create a new User instance:

sql
Copy code
(hbnb) create User
Show information about a specific Place instance with ID 1234-5678:

scss
Copy code
(hbnb) show Place 1234-5678
Update the name attribute of a User instance with ID 9876-5432-1011:

sql
Copy code
(hbnb) update User 9876-5432-1011 name "John Doe"
Delete a Review instance with ID abcdefg-123456:

scss
Copy code
(hbnb) destroy Review abcdefg-123456
