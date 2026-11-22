#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# Базовые скорости
speed = 0.5
turn = 1.0

msg = """
Управление TurtleBot3:
---------------------------
   W (вперед)
   S (назад)
   A (влево)
   D (вправо)
   CTRL-C для выхода
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('teleop_keyboard')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    print(msg)
    
    x = 0
    th = 0
    
    try:
        while not rospy.is_shutdown():
            key = getKey()
            
            if key == 'w' or key == 'W':
                x = speed
                th = 0
            elif key == 's' or key == 'S':
                x = -speed
                th = 0
            elif key == 'a' or key == 'A':
                x = 0
                th = turn
            elif key == 'd' or key == 'D':
                x = 0
                th = -turn
            elif key == '\x03': # Ctrl+C
                break
            else:
                x = 0
                th = 0
            
            twist = Twist()
            twist.linear.x = x
            twist.angular.z = th
            pub.publish(twist)
            
    except Exception as e:
        print(e)
    finally:
        twist = Twist()
        twist.linear.x = 0; twist.angular.z = 0
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)