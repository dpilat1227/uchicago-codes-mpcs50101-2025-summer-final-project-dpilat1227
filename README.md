# Final Project 
**mpcs50101** — Summer 2025

Drew Pilat

---  

## How To Make Task Manager Executable

### 1) Make the file executable

In terminal (navigate to project folder) run:
```bash
chmod +x todo.py
``` 

### 2) Copy it to a directory in PATH (Mac/Linux)
Copy the file to /usr/local/bin/:
```bash
sudo cp todo.py /usr/local/bin/todo
```
Note: You can rename `todo.py` to just `todo` so we can run it as `todo` instead of `python todo.py` (much easier)

### 3) Test
Try these commands from another directory:
```bash
# Add a new task with a priority
todo --add "Finish the README" --priority 3

# List all current tasks
todo --list

# Complete a task by its ID
todo --done 3
```

### What I updated in `todo.py`
- Added shebang line (#!/usr/bin/env python3) at the top of code
    - This tells the system to use Python to run this file
- The pickle file now saves to the home directory (~/.todo.pickle) 
    - Tasks are now available wherever the command is run

### How to use it
**BEFORE we had to type:**
```bash
python todo.py --add "Task 1" --due 8/20/2025 --priority 1
python todo.py --list
python todo.py --done 1
```
**NOW we can simply type:**
```bash
todo --add "Task 1" --due 8/20/2025 --priority 1
todo --list
todo --done 1
```

Which is way easier!

--- 

**PS - Thank you Professor Andrew and Jiamao Zheng.**

I really enjoyed the course. I hope to register for more of your courses during my program. 
