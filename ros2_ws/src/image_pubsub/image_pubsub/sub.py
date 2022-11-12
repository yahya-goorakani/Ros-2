import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class Subscriber(Node):
    def __init__(self):
        super().__init__('image_sub')
        self.br = CvBridge()
        self.subscription = self.create_subscription(Image, '/image', self.get, 10)
        self.subscription

    def get(self, msg):
        self.get_logger().info('Receiving')
        current_frame = self.br.imgmsg_to_cv2(msg)

        cv2.imshow("camera", current_frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()



def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
