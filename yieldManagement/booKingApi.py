#https://rapidapi.com/ntd119/api/booking-com18
import requests
from .models import Vendor, MarketPlaceModel
from datetime import datetime, date

headers = {
	"X-RapidAPI-Key": "879e4c4d8bmsh7dadfff89843fe9p1e7f39jsn6fdc5124ea0b",
	"X-RapidAPI-Host": "booking-com18.p.rapidapi.com"
} 
def bookingRapidApi(locationId, location):
   MarketPlaceModel.objects.all().delete()
   print(MarketPlaceModel.objects.all())
   url = "https://booking-com18.p.rapidapi.com/stays/search"
   for i in range(7):
      querystring = {"locationId":"eyJjaXR5X25hbWUiOiJNb250csOpYWwiLCJjb3VudHJ5IjoiRnJhbmNlIiwiZGVzdF9pZCI6Ii0xNDUzMzA4IiwiZGVzdF90eXBlIjoiY2l0eSJ9",
               "checkinDate":str(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day+i}", '%Y-%m-%d').date()),"checkoutDate":str(datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day) +1+i}", '%Y-%m-%d').date())}
      vendor = Vendor.objects.filter(name="booking.com").first()
      print(vendor)
      response = requests.get(url, headers=headers, params=querystring)
      
      print(response.status_code)
      if response.status_code == 200:
            for data in response.json()["data"]:
               subdata = {"name":data["name"], "price":data["priceBreakdown"]["grossPrice"]["amountRounded"], "chk-in":f"2024-05-{1+i}"}
               if i == 0:
                  hotelMarket = MarketPlaceModel.objects.filter(hotel=data["name"]).first()
                  if  hotelMarket == None:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn0= price)
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn0= price)
                           Getbook.save()
                  else:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           hotelMarket.CheckIn0 = price
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           hotelMarket.CheckIn0 = price
                           Getbook.save()
               elif i == 1:
                  hotelMarket = MarketPlaceModel.objects.filter(hotel=data["name"]).first()
                  if  hotelMarket == None:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn1= price)
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn1= price)
                           Getbook.save()
                  else:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           hotelMarket.CheckIn1 = price
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           hotelMarket.CheckIn1 = price
                           Getbook.save()
               elif i == 2:
                  hotelMarket = MarketPlaceModel.objects.filter(hotel=data["name"]).first()
                  if  hotelMarket == None:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn2= price)
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn2= price)
                           Getbook.save()
                  else:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           hotelMarket.CheckIn2 = price
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           hotelMarket.CheckIn2 = price
                           Getbook.save()
               elif i == 3:
                  hotelMarket = MarketPlaceModel.objects.filter(hotel=data["name"]).first()
                  if  hotelMarket == None:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn3= price)
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn3= price)
                           Getbook.save()
                  else:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           hotelMarket.CheckIn3 = price
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           hotelMarket.CheckIn3 = price
                           Getbook.save()
               elif i == 4:
                  hotelMarket = MarketPlaceModel.objects.filter(hotel=data["name"]).first()
                  if  hotelMarket == None:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn4= price)
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn4= price)
                           Getbook.save()
                  else:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           hotelMarket.CheckIn4 = price
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           hotelMarket.CheckIn4 = price
                           Getbook.save()
               elif i == 5:
                  hotelMarket = MarketPlaceModel.objects.filter(hotel=data["name"]).first()
                  if  hotelMarket == None:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn5= price)
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn5= price)
                           Getbook.save()
                  else:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           hotelMarket.CheckIn5 = price
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           hotelMarket.CheckIn5 = price
                           Getbook.save()
               else:
                  hotelMarket = MarketPlaceModel.objects.filter(hotel=data["name"]).first()
                  if  hotelMarket == None:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn6= price)
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           Getbook = MarketPlaceModel(vendor = vendor, hotel=data["name"], hotelId = data["id"],
                                                  locationId=locationId,
                                                    location=location,CheckIn6= price)
                           Getbook.save()
                  else:
                     try:
                           price = data["priceBreakdown"]["strikethroughPrice"]["value"]
                           hotelMarket.CheckIn6 = price
                           Getbook.save()
                     except:
                           price = data["priceBreakdown"]["grossPrice"]["value"]
                           hotelMarket.CheckIn6 = price
                           Getbook.save()
                
def bookingRapidApiHotel(hotel, chkin, chkout):
   url = "https://booking-com18.p.rapidapi.com/stays/detail"
   marketObj = MarketPlaceModel.objects.filter(hotel = hotel).first()
   querystring = {"hotelId":marketObj.hotelId,
                  "checkinDate":chkin,
                  "checkoutDate":chkout}

   headers = {
	"X-RapidAPI-Key": "879e4c4d8bmsh7dadfff89843fe9p1e7f39jsn6fdc5124ea0b",
	"X-RapidAPI-Host": "booking-com18.p.rapidapi.com"
}  
   
   response = requests.get(url, headers=headers, params=querystring)
   print(response.status_code)
   if response.status_code == 200:
      try:
         print(response.json()["data"]["alternate_availability"])
         for prices in response.json()["data"]["alternate_availability"]:
            if diffDate(prices["checkin"], prices["checkout"]) == 1:
               if diffDate(str(date.today()), prices["checkin"]) == 1:
                  marketObj.CheckIn1 = prices["price"]
                  marketObj.save()
               elif diffDate(str(date.today()), prices["checkin"]) == 2:
                  marketObj.CheckIn2 = prices["price"]
                  marketObj.save()
               elif diffDate(str(date.today()), prices["checkin"]) == 3:
                  marketObj.CheckIn3 = prices["price"]
                  marketObj.save()
               elif diffDate(str(date.today()), prices["checkin"]) == 4:
                  marketObj.CheckIn4 = prices["price"]
                  marketObj.save()
               elif diffDate(str(date.today()), prices["checkin"]) == 5:
                  marketObj.CheckIn5 = prices["price"]
                  marketObj.save()
               elif diffDate(str(date.today()), prices["checkin"]) == 6:
                  marketObj.CheckIn6 = prices["price"]
                  marketObj.save()
               elif diffDate(str(date.today()), prices["checkin"]) == 0:
                  marketObj.CheckIn0 = prices["price"]
                  marketObj.save()
      except:
         try:
            print(response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"])
            if diffDate(str(date.today()), chkin) == 1:
                  marketObj.CheckIn1 = response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 2:
                  marketObj.CheckIn2 = response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 3:
                  marketObj.CheckIn3 = response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 4:
                  marketObj.CheckIn4 = response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 5:
                  marketObj.CheckIn5 = response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 6:
                  marketObj.CheckIn6 = response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 0:
                  marketObj.CheckIn0 = response.json()["data"]["composite_price_breakdown"]["gross_amount_hotel_currency"]["value"]
                  marketObj.save()

         except:
            print(response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"])
            if diffDate(str(date.today()), chkin) == 1:
                  marketObj.CheckIn1 = response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 2:
                  marketObj.CheckIn2 = response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 3:
                  marketObj.CheckIn3 = response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 4:
                  marketObj.CheckIn4 = response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 5:
                  marketObj.CheckIn5 = response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 6:
                  marketObj.CheckIn6 = response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"]
                  marketObj.save()
            elif diffDate(str(date.today()), chkin) == 0:
                  marketObj.CheckIn0 = response.json()["data"]["composite_price_breakdown"]["gross_amount_per_night"]["value"]
                  marketObj.save()
            else:
                print("Oops something is wrong")



#https://rapidapi.com/ntd119/api/booking-com18
#https://rapidapi.com/tipsters/api/booking-com

def  bookingRapidApiLocationId(city):
   url = "https://booking-com18.p.rapidapi.com/stays/auto-complete"

   querystring = {"query":city}

   headers = {
	"X-RapidAPI-Key": "879e4c4d8bmsh7dadfff89843fe9p1e7f39jsn6fdc5124ea0b",
	"X-RapidAPI-Host": "booking-com18.p.rapidapi.com"
} 

   response = requests.get(url, headers=headers, params=querystring)

   print(response.status_code)
   if response.status_code == 200:
      for data in response.json()["data"]:
               locationid = data["id"]
      return locationid
   


def diffDate(chkin, chkout):
    
    start_date = datetime.strptime(str(chkin), '%Y-%m-%d')
    end_date = datetime.strptime(str(chkout), '%Y-%m-%d')
    print(start_date)
    difference = end_date.date() - start_date.date()
    print(difference.days)
    return int(difference.days)

