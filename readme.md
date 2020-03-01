# Smarty Pants, done correctly this time!
**discription:** The inspiration for this project comes from the material covered in my 
csci 241 datastructures course. In this class we learned about graphs and dijkstra's shortest
path algorithm. This made me think, what if each vertex represented some object and the 
edges and their weights represented the positive or negative relationship between those two
objects. If a relationship suddenly became more negative (the weight increased) then a path
finding algorithmn like djkstra would be less likely to include that relationship or a combination
of those two objects in it's optimal path. To me this sounded like a design for a program that wanted 
to draw various conclusions based on what the relationships of the 'system' were at the moment.
This project is an attempt to implement that system in a way that resembles a neural network. 
I am going to be applying this neural network is for learning a users clothing style preferences.
As a person who doesn't know what he's doing when putting on cloths I thought this would be something 
that I would benefit from having. The end goal is a program that can store your clothing inventory, 
track your preferences using a simple feedback interface, and then display analytics about your
preferences. Ex. 50% of the time you wear a red shirt you wear white shoes. 


**Software Development Goals**
- to gain familiarity with the python unittest module
- to use NumPy style docstrings
- to create class diagrams for each stage of development
- to track current goals and progress using github projects

**Software Goals**
- develop closet objects in such a way that this neural network can be resused for other purposes
- implement local and remote saving functionality, with some dbms
- implement a versital GUI (web based?)
- implement algorithmns to improve runtime, don't just use the obvious solution
- implement datastructures to optimize performance as much as possible
- use the mvc dessign architecture
- use design patterns
- gain a better understanding of the Errors in python
- develop thorough test cases for all non trivial functions
