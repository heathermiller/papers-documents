clear all;
% close all;

sizes = [
20;
40;
60;
80;
100;
120;
140;
160;
180;
200;
]*1e3;

multiJVM_types = [
4;
7;
10;
14;
17;
16;
19;
24;
30;
30;
];

multiJVM_NOtypes = [
5;
9;
13;
18;
22;
26;
30;
35;
39;
43;
];

y = sizes;

figure;

hold on;
plot(y, multiJVM_types,'-x','Color',0.4*[1 1 1],'LineWidth',2);

hold on;
plot(y, multiJVM_NOtypes, '-o', 'Color', 0.8*[1 1 1],'LineWidth',2);

% hold on;
% plot(y, scala, '-k','LineWidth',2);

set(gcf,'PaperPositionMode','auto');
set(gca,'FontName','Times New Roman');
% set(gca,'XTickLabel', y);
set(gca,'FontSize',18);
set(gca,'XGrid','on','YGrid','on');
% ax = gca;
% had to do this by hand! go into figure properties
% gca.XTickLabel = {'20k','40k','60k','80k','100k','120k','140k','160k','180k','200k'};
xlabel('Number of Elements')
ylabel('Time [s]')
title('Impact of Static Types on Performance, End-to-End Application (groupBy + join) ')

l2 = legend('Static Serialization Enabled', 'Runtime Serialization','Location','NorthWest');
set(l2,'FontSize',14,'Color',[1 1 1]);


