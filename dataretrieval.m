% Set your ThingSpeak channel ID and read API key
channelID = 2488606;
readAPIKey = 'TX0JBJABG0LKT9NY';

% Get the current time and time five hours ago
currentTime = datetime('now', 'TimeZone', 'UTC');
fiveHoursAgo = currentTime - hours(5);

% Set up the ThingSpeak URL for fetching data
url = sprintf('https://api.thingspeak.com/channels/%d/feeds.json?api_key=%s&start=%s&end=%s', ...
              channelID, readAPIKey, datestr(fiveHoursAgo, 'yyyy-mm-ddTHH:MM:SSZ'), ...
              datestr(currentTime, 'yyyy-mm-ddTHH:MM:SSZ'));

% Fetch data from ThingSpeak
data = webread(url);

% Extract sensor data
if ~isempty(data.feeds)
    sensorData = [data.feeds.field1]; % Assuming the sensor data is in Field 1
    timestamps = datetime({data.feeds.created_at}, 'InputFormat', 'yyyy-MM-dd''T''HH:mm:ss''Z''', 'TimeZone', 'UTC');
    
    % Display sensor data
    disp('Sensor Data:');
    disp(sensorData);
    disp('Timestamps:');
    disp(timestamps);
else
    disp('No data found in the specified time range.');
end