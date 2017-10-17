import cv2
from moviepy.editor import *

def rotate(image, angle, center=None, scale=1.0):
	"""
	https://github.com/jrosebr1/imutils/blob/master/imutils/convenience.py#L25
	"""
	(h, w) = image.shape[:2]
	if center is None:
		center = (w // 2, h // 2)
	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w, h))
	return rotated

def createAnimation(ringImg):
	ringSeq = [rotate(ringImg,angle) for angle in range(360)]
	ringClip = ImageSequenceClip(ringSeq,fps=36)
	faceClip = ImageClip('face.png',duration=10)
	backgroundClip = ColorClip((1000,1000),color=(255,255,255),duration=10)
	finalClip = CompositeVideoClip([backgroundClip,ringClip,faceClip])

	finalClip.write_videofile("ani.mp4")

if __name__ == '__main__':
	ringImg = cv2.imread('ring.png',cv2.IMREAD_UNCHANGED)
	if ringImg is None:
		raise IOError("ring.png do not exist")
	ringImg = cv2.cvtColor(ringImg,cv2.COLOR_BGRA2RGBA)

	createAnimation(ringImg)

