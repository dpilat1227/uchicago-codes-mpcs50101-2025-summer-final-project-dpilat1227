# Final Project 
**MPCS50101 - Summer 2025**


### How To Make Task Manager Executable / Run From Anywhere

### 1) Make the file executable

- In terminal (navigate to project folder) run:
```bash
chmod +x todo.py
``` 

### 2) Copy it to a directory in PATH (Mac/Linux)
- Copy the file to /usr/local/bin/:
```bash
sudo cp todo.py /usr/local/bin/todo
```
- Note: You can rename "todo.py" to just "todo" so we can run it as "todo" instead of "python todo.py" (much easier)

### 3) Test
- Try these commands in terminal from another directory:
    - `todo --add "Task manage from anywhere!" --priority 2`
    - `todo --list`


### What I updated in `todo.py`
- Added shebang line (#!/usr/bin/env python3) at the top of code
    - This tells the system to use Python to run this file
- The pickle file now saves to the home directory (~/.todo.pickle) 
    - Tasks are now available wherever the command is run

### How to use it
- **BEFORE we had to type:**
    - `python todo.py --add "Task 1" --due 8/20/2025 --priority 1`
    - `python todo.py --list`
    - `python todo.py --done 1`

- **NOW we can simply type:**
    - `todo --add "Task 1" --due 8/20/2025 --priority 1`
    - `todo --list`
    - `todo --done 1`

Which is way easier!

--- 

**PS - Thank you Professor Andrew and Jiamao Zheng.**

I really enjoyed the course. I hope to register for one of your other courses if possible.
