# USAGE
# python human_activity_reco.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt --input example_activities.mp4
# python human_activity_reco.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt

# import the necessary packages
import numpy as np
import argparse
import imutils
import sys
import cv2


CLASSES = open('action_recognition_kinetics.txt').read().strip().split("\n")
SAMPLE_DURATION = 16
SAMPLE_SIZE = 112

# load the human activity recognition model
print("[INFO] loading human activity recognition model...")
net = cv2.dnn.readNet('resnet-34_kinetics.onnx')

# grab a pointer to the input video stream
print("[INFO] accessing video stream...")
vs = cv2.imread('img.jpeg')
frames=[]
# loop until we explicitly break from it
# initialize the batch of frames that will be passed through the

frames.append(vs)
# now that our frames array is filled we can construct our blob
blob = cv2.dnn.blobFromImages(frames, 1.0,
	(SAMPLE_SIZE, SAMPLE_SIZE), (114.7748, 107.7354, 99.4750),
	swapRB=True, crop=True)
blob = np.transpose(blob, (1, 0, 2, 3))
blob = np.expand_dims(blob, axis=0)

# pass the blob through the network to obtain our human activity
# recognition predictions
net.setInput(blob)
outputs = net.forward()
label = CLASSES[np.argmax(outputs)]

# loop over our frames
for frame in frames:
	# draw the predicted activity on the frame
	cv2.rectangle(frame, (0, 0), (300, 40), (0, 0, 0), -1)
	cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
		0.8, (255, 255, 255), 2)

		# display the frame to our screen
	cv2.imshow("Activity Recognition", frame)
	key = cv2.waitKey(0)

cv2.destroyAllWindows()