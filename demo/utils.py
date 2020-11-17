#!/usr/bin/env python

from sympy import pi
from pydy.viz import (Scene, VisualizationFrame, Cube, Sphere, Cylinder,
                      PerspectiveCamera)


def pydy_n_link_pendulum_scene(sys):

    inertial_frame = sys.eom_method._inertial

    particles = sys.eom_method.bodylist

    cart_point = particles[0].point

    for p in cart_point._pos_dict.keys():
        if p.name == 'O':
            origin = p

    for c in sys.constants.keys():
        if c.name.startswith('l'):
            length = c
            break

    cart_shape = Cube(0.3, color='red', name='cart')

    viz_frames = [VisualizationFrame(inertial_frame, cart_point,
                                     cart_shape)]

    for i, particle in enumerate(particles):
        joint_shape = Sphere(color='blue', radius=0.1,
                             name='joint{}'.format(i))
        link_shape = Cylinder(length, 0.05, color='blue',
                              name='link{}'.format(i))
        viz_frames.append(VisualizationFrame(inertial_frame, particle,
                                             joint_shape))

        if i != len(particles) - 1:
            vec = particle.point.pos_from(particles[i + 1].point).normalize()
            mid_point = particle.point.locatenew('mid', -length / 2 * vec)

            for frame in inertial_frame._dcm_dict.keys():
                if frame.name.endswith(str(i)):
                    break

            rot_frame = frame.orientnew('eee', 'Axis', [pi / 2, frame.z])

            viz_frames.append(VisualizationFrame(rot_frame, mid_point,
                                                 link_shape))

    # TODO : This should cause the camera to follow the cart, but it doesn't
    # seem to be working. Also, if OrthoGraphicCamera is used, it rotates
    # the inertial frame's axes and it is super zoomed out.
    camera_point = cart_point.locatenew('Camera Location', 30 *
                                        inertial_frame.z)
    primary_camera = PerspectiveCamera(inertial_frame, camera_point)

    scene = Scene(inertial_frame, origin, *viz_frames)

    scene.cameras = [primary_camera]
    scene.constants = sys.constants
    scene.states_symbols = sys.states

    return scene
