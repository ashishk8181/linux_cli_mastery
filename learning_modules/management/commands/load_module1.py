from django.core.management.base import BaseCommand
from learning_modules.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load Module 1 lessons into database'

    def handle(self, *args, **kwargs):
        # Create Module 1
        module1, created = Module.objects.get_or_create(
            slug='module-1-linux-fundamentals',
            defaults={
                'title': 'MODULE 1: Linux Fundamentals & File System Basics',
                'description': 'Master the basics of Linux command line, file system navigation, and file management.',
                'order': 1
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created module: {module1.title}'))
        
        # Lesson 1
        lesson1, created = Lesson.objects.get_or_create(
            module=module1,
            slug='introduction-to-linux-cli',
            defaults={
                'title': 'Lesson 1: Introduction to the Linux CLI',
                'order': 1,
                'objectives': [
                    'Understand what a shell is',
                    'Understand terminal vs shell',
                    'Learn command structure',
                ],
                'content': '''What is the Terminal?

The terminal is a program that allows you to interact with your operating system using text commands.
It provides access to a shell.

What is a Shell?

A shell is a command interpreter.

Common Linux shells:
• `bash` (most common)
• `zsh`
• `sh`

When you type a command, the shell:
1. Reads your command
2. Executes it
3. Returns the output

Command Structure

Most Linux commands follow this structure:
`command [options] [arguments]`

Example:
`ls -l /home`

• `ls` → command
• `-l` → option
• `/home` → argument''',
                'practice_commands': [
                    'whoami',
                    'pwd',
                    'uname -a',
                    'echo "Welcome to Linux Mastery"'
                ],
                'challenge': 'Print the following exactly: Linux is powerful!'
            }
        )
        
        # Lesson 2
        lesson2, created = Lesson.objects.get_or_create(
            module=module1,
            slug='linux-directory-structure',
            defaults={
                'title': 'Lesson 2: Linux Directory Structure',
                'order': 2,
                'objectives': [
                    'Understand the Linux filesystem hierarchy',
                    'Identify important system directories',
                    'Navigate the root directory',
                ],
                'content': '''The Linux Filesystem Hierarchy

Everything in Linux starts from: `/`
This is called the root directory.

Linux follows a standard called: Filesystem Hierarchy Standard (FHS)

Important Directories:

`/` - Root of everything
`/home` - User home directories (Example: `/home/ashish`)
`/etc` - System configuration files
`/var` - Logs and variable data
`/usr` - User-installed programs
`/bin` - Essential command binaries
`/tmp` - Temporary files''',
                'practice_commands': [
                    'ls /',
                    'cd /home',
                    'pwd'
                ],
                'challenge': 'Answer: Where are system configuration files stored? Where are user home directories stored?'
            }
        )
        
        # Lesson 3
        lesson3, created = Lesson.objects.get_or_create(
            module=module1,
            slug='navigation-commands',
            defaults={
                'title': 'Lesson 3: Navigation Commands',
                'order': 3,
                'objectives': [
                    'Move between directories',
                    'Understand relative vs absolute paths',
                ],
                'content': '''Absolute Path
Starts from root `/`
Example: `cd /home/user`

Relative Path
Based on current location
Example: `cd Documents`

Important Navigation Commands:

`pwd` - Print current directory
`ls` - List directory contents
  Options:
  • `ls -l` → detailed view
  • `ls -a` → show hidden files
  • `ls -lh` → human readable sizes

`cd` - Change directory
`cd ..` - Go one level up
`cd ~` - Go to home directory''',
                'practice_commands': [
                    'mkdir testdir',
                    'cd testdir',
                    'pwd',
                    'cd ..'
                ],
                'challenge': 'Create a directory named linux_practice, enter it, then return to previous directory'
            }
        )
        
        # Lesson 4
        lesson4, created = Lesson.objects.get_or_create(
            module=module1,
            slug='creating-files-and-directories',
            defaults={
                'title': 'Lesson 4: Creating Files and Directories',
                'order': 4,
                'objectives': [
                    'Create directories',
                    'Create files',
                    'Understand file structure',
                ],
                'content': '''mkdir - Create directory

Create directory:
`mkdir myfolder`

Create nested directory:
`mkdir -p project/docs`

touch - Create empty file

Create empty file:
`touch notes.txt`

ls -l - View file details

View file details:
• Permissions
• Owner
• Size
• Date''',
                'practice_commands': [
                    'mkdir linux_project',
                    'cd linux_project',
                    'mkdir docs scripts',
                    'touch README.md'
                ],
                'challenge': '''Create this structure:
linux_project/
 ├── docs/
 ├── scripts/
 └── README.md'''
            }
        )
        
        # Lesson 5
        lesson5, created = Lesson.objects.get_or_create(
            module=module1,
            slug='copying-moving-deleting',
            defaults={
                'title': 'Lesson 5: Copying, Moving & Deleting',
                'order': 5,
                'objectives': [
                    'Copy files',
                    'Move files',
                    'Delete safely',
                ],
                'content': '''cp - Copy

Copy file:
`cp file1.txt file2.txt`

Copy directory:
`cp -r folder1 folder2`

mv - Move or rename

Move or rename:
`mv old.txt new.txt`

rm - Delete

Delete file:
`rm file.txt`

Delete directory:
`rm -r folder`

**Warning:** Be careful — deletion is permanent.''',
                'practice_commands': [
                    'touch test.txt',
                    'cp test.txt backup.txt',
                    'mv backup.txt archive.txt',
                    'rm archive.txt'
                ],
                'challenge': '''Final Module Challenge (Mission Mode)

Create the following structure:
my_lab/
 ├── configs/
 │     └── app.conf
 ├── logs/
 └── README.md

Then:
1. Copy README.md into configs/
2. Rename it to readme_backup.md
3. Delete the logs/ directory'''
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded Module 1 with 5 lessons'))
