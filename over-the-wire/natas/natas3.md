## Natas 3

As usual, we look at the page's source to look for clues. Like the previous challenge, there's nothing on this page. The hint given is that "not even Google" will find information leaks. 

The **robots exclusion protocol** is a standard which allows sites to communicate with web crawlers, search engines, and similar data processing services (such as the aforementioned Google) to tell them which parts of the site not to process or scan. These paths will generally be located in the site's *robot.txt* file. Let's check there:

http://natas3.natas.labs.overthewire.org/robots.txt

The file exists, and it denies agents from accessing the `/s3cr3t/` URL pattern. Let's try visiting it:

http://natas3.natas.labs.overthewire.org/s3cr3t/

And now we see another users.txt file, which contains the password for natas4. Next level.

password4: `Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`
