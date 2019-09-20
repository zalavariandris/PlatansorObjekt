from collections import namedtuple

Rectangle = namedtuple("Rectangle", "top left bottom right")
class Rectangle(Rectangle):
	@property
	def width(self):
		return self.right-self.left

	@property
	def height(self):
		return self.bottom-self.top

	@property
	def center(self):
	    return (self.left+self.right)/2, (self.top+self.bottom)/2

	def shrink(self, margin:float)->tuple:
	    return Rectangle(self.top+margin, self.left+margin, self.bottom-margin, self.right-margin)

	def scale(self: tuple, factor, center=None):
	    # 
	    top, left, bottom, right = self
	    
	    # center default value
	    if not center:
	        center = ( (left+right)/2, (top+bottom)/2 ) 
	    
	    # scale rect around center
	    top = (top-center[1])*factor+center[1]
	    left = (left-center[0])*factor+center[0]
	    bottom = (bottom-center[1])*factor+center[1]
	    right = (right-center[0])*factor+center[0]
	    
	    return Rectangle(top, left, bottom, right)

	def fitIn(self, target):
	    top, left, bottom, right = self
	    width = self.width
	    height = self.height
	    target_top, target_left, target_bottom, target_right = target
	    
	    sw = (target_right-target_left) / width
	    sh = (target_bottom-target_top) / height

	    if sw < sh:
	        top = (target_top+target_bottom)/2 - height*sw /2
	        bottom = (target_top+target_bottom)/2 + height*sw /2
	        left = target_left
	        right = target_right
	    else:
	        top = target_top
	        bottom = target_bottom
	        left = (target_left+target_right)/2-width*sh/2
	        right = (target_left+target_right)/2+width*sh/2
	    
	    return Rectangle(top, left, bottom, right)