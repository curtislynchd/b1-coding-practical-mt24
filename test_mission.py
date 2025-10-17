# test_mission.py
print("Script started")

from uuv_mission.dynamic import Mission

m = Mission.from_csv('data/mission.csv')
print(m.reference.shape, m.cave_height.shape, m.cave_depth.shape)
print("First 5 reference values:", m.reference[:5])