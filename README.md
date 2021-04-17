# object-dimension-measurement

Estimation of the object's dimensions in real-time:

        # using opencv and numpy
	
	- Applying contour method to find biggest contour first
	
	- Convert img to grey scale 
	
	- then apply guassian blur on image 
	
	- Apply Canny edge detector algorithm to find the edges (input the blurred image)
	
	- Apply erosion & dialation on image
	
	- Find the contours
	
	- Optimize getContours() 
	
	- Warp: to get sequence of contours
	
	- Apply padding to remove the extra corner pixels
	
	- Find objects within input image
	
	- Obtain object's measurement with suitable representation
