from abc import ABC, abstractmethod


class Seismogram(ABC):
    @abstractmethod
    def process(self):
        pass


class Accelerometer(Seismogram):
    def process(self):
        print("Measuring...")


class LowQualitySeismogram():
    def process(self):
        print("running")


class Seismologist:
    def work(self, seis):
        print("Measuring Earthquakes")
        seis.process()

# if it's an abstract class cannot instantiate an object
# seis = Seismogram()
# seis.process()


low_seis = LowQualitySeismogram()
low_seis.process()

accelerometer = Accelerometer()
seism = Seismologist()
seism.work(accelerometer)
