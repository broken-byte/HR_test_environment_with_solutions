The HackerRank Interview Prep Kit Solution Stash/ Test Environment!
-------------------------------------------------------------------
This repo is both a stash of my solutions to the Hacker Rank Interview 
Prep Kit AND a a testing environment that makes it easy to do the challenges
On your local machine. 

Common problems I encounter in integrated web IDE's like the one featured 
on HackerRank is the lack of good linting and/or not enough feedback on test
failures (especially on the long time complexity tests). Inevitably I found 
myself copy pasting the test data and making my own tests.

Pretty soon I got tired of rewriting unit tests so I wrote code inside of the
test_utilities directory that makes dynamically generated tests given the test data and 
the function you wanna test. I've also added code to process the text files
that Hacker Rank provides which contain the SUPER long test data for time complexity
tests.

The repo is divided up into different topics from data structures & algorithms,i.e., 
sorting, arrays, greedy algorithms, etc. (not including the test_utilities directory)

It is further divided into easy, medium, hard, and advanced problem sets for each topic. 

Some problems from the HackerRank Interview Prep Kit are omitted from here since they were either:
1. Too easy to warrant a full test suite + file structure and were solved
within hacker rank's awesome integrated web IDE (which is awesome), or,
2. Not well worded or too tedious to replicate in this environment.

Installation
------------
1. Clone the repo!

2. Navigate to the generated directory and within your terminal, run:

    `python3 -m venv env`
    
    if you haven't installed python virtual environments before, look up just that, then run:
    
    `pip install virtualenv`
    
    If you haven't installed pip, its a package manager for Python, so look it up and install :)
3. run:

    `source env/bin/activate`
    
    to activate your virtual environment. You should see a `(env)` in front of your terminal
    prompt now.
    
4. run:
    
    `pip install -r dependencies.txt`
    
    to install the dependencies for the test environment. 
    
5. You're all set! :)

How to Use
------------
 I've already written test data for the challenges I've done. all the test data is in the 
 respective directories of each challenge, inside the test_resources folder. I've separated
 the functionality tests from the time complexity tests in the respectively named files.
 
 ###Example 0
 
 I have a challenge called 

Feel free to shoot me any questions regarding this repo! Happy coding! <3

The link to the interview prep kit is: [Here](https://www.hackerrank.com/interview/interview-preparation-kit)

