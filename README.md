# Aganitha bootcamp

# Task (ex-tools-1)

A web server with just one page displaying my name and photo. Used Google Cloud VM and Apache to run the server.
[Website link](https://geethar.mooo.com/)

## 🔧 Tools Used

- Google Cloud Platform (Compute Engine)
- Apache2 Web Server
- afraid.org (FreeDNS)
- ChatGPT and YouTube for support

## ⚙️ Steps Followed

1. **Set up VM** on GCP (Debian OS) following [this YouTube tutorial](https://youtu.be/6meDCnIW4sU?si=WvKlXC8kp6Z4ZCoU) and [Google Docs](https://cloud.google.com/compute/docs/tutorials/basic-webserver-apache).
2. **Installed Apache** with:
   ```bash
   sudo apt update
   sudo apt install apache2
   ```
3. **Uploaded HTML and image** to `/var/www/html` using the SSH file upload option.
4. **Set up free subdomain** using [afraid.org](https://freedns.afraid.org) and pointed it to my external IP.
5. **Configured Apache** with:
   ```bash
   sudo nano /etc/apache2/sites-available/000-default.conf
   # Added: ServerName geethar.mooo.com
   sudo systemctl reload apache2
   ```

## ✅ Website Live At

- IP: http://35.184.39.201  
- Domain: [Website link](https://geethar.mooo.com/)

## 🧠 ChatGPT Help

Used ChatGPT for assistance. https://chatgpt.com/share/6815c99d-cfe8-800c-92ca-581a786a6baf
