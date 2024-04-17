scriptpath = fileparts(mfilename('fullpath'));
addpath(scriptpath)
addpath('mr')
clc;
clear;

%% JUST LEFT LEG
% Slist = [[0;0;1; 468.7500; 22.6300; 0], ...
%         [0;-1;0; -25.6400; 0; -21.3700], ...
%         [1;0;0; 0; -29.1400; -450.4500], ...
%         [1;0;0; 0; -29.1400; -266.5500], ...
%         [-1;0;0; 0; 29.1400; 35]];
% M = [[1, 0, 0, 22.63]; [0, 1, 0, -468.74]; [0, 0, 1, 12.74]; [0, 0, 0, 1]];
% thetalist =[deg2rad(0); deg2rad(0); deg2rad(-20); deg2rad(40); deg2rad(20)];

%% JUST RIGHT LEG
Slist = [[0;0;1; 468.7500; -22.6300; 0], ...
        [0;-1;0; -25.6400; 0; 21.3700], ...
        [1;0;0; 0; -29.1400; -450.4500], ...
        [1;0;0; 0; -29.1400; -266.5500], ...
        [-1;0;0; 0; 29.1400; 35]];
M = [[1, 0, 0, -22.63]; [0, 1, 0, -468.74]; [0, 0, 1, 12.74]; [0, 0, 0, 1]];
thetalist =[deg2rad(0); deg2rad(0); deg2rad(20); deg2rad(-40); deg2rad(-20)];

%% RIGHT ARM
% Slist = [[-1;0;0; 0; -37.5100; 8.7000], ...
%         [0;0;1; 8.7000; -318.5300; 0], ...
%         [1;0;0; 0; 25.9100; -8.7000], ...
%         [0;1;0; -12.9800; 0; 161.7500], ...
%         [0;-1;0; 7; 0; -52]];
% M = [[1, 0, 0, -343.73]; [0, 1, 0, -8.7]; [0, 0, 1, -36.51]; [0, 0, 0, 1]];
% thetalist = [deg2rad(-20); deg2rad(90); deg2rad(0); deg2rad(110); deg2rad(0)];

%% LEFT ARM
% Slist = [[1;0;0;0; 37.51; -8.2], ...
%         [0;0;1; 8.2; 318.53; 0], ...
%         [-1;0;0; 0; -25.9100; 8.2], ...
%         [0;1;0;-12.9800; 0; -161.7500], ...
%         [0;-1;0; 7; 0; 52]];
% M = [[1, 0, 0, 343.73]; [0, 1, 0, -8.2]; [0, 0, 1, -36.51]; [0, 0, 0, 1]];
% thetalist =[deg2rad(20); deg2rad(-90); deg2rad(0); deg2rad(-110); deg2rad(0)];


T = FKinBody(M, Slist, thetalist)

% Code to print matrix in Python or MATLAB syntax
fprintf("MATLAB: \n [")
for i = 1:3
    fprintf('%f, ', T(i,1:end-1)); % Print all elements except the last one
    fprintf('%f;\n', T(i,end))
end
fprintf('%f, ', T(4,1:end-1)); % Print all elements except the last one
fprintf('%f]\n \n', T(4,end))

fprintf("Python: \n")
fprintf('[[')
for i = 1:3
    fprintf('%f, ', T(i,1:(end-1)))
    fprintf('%f], \n [', T(i,end))
end
fprintf('%f, ', T(4,1:(end-1)))
fprintf('%f]] \n', T(4,end))