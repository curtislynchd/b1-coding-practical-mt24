from uuv_mission.dynamic import Mission
#testing implementation of extracting mission data from csv file
mission = Mission.from_csv("data/mission.csv")
print("Reference:", mission.reference[:5])
print("Cave Height:", mission.cave_height[:5])
print("Cave Depth:", mission.cave_depth[:5])    