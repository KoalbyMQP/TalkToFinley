import sys, time, math

import numpy as np 
sys.path.append("./")
from backend.KoalbyHumanoid.Robot import Robot
from backend.KoalbyHumanoid.trajPlannerTime import TrajPlannerTime
# from backend.Testing import finlyViaPoints as via

def main():
    # Edit to declare if you are testing the sim or the real robot
    is_real = True

    robot = Robot(is_real)

    print("Setup Complete")

    ################################################################
    """
    FOR DESIGN TEAM

    This file is to log the via points of the trajectories for the demo in effort to clean up the main code.
    Angles are in radians and can be calculated using the MATLAB scripts found in backend>KoalbyHumanoid>MATLAB Scripts.

    Format of each list goes as follows:
        [0]: list of t_f for each via point
        [1]: list of joint angles (rad)
        [2]: list of joint velocities through each via_point (v_f)
        [3]: list of joint accelerations through each via point (a_f)
    """

    ##first movement to grab the candy
    leftArmTraj1 = [
        [[0,0,0,0,0], [1.5,1.5,1.5,1.5,1.5], [3,3,3,3,3]],
        [[0.000000, 1.570796, 0.000000, 1.570796, 0.000000], ##starting position (0,0,0)
        [-0.399673, 0.908213, 0.258504, 1.653297, 0.000000], ## X125, Y0, Z50 : arm left and back
        [-0.266709, 0.697618, 0.206337, 1.413457, 0.000000]], ##X175, Y-3, Z-35: arm more left and align with candy
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]

    ##second movement to move the candy
    leftArmTraj2 = [
        [[0,0,0,0,0],[3,3,3,3,3],[6,6,6,6,6]],
        [[-0.266709, 0.697618, 0.206337, 1.413457, 0.000000], ##X175, Y-35, Z-3: arm more left and align with candy
        [0.121513, 0.669234, -0.101738, 1.342783, 0.000000], ##X175, Y8, Z-20: arm up holding candy
        [-0.804261, 1.486360, 0.088339, 0.689863, 0.000000]], ##X15, Y10, Z120: arm moves right holding candy then drop -- here is where numbers change
        [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
        [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]]

    #third movement after releasing candy
    leftArmTraj3= [
        [[0,0,0,0,0],[3,3,3,3,3]],
        [[-0.804261, 1.486360, 0.088339, 0.689863, 0.000000],
        [0.000000, 1.570798, 0.000000, 1.570796, 0.000000]], ##ending position (0,0,0)
        [[0,0,0,0,0], [0,0,0,0,0]],
        [[0,0,0,0,0], [0,0,0,0,0]]]
    ###############################


    #Starting Agnles
    robot.motors[0].target = (math.radians(20), 'P')
    robot.motors[1].target = (math.radians(-80), 'P')
    robot.motors[3].target = (math.radians(-90), 'P')

    robot.motors[5].target = (math.radians(-20), 'P')
    robot.motors[6].target = (math.radians(90), 'P')
    robot.motors[8].target = (math.radians(120), 'P')

    robot.motors[18].target = (math.radians(90), 'P')
    robot.motors[17].target = (math.radians(-90), 'P')
    robot.motors[23].target = (math.radians(-90), 'P')
    robot.motors[22].target = (math.radians(90), 'P')

    robot.motors[5].target = (math.radians(0), 'P')
    robot.motors[6].target = (math.radians(90), 'P')
    robot.motors[7].target = (math.radians(0), 'P')
    robot.motors[8].target = (math.radians(90), 'P')
    robot.motors[9].target = (math.radians(0), 'P')

    robot.motors[27].target = (math.radians(-15), 'P')
    prevTime = time.time()
    startTime = time.time()

    while time.time() - startTime <= 4:
        #robot.IMUBalance(0,0)
        robot.moveAllToTarget()

    lArm_tj = TrajPlannerTime(leftArmTraj1[0], leftArmTraj1[1], leftArmTraj1[2], leftArmTraj1[3])

    state = 0
    startTime = time.time()

    print("State = 0")

    ## Moving Left Arm to Grab Candy
    while time.time() - startTime <= 3:
        l_points = lArm_tj.getQuinticPositions(time.time() - startTime)
        
        robot.motors[5].target = (l_points[0], 'P')
        robot.motors[6].target = (l_points[1], 'P')
        robot.motors[7].target = (l_points[2], 'P')
        robot.motors[8].target = (l_points[3], 'P')
        robot.motors[9].target = (l_points[4], 'P')
        #robot.motors[8].target = (math.radians(45), 'P')
        #robot.IMUBalance(0, 0)
        #robot.moveAllToTarget()
        #robot.motors[27].target = (math.radians(15), 'P')
        robot.moveAllToTarget()
    ## Grab Candy
    #sim = robot.sim
    #candy = sim.getObject("./candy")
    #hand = sim.getObject("./LeftHand_respondable")
    #forceSensor = sim.createForceSensor(0, [0,0,0,0,0], [0,0,0,0,0])
    #sim.setObjectParent(forceSensor, hand, True)
    #sim.setObjectParent(candy, forceSensor, True)

    lArm_tj = TrajPlannerTime(leftArmTraj2[0], leftArmTraj2[1], leftArmTraj2[2], leftArmTraj2[3])

    state = 0
    startTime = time.time()

    print("State = 1")
    ## Moving Left Arm to Grab Candy
    while time.time() - startTime <= 6:
        l_points = lArm_tj.getQuinticPositions(time.time() - startTime)
        
        robot.motors[5].target = (l_points[0], 'P')
        robot.motors[6].target = (l_points[1], 'P')
        robot.motors[7].target = (l_points[2], 'P')
        robot.motors[8].target = (l_points[3], 'P')
        robot.motors[9].target = (l_points[4], 'P')

        #robot.IMUBalance(0, 0)
        robot.moveAllToTarget()
        robot.motors[27].target = (math.radians(20), 'P')
        robot.moveAllToTarget()
    #forceSensor = sim.createForceSensor(0, [0,0,0,0,0], [0,0,0,0,0])

    # print(sim.getObject("./"))
    #table = sim.getObject("./Table")
    #sim.setObjectParent(candy, table, True)

    ## Moving Left Arm With Candy
    lArm_tj = TrajPlannerTime(leftArmTraj3[0], leftArmTraj3[1], leftArmTraj3[2], leftArmTraj3[3])
    startTime = time.time()
    print("State = 2")

    while time.time() - startTime <= 3:
        l_points = lArm_tj.getQuinticPositions(time.time() - startTime)
        
        robot.motors[5].target = (l_points[0], 'P')
        robot.motors[6].target = (l_points[1], 'P')
        robot.motors[7].target = (l_points[2], 'P')
        robot.motors[8].target = (l_points[3], 'P')
        robot.motors[9].target = (l_points[4], 'P')

        #robot.IMUBalance(0, 0)
        robot.moveAllToTarget()
        robot.motors[27].target = (math.radians(0), 'P')
        robot.moveAllToTarget()
    ##while loop for traj
