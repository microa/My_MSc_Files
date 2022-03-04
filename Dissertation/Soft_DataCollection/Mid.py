import serial # Import UART Module
import pandas as pd




class GVar():

    GL = [0 for i in range(24)]
    GM = [[0 for i in range(8)] for i in range(3)]
    GC = ["M0", 500, "M1", 500, "M2", 500, 5000]
    GLB_CurrentPos = [0,0,0]
    GLB_ReferPos = [0,0,0]


    #ADC Reader
    ADR_Serial_Port = 'COM5'
    ADR_Serial_Baud = 115200


    #Sending Data (Motor control)
    SDF_Serial_Port = 'COM3'
    SDF_Serial_Baud = 9600

    Movement = [[1, 10, 2, 800, 3, 800, 2000, 2000],   #[0][2][4]:Motor ID, [1][3][5]:Destination, [6]:Speed [7]:delay time
                [1, 200, 2, 600, 3, 600, 2000, 2000]
                ]

    Overload = 0