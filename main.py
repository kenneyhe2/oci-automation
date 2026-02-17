import pexpect
import sys


# The exact SSH command from your request
ssh_command = (
    "ssh -v -i ~/Downloads/ssh-key-2026-02-17.key -o HostKeyAlgorithms=+ssh-rsa "    
    "-o PubkeyAcceptedKeyTypes=+ssh-rsa "
    "-o ProxyCommand='ssh -W %h:%p -p 443 ocid1.instanceconsoleconnection.oc1.iad.anuwcljrqw2xtbqcl2xuvmc3sotjfuhwlulnodyqlvmq2x6rqwaqh65gsroa@instance-console.us-ashburn-1.oci.oraclecloud.com' "
    "ocid1.instance.oc1.iad.anuwcljrqw2xtbqch2cmn6f6bwjozhx3hc6aqjghhh2265ztev4as5triqhq"
)

print("Starting SSH connection...")

# We use spawn to keep the connection interactive
child = pexpect.spawn(ssh_command)
child.sendline('\r\r')

# Optional: Log output to console so you can see what's happening
child.logfile = sys.stdout.buffer

# 1. Handle "First Time" Connection (SSH Fingerprint)
# We expect either the fingerprint prompt OR the login prompt immediately.
index = child.expect([
    '(?i)are you sure you want to continue connecting',  # 0: Fingerprint
    '(?i)login:',                                        # 1: Login prompt
    pexpect.TIMEOUT                                      # 2: Timeout
], timeout=90)

if index == 0:
    # If asked for fingerprint confirmation
    print("\n--- Sending 'yes' for fingerprint ---")
    child.sendline('yes\r\r\r')
    # After saying yes, wait for the login prompt
    child.expect('(?i)login:')

# 2. Handle Login
# (If we skipped the 'if' block above, we are already at the login prompt)
print("\n--- Sending Login ---")
child.sendline('helloworld')

# 3. Handle Password
child.expect('(?i)password:')
print("\n--- Sending Password ---")
child.sendline('byeworld')

# 4. Hand control over to the user (Interactive Mode)
# This keeps the SSH session alive so you can type commands.
print("\n--- Interaction Started ---")
child.interact()
