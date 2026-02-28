from django.core.management.base import BaseCommand
from learning_modules.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load Module 3: Permissions & Ownership'

    def handle(self, *args, **kwargs):
        # Delete and recreate Module 3
        Module.objects.filter(slug="permissions-ownership").delete()
        
        module = Module.objects.create(
            slug="permissions-ownership",
            title="Module 3: Permissions & Ownership",
            description="Master Linux file permissions and ownership",
            order=3
        )

        # Lesson 1
        Lesson.objects.create(
            module=module,
            slug="understanding-file-permissions",
            title="Understanding File Permissions",
            order=1,
            objectives=[
                "Understand Linux permission model",
                "Read permission strings",
                "Identify user, group, and others",
                "Interpret ls -l output"
            ],
            content="""Why Permissions Matter

Linux is a multi-user system.

Permissions control:
• Who can read a file
• Who can modify a file
• Who can execute a file

Without permissions, systems would be insecure.

Viewing Permissions

Run:
    `ls -l`

Example output:
    `-rwxr-xr-- 1 ashish staff 4096 Jan 1 12:00 script.sh`

Let's break it down:
    -rwxr-xr--

**Permission Structure**

    [Type][Owner][Group][Others]

Example: `-rwxr-xr--`

• `-` → Regular file
• `rwx` → Owner permissions
• `r-x` → Group permissions
• `r--` → Others permissions

**What r, w, x Mean**

• `r` → Read
• `w` → Write
• `x` → Execute

**Directory Permissions**

For directories:
• `r` → List contents
• `w` → Create/delete files
• `x` → Enter directory""",
            practice_commands=[
                "touch test.txt",
                "ls -l test.txt"
            ],
            challenge="Create a file and interpret its permission string."
        )

        # Lesson 2
        Lesson.objects.create(
            module=module,
            slug="changing-permissions-chmod",
            title="Changing Permissions with chmod",
            order=2,
            objectives=[
                "Change file permissions",
                "Understand symbolic mode",
                "Understand numeric (octal) mode"
            ],
            content="""Symbolic Mode

    chmod u+x script.sh

**Meaning:**
• `u` → user (owner)
• `g` → group
• `o` → others
• `a` → all
• `+` → add permission
• `-` → remove permission

Example:
    `chmod g-w file.txt`

Removes write permission from group.

**Numeric (Octal) Mode**

Each permission has a numeric value:
• `r` → 4
• `w` → 2
• `x` → 1

They are added together.

**For example:**
• Owner: `rwx` → 4+2+1 = 7
• Group: `r-x` → 4+0+1 = 5
• Others: `r--` → 4+0+0 = 4

So:
    `chmod 754 script.sh`

**Numeric Breakdown**

Here is the fundamental rule:
    permission = r(4) + w(2) + x(1)

That's how every permission number is calculated.

**Examples:**
• `7` = rwx
• `6` = rw-
• `5` = r-x
• `4` = r--""",
            practice_commands=[
                "touch demo.sh",
                "chmod 755 demo.sh",
                "ls -l demo.sh"
            ],
            challenge="""Make a file:
• Executable only by owner
• Readable by group
• No access for others

Hint: chmod 540 filename"""
        )

        # Lesson 3
        Lesson.objects.create(
            module=module,
            slug="changing-ownership-chown",
            title="Changing Ownership with chown",
            order=3,
            objectives=[
                "Change file owner",
                "Change group ownership",
                "Understand ownership structure"
            ],
            content="""Viewing Owner and Group

    ls -l file.txt

Example:
    `-rw-r--r-- 1 ashish staff 0 Jan 1 12:00 file.txt`

• `ashish` → Owner
• `staff` → Group

**Change Owner**

    `sudo chown user file.txt`

**Change Owner and Group**

    `sudo chown user:group file.txt`

**Change Only Group**

    `sudo chgrp group file.txt`""",
            practice_commands=[
                "touch sample.txt",
                "sudo chown root sample.txt",
                "ls -l sample.txt"
            ],
            challenge="Change file ownership to another user and verify."
        )

        # Lesson 4
        Lesson.objects.create(
            module=module,
            slug="special-permissions",
            title="Special Permissions (Advanced)",
            order=4,
            objectives=[
                "Understand SUID",
                "Understand SGID",
                "Understand Sticky Bit"
            ],
            content="""SUID (Set User ID)

When set on executable:
• File runs with owner's privileges

    `chmod u+s program`

Example: `/usr/bin/passwd` uses SUID.

**SGID (Set Group ID)**

When set:
• File runs with group privileges

    `chmod g+s program`

**Sticky Bit**

Used mainly on directories like `/tmp`.
• Only file owner can delete their files

    `chmod +t directory`

Example:
    `ls -ld /tmp`

You'll see `t` in permission string.""",
            practice_commands=[
                "mkdir shared",
                "chmod 1777 shared",
                "ls -ld shared"
            ],
            challenge="""Set up a directory where:
• Everyone can create files
• Only file owners can delete their own files

Hint: Use chmod 1777 dirname"""
        )

        # Lesson 5 - Final Mission
        Lesson.objects.create(
            module=module,
            slug="final-mission",
            title="Final Module Mission",
            order=5,
            objectives=[
                "Apply permission concepts",
                "Troubleshoot permission issues",
                "Secure files properly"
            ],
            content="""**Real-World Scenario**

You are a junior sysadmin.

**Scenario:**
A script named `backup.sh` is not running.

You inspect:
    `ls -l backup.sh`

It shows:
    `-rw-r--r-- 1 ashish staff 1024 Jan 1 12:00 backup.sh`

**Problem:**
The script is not executable.

**Task:**
1. Make it executable by owner only
2. Verify permissions
3. Explain why others should not have execute access

**Solution:**
    `chmod u+x backup.sh`
    `ls -l backup.sh`

**Why restrict execute access?**
• Security: Prevents unauthorized users from running scripts
• Control: Only authorized users should execute system scripts
• Audit: Easier to track who can run critical operations""",
            practice_commands=[
                "touch backup.sh",
                "chmod u+x backup.sh",
                "ls -l backup.sh"
            ],
            challenge="""**Complete Mission:**
1. Create a script file
2. Set permissions to 700 (owner only)
3. Verify it's executable by you but not by others
4. Explain the security benefit"""
        )

        self.stdout.write(self.style.SUCCESS('✅ Module 3 loaded successfully!'))
