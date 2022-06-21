# CME-Module-RDP-login-checker
CrackMapExec module RDP login checker
- install hydra (if not installed)
- clone python file to  /root/.cme/modules/rdplogin.py (temporary solution for new feature https://github.com/byt3bl33d3r/CrackMapExec)
- crackmapexec smb 10.10.10.10 -u someuser -p somepass **-M rdplogin**
- _tested with **impacket-rdp_check** tested but this was reliable, code maybe later (for PTH)._

https://user-images.githubusercontent.com/49560894/174825668-8ab8ce46-578e-4f2f-baa9-93cc84e3d18f.mp4

