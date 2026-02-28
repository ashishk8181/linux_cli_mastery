from django.core.management.base import BaseCommand
from learning_modules.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load Module 4: Process Management & System Monitoring'

    def handle(self, *args, **kwargs):
        # Delete and recreate Module 4
        Module.objects.filter(slug="process-management").delete()
        
        module = Module.objects.create(
            slug="process-management",
            title="Module 4: Process Management & System Monitoring",
            description="Master process management and system monitoring",
            order=4
        )

        # Lesson 1
        Lesson.objects.create(
            module=module,
            slug="understanding-processes",
            title="Understanding Processes",
            order=1,
            objectives=[
                "Understand what a process is",
                "Identify running processes",
                "Understand PID (Process ID)",
                "Learn process hierarchy"
            ],
            content="""What is a Process?

A process is a running instance of a program.

Example: When you run `nano file.txt`, the system creates a process for `nano`.

Each process has:
• `PID` (Process ID)
• `PPID` (Parent Process ID)
• Owner
• `CPU` usage
• `Memory` usage

**View Running Processes**

Basic View:
    `ps`

Shows processes in current shell.

Full System View:
    `ps aux`

• `a` → all users
• `u` → user-oriented format
• `x` → processes without terminal

**Understanding ps aux Output**

Example:
    USER   PID  %CPU %MEM  VSZ  RSS TTY  STAT START TIME COMMAND

Key fields:
• `PID` → Process ID
• `%CPU` → CPU usage
• `%MEM` → Memory usage
• `COMMAND` → Executed program

**Process Tree**

    `ps -ef --forest`

Shows parent-child relationships.""",
            practice_commands=[
                "`ps aux`",
                "`ps -ef`"
            ],
            challenge="Find the PID of your current shell process.\nHint: `echo $$`"
        )

        # Lesson 2
        Lesson.objects.create(
            module=module,
            slug="real-time-monitoring",
            title="Real-Time Monitoring",
            order=2,
            objectives=[
                "Monitor CPU usage",
                "Monitor memory usage",
                "Identify resource-heavy processes"
            ],
            content="""`top` Command

    top

Shows live updating process list.

**Important keys inside top:**
• `q` → Quit
• `k` → Kill process
• `M` → Sort by memory
• `P` → Sort by CPU

**Understanding Load Average**

Inside `top`, you will see:
    load average: 0.15, 0.10, 0.05

These represent:
• Last 1 minute
• Last 5 minutes
• Last 15 minutes

Load average roughly means:
    load average ≈ runnable processes / cpu cores

If load average is higher than number of CPU cores, system is overloaded.

**Example:**
• 4 cores
• Load average = 6
• → System is stressed

**htop (If Installed)**

Better UI than `top`:
    `htop`""",
            practice_commands=[
                "top",
                "uptime"
            ],
            challenge="Find the process consuming the most memory.\nHint: In `top`, press `M` to sort by memory"
        )

        # Lesson 3
        Lesson.objects.create(
            module=module,
            slug="managing-processes",
            title="Managing Processes",
            order=3,
            objectives=[
                "Stop processes",
                "Send signals",
                "Understand signals"
            ],
            content="""Kill a Process

    `kill PID`

Default signal: `SIGTERM` (15)

**Force Kill**

    `kill -9 PID`

Signal 9 → `SIGKILL`

**Warning:** Use only when necessary.

**Common Signals**

• `SIGTERM` (15) → Graceful termination
• `SIGKILL` (9) → Immediate kill
• `SIGSTOP` (19) → Pause process
• `SIGCONT` (18) → Resume process

**Kill by Name**

    `killall processname`

Example:
    `killall firefox`""",
            practice_commands=[
                "sleep 1000 &",
                "ps aux | grep sleep",
                "kill <PID>"
            ],
            challenge="Start a background sleep process and terminate it safely.\nHint: `sleep 100 &` then `kill %1`"
        )

        # Lesson 4
        Lesson.objects.create(
            module=module,
            slug="background-foreground-jobs",
            title="Background & Foreground Jobs",
            order=4,
            objectives=[
                "Run background jobs",
                "Move jobs between background and foreground",
                "View job list"
            ],
            content="""Run in Background

    `sleep 60 &`

`&` → background execution

**List Jobs**

    `jobs`

**Bring to Foreground**

    `fg %1`

**Suspend Process**

While running, press:
    `Ctrl + Z`

Then:
    `bg`

This resumes the process in background.""",
            practice_commands=[
                "sleep 200 &",
                "jobs",
                "fg %1"
            ],
            challenge="""Suspend a process and resume it in background.

Steps:
1. Run: `sleep 300`
2. Press `Ctrl+Z`
3. Run: `bg`
4. Run: `jobs`"""
        )

        # Lesson 5
        Lesson.objects.create(
            module=module,
            slug="system-resource-monitoring",
            title="System Resource Monitoring",
            order=5,
            objectives=[
                "Check memory usage",
                "Check disk usage",
                "Monitor uptime"
            ],
            content="""Memory Usage

    `free -h`

Shows:
• Total memory
• Used memory
• Free memory

**Disk Usage**

    `df -h`

Shows disk space.

**Directory Size**

    `du -sh foldername`

**Uptime**

    `uptime`

Shows:
• System running time
• Load average""",
            practice_commands=[
                "free -h",
                "df -h",
                "uptime"
            ],
            challenge="""**Final Module Mission (Production Scenario)**

You are investigating a slow server.

**Tasks:**
1. Check load average
2. Identify high CPU process
3. Check memory usage
4. Find large directories
5. Kill misbehaving process safely

**Commands you may use:**
• `top`
• `ps`
• `kill`
• `free`
• `df`
• `du`

**Solution approach:**
    uptime                    # Check load
    top                       # Find high CPU process
    free -h                   # Check memory
    du -sh /var/* | sort -h   # Find large dirs
    kill -15 <PID>            # Kill safely"""
        )

        self.stdout.write(self.style.SUCCESS('✅ Module 4 loaded successfully!'))
