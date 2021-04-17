# object-dimension-measurement

Estimation of the object's dimensions in real-time:

        - using opencv and numpy
	
	- Applying contour method to find biggest contour first
	
	- Convert img to grey scale 
	
	- then apply guassian blur on image 
	
	- Apply Canny edge detector algorithm to find the edges (input the blurred image)
	
	- Apply erosion & dialation on image
	
	- Find the contours
	
	- Optimize getContours() to detect the A4 sheet paper
	
	- Warp: to get sequence of contours
	
	- Apply padding to remove the corner extra pixels
	
	- Find objects within our A4 paper
	
	- Obtain object's measurement with suitable representation
