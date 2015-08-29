freq = 2

data = load('log.txt');
cur1 = data(:,1);


%time = 0:(length(data)-1);
%time = time*0.004;

time = data(:,7) - data(1,7);

for i=3:3
    figure;
    plot(diff(smooth(diff(smooth(data(:,i),10)),10))D/0.004^2);
end

