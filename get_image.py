import cv2, rospy
from poppy_controllers.srv import GetImage
from cv_bridge import CvBridge

i=1
while True:
    get_image = rospy.ServiceProxy("get_image", GetImage)
    response  = get_image()
    bridge    = CvBridge()
    image     = bridge.imgmsg_to_cv2(response.image)
    cv2.imwrite(f"image{i:03d}.png", image)
    cv2.imshow("Poppy camera", image)
    cv2.waitKey(0)
    i += 1

