#!/usr/bin/env python
import rospy
from CR_week6_test.msg import perceived_info
from CR_week6_test.msg import robot_info
from CR_week6_test.srv import predict_robot_expression

global PubExpression

def service_client(p_info):
    print ("Recieved Perception Info")
    print ("Calling service")
    rospy.wait_for_service('RobotExpressionPrediction')
    PubExpression = rospy.Publisher("Robot_Expression", robot_info, queue_size=10)
    print ("Requesting")
    rospy.loginfo(p_info)
    try:
        Predict = rospy.ServiceProxy('RobotExpressionPrediction', predict_robot_expression)
        resp1 = Predict(p_info)
        PubExpression.publish(resp1.prediction)  # publish object to topic IntTopicObject
        print("Prediction")
        rospy.loginfo(resp1.prediction)

    except rospy.ServiceException, e:
        print ("Service call failed: %s" % e)





##listens for topic percieved, calls service client to get the robot predicted values when it recieves a subscribed topic message
def listener():
    PubExpression = rospy.Publisher("Robot_Expression", robot_info, queue_size=10)
    print ("Waiting for publisher")
    rospy.init_node('Robot_Controller', anonymous=True)
    rospy.Subscriber("Perceived", perceived_info, service_client)

    rospy.spin()



if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass