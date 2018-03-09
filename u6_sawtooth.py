import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
import time as t
import u6

#open device, get ready to use
#only run this once before using device
#>>> dd = open_device
def open_device():
    import u6
    d = u6.U6()
    d.getCalibrationData()
    print d
    return d

#generate the wave form that we will be using
#specify step resolution and number of periods
#we are limited by read/write speeds of DAC
def make_saw():
    
    periods = 1000
    steps = 10000

    t = np.linspace(0, 1, steps)
    saw = signal.sawtooth(2 * np.pi * periods * t)

    df_saw = pd.DataFrame({
                               
                           "Time": t,
                           "Amplitude": saw,
                               
                             })
    amp = df_saw['Amplitude']
    time = df_saw['Time']
   
    '''
    plt.figure()
    plt.clf()
    plt.plot(df_saw)
    '''
    return(df_saw)


#this actually outputs the waveform
#arguments are the device and the waveform dataframe
#running from terminal
#>>> saw_stepper(dd,make_saw())
def saw_stepper(d,df):
    amp = df['Amplitude']
    time = df_saw['Time']
        
    for i in range(0, len(amp)):
        volt = amp.loc[i]
        
		#applys voltage to the dac
        dac0 = d.voltageToDACBits(volt, dacNumber = 0, is16Bits = False)
        d.getFeedback(u6.DAC0_8(dac0))
        
        t.sleep(.1)


#saw_stepper(d,make_saw())

#d.close()
