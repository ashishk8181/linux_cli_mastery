from django.core.management.base import BaseCommand
from learning_modules.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load Module 7: Advanced Bash Scripting'

    def handle(self, *args, **kwargs):
        # Delete and recreate Module 7
        Module.objects.filter(slug="advanced-bash-scripting").delete()
        
        module = Module.objects.create(
            slug="advanced-bash-scripting",
            title="Module 7: Advanced Bash Scripting",
            description="Master advanced Bash scripting techniques",
            order=7
        )

        # Lesson 1
        Lesson.objects.create(
            module=module,
            slug="arrays-in-bash",
            title="Arrays in Bash",
            order=1,
            objectives=[
                "Declare arrays",
                "Access elements",
                "Loop through arrays",
                "Get array length"
            ],
            content="""Declaring an Array

    `#!/bin/bash
    
    fruits=("apple" "banana" "mango")`

**Access Elements**

    `echo ${fruits[0]}
    echo ${fruits[1]}`

**Array Length**

    `echo ${#fruits[@]}`

**Loop Through Array**

    `for fruit in "${fruits[@]}"; do
        echo $fruit
    done`

**Add Elements**

    `fruits+=("orange")`

**All Elements**

    `echo "${fruits[@]}"  # All elements
    echo "${fruits[*]}"  # All as single string`""",
            practice_commands=[
                'fruits=("apple" "banana" "mango")',
                'echo ${fruits[0]}',
                'echo ${#fruits[@]}'
            ],
            challenge="""Create script that:
• Takes filenames as arguments
• Stores them in array
• Prints how many were passed

Hint:
    files=("$@")
    echo "Total files: ${#files[@]}" """
        )

        # Lesson 2
        Lesson.objects.create(
            module=module,
            slug="case-statement",
            title="The case Statement",
            order=2,
            objectives=[
                "Replace multiple if-else blocks",
                "Handle command-line arguments",
                "Create interactive scripts"
            ],
            content="""Basic Syntax

    `case $variable in
        pattern1)
            command
            ;;
        pattern2)
            command
            ;;
        *)
            default_command
            ;;
    esac`

**Example: Menu Script**

    `#!/bin/bash
    
    echo "1) Show Date"
    echo "2) Show Uptime"
    read choice
    
    case $choice in
        1)
            date
            ;;
        2)
            uptime
            ;;
        *)
            echo "Invalid option"
            ;;
    esac`

**Pattern Matching**

    `case $1 in
        start|START)
            echo "Starting..."
            ;;
        stop|STOP)
            echo "Stopping..."
            ;;
    esac`""",
            practice_commands=[
                'read choice',
                'case $choice in 1) echo "One";; *) echo "Other";; esac'
            ],
            challenge="""Build a mini CLI tool:

    ./tool.sh status
    ./tool.sh logs
    ./tool.sh users

Use `case` to handle arguments.

Example:
    case $1 in
        status) echo "Running";;
        logs) tail /var/log/syslog;;
        users) who;;
    esac"""
        )

        # Lesson 3
        Lesson.objects.create(
            module=module,
            slug="error-handling-exit-codes",
            title="Error Handling & Exit Codes",
            order=3,
            objectives=[
                "Understand exit status",
                "Use $?",
                "Use exit properly",
                "Stop script on errors"
            ],
            content="""Exit Status

Every command returns a status:
• `0` → Success
• Non-zero → Failure

**Check Exit Code**

    `ls file.txt
    echo $?`

**Exit Script Manually**

    `exit 1`

**Exit Code Concept**

    `exit_code = 0 (success), exit_code ≠ 0 (failure)`

**Stop Script on First Error**

    `set -e`

**Better Error Handling Pattern**

    `if ! cp file1 file2; then
        echo "Copy failed"
        exit 1
    fi`

**Check Command Success**

    `if command; then
        echo "Success"
    else
        echo "Failed"
        exit 1
    fi`""",
            practice_commands=[
                'ls /nonexistent',
                'echo $?',
                'ls /etc && echo "Success"'
            ],
            challenge="""Create script that:
• Accepts filename as argument
• If file doesn't exist → exit 1
• If exists → print size

Hint:
    if [ ! -f "$1" ]; then
        echo "File not found"
        exit 1
    fi
    ls -lh "$1" """
        )

        # Lesson 4
        Lesson.objects.create(
            module=module,
            slug="traps-and-signals",
            title="Traps & Signals",
            order=4,
            objectives=[
                "Handle Ctrl+C",
                "Clean up temporary files",
                "Understand signals"
            ],
            content="""What is trap?

`trap` allows you to catch signals.

**Example signals:**
• `SIGINT` → Ctrl+C
• `SIGTERM` → Termination
• `EXIT` → Script exit

**Basic Trap Example**

    `trap "echo 'Script interrupted'; exit" SIGINT`

**Cleanup Example**

    `#!/bin/bash
    
    tempfile="temp.txt"
    touch $tempfile
    
    trap "rm -f $tempfile; echo 'Cleaned up'; exit" SIGINT
    
    while true; do
        sleep 1
    done`

If user presses `Ctrl+C` → file removed.

**Trap on Exit**

    `trap "echo 'Exiting...'" EXIT`

Runs when script exits (any reason).""",
            practice_commands=[
                'trap "echo Interrupted" SIGINT',
                'sleep 100'
            ],
            challenge="""Write script that:
• Runs infinite loop
• Handles `Ctrl+C` gracefully
• Prints "Shutting down safely..."

Example:
    trap "echo 'Shutting down safely...'; exit" SIGINT
    while true; do
        echo "Running..."
        sleep 2
    done"""
        )

        # Lesson 5
        Lesson.objects.create(
            module=module,
            slug="defensive-scripting-best-practices",
            title="Defensive Scripting Best Practices",
            order=5,
            objectives=[
                "Write safe scripts",
                "Prevent common mistakes",
                "Follow production patterns"
            ],
            content="""Use Strict Mode

Add at top of scripts:

    `set -euo pipefail`

**Meaning:**
• `-e` → exit on error
• `-u` → error on undefined variable
• `-o pipefail` → fail if any command in pipe fails

**Validate Inputs**

    `if [ $# -lt 1 ]; then
        echo "Usage: $0 filename"
        exit 1
    fi`

**Quote Variables**

❌ Bad:
    `rm $file`

✅ Good:
    `rm "$file"`

Prevents word splitting.

**Check Before Acting**

    `if [ -f "$file" ]; then
        rm "$file"
    fi`

**Use Functions**

    `validate_input() {
        if [ -z "$1" ]; then
            echo "Error: Empty input"
            return 1
        fi
    }`""",
            practice_commands=[
                'set -euo pipefail',
                'echo "$variable"'
            ],
            challenge="""Rewrite a previous script using:
• `set -e`
• Input validation
• Error checking
• Proper quoting

Make it production-ready!"""
        )

        # Lesson 6 - Final Mission
        Lesson.objects.create(
            module=module,
            slug="final-production-mission",
            title="Final Production Mission",
            order=6,
            objectives=[
                "Combine all advanced concepts",
                "Create production-ready script",
                "Implement comprehensive error handling"
            ],
            content="""**Production-Level Script**

Create a script called `deploy.sh`

**Requirements:**
1. Accept argument (`start` | `stop` | `status`)
2. Use `case` statement
3. Validate argument
4. Log output to file
5. Handle `Ctrl+C` safely
6. Exit properly with status codes
7. Use strict mode

**Bonus:**
• Use functions
• Use arrays
• Add colored output

**Example Structure:**

    `#!/bin/bash
    set -euo pipefail
    
    # Colors
    RED='\\033[0;31m'
    GREEN='\\033[0;32m'
    NC='\\033[0m'`
    
    # Cleanup on exit
    `trap "echo 'Exiting...'; exit" SIGINT`
    
    # Validate input
    `if [ $# -ne 1 ]; then
        echo "Usage: $0 {start|stop|status}"
        exit 1
    fi`
    
    # Log function
    `log() {
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a deploy.log
    }`
    
    # Main logic
    `case $1 in
        start)
            log "${GREEN}Starting service...${NC}"
            # Your start logic
            ;;
        stop)
            log "${RED}Stopping service...${NC}"
            # Your stop logic
            ;;
        status)
            log "Checking status..."
            # Your status logic
            ;;
        *)
            echo "Invalid option: $1"
            exit 1
            ;;
    esac
    
    log "Operation completed successfully"
    exit 0`

**Test Your Script:**

    `chmod +x deploy.sh`
    `./deploy.sh start`
    `./deploy.sh status`
    `./deploy.sh stop`
    `cat deploy.log`

**Advanced Features:**
• Add service array: `services=("web" "db" "cache")`
• Loop through services
• Check if processes are running
• Implement restart function
• Add verbose mode with `-v` flag""",
            practice_commands=[
                'touch deploy.sh',
                'chmod +x deploy.sh',
                './deploy.sh start'
            ],
            challenge="""**Complete Production Script:**

Create `deploy.sh` with ALL requirements:
✓ Strict mode
✓ Input validation
✓ Case statement
✓ Logging
✓ Signal handling
✓ Exit codes
✓ Functions
✓ Colors

**Verification Checklist:**
1. Script handles invalid arguments
2. Logs are created
3. Ctrl+C is handled gracefully
4. Exit codes are correct (0 for success, 1 for error)
5. All variables are quoted
6. Functions are used for reusable code"""
        )

        self.stdout.write(self.style.SUCCESS('✅ Module 7 loaded successfully!'))
