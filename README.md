# Automate-Boring-Stuff
For now, I'll be listing my notes below in this readme file. If it becomes problematic or clunky, I'll most likely move it to a different file.
Something to keep in mind is this readme file and most, if not all, of the python files will not meet the standards of many style guides, like limiting each line to 80 chars, etc.

# Chapter 1 notes

- The first chapter went over materials that are almost identical to what I learned in c++ so it was hard to take notes of "new" concepts

- The way the code is written was the biggest change moving from c++ to python for me
  - It seems like code can be written in a more direct manner, such as excluding "std::cout/endl" and even ";" at the end of a line

- The material that was almost, if not, identical to what I learned in c++ was the mathematical symbols, like basic operations, finding the remainder in division, etc.

- I think the hardest part about this chapter was navigating visual studio code since I did not use it while learning c++
  - If you're new to it as well, I would spend an hour or so just checking out the options, that helped me the most to figure out what was immediately useful for this chapter

- I took a peek at chapter 2 and noticed it covers logic, like if/else if/else statments, so I'm looking forward to learn how python handles these topics compared to c++

# Chapter 2 notes

- This chapter covers concepts including boolean values and operators, comparison operators, if/else/elif (else if) statements, while/for loops, break/continue statements, 
  -  An interesting topic this chapter went over is the "truthy" and "falsey" values as a different way to allow people reviewing your code to understand conditions in your loops, such as instead of using " variable != (value) " comparison, you could put " not (variable) " and make the variable an empty string or equal to 0
  -  Some new concepts I learned include the range function and its arguments, importing modules, 
     - The importing module section seems like its the same as using " include < __ > " in c++

# Chapter 3 notes

- This chapter covers concepts related to functions 
  - To create a function you would start with the def statement (ex, def function_one():)
  - Like in C++:
    - we can add arguments inside of the parantheses of the function
    - variables are "forgotten" after leaving a function
    - The return keyword can be used to obtain a specific value
  - A new concept I learned, or at least was not covered when I was learning C++, is keyword arguments used to manipulate how functions execute
    - like print(__ , end='') signifies the program to print something with no newline at the end
- Another topic this chapter covers is call stack and scope of a function
  - So far, it seems like it works as how I learned it in C++, meaning functions don't need to end for another one to start, there is a difference between global and local variables, both variables are "forgotten" when their scope ends, etc.
- Another concept that I believe was helpful for easily reading code is the global statement, I believe c++ did not have some indicator that you are specifically interacting with a global variable
  - However, I noticed the example using a global and local variable with the same name in a function, but attempting to print it before assigning it its local value ending in an error was interesting. I am not sure why python does not instead fall back to using the global variable's value, but it seems like it is just a rule to keep in mind
- The Try and Except statements reminded me of a switch statement or if else statements since you are making certain conditions result in specific outcomes
  - In the example they include of a program dividing 42 by the user's input, an input of 0 would result in a "ZeroDivisionError", and so they use the Except statements to print "Error: invalid argument" if the user attempts to divide by 0. It seems similar to an if else statement because they could have also put if the int is less than or greater than 0, then divide or else print out the error message
  - 
