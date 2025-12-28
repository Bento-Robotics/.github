import rclpy
from rclpy.node import Node

from std_msgs.msg import String


timer_period = 0.5  # seconds


class MinimalPublisher( Node ):
    # __init__  ist der Konstruktor dieser Klasse. Hier soll diese eingerichtet werden.
    def __init__(self):
        super().__init__('minimal_publisher') # ruft den Konstruktor der  Node  Klasse auf
        self.publisher_ = self.create_publisher( String, 'topic', 10 ) # Queue Länge = 10
        self.timer = self.create_timer( timer_period, self.timer_callback )
        # timer_callback wird hier vor der Definition verwendet! Wie ist das möglich?

        self.i = 0


    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info( 'Publishing: "%s"' % msg.data )

        self.i += 1 # dasselbe wie  self.i = self.i + 1  ; gibts übrigens für alles: += -= *= /=

# ende von class


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Explizit herunterfahren
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
