## Natas 2

It makes sense to start off doing the same thing as the previous two levels - view the source. But, ignoring the default `head` lines, there's nothing in the `body` of index.html except the heading and one line:

`<img src="files/pixel.png">`

The debugging tools show that the image is just a single pixel in the main text box, nothing important. But what is important is the URL path: it shows "files/". Let's append that to the end of the home page's URL:

http://natas2.natas.labs.overthewire.org/files/

Here we see pixel.png as expected, as well as a file called users.txt in the same directory. Opening it shows a list of users and their passwords, including natas3's. Next level.

password3: `sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14`
