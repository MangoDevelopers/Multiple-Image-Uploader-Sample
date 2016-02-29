# Multiple-Image-Uploader-Sample
## Multiple Image Uploader Android Sample with Django Backend
### URL Config
+ ### The root url [`/`]
	This is the skeleton form for uploading images. It has a username field (name="`username`") and a file input field (name="`fileinput`").
+ ### Post URL [`/post`]
	This is the action part of the skeleton form. This is the url to which the form is posted. It takes the images posted in the form and processes the images into JPEG form whatever the format may the image be, and stores in the server.
+ ### Username URL [`/[username]`]
	This url returns a json object, containing the list of image urls in them. The domain name or the IP should be prefixed with the `url` string to get the image.
+ ### Image URL [`/[username]/[image_name]`]
	This is the url that is used to get the image stored in the server. This is the image url returned during the form posting and from the Username URL.

Accordingly each URI method may return unexpected result if the inputs given are not matched.
+ Post URL
 	* If a file of any content type but image is posted it will return a json object as follows :(status code `500`)
 	  ```json
 	  {
		"status": ​500,
		"error": "Image type not recogonsied"
	  }
 	  ```
+ Username URL
	* If the username in the url is not found in the system :(status code `404`)
	  ```json
	  {
		"status": ​404,
		"error": "User not found"
	  }
	  ```
+ Image URL
	* In the image url if the username entered is not found, it will return a json as above. And if the image of given name in the url is not found :
		```json
		{
			"status": ​404,
			"error": "Image not found"
		}
		```