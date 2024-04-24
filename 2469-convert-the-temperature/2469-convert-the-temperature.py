class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        kelvin = celsius + 273.15
        
        Fahrenheit = celsius * 1.80 + 32
       
        kelvin = float(f"{kelvin:.5f}")
        Fahrenheit= float(f"{Fahrenheit:.5f}")
        
        ans = [kelvin,Fahrenheit]
        return ans

        