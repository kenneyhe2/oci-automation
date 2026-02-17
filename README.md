# oci-automation
``` plaintext
must use serial console to add authorized keys (rsa-sha2-512)
run below to authorized keys and double check fingerprint
chmod 600 /home/opc/.ssh/authorized_keys 
chown -R opc:opc /home/opc/.ssh
216333bf247ca1e745b52191f1396271f868d28b26d37baab1b8e670db80d300  authorized_keys

run below to login
ssh -v -i key opc@172.0.0.1
```
