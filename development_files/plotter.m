freq = 2

data = load('log.txt');
dataX = data(:,1);
dataY = data(:,2);
dataZ = data(:,3);

dataA = data(:,4);
dataB = data(:,5);
dataC = data(:,6);

time = 0:(length(data)-1);
time = time*0.004;

%data2 = (1-cos(time*2*pi*freq))*5+45;
VZ = diff(smooth(dataZ,500))
AccZ = diff(smooth(VZ, 500))
plot(time, dataZ)
hold on
%plot(time, data2, 'g')
