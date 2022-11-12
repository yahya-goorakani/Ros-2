import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class Publisher(Node):

    def __init__(self):
        super().__init__('image_pub')
        self.publisher_ = self.create_publisher(Image, '/image', 10)
        timer_period = 0.01  
        self.timer = self.create_timer(timer_period, self.send)
        self.i = 0
        self.cam = cv2.VideoCapture(0)
        self.br = CvBridge()

    def send(self):
        color = (50, 128, 255)
        ret, frame = self.cam.read()
        if ret:
            cv2.putText(frame,'Hello ROS2!', (150,50), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 4,
                    cv2.LINE_AA)
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame, 'bgr8'))

        self.get_logger().info('Publishing')

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
