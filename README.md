# Python socket programming

I had problem with the firewall. The command that fixed it:

Opens the port 5555 for tcp connections

> sudo firewall-cmd --add-port=5555/tcp --permanent

Remember to reaload the firewall to apply changes:

> sudo firewall-cmd --reload

You can check what ports are open with:

> sudo firewall-cmd --list-ports
