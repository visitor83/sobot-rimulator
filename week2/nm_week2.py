#!/usr/bin/python
# -*- Encoding: utf-8 -*
# Python implementation of the Week 2 exercise.

from math import *

# Khepera3 Properties
KHEPERA3_WHEEL_RADIUS = 0.021         # meters
KHEPERA3_WHEEL_BASE_LENGTH = 0.0885   # meters

class DifferentialDriveDynamics:
  
  def __init__( self, wheel_radius, wheel_base_length):
    self.wheel_radius = wheel_radius
    self.wheel_base_length = wheel_base_length
    
  def uni_to_diff( self, v, w ):
    # v = translational velocity (meters/sec)
    # w = angular velocity (radians/sec)
    
    R = self.wheel_radius
    L = self.wheel_base_length
    
    v_l = ( (2.0 * v) - (w*L) ) / (2.0 * R)
    v_r = ( (2.0 * v) + (w*L) ) / (2.0 * R)
    
    return v_l, v_r
    
  def diff_to_uni( self, v_l, v_r ):
    # v_l = left-wheel angular velocity (radians/sec)
    # v_r = right-wheel angular velocity (radians/sec)
    
    R = self.wheel_radius
    L = self.wheel_base_length
    
    v = ( R / 2.0 ) * ( v_r + v_l )
    w = ( R / L ) * ( v_r - v_l )
    
    return v, w
    

#class Robot # Khepera3 robot, properties copied from Sim.I.Am
#  
#  def __init__:
#    self.wheel_radius = KHEPERA3_WHEEL_RADIUS             # meters
#    self.wheel_base_length = KHEPERA3_WHEEL_BASE_LENGTH   # meters


#dynamics = DifferentialDriveDynamics( KHEPERA3_WHEEL_RADIUS, KHEPERA3_WHEEL_BASE_LENGTH )
#v_l, v_r = dynamics.uni_to_diff( 3.0, (-pi / 2.0 ) )
#print v_l * dynamics.wheel_radius
#print v_r * dynamics.wheel_radius
#print "\n\n"
#v, w = dynamics.diff_to_uni( 3 / KHEPERA3_WHEEL_RADIUS, 6 / KHEPERA3_WHEEL_RADIUS )
#print str(v) + " m/s"
#print str(w/pi) + "pi rad/sec"
