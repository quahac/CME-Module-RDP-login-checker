# NetExec / CrackMapExec module RDP login checker
- install hydra (if not installed) - ```sudo apt install hydra```
- for NetExec      = clone python file to  /root/.nxc/modules/rdplogin.py (https://github.com/Pennyw0rth/NetExec)
- for CrackMapExec = clone python file to  /root/.cme/modules/rdplogin.py (https://github.com/byt3bl33d3r/CrackMapExec)
- nxc smb 10.10.10.10 -u someuser -p somepass **-M rdplogin**
- crackmapexec smb 10.10.10.10 -u someuser -p somepass **-M rdplogin**
- Why? Hydra is a little bit faster then RDP protocol nxc / cme and is just for checking if RDP login is possible with tested account on SMB

https://user-images.githubusercontent.com/49560894/174825668-8ab8ce46-578e-4f2f-baa9-93cc84e3d18f.mp4
