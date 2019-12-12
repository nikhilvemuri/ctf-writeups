# Natas

Natas is a wargame based on web server security challenges.
http://overthewire.org/wargames/natas


## Natas 0


Once inside level 0 (use the password given on the starter page), we can inspect the source code of the landing page to find the password for level 1 commented inside the `body` of the HTML source. On to level 1.

password1: `gtVrDuiDfck831PqWsLEZy5gyDz1clto`


## Natas 1

This level is almost identical to the previous one, with the difference being that right-clicking is disabled. 

There are multiple ways to get around this, such as by opening your browser's debugging tools and visiting index.html, or by adding `view-source:` in front of the page's URL in the address bar. 

Once again, the password can be found inside the `body` tag of the HTML code.

password2: `ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi`


## Natas 2

It makes sense to start off doing the same thing as the previous two levels - view the source. But, ignoring the default `head` lines, there's nothing in the `body` of index.html except the heading and one line:

`<img src="files/pixel.png">`

The debugging tools show that the image is just a single pixel in the main text box, nothing important. But what is important is the URL path: it shows "files/". Let's append that to the end of the home page's URL:

http://natas2.natas.labs.overthewire.org/files/

Here we see pixel.png as expected, as well as a file called users.txt in the same directory. Opening it shows a list of users and their passwords, including natas3's. Next level.

password3: `sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14`


## Natas 3

As usual, we look at the page's source to look for clues. Like the previous challenge, there's nothing on this page. The hint given is that "not even Google" will find information leaks. 

The **robots exclusion protocol** is a standard which allows sites to communicate with web crawlers, search engines, and similar data processing services (such as the aforementioned Google) to tell them which parts of the site not to process or scan. These paths will generally be located in the site's *robot.txt* file. Let's check there:

http://natas3.natas.labs.overthewire.org/robots.txt

The file exists, and it denies agents from accessing the `/s3cr3t/` URL pattern. Let's try visiting it:

http://natas3.natas.labs.overthewire.org/s3cr3t/

And now we see another users.txt file, which contains the password for natas4. Next level.

password4: `Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`

