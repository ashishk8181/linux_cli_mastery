from django.core.management.base import BaseCommand
from learning_modules.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load Module 6: Bash Scripting'

    def handle(self, *args, **kwargs):
        # Delete and recreate Module 6
        Module.objects.filter(slug="bash-scripting").delete()
        
        module = Module.objects.create(
            slug="bash-scripting",
            title="Module 6: Bash Scripting",
            description="Master Bash scripting and automation",
            order=6
        )

        # Lesson 1
        Lesson.objects.create(
            module=module,
            slug="introduction-to-bash-scripts",
            title="Introduction to Bash Scripts",
            order=1,
            objectives=[
                "Understand what a Bash script is",
                "Write your first script",
                "Make a script executable",
                "Run scripts properly"
            ],
            content="""What is a Bash Script?

A Bash script is a file containing multiple shell commands executed sequentially.

Instead of typing commands manually, you automate them.

**Creating Your First Script**

Create a file:
    `touch hello.sh`

Open it:
    `nano hello.sh`

Add:
    `#!/bin/bash
    echo "Hello, Linux Mastery!"`

**Shebang Line**

    `#!/bin/bash`

This tells the system which interpreter to use.

**Make Script Executable**

    `chmod +x hello.sh`

Run it:
    `./hello.sh`""",
            practice_commands=[
                "touch hello.sh",
                "chmod +x hello.sh",
                "./hello.sh"
            ],
            challenge="""Create a script called `system_info.sh` that prints:
• Hostname
• Uptime
• Memory usage

Hint: Use `hostname`, `uptime`, and `free -h` commands"""
        )

        # Lesson 2
        Lesson.objects.create(
            module=module,
            slug="variables-in-bash",
            title="Variables in Bash",
            order=2,
            objectives=[
                "Create variables",
                "Use variables",
                "Understand quoting"
            ],
            content="""Declaring Variables

    `name="Ashish"`

**Important:** No spaces around `=`.

**Using Variables**

    `echo $name`

Or safer:
    `echo "$name"`

**Example Script**

    `#!/bin/bash
    user=$(whoami)
    dir=$(pwd)
    
    echo "User: $user"
    echo "Directory: $dir"`

**Command Substitution**

    `variable=$(command)`

Captures command output into variable.""",
            practice_commands=[
                "name='John'",
                "echo $name",
                "user=$(whoami)"
            ],
            challenge="""Ask user for their name and greet them.

Hint:
    `read username
    echo "Hello $username"`

Create a script that does this."""
        )

        # Lesson 3
        Lesson.objects.create(
            module=module,
            slug="conditional-statements",
            title="Conditional Statements",
            order=3,
            objectives=[
                "Use if statements",
                "Compare numbers",
                "Compare strings"
            ],
            content="""Basic If Statement

    `if [ condition ]; then
        command
    fi`

**Numeric Comparison**

• `-eq` → equal
• `-ne` → not equal
• `-gt` → greater than
• `-lt` → less than

**Example**

    `#!/bin/bash
    num=10
    
    if [ $num -gt 5 ]; then
        echo "Greater than 5"
    fi`

**String Comparison**

    `if [ "$name" = "Ashish" ]; then
        echo "Hello Ashish"
    fi`

**File Tests**

• `-f file` → file exists
• `-d dir` → directory exists
• `-r file` → file is readable""",
            practice_commands=[
                "if [ 10 -gt 5 ]; then echo 'yes'; fi",
                "if [ -f /etc/passwd ]; then echo 'exists'; fi"
            ],
            challenge="""Check if a file exists:

    if [ -f filename ]; then
        echo "File exists"
    else
        echo "File not found"
    fi

Create a script that checks if `/etc/hosts` exists."""
        )

        # Lesson 4
        Lesson.objects.create(
            module=module,
            slug="loops",
            title="Loops",
            order=4,
            objectives=[
                "Use for loops",
                "Use while loops",
                "Automate repetitive tasks"
            ],
            content="""For Loop

    `for i in 1 2 3 4 5; do
        echo $i
    done`

**Range Loop**

    `for i in {1..5}; do
        echo $i
    done`

**While Loop**

    `count=1
    
    while [ $count -le 5 ]; do
        echo $count
        count=$((count+1))
    done`

**Arithmetic Expansion**

    `new_value = old_value + 1`

That's what happens in:
    `count=$((count+1))`

**Loop Through Files**

    `for file in *.txt; do
        echo $file
    done`""",
            practice_commands=[
                "for i in {1..5}; do echo $i; done",
                "for file in *.txt; do echo $file; done"
            ],
            challenge="""Create script that:
• Loops through all `.txt` files
• Prints file names

Hint:
    `for file in *.txt; do
        echo "Found: $file"
    done`"""
        )

        # Lesson 5
        Lesson.objects.create(
            module=module,
            slug="functions-in-bash",
            title="Functions in Bash",
            order=5,
            objectives=[
                "Create reusable functions",
                "Pass arguments",
                "Return values"
            ],
            content="""Define Function

    `greet() {
        echo "Hello $1"
    }`

Call it:
    `greet Ashish`

**Arguments**

Inside function:
• `$1` → first argument
• `$2` → second argument
• `$#` → number of arguments

**Example**

    `#!/bin/bash
    
    add() {
        result=$(( $1 + $2 ))
        echo "Sum: $result"
    }
    
    add 5 10`

**Function with Return**

    `check_file() {
        if [ -f "$1" ]; then
            return 0  # success
        else
            return 1  # failure
        fi
    }`""",
            practice_commands=[
                "greet() { echo 'Hello $1'; }",
                "greet World"
            ],
            challenge="""Create script that:
• Accepts two numbers as arguments
• Prints which one is larger

Hint:
    if [ $1 -gt $2 ]; then
        echo "$1 is larger"
    else
        echo "$2 is larger"
    fi"""
        )

        # Lesson 6 - Final Mission
        Lesson.objects.create(
            module=module,
            slug="final-automation-mission",
            title="Final Automation Mission",
            order=6,
            objectives=[
                "Combine all scripting concepts",
                "Create production-ready script",
                "Implement error handling"
            ],
            content="""**Automation Scenario**

You are a system administrator.

Create a script called `health_check.sh` that:

**Requirements:**
1. Prints hostname
2. Prints uptime
3. Prints memory usage
4. Checks if `/var/log/syslog` exists
5. Prints total number of users
6. Prints load average

**Bonus:**
• Colorize output
• Add timestamp

**Example Structure:**

    #!/bin/bash
    
    echo "=== System Health Check ==="
    echo "Date: $(date)"
    echo ""
    
    echo "Hostname: $(hostname)"
    echo "Uptime: $(uptime -p)"
    echo ""
    
    echo "Memory Usage:"
    free -h
    echo ""
    
    if [ -f /var/log/syslog ]; then
        echo "Syslog: EXISTS"
    else
        echo "Syslog: NOT FOUND"
    fi
    
    echo "Total Users: $(who | wc -l)"
    echo "Load Average: $(uptime | awk -F'load average:' '{print $2}')"

**Color Codes (Bonus):**

    RED='\\033[0;31m'
    GREEN='\\033[0;32m'
    NC='\\033[0m'  # No Color
    
    echo "${GREEN}Success${NC}"
    echo "${RED}Error${NC}"

**Test Your Script:**
    chmod +x health_check.sh
    ./health_check.sh""",
            practice_commands=[
                "touch health_check.sh",
                "chmod +x health_check.sh",
                "./health_check.sh"
            ],
            challenge="""**Complete the Mission:**

Create `health_check.sh` with all requirements.

**Verification:**
1. Script runs without errors
2. All information is displayed
3. File check works correctly
4. Output is readable

**Advanced Challenge:**
Add a function that checks disk usage and warns if any partition is over 80% full."""
        )

        self.stdout.write(self.style.SUCCESS('✅ Module 6 loaded successfully!'))
