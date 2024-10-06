class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Given a date string in the form "Day Month Year"
        # Convert the date string to the format "YYYY-MM-DD"
        date = date.split(" ")
        result = []
        months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
        days = {
  "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", 
  "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", 
  "28th", "29th", "30th", "31st"
}
        
        result.append(date[2])
        month_convert = str(months.index(date[1]) + 1)
        day_convert = str(days.index(date[0]) + 1)
        if len(month_convert) == 1:
            month_convert = "0" + f"{month_convert}"
        if len(day_convert) == 1:
            day_convert = "0" + f"{day_convert}"
        result.append(month_convert)
        result.append(day_convert)
        
        return f"{result[0]}-{result[1]-{result[2]}}" 
        
            
        
  
  
  
  
  
  
        
# so1 = Solution()
# so1.reformatDate("20 20 20")