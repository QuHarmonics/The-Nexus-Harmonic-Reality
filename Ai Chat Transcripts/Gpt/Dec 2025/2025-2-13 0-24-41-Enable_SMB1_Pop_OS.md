# Enable SMB1 Pop OS

https://chat.openai.com/c/67ad8218-ba3c-8011-a3f4-356b33d941d5

## USER
pop os how do i enable smb 1

## ASSISTANT
To enable SMB1 on **Pop!_OS** (or any Ubuntu-based system), follow these steps:

### **1. Install Samba (if not already installed)**
Open a terminal and run:
```bash
sudo apt update
sudo apt install samba -y
```

### **2. Enable SMB1 in the Samba Configuration**
Edit the Samba configuration file:
```bash
sudo nano /etc/samba/smb.conf
```
Add the following lines under the `[global]` section:
```ini
client min protocol = NT1
server min protocol = NT1
```
This forces Samba to allow SMB1 connections.

### **3. Restart Samba**
Save the file (`CTRL+X`, then `Y`, then `Enter`) and restart Samba:
```bash
sudo systemctl restart smbd
```

### **4. Verify SMB1 is Enabled**
Run:
```bash
smbclient -L localhost -U%
```
If SMB1 is enabled, it should list available shares.

### **5. (Optional) Check SMB Version Support**
If you want to confirm the SMB versions available on your system:
```bash
smbd --version
smbclient --version
```

**⚠️ Security Note:**  
SMB1 is outdated and insecure. If possible, use SMB2 or SMB3 instead. Consider enabling it only temporarily or in isolated network environments.

Let me know if you need additional help! 🚀

