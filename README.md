# RL_Env
HDR simulations to emulate the Reinforcement learning environment

This repo has several scripts which generate HDR simulated images from which glare(in the form of DGP) is calculated.
The model for the environment is the livinglab in kaiserslautern with 3 zones of Electrochromic glass, each with a chance
of 4 different light transmission states. The simulations create HDR images for view points of the occupants at every hour based on a climate file.
The simulations itself are created based Radiance, a raytracing engine based on Monte-carlo approach. Since it is difficult
to create parametric simulations with Radiance alone, its tools are wrapped in several layers of python code.
The voluminous amount of data generated(HDRs) processed for glare(in the form of DGP), vertical Illuminance in a Async fashion
in multiprocessing environment and is stored in SQlite database.
