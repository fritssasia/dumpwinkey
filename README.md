# What is dumpwinkey

dumpwinkey just a simple tool to get windows product keys that might be stored in the BIOS
by checking whether COA (Certificate of Authenticity) is embedded in the BIOS or not
this tool actually only helps automate the process of finding a Windows product key, by utilizing the os module

# Requirements
```
pip install -r requirements.txt
```


# How To Use
```
sudo python dumpwinkey.py
```


# Note
- dumpwinkey requires root access

- sorry if this tool is less than perfect, I'm still a newbie
help me by giving advice and input
You can also help develop it! Thank you :)


# Screenshot
### display when dumpwinkey doesn't have root access
![alt text](https://imgur.com/2H7hnSr.png "Need root access")

### First look
![alt text](https://imgur.com/h2n2zih.png "First look dumpwinkey")

### Success get the windows product key
![alt text](https://imgur.com/Ez6IG2Z.png "Your Windows product key has been saved")

### The final result
![alt text](https://https://imgur.com/hTFM48r.jpg "You have successfully gotten a Windows product key")
