# Understanding Routing
A brief exercise completed for Coding Dojo
### Objectives:
Create a server file that generates the specified responses for the following url requests:
* localhost:5000/ - have it say "Hello World!"
* localhost:5000/dojo - have it say "Dojo!"
* Create one url pattern and function that can handle the following examples:
    - localhost:5000/say/flask - have it say "Hi Flask!"
    - localhost:5000/say/michael - have it say "Hi Michael!"
    - localhost:5000/say/john - have it say "Hi John!"
* Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
    - localhost:5000/repeat/35/hello - have it say "hello" 35 times
    - localhost:5000/repeat/80/bye - have it say "bye" 80 times
    - localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

### Additional functionality for extra practice:
* For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
* Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."
