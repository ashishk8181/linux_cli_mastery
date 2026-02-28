from django.core.management.base import BaseCommand
from learning_modules.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load Module 5: Networking Fundamentals'

    def handle(self, *args, **kwargs):
        # Delete and recreate Module 5
        Module.objects.filter(slug="networking-fundamentals").delete()
        
        module = Module.objects.create(
            slug="networking-fundamentals",
            title="Module 5: Networking Fundamentals",
            description="Master Linux networking basics and troubleshooting",
            order=5
        )

        # Lesson 1
        Lesson.objects.create(
            module=module,
            slug="understanding-ip-addresses",
            title="Understanding IP Addresses",
            order=1,
            objectives=[
                "Understand what an IP address is",
                "Identify IPv4 structure",
                "Understand subnet basics",
                "View your system's IP address"
            ],
            content="""What is an IP Address?

An IP address uniquely identifies a device on a network.

Example: `192.168.1.10`

IPv4 addresses are 32-bit numbers divided into 4 octets.

**IPv4 Structure**

    IPv4 = 32 bits = 4 × 8-bit octets

Each octet ranges from: `0` to `255`

Example: `192.168.1.10`
• `192`
• `168`
• `1`
• `10`

**View IP Address**

    `ip addr`

Or:
    `ip a`

Look for:
• `inet` → IPv4 address
• `lo` → loopback interface

**Loopback Address**

    127.0.0.1

Used for local machine communication.""",
            practice_commands=[
                "ip addr",
                "ip a"
            ],
            challenge="Find your default network interface name.\nHint: Look for `eth0`, `ens33`, or `wlan0` in `ip addr` output"
        )

        # Lesson 2
        Lesson.objects.create(
            module=module,
            slug="routing-basics",
            title="Routing Basics",
            order=2,
            objectives=[
                "Understand default gateway",
                "View routing table",
                "Understand network traffic flow"
            ],
            content="""View Routing Table

    `ip route`

Example output:
    default via 192.168.1.1 dev eth0

**Meaning:**
• `default` → default route
• `via` → gateway
• `dev` → interface

**How Routing Works**

When you access `google.com`, traffic flows:
    Your machine → Default Gateway → Internet

**Subnet Concept**

    network = IP AND subnet_mask

Example:
• IP: `192.168.1.10`
• Mask: `255.255.255.0`
• Network: `192.168.1.0`""",
            practice_commands=[
                "ip route",
                "ip route show"
            ],
            challenge="Identify your default gateway.\nHint: Look for the line starting with `default via` in `ip route`"
        )

        # Lesson 3
        Lesson.objects.create(
            module=module,
            slug="testing-connectivity",
            title="Testing Connectivity",
            order=3,
            objectives=[
                "Test network reachability",
                "Understand latency",
                "Diagnose connectivity issues"
            ],
            content="""`ping` Command

    `ping google.com`

Shows:
• Round trip time (RTT)
• Packet loss

Stop with: `Ctrl + C`

**Check Open Ports with ss**

    `ss -tulnp`

**Options:**
• `t` → TCP
• `u` → UDP
• `l` → Listening
• `n` → Numeric
• `p` → Process

**DNS Lookup**

    `nslookup google.com`

Or:
    `dig google.com`""",
            practice_commands=[
                "ping 8.8.8.8",
                "ss -tuln",
                "nslookup google.com"
            ],
            challenge="Find which port your SSH service is listening on.\nHint: `ss -tulnp | grep ssh`"
        )

        # Lesson 4
        Lesson.objects.create(
            module=module,
            slug="network-interfaces-configuration",
            title="Network Interfaces & Configuration",
            order=4,
            objectives=[
                "Bring interface up/down",
                "Understand interface states",
                "View MAC address"
            ],
            content="""Bring Interface Down

    `sudo ip link set eth0 down`

Bring it up:
    `sudo ip link set eth0 up`

**Show Interface Details**

    `ip link show`

Shows:
• Interface state (`UP`/`DOWN`)
• MAC address

**Interface States**

• `UP` → Interface is active
• `DOWN` → Interface is inactive
• `LOWER_UP` → Physical link is connected""",
            practice_commands=[
                "ip link show",
                "ip link show eth0"
            ],
            challenge="What happens to network connectivity if interface is down?\nAnswer: All network communication through that interface stops"
        )

        # Lesson 5
        Lesson.objects.create(
            module=module,
            slug="basic-firewall-concepts",
            title="Basic Firewall Concepts",
            order=5,
            objectives=[
                "Understand firewall purpose",
                "View firewall rules",
                "Basic iptables understanding"
            ],
            content="""View iptables Rules

    `sudo iptables -L`

**Chains:**
• `INPUT` → Incoming traffic
• `OUTPUT` → Outgoing traffic
• `FORWARD` → Forwarded traffic

**What Firewall Does**

Firewall filters packets based on:
• Source IP
• Destination IP
• Port
• Protocol

**Example: Block Port 80**

    `sudo iptables -A INPUT -p tcp --dport 80 -j DROP`

**Breakdown:**
• `-A INPUT` → Append to INPUT chain
• `-p tcp` → Protocol TCP
• `--dport 80` → Destination port 80
• `-j DROP` → Jump to DROP (reject packet)""",
            practice_commands=[
                "sudo iptables -L",
                "sudo iptables -L -n"
            ],
            challenge="""**Final Module Mission (Network Debug Scenario)**

A server cannot access the internet.

**Tasks:**
1. Check IP address
2. Check routing table
3. Verify default gateway
4. Ping gateway
5. Check firewall rules
6. Verify DNS resolution

**Commands you may use:**
• `ip addr`
• `ip route`
• `ping`
• `ss`
• `iptables`
• `nslookup`

**Solution approach:**
    ip addr                    # Check IP
    ip route                   # Check gateway
    ping <gateway-ip>          # Test gateway
    ping 8.8.8.8              # Test internet
    nslookup google.com        # Test DNS
    sudo iptables -L           # Check firewall"""
        )

        self.stdout.write(self.style.SUCCESS('✅ Module 5 loaded successfully!'))
