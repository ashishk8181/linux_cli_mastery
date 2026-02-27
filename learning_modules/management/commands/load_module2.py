from django.core.management.base import BaseCommand
from learning_modules.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load Module 2: File Viewing & Text Processing'

    def handle(self, *args, **kwargs):
        # Delete and recreate Module 2
        Module.objects.filter(slug="file-viewing-text-processing").delete()
        
        module = Module.objects.create(
            slug="file-viewing-text-processing",
            title="Module 2: File Viewing & Text Processing",
            description="Master file viewing, searching, and text processing commands",
            order=2
        )

        # Lesson 1
        Lesson.objects.create(
            module=module,
            slug="viewing-file-contents",
            title="Viewing File Contents",
            order=1,
            objectives=[
                "Display file contents in different ways",
                "View large files safely",
                "Inspect specific parts of a file"
            ],
            content="""cat — Display Entire File

`cat` prints the entire file to the terminal.

    `cat filename.txt`

**Warning:** Avoid using `cat` on very large files.

Show Line Numbers:
    `cat -n filename.txt`

less — View Large Files Safely

`less` allows scrolling without loading everything into memory at once.

    `less filename.txt`

Navigation inside `less`:
• `Space` → Next page
• `b` → Previous page
• `/word` → Search
• `q` → Quit

head — View Beginning of File

    `head filename.txt`

Default: first 10 lines.

Specify number:
    `head -n 5 filename.txt`

tail — View End of File

    `tail filename.txt`

Last 10 lines by default.

Specify number:
    `tail -n 3 filename.txt`

tail -f — Monitor Live Logs

    `tail -f logfile.log`

Used for:
• Monitoring logs
• Debugging servers
• Watching real-time output""",
            practice_commands=[
                "head -n 5 /etc/passwd",
                "tail -n 5 /etc/passwd",
                "less /etc/services"
            ],
            challenge="Display the last 3 lines of /etc/passwd."
        )

        # Lesson 2
        Lesson.objects.create(
            module=module,
            slug="searching-with-grep",
            title="Searching Inside Files with grep",
            order=2,
            objectives=[
                "Search for patterns inside files",
                "Use common grep options",
                "Understand basic pattern matching"
            ],
            content="""Basic Search

    `grep root /etc/passwd`

Search for "root" in file.

Case-Insensitive Search with `-i`

    `grep -i error logfile.log`

Show Line Numbers with `-n`

    `grep -n root /etc/passwd`

Recursive Search with `-r`

    `grep -r "TODO"`

Search all files in current directory.

Count Matches with `-c`

    `grep -c root /etc/passwd`

**Common Use Cases:**
• Finding errors in logs
• Searching configuration files
• Locating specific users or processes""",
            practice_commands=[
                "grep bash /etc/passwd",
                "grep -i ssh /etc/services"
            ],
            challenge="Find how many users use /bin/bash as their shell.\nHint: Use grep with -c option"
        )

        # Lesson 3
        Lesson.objects.create(
            module=module,
            slug="pipes-command-chaining",
            title="Pipes & Command Chaining",
            order=3,
            objectives=[
                "Combine commands",
                "Filter output",
                "Understand data flow"
            ],
            content="""The Pipe Operator `|`

The pipe sends output of one command to another.

    `command1 | command2`

Example:
    `ls -l | grep ".txt"`

**Flow:**
1. `ls -l` produces output
2. `grep` filters it

Example: Count Files

    `ls | wc -l`

Counts number of files.

Combine with `grep`

    `ps aux | grep ssh`

Find running SSH processes.

**Real-World Examples:**
• Filter logs: `cat error.log | grep "FATAL"`
• Count users: `cat /etc/passwd | wc -l`
• Find processes: `ps aux | grep python`""",
            practice_commands=[
                "ls | wc -l",
                "ps aux | grep bash",
                "cat /etc/passwd | grep root"
            ],
            challenge="Count how many .conf files exist in /etc.\nHint: Use ls /etc | grep .conf | wc -l"
        )

        # Lesson 4
        Lesson.objects.create(
            module=module,
            slug="redirection",
            title="Redirection",
            order=4,
            objectives=[
                "Save output to files",
                "Append output",
                "Redirect errors"
            ],
            content="""Redirect Output `>`

    `ls > output.txt`

Overwrites file.

Append Output `>>`

    `echo "New line" >> output.txt`

Redirect Errors `2>`

    `ls nonexistentfile 2> error.txt`

Redirect Both Output & Errors

    `command > all_output.txt 2>&1`

**Common Patterns:**
• Save logs: `command > logfile.txt`
• Append to logs: `command >> logfile.txt`
• Discard output: `command > /dev/null`
• Discard errors: `command 2> /dev/null`""",
            practice_commands=[
                "ls -l > listing.txt",
                "grep root /etc/passwd > root_users.txt",
                "echo 'Hello' >> output.txt"
            ],
            challenge="Save all users containing 'bash' into a file called bash_users.txt.\nHint: grep bash /etc/passwd > bash_users.txt"
        )

        # Lesson 5
        Lesson.objects.create(
            module=module,
            slug="text-processing-tools",
            title="Basic Text Processing Tools",
            order=5,
            objectives=[
                "Extract columns",
                "Sort data",
                "Remove duplicates"
            ],
            content="""`wc` — Word Count

    `wc filename.txt`

Shows:
• Lines
• Words
• Characters

Options:
    `wc -l filename.txt  # Lines only`
    `wc -w filename.txt  # Words only`

`sort`

    `sort filename.txt`

Reverse sort:
    `sort -r filename.txt`

Numeric sort:
    `sort -n filename.txt`

`uniq`

Removes duplicate lines:
    `uniq filename.txt`

(Usually combined with `sort`)

`cut`

Extract columns:
    `cut -d ":" -f 1 /etc/passwd`

• `-d` → delimiter
• `-f` → field

**Real Examples:**
• Extract usernames: `cut -d ":" -f 1 /etc/passwd`
• Sort and dedupe: `sort file.txt | uniq`
• Count unique lines: `sort file.txt | uniq | wc -l`""",
            practice_commands=[
                "cut -d ':' -f 1 /etc/passwd",
                "sort /etc/passwd",
                "wc -l /etc/passwd"
            ],
            challenge="""**Final Module Challenge (Mission Mode)**

You are investigating a system.

**Task:**
1. Extract usernames from `/etc/passwd`
2. Save them into `users.txt`
3. Sort them alphabetically
4. Count total number of users

**Hint:** Use combination of `cut`, `sort`, and `wc`

**Solution steps:**
    cut -d ':' -f 1 /etc/passwd > users.txt
    sort users.txt -o users.txt
    wc -l users.txt"""
        )

        self.stdout.write(self.style.SUCCESS('✅ Module 2 loaded successfully!'))
