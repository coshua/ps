class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heater_pointer = 0
        minrad = 0
        houses.sort()
        heaters.sort()
        for house in houses:
            while heater_pointer < len(heaters) - 1 and abs(heaters[heater_pointer] - house) >= abs(heaters[heater_pointer + 1] - house):
                heater_pointer += 1
            print(house, heaters[heater_pointer])
            minrad = max(minrad, abs(heaters[heater_pointer] - house))
        
        return minrad