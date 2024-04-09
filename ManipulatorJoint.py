#!/usr/bin/env python3
import rospy
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
import time


def set_joints(joint1, joint2, joint3, joint4, t):
    service_name = "/goal_joint_space_path"
    rospy.wait_for_service(service_name)
    
    try:
        service = rospy.ServiceProxy(service_name, SetJointPosition)
        
        request = SetJointPositionRequest()
        request.joint_position.joint_name = ["joint1", "joint2", "joint3", "joint4"]
        request.joint_position.position = [joint1, joint2, joint3, joint4]
        request.path_time = t
        
        response = service(request)
        return response
    except Exception as e:
        rospy.loginfo("%s" % e)
        return False


if __name__ == "__main__":
    rospy.init_node("ros_tutorial")
    rospy.loginfo("ros_tutorial node start!")
    
    t = 3.0
    
    joint1, joint2, joint3, joint4 = 0.0, 0.0, 0.0, 0.0
    set_joints(joint1, joint2, joint3, joint4, t)
    time.sleep(t)
    
    joint1, joint2, joint3, joint4 = -3.14 / 2, -3.14 / 4, 3.14 / 4, 3.14 / 4
    set_joints(joint1, joint2, joint3, joint4, t)
    time.sleep(t)

    joint1, joint2, joint3, joint4 = 0.0, 0.0, 0.0, 0.0
    set_joints(joint1, joint2, joint3, joint4, t)
    time.sleep(t)
    
    rospy.loginfo("ros_tutorial node end!")