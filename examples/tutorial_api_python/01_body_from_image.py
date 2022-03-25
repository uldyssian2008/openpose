@@ -5,8 +5,10 @@
import os
from sys import platform
import argparse
import pyopenpose as op

try:
    """
    # Import Openpose (Windows/Ubuntu/OSX)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
@@ -25,15 +27,15 @@
    except ImportError as e:
        print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e

    """
    # Flags
    parser = argparse.ArgumentParser()
    #parser.add_argument("--image_path", default="../../../examples/media/COCO_val2014_000000000192.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
    parser.add_argument("--image_path", default="../../examples/media/COCO_val2014_000000000192.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
    args = parser.parse_known_args()

    # Custom Params (refer to include/openpose/flags.hpp for more parameters)
    params = dict()
    #params["model_folder"] = "../../../models/"
    params["model_folder"] = "../../models/"

    # Add others in path?
    for i in range(0, len(args[1])):
@@ -64,8 +66,9 @@

    # Display Image
    print("Body keypoints: \n" + str(datum.poseKeypoints))
    #cv2.imshow("OpenPose 1.6.0 - Tutorial Python API", datum.cvOutputData)
    #cv2.waitKey(0)
    cv2.imwrite("result_body.jpg", datum.cvOutputData)
    #cv2.imshow("OpenPose 1.6.0 - Tutorial Python API", datum.cvOutputData)
    #cv2.waitKey(0)
except Exception as e:
    print(e)
    sys.exit(-1)
