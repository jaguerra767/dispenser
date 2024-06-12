from Phidget22.Devices.VoltageRatioInput import *
import matplotlib.pyplot as plt
import time

cell_10kg = VoltageRatioInput()
cell_10kg.setDeviceSerialNumber(716692)
cell_10kg.setChannel(0)
cell_10kg.openWaitForAttachment(1000)
cell_10kg.setDataInterval(cell_10kg.getMinDataInterval())

cell_5kg = VoltageRatioInput()
cell_10kg.setDeviceSerialNumber(716710)
cell_10kg.setChannel(2)
cell_10kg.openWaitForAttachment(2000)
cell_10kg.setDataInterval(cell_10kg.getMinDataInterval())


def get_data(cell, samples=100, sample_rate=10):
    data = []
    for i in range(samples):
        data += [cell.getVoltageRatio()]
        time.sleep(1 / sample_rate)
    return data


def plot(cell1, cell2):
    data_10kg = get_data(cell1)
    data_5kg = get_data(cell2)

    plt.close()
    plt.plot(data_10kg)
    plt.plot(data_5kg)
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.grid()
    plt.savefig('cell_testing.png')


def run(cell1=cell_10kg, cell2=cell_5kg):
    plot(cell1, cell2)


run()
